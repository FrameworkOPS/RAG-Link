#!/usr/bin/env python3
"""
fieldy_digest.py — Daily Fieldy digest posted to Slack.

Summarises yesterday's Fieldy conversations using Claude Haiku,
then posts a structured breakdown to the configured Slack channel
via incoming webhook.

Env vars:
    FIELDY_API_KEY         sk-f-...
    ANTHROPIC_API_KEY      sk-ant-...
    SLACK_WEBHOOK_URL      https://hooks.slack.com/services/...
    SLACK_DIGEST_CHANNEL   (optional, for display only — webhook already targets a channel)

Usage:
    python fieldy_digest.py              # yesterday
    python fieldy_digest.py --hours 48   # last 48 hrs
    python fieldy_digest.py --dry-run    # print to terminal, skip Slack
"""

import os, sys, time, json, logging, argparse
from datetime import datetime, timedelta, timezone

import requests
import anthropic
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

FIELDY_API_KEY    = os.environ["FIELDY_API_KEY"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")
FIELDY_BASE       = "https://api.fieldy.ai/api/public/v2"

try:
    import certifi
    VERIFY = certifi.where()
except ImportError:
    VERIFY = True

_fsess = requests.Session()
_fsess.headers.update({"Authorization": f"Bearer {FIELDY_API_KEY}"})


# ── Fieldy fetch ──────────────────────────────────────────────────────────────
def fetch_conversations(start: datetime, end: datetime) -> list[dict]:
    items, cursor = [], None
    while True:
        params = {"startTime": start.isoformat(), "endTime": end.isoformat(), "per_page": 50}
        if cursor:
            params["cursor"] = cursor
        r = _fsess.get(f"{FIELDY_BASE}/conversations", params=params, verify=VERIFY, timeout=20)
        r.raise_for_status()
        data  = r.json()
        batch = data.get("items", [])
        items.extend(batch)
        cursor = data.get("nextCursor")
        if not cursor or not batch:
            break
        time.sleep(0.4)
    return items


def fetch_tasks(status: str = "new") -> list[dict]:
    items, cursor = [], None
    while True:
        params = {"status": status, "per_page": 50}
        if cursor:
            params["cursor"] = cursor
        r = _fsess.get(f"{FIELDY_BASE}/tasks", params=params, verify=VERIFY, timeout=20)
        r.raise_for_status()
        data  = r.json()
        batch = data.get("items", [])
        items.extend(batch)
        cursor = data.get("nextCursor")
        if not cursor or not batch:
            break
        time.sleep(0.3)
    return items


# ── Claude digest ─────────────────────────────────────────────────────────────
DIGEST_PROMPT = """You are a personal operations assistant for Chance Peare, fractional COO of Framework OPS LLC.

Below are Fieldy wearable AI conversations recorded over the past {hours} hours. These capture Chance's real-world conversations, thoughts, and interactions.

Summarise this into a daily operations digest with these sections:

## 🎯 Key Business Decisions
Any decisions made, commitments given, or strategic choices discussed.

## 🔨 Work & Client Activity  
Work-related conversations, client interactions, project updates.

## ✅ Action Items Captured
Any tasks, follow-ups, or to-dos mentioned.

## 💡 Notable Notes
Anything else worth remembering — observations, ideas, personal notes.

Keep it concise and useful. Skip personal/trivial content (family routines, errands). Focus on what matters for running Framework OPS and Skyright.

---
CONVERSATIONS:
{conversations}
"""

def generate_digest(conversations: list[dict], open_tasks: list[dict], hours: int) -> str:
    conv_text = "\n\n---\n\n".join(
        f"**{c.get('title', 'Untitled')}**\n{c.get('summary') or c.get('content') or '(no content)'}"
        for c in conversations
    )

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    msg = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1500,
        messages=[{
            "role": "user",
            "content": DIGEST_PROMPT.format(hours=hours, conversations=conv_text or "(no conversations recorded)")
        }]
    )
    digest = msg.content[0].text

    if open_tasks:
        task_lines = "\n".join(f"• {t['title']}" for t in open_tasks[:10])
        digest += f"\n\n## 📋 Open Tasks ({len(open_tasks)} total)\n{task_lines}"

    return digest


# ── Slack post ────────────────────────────────────────────────────────────────
def post_to_slack(text: str, date_label: str):
    if not SLACK_WEBHOOK_URL:
        log.warning("SLACK_WEBHOOK_URL not set — skipping Slack post. Set it in .env")
        return False

    payload = {
        "text": f"*Fieldy Daily Digest — {date_label}*",
        "blocks": [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": f"Fieldy Digest — {date_label}"}
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": text[:3000]}
            }
        ]
    }
    r = requests.post(SLACK_WEBHOOK_URL, json=payload, verify=VERIFY, timeout=15)
    r.raise_for_status()
    log.info("Posted to Slack ✓")
    return True


# ── Main ──────────────────────────────────────────────────────────────────────
def run(hours: int = 24, dry_run: bool = False):
    now      = datetime.now(timezone.utc)
    start    = now - timedelta(hours=hours)
    date_lbl = start.strftime("%b %d") + " – " + now.strftime("%b %d, %Y")

    log.info(f"Fetching Fieldy conversations ({hours}hrs)…")
    conversations = fetch_conversations(start, now)
    log.info(f"  {len(conversations)} conversations")

    log.info("Fetching open tasks…")
    open_tasks = fetch_tasks("new")
    log.info(f"  {len(open_tasks)} open tasks")

    if not conversations and not open_tasks:
        log.info("Nothing to digest.")
        return

    log.info("Generating digest with Claude Haiku…")
    digest = generate_digest(conversations, open_tasks, hours)

    if dry_run:
        print(f"\n{'='*60}")
        print(f"FIELDY DIGEST — {date_lbl}")
        print('='*60)
        print(digest)
        print('='*60)
        return

    post_to_slack(digest, date_lbl)
    log.info("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hours",   type=int, default=24)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run(hours=args.hours, dry_run=args.dry_run)
