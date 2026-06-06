# Muon Paper Agent

`muon-paper-agent` is a GitHub Actions driven research scout for Muon-related papers. Every morning it searches recent papers, ranks them for Muon relevance, builds a compact digest, and emails the result.

## What It Does

- Searches arXiv for papers from the last 48 hours using Muon-adjacent keywords.
- Scores each paper using explicit relevance signals.
- Classifies papers into Muon-relevant categories.
- Summarizes the top matches with an OpenAI model when available.
- Falls back to keyword-based summaries if the OpenAI API is unavailable.
- Sends a daily email via SMTP.
- Stores paper state in `data/seen_papers.json` to avoid repeat sends.

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
    send_email.py
    storage.py
  data/
    seen_papers.json
    daily_digest.md
```

For the current workspace layout, the active GitHub Actions file is also placed at [`.github/workflows/daily_muon_digest.yml`](/Users/eleanor/Desktop/Candidacy writing exam/.github/workflows/daily_muon_digest.yml). The duplicate copy inside `muon-paper-agent/` keeps the project self-contained if you later make that folder its own repository root.

## GitHub Secrets

Add these repository secrets in `Settings -> Secrets and variables -> Actions`:

- `OPENAI_API_KEY`
- `SEMANTIC_SCHOLAR_API_KEY`
- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USERNAME`
- `SMTP_PASSWORD`
- `EMAIL_FROM`
- `EMAIL_TO`

`SEMANTIC_SCHOLAR_API_KEY` is optional. If it is missing, enrichment is skipped.

## Manual Run

1. Open the repository on GitHub.
2. Go to `Actions`.
3. Select `Daily Muon Paper Digest`.
4. Click `Run workflow`.

The workflow also runs every day at `9:00 AM America/Los_Angeles`.

## Changing Keywords

Edit `config.yaml` and update the `keywords` list. The arXiv query builder will OR these terms together.

## Changing the Email Recipient

Update the `EMAIL_TO` GitHub secret. You can also change `EMAIL_FROM` if your SMTP provider requires a different sender address.

## Debugging Failed Runs

1. Open the latest workflow run in `Actions`.
2. Inspect the `Run daily digest` step logs.
3. Confirm secrets are populated and valid.
4. Check whether the SMTP provider blocked login or required an app password.
5. Look at `data/daily_digest.md` in the repo after a successful run to inspect the rendered digest content.

## Local Development

Run locally from the project directory:

```bash
pip install -r requirements.txt
python main.py
```

If `OPENAI_API_KEY` is unset or the OpenAI request fails, the agent still sends a simpler digest using rule-based summaries.
