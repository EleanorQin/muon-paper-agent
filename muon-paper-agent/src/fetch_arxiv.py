from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from typing import Any
from xml.etree import ElementTree

import requests

ARXIV_API_URL = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
LOGGER = logging.getLogger(__name__)


def _build_query(keywords: list[str]) -> str:
    terms = []
    for keyword in keywords:
        safe = keyword.replace('"', "")
        terms.append(f'all:"{safe}"')
    return " OR ".join(terms)


def _build_queries(config: dict[str, Any]) -> list[str]:
    if config.get("fetch_mode") == "per_keyword":
        return [f'all:"{keyword.replace(chr(34), "")}"' for keyword in config["keywords"]]
    return [_build_query(config["keywords"])]


def _parse_arxiv_id(id_text: str) -> str:
    return id_text.rstrip("/").split("/")[-1]


def _extract_authors(entry: ElementTree.Element) -> list[str]:
    values = []
    for author in entry.findall("atom:author", ATOM_NS):
        name = author.findtext("atom:name", default="", namespaces=ATOM_NS)
        if name:
            values.append(" ".join(name.split()))
    return values


def _category_allowed(categories: list[str], config: dict[str, Any]) -> bool:
    filters = config.get("source_filters", {})
    allowed_prefixes = filters.get("allowed_category_prefixes", [])
    blocked_prefixes = filters.get("blocked_category_prefixes", [])

    if any(category.startswith(prefix) for prefix in blocked_prefixes for category in categories):
        return False
    if not allowed_prefixes:
        return True
    return any(category.startswith(prefix) for prefix in allowed_prefixes for category in categories)


def fetch_recent_arxiv_papers(config: dict[str, Any]) -> list[dict[str, Any]]:
    max_results = int(config.get("max_results_per_query", 25))
    cutoff = datetime.now(timezone.utc) - timedelta(hours=int(config["lookback_hours"]))
    papers_by_id: dict[str, dict[str, Any]] = {}

    for query in _build_queries(config):
        params = {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": max_results,
        }

        try:
            response = requests.get(ARXIV_API_URL, params=params, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.warning("arXiv request failed for query '%s': %s", query, exc)
            continue

        LOGGER.info("arXiv query: %s", response.url)

        try:
            root = ElementTree.fromstring(response.text)
        except ElementTree.ParseError as exc:
            LOGGER.warning("Failed to parse arXiv feed for query '%s': %s", query, exc)
            continue

        for entry in root.findall("atom:entry", ATOM_NS):
            published_text = entry.findtext("atom:published", default="", namespaces=ATOM_NS)
            updated_text = entry.findtext("atom:updated", default="", namespaces=ATOM_NS)

            try:
                published_at = datetime.fromisoformat(published_text.replace("Z", "+00:00"))
                updated_at = datetime.fromisoformat(updated_text.replace("Z", "+00:00"))
            except ValueError:
                continue

            if updated_at < cutoff and published_at < cutoff:
                continue

            title = entry.findtext("atom:title", default="", namespaces=ATOM_NS)
            summary = entry.findtext("atom:summary", default="", namespaces=ATOM_NS)
            paper_id = entry.findtext("atom:id", default="", namespaces=ATOM_NS)
            authors = _extract_authors(entry)
            categories = [node.attrib.get("term", "") for node in entry.findall("atom:category", ATOM_NS)]
            categories = [category for category in categories if category]
            if not _category_allowed(categories, config):
                continue

            parsed_id = _parse_arxiv_id(paper_id)
            existing = papers_by_id.get(parsed_id)
            candidate = {
                "id": parsed_id,
                "source": "arXiv",
                "title": " ".join(title.split()),
                "authors": authors,
                "summary": " ".join(summary.split()),
                "link": paper_id,
                "published_at": published_at.isoformat(),
                "updated_at": updated_at.isoformat(),
                "categories": categories,
            }
            if existing is None or candidate["updated_at"] > existing["updated_at"]:
                papers_by_id[parsed_id] = candidate

    LOGGER.info("Retained %d category-matched arXiv papers after deduplication", len(papers_by_id))
    return list(papers_by_id.values())
