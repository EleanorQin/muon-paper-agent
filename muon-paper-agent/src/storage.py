from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_seen_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"papers": {}, "history": []}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_digest_markdown(path: Path, markdown: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown + "\n", encoding="utf-8")


def archive_digest_markdown(directory: Path, subject: str, markdown: str) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    stamp = datetime.utcnow().strftime("%Y-%m-%d")
    archive_path = directory / f"{stamp}.md"
    archive_text = "\n".join([f"# {subject}", "", markdown.strip()]).strip() + "\n"
    archive_path.write_text(archive_text, encoding="utf-8")


def save_seen_state(path: Path, seen_state: dict[str, Any], papers: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    seen_papers = seen_state.setdefault("papers", {})
    history = seen_state.setdefault("history", [])

    for paper in papers:
        key = str(paper.get("id") or paper.get("title", "")).strip().lower()
        seen_papers[key] = {
            "title": paper.get("title"),
            "link": paper.get("link"),
            "relevance_score": paper.get("relevance_score"),
            "last_sent_at": datetime.utcnow().isoformat() + "Z",
            "category": paper.get("category"),
        }

    history.append(
        {
            "sent_at": datetime.utcnow().isoformat() + "Z",
            "paper_count": len(papers),
        }
    )
    seen_state["history"] = history[-60:]

    with path.open("w", encoding="utf-8") as handle:
        json.dump(seen_state, handle, indent=2, sort_keys=True)
