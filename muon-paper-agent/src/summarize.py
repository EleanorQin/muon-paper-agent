from __future__ import annotations

import json
import logging
import os
from typing import Any

from openai import OpenAI

LOGGER = logging.getLogger(__name__)


def _rule_based_summary(paper: dict[str, Any], config: dict[str, Any]) -> dict[str, str]:
    score = float(paper["relevance_score"])
    thresholds = config["ranking"]["category_thresholds"]
    if score >= float(thresholds["must_read"]):
        action = "Must read"
    elif score >= float(thresholds["skim"]):
        action = "Skim"
    else:
        action = "Ignore"

    category = paper.get("category", "Other Possibly Useful")
    title = paper.get("title", "")
    summary_text = paper.get("summary", "")
    why = f"This looks relevant because it falls under {category.lower()} and matched several Muon-adjacent ranking signals."

    use_hint = "Future work"
    lower = f"{title} {summary_text}".lower()
    if "proof" in lower or "theorem" in lower:
        use_hint = "Proof idea"
    elif "experiment" in lower or "benchmark" in lower:
        use_hint = "Experiment"
    elif "related work" in lower or "survey" in lower:
        use_hint = "Related work"

    sentence = summary_text.split(". ")[0].strip() if summary_text else "Recent optimization paper potentially related to Muon."
    technical = "Matched signals: " + ", ".join(
        name for name, matched in paper.get("signals", {}).items() if matched
    )

    return {
        "one_sentence_summary": sentence.rstrip(".") + ".",
        "why_it_matters": why,
        "technical_notes": technical,
        "recommended_action": action,
        "potential_use": use_hint,
    }


def _build_prompt(paper: dict[str, Any]) -> str:
    payload = {
        "title": paper.get("title"),
        "authors": paper.get("authors"),
        "summary": paper.get("summary"),
        "category": paper.get("category"),
        "relevance_score": paper.get("relevance_score"),
        "signals": paper.get("signals"),
    }
    return (
        "You are summarizing new research papers for a Muon optimizer research digest.\n"
        "Return strict JSON with keys: one_sentence_summary, why_it_matters, technical_notes, "
        "recommended_action, potential_use.\n"
        "Recommended action must be one of: Must read, Skim, Ignore.\n"
        "Potential use must be one of: Related work, Proof idea, Experiment, Future work.\n"
        "Be concise, technical, and grounded in the provided metadata.\n"
        f"Paper metadata:\n{json.dumps(payload, ensure_ascii=True)}"
    )


def summarize_papers(papers: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not papers:
        return papers

    client = OpenAI(api_key=api_key) if api_key else None
    model = config["digest"]["summary_model"]

    for paper in papers:
        paper["digest_summary"] = _rule_based_summary(paper, config)
        if not client:
            continue

        try:
            response = client.responses.create(
                model=model,
                input=_build_prompt(paper),
                temperature=0.2,
            )
            content = response.output_text.strip()
            parsed = json.loads(content)
            paper["digest_summary"] = {
                "one_sentence_summary": parsed["one_sentence_summary"],
                "why_it_matters": parsed["why_it_matters"],
                "technical_notes": parsed["technical_notes"],
                "recommended_action": parsed["recommended_action"],
                "potential_use": parsed["potential_use"],
            }
        except Exception as exc:
            LOGGER.warning("OpenAI summarization failed for '%s': %s", paper.get("title"), exc)

    return papers
