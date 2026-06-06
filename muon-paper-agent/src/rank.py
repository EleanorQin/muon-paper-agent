from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

PHYSICS_TERMS = [
    "neutrino",
    "supernova",
    "cosmic ray",
    "muon collider",
    "high-energy",
    "astrophysical",
    "magnet",
    "hadron",
    "detector",
    "icecube",
    "gamma ray",
]

OPTIMIZATION_TERMS = [
    "optimizer",
    "optimization",
    "training",
    "gradient",
    "precondition",
    "llm",
    "language model",
    "attention",
    "transformer",
    "matrix",
    "shampoo",
    "newton-schulz",
]

ML_CONTEXT_TERMS = [
    "llm",
    "language model",
    "transformer",
    "pretraining",
    "fine-tuning",
    "neural network",
    "deep learning",
    "model training",
    "attention",
    "autoregressive",
]

GENERIC_MATH_OPT_TERMS = [
    "monotone operator",
    "hilbert space",
    "cocoercive",
    "forward-backward splitting",
    "maximal monotone",
    "variational inequality",
    "performative prediction",
]

THEORY_TERMS = [
    "theorem",
    "proof",
    "lemma",
    "proposition",
    "corollary",
    "convergence",
    "bound",
    "theoretical",
    "quadratic",
    "curvature perspective",
    "analysis",
]

EXPERIMENT_TERMS = [
    "experiment",
    "empirical",
    "benchmark",
    "ablation",
    "evaluation",
    "pretraining",
    "training efficiency",
    "results",
    "dataset",
    "implementation",
    "scalability",
]

MUON_CORE_TERMS = [
    "muon optimizer",
    "orthogonalized momentum",
    "newton-schulz",
    "matrix sign",
    "orthogonalized",
    "spectral scaling laws of muon",
    "demuon",
]

MUON_ADJACENT_TERMS = [
    "preconditioning",
    "shampoo",
    "second-order",
    "natural gradient",
    "spectral norm",
    "low-rank",
    "curvature",
    "optimizer",
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


def _categorize(text: str, paper_type: str) -> str:
    if _contains_any(text, PHYSICS_TERMS):
        return "Not Relevant"
    if _contains_any(text, MUON_CORE_TERMS):
        return "Muon Core"
    if _contains_any(text, MUON_ADJACENT_TERMS):
        if paper_type == "Theory":
            return "Muon-Adjacent Theory"
        if paper_type == "Experiment":
            return "Muon-Adjacent Experiments"
        if paper_type == "Theory + Experiment":
            return "Muon-Adjacent Theory+Experiments"
    return "Not Relevant"


def _paper_type(text: str) -> str:
    has_theory = _contains_any(text, THEORY_TERMS)
    has_experiment = _contains_any(text, EXPERIMENT_TERMS)
    if has_theory and has_experiment:
        return "Theory + Experiment"
    if has_theory:
        return "Theory"
    if has_experiment:
        return "Experiment"
    return "Unclear"


def _is_muon_core(text: str) -> bool:
    return _contains_any(text, MUON_CORE_TERMS)


def _is_muon_adjacent(text: str) -> bool:
    has_adjacent_term = _contains_any(text, MUON_ADJACENT_TERMS)
    has_ml_context = _contains_any(text, ML_CONTEXT_TERMS)
    has_muon_context = "muon" in text or _contains_any(text, ["orthogonalized", "newton-schulz", "shampoo", "matrix preconditioning"])
    return has_adjacent_term and (has_ml_context or has_muon_context)


def rank_papers(papers: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    weights = config["ranking"]["signal_weights"]
    ranked: list[dict[str, Any]] = []

    for paper in papers:
        text = _combined_text(paper)
        has_muon_term = "muon" in text
        has_optimization_context = _contains_any(text, OPTIMIZATION_TERMS)
        has_physics_context = _contains_any(text, PHYSICS_TERMS)
        has_ml_context = _contains_any(text, ML_CONTEXT_TERMS)
        has_generic_math_opt = _contains_any(text, GENERIC_MATH_OPT_TERMS)
        signals = {
            "direct_muon_match": _contains_any(text, ["muon optimizer", "orthogonalized momentum"]) or (has_muon_term and has_optimization_context and not has_physics_context),
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
        if has_physics_context:
            score -= float(weights.get("particle_physics_penalty", 0.0))
        if has_generic_math_opt and not has_ml_context and not has_muon_term:
            score -= float(weights.get("generic_math_optimization_penalty", 0.0))

        semantic = paper.get("semantic_scholar", {})
        if isinstance(semantic, dict) and semantic.get("citation_count", 0):
            score += min(float(semantic.get("citation_count", 0)) / 50.0, 1.0) * float(weights.get("citation_bonus", 0.0))

        paper["signals"] = signals
        paper["relevance_score"] = round(max(score, 0.0), 2)
        paper["paper_type"] = _paper_type(text)
        if _is_muon_core(text):
            paper["category"] = "Muon Core"
        elif _is_muon_adjacent(text):
            if paper["paper_type"] == "Theory":
                paper["category"] = "Muon-Adjacent Theory"
            elif paper["paper_type"] == "Experiment":
                paper["category"] = "Muon-Adjacent Experiments"
            elif paper["paper_type"] == "Theory + Experiment":
                paper["category"] = "Muon-Adjacent Theory+Experiments"
            else:
                paper["category"] = "Muon-Adjacent Theory"
        else:
            paper["category"] = "Not Relevant"
        ranked.append(paper)

    ranked.sort(key=lambda item: (item["relevance_score"], item.get("updated_at", "")), reverse=True)
    return ranked
