from __future__ import annotations

from typing import Any


def _paper_key(paper: dict[str, Any]) -> str:
    return str(paper.get("id") or paper.get("title", "")).strip().lower()


def filter_new_papers(
    papers: list[dict[str, Any]],
    seen_state: dict[str, Any],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    resend_delta = float(config["state"]["resend_if_score_improves_by"])
    unique: dict[str, dict[str, Any]] = {}

    for paper in papers:
        key = _paper_key(paper)
        previous = unique.get(key)
        if previous is None or paper["relevance_score"] > previous["relevance_score"]:
            unique[key] = paper

    fresh: list[dict[str, Any]] = []
    seen_papers = seen_state.setdefault("papers", {})

    for key, paper in unique.items():
        old = seen_papers.get(key)
        if not old:
            fresh.append(paper)
            continue
        old_score = float(old.get("relevance_score", 0.0))
        if paper["relevance_score"] >= old_score + resend_delta:
            paper["resend_reason"] = "importance increased"
            fresh.append(paper)

    fresh.sort(key=lambda item: item["relevance_score"], reverse=True)
    return fresh
