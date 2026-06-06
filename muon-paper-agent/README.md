# Muon Paper Agent

`muon-paper-agent` is a GitHub Actions driven research scout for Muon-related papers. Every morning it searches recent papers, ranks them for Muon relevance, builds a compact digest, and posts the result to Slack.

## What It Does

- Searches arXiv for papers from the last 48 hours using Muon-adjacent keywords.
- Scores each paper using explicit relevance signals.
- Classifies papers into `Muon Core`, `Muon-Adjacent Theory`, `Muon-Adjacent Experiments`, `Muon-Adjacent Theory+Experiments`, or `Not Relevant`.
- Labels each paper as `Theory`, `Experiment`, `Theory + Experiment`, or `Unclear`.
- Summarizes the top matches with an OpenAI model when available.
- Falls back to keyword-based summaries if the OpenAI API is unavailable.
- Sends a daily Slack digest via incoming webhook, prioritizing near-full abstracts over extra commentary.
- Stores paper state in `data/seen_papers.json` to avoid repeat sends.
- Archives each daily digest in `data/archive/` so old runs stay visible in GitHub.

## Repository Layout

```text
muon-paper-agent/
  main.py
  requirements.txt
  config.yaml
  README.md
  .github/workflows/daily_muon_digest.yml
  src/
    __init__.py
    fetch_arxiv.py
    fetch_semantic_scholar.py
    fetch_openreview.py
    deduplicate.py
    rank.py
    summarize.py
    render_email.py
    send_slack.py
    storage.py
  data/
    seen_papers.json
    daily_digest.md
    archive/
      YYYY-MM-DD.md
```

For the current workspace layout, the active GitHub Actions file is also placed at [`.github/workflows/daily_muon_digest.yml`](/Users/eleanor/Desktop/Candidacy writing exam/.github/workflows/daily_muon_digest.yml). The duplicate copy inside `muon-paper-agent/` keeps the project self-contained if you later make that folder its own repository root.

## GitHub Secrets

Add these repository secrets in `Settings -> Secrets and variables -> Actions`:

- `OPENAI_API_KEY`
- `SEMANTIC_SCHOLAR_API_KEY`
- `SLACK_WEBHOOK_URL`

`SEMANTIC_SCHOLAR_API_KEY` is optional. If it is missing, enrichment is skipped.
`SLACK_WEBHOOK_URL` is the incoming webhook URL for the Slack channel that should receive the digest.

## Creating the Slack Webhook

1. Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps).
2. Enable `Incoming Webhooks`.
3. Click `Add New Webhook to Workspace`.
4. Pick the channel where you want the digest posted.
5. Copy the generated webhook URL and save it as the `SLACK_WEBHOOK_URL` GitHub secret.

## Manual Run

1. Open the repository on GitHub.
2. Go to `Actions`.
3. Select `Daily Muon Paper Digest`.
4. Click `Run workflow`.

The workflow also runs every day at `9:00 AM America/Los_Angeles`.

## Changing Keywords

Edit `config.yaml` and update the `keywords` list. The arXiv query builder will OR these terms together.

## Changing the Slack Destination

Update the `SLACK_WEBHOOK_URL` GitHub secret to point to a webhook for a different channel.

## Debugging Failed Runs

1. Open the latest workflow run in `Actions`.
2. Inspect the `Run daily digest` step logs.
3. Confirm secrets are populated and valid.
4. Check whether the Slack webhook URL is still valid and points to the intended channel.
5. Look at `data/daily_digest.md` for the latest output and `data/archive/` for historical daily digests.

## Local Development

Run locally from the project directory:

```bash
pip install -r requirements.txt
python main.py
```

If `OPENAI_API_KEY` is unset or the OpenAI request fails, the agent still sends a simpler digest using rule-based summaries.
