from __future__ import annotations

import logging
import os
from typing import Any

import requests

LOGGER = logging.getLogger(__name__)


def _truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def _paper_lines(index: int, paper: dict[str, Any]) -> str:
    summary = paper["digest_summary"]
    return "\n".join(
        [
            f"*{index}. <{paper['link']}|{paper['title']}>*",
            f"Category: {paper['category']} | Score: {paper['relevance_score']}",
            f"Summary: {_truncate(summary['one_sentence_summary'], 280)}",
            f"Why it matters: {_truncate(summary['why_it_matters'], 280)}",
            f"Action: {summary['recommended_action']} | Use: {summary['potential_use']}",
        ]
    )


def _build_payload(digest: dict[str, Any]) -> dict[str, Any]:
    highlighted = digest.get("highlighted", [])
    papers = digest.get("papers", [])

    if not highlighted:
        text = digest["plain_text"]
        return {
            "text": digest["subject"],
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": _truncate(text, 2900)},
                }
            ],
        }

    blocks: list[dict[str, Any]] = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": digest["subject"][:150]},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Top highlights:* {len(highlighted)} | *Total papers:* {len(papers)}",
            },
        },
        {"type": "divider"},
    ]

    for index, paper in enumerate(highlighted, start=1):
        blocks.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": _truncate(_paper_lines(index, paper), 2900)},
            }
        )
        blocks.append({"type": "divider"})

    if len(papers) > len(highlighted):
        remainder = [
            f"{index}. <{paper['link']}|{paper['title']}> ({paper['relevance_score']}, {paper['category']})"
            for index, paper in enumerate(papers[len(highlighted):], start=len(highlighted) + 1)
        ]
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Additional papers:*\n" + _truncate("\n".join(remainder), 2900),
                },
            }
        )

    return {
        "text": digest["subject"],
        "blocks": blocks,
    }


def send_digest_slack(digest: dict[str, Any], config: dict[str, Any]) -> None:
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        LOGGER.warning("Skipping Slack notification because SLACK_WEBHOOK_URL is missing")
        return

    try:
        response = requests.post(webhook_url, json=_build_payload(digest), timeout=30)
        response.raise_for_status()
        LOGGER.info("Digest posted to Slack")
    except requests.RequestException as exc:
        LOGGER.warning("Failed to post digest to Slack: %s", exc)
