from __future__ import annotations

from datetime import datetime
from typing import Any


def _is_relevant(paper: dict[str, Any]) -> bool:
    return paper.get("category") != "Not Relevant"


def _paper_block(index: int, paper: dict[str, Any]) -> str:
    authors = ", ".join(paper.get("authors", [])[:6]) or "Unknown authors"
    abstract = (paper.get("summary", "") or "").strip()
    return "\n".join(
        [
            f"{index}. {paper['title']}",
            f"Authors: {authors}",
            f"Link: {paper['link']}",
            f"Category: {paper['category']}",
            f"Paper type: {paper.get('paper_type', 'Unclear')}",
            f"Relevance score: {paper['relevance_score']}",
            f"Abstract: {abstract}",
        ]
    )


def render_digest(papers: list[dict[str, Any]], config: dict[str, Any]) -> dict[str, Any]:
    today = datetime.now().date().isoformat()
    max_highlighted = int(config["digest"]["highlighted_papers"])
    weak_threshold = float(config["digest"]["weak_match_threshold"])

    relevant_papers = [paper for paper in papers if _is_relevant(paper)]
    strong_papers = [paper for paper in relevant_papers if paper["relevance_score"] >= weak_threshold]
    highlighted = strong_papers[:max_highlighted]

    if not strong_papers:
        subject = f"{config['notification']['subject_prefix']} - {today}"
        weak_lines = [
            "No important new papers today.",
            "",
            "Weak matches:",
        ]
        weak_lines.extend(
            f"- {paper['title']} ({paper['relevance_score']}) - {paper['link']}" for paper in relevant_papers[:max_highlighted]
        )
        if not relevant_papers:
            weak_lines.append("- No recent papers matched the current search window.")
        body = "\n".join(weak_lines)
        return {
            "subject": subject,
            "plain_text": body,
            "markdown": body,
            "papers": relevant_papers,
            "highlighted": [],
        }

    subject = f"{config['notification']['subject_prefix']} - {today}"
    sections = ["# Daily Muon Paper Digest", "", "## Top Highlights", ""]

    for index, paper in enumerate(highlighted, start=1):
        sections.append(_paper_block(index, paper))
        sections.append("")

    sections.append("## Full Top 10")
    sections.append("")
    for index, paper in enumerate(relevant_papers[: config["digest"]["max_papers"]], start=1):
        sections.append(_paper_block(index, paper))
        sections.append("")

    markdown = "\n".join(sections).strip()
    return {
        "subject": subject,
        "plain_text": markdown,
        "markdown": markdown,
        "papers": relevant_papers[: config["digest"]["max_papers"]],
        "highlighted": highlighted,
    }
