from __future__ import annotations

import logging
from pathlib import Path

from src.deduplicate import filter_new_papers
from src.fetch_arxiv import fetch_recent_arxiv_papers
from src.fetch_openreview import enrich_with_openreview
from src.fetch_semantic_scholar import enrich_with_semantic_scholar
from src.rank import rank_papers
from src.render_email import render_digest
from src.send_slack import send_digest_slack
from src.storage import load_config, load_seen_state, save_digest_markdown, save_seen_state
from src.summarize import summarize_papers


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def main() -> None:
    configure_logging()
    logger = logging.getLogger("muon-paper-agent")

    base_dir = Path(__file__).resolve().parent
    config = load_config(base_dir / "config.yaml")
    seen_state = load_seen_state(base_dir / "data" / "seen_papers.json")

    logger.info("Starting daily Muon digest run")
    logger.info("Searching arXiv with %d keywords", len(config["keywords"]))

    papers = fetch_recent_arxiv_papers(config)
    logger.info("Fetched %d recent papers from arXiv", len(papers))

    papers = enrich_with_semantic_scholar(papers)
    papers = enrich_with_openreview(papers)

    scored_papers = rank_papers(papers, config)
    fresh_papers = filter_new_papers(scored_papers, seen_state, config)
    logger.info("%d papers remain after deduplication/state filtering", len(fresh_papers))

    selected_papers = fresh_papers[: config["digest"]["max_papers"]]
    summarized_papers = summarize_papers(selected_papers, config)

    digest = render_digest(summarized_papers, config)
    save_digest_markdown(base_dir / "data" / "daily_digest.md", digest["markdown"])

    send_digest_slack(digest, config)
    save_seen_state(base_dir / "data" / "seen_papers.json", seen_state, summarized_papers)

    logger.info(
        "Digest completed: %d highlighted, %d total entries",
        len(digest["highlighted"]),
        len(digest["papers"]),
    )


if __name__ == "__main__":
    main()
