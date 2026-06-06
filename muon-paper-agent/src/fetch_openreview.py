from __future__ import annotations

import logging

LOGGER = logging.getLogger(__name__)


def enrich_with_openreview(papers: list[dict[str, object]]) -> list[dict[str, object]]:
    # Placeholder hook for later OpenReview enrichment.
    LOGGER.info("OpenReview enrichment is not configured yet; skipping")
    return papers
