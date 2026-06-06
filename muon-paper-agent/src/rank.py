from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


CATEGORY_RULES = [
    ("Direct Muon", ["muon"]),
    ("Orthogonalized Updates / Newton-Schulz", ["orthogonalized", "newton-schulz", "matrix sign"]),
    ("Matrix Preconditioning / Shampoo / Second-order", ["preconditioning", "shampoo", "second-order", "natural gradient"]),
    ("Spectral Norm / Low-rank Geometry", ["spectral norm", "spectral", "low-rank"]),
    ("LLM Training Stability / Attention / QK-clip", ["llm", "training stability", "attention", "qk", "logit clipping"]),
    ("Bilevel Optimization Related", ["bilevel", "hypergradient", "meta-learning"]),
]


def _combined_text(paper: dict[str, Any]) -> str:
    return " ".join(
        [
            paper.get("title", ""),
            paper.get("summary", ""),
            " ".join(paper.get("categories", [])),
        ]
    ).lower()


def _contains_any(text: str, needles: list[str]) -> bool:
    return any(needle in text for needle in needles)


def _recency_score(updated_at: str) -> float:
    try:
        updated = datetime.fromisoformat(updated_at)
    except ValueError:
        return 0.0
    age_hours = max((datetime.now(timezone.utc) - updated).total_seconds() / 3600.0, 0.0)
    if age_hours <= 12:
        return 1.0
    if age_hours <= 24:
        return 0.75
    if age_hours <= 48:
        return 0.5
    return 0.0


def _categorize(text: str) -> str:
    for label, triggers in CATEGORY_RULES:
        if _contains_any(text, triggers):
            return label
    return "Other Possibly Useful"


def rank_papers(papers: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    weights = config["ranking"]["signal_weights"]
    ranked: list[dict[str, Any]] = []

    for paper in papers:
        text = _combined_text(paper)
        signals = {
            "direct_muon_match": _contains_any(text, ["muon optimizer", "muon", "orthogonalized momentum"]),
            "optimizer_match": _contains_any(text, ["optimizer", "optimization", "training"]),
            "orthogonalization_match": _contains_any(text, ["orthogonal", "orthogonalized", "newton-schulz", "matrix sign"]),
            "spectral_norm_match": _contains_any(text, ["spectral norm", "spectral", "logit clipping", "qk clip"]),
            "llm_training_stability_match": _contains_any(text, ["llm", "language model", "training stability", "attention"]),
            "bilevel_relevance_match": _contains_any(text, ["bilevel", "hypergradient", "meta-learn", "implicit differentiation"]),
            "second_order_match": _contains_any(text, ["second-order", "newton", "curvature", "shampoo", "precondition"]),
            "low_rank_geometry_match": _contains_any(text, ["low-rank", "manifold", "geometry"]),
        }

        score = 0.0
        for signal_name, matched in signals.items():
            if matched:
                score += float(weights.get(signal_name, 0.0))

        score += _recency_score(str(paper.get("updated_at", ""))) * float(weights.get("recency", 0.0))

        semantic = paper.get("semantic_scholar", {})
        if isinstance(semantic, dict) and semantic.get("citation_count", 0):
            score += min(float(semantic.get("citation_count", 0)) / 50.0, 1.0) * float(weights.get("citation_bonus", 0.0))

        paper["signals"] = signals
        paper["relevance_score"] = round(score, 2)
        paper["category"] = _categorize(text)
        ranked.append(paper)

    ranked.sort(key=lambda item: (item["relevance_score"], item.get("updated_at", "")), reverse=True)
    return ranked
