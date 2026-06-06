from __future__ import annotations

import logging
import os
from typing import Any

import requests

LOGGER = logging.getLogger(__name__)
API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"


def enrich_with_semantic_scholar(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
    if not api_key or not papers:
        return papers

    headers = {"x-api-key": api_key}
    fields = "title,authors,citationCount,influentialCitationCount,url,year"

    for paper in papers:
        params = {
            "query": paper["title"],
            "limit": 1,
            "fields": fields,
        }
        try:
            response = requests.get(API_URL, headers=headers, params=params, timeout=20)
            response.raise_for_status()
            results = response.json().get("data", [])
        except requests.RequestException as exc:
            LOGGER.warning("Semantic Scholar lookup failed for '%s': %s", paper["title"], exc)
            continue
        except ValueError as exc:
            LOGGER.warning("Semantic Scholar returned invalid JSON for '%s': %s", paper["title"], exc)
            continue

        if not results:
            continue

        match = results[0]
        paper["semantic_scholar"] = {
            "citation_count": match.get("citationCount", 0),
            "influential_citation_count": match.get("influentialCitationCount", 0),
            "url": match.get("url"),
            "year": match.get("year"),
        }

    return papers
