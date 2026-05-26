"""
scheduled_fieldy.py — Daily Fieldy pipeline entry point

Runs all three Fieldy integrations in sequence:
  1. ingest/fieldy.py     → RAG (Supabase pgvector)
  2. obsidian/fieldy_to_obsidian.py → Obsidian vault notes
  3. digest/fieldy_digest.py → Slack daily digest

One failure does NOT block the others. Exit code:
  0 = all succeeded
  1 = one or more failures

Usage:
    python scheduled_fieldy.py              # default: last 24 hrs
    python scheduled_fieldy.py --hours 48   # custom window
    python scheduled_fieldy.py --dry-run    # print only, no writes

Cron (6 AM daily):
    0 6 * * * cd /path/to/fieldy && /usr/bin/python3 scheduled_fieldy.py >> /tmp/fieldy.log 2>&1
"""

import sys
import logging
import argparse
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger(__name__)


def run_ingest(start_dt, end_dt, dry_run):
    log.info("━━━ STEP 1/3: RAG Ingestion (Supabase) ━━━")
    try:
        from ingest.fieldy import run
        ingested, skipped, errors = run(start_dt, end_dt, dry_run=dry_run)
        log.info("RAG ingest complete — ingested: %d, skipped: %d, errors: %d",
                 ingested, skipped, errors)
        return errors == 0
    except Exception as exc:
        log.error("RAG ingest FAILED: %s", exc, exc_info=True)
        return False


def run_obsidian(start_dt, end_dt, dry_run):
    log.info("━━━ STEP 2/3: Obsidian Sync ━━━")
    try:
        from obsidian.fieldy_to_obsidian import run
        written, skipped, errors = run(start_dt, end_dt, dry_run=dry_run)
        log.info("Obsidian sync complete — written: %d, skipped: %d, errors: %d",
                 written, skipped, errors)
        return errors == 0
    except Exception as exc:
        log.error("Obsidian sync FAILED: %s", exc, exc_info=True)
        return False


def run_digest(start_dt, end_dt, dry_run):
    log.info("━━━ STEP 3/3: Slack Digest ━━━")
    try:
        from digest.fieldy_digest import run
        run(start_dt, end_dt, dry_run=dry_run)
        log.info("Slack digest complete")
        return True
    except Exception as exc:
        log.error("Slack digest FAILED: %s", exc, exc_info=True)
        return False


def parse_args():
    parser = argparse.ArgumentParser(description="Daily Fieldy pipeline runner")
    parser.add_argument("--hours", type=float, default=24,
                        help="Look-back window in hours (default: 24)")
    parser.add_argument("--start", help="Start date YYYY-MM-DD (overrides --hours)")
    parser.add_argument("--end",   help="End date YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print output only — no DB writes, no Slack posts, no file writes")
    parser.add_argument("--skip-ingest",  action="store_true", help="Skip RAG ingest step")
    parser.add_argument("--skip-obsidian", action="store_true", help="Skip Obsidian sync step")
    parser.add_argument("--skip-digest",  action="store_true", help="Skip Slack digest step")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    now = datetime.now(timezone.utc)

    if args.start:
        start_dt = datetime.fromisoformat(args.start).replace(tzinfo=timezone.utc)
        end_dt   = (
            datetime.fromisoformat(args.end).replace(tzinfo=timezone.utc)
            if args.end else now
        )
    else:
        end_dt   = now
        start_dt = end_dt - timedelta(hours=args.hours)

    log.info("Fieldy pipeline starting | window: %s → %s | dry_run: %s",
             start_dt.strftime("%Y-%m-%d %H:%M UTC"),
             end_dt.strftime("%Y-%m-%d %H:%M UTC"),
             args.dry_run)

    results = {}

    if not args.skip_ingest:
        results["ingest"]  = run_ingest(start_dt, end_dt, args.dry_run)

    if not args.skip_obsidian:
        results["obsidian"] = run_obsidian(start_dt, end_dt, args.dry_run)

    if not args.skip_digest:
        results["digest"]  = run_digest(start_dt, end_dt, args.dry_run)

    # Summary
    log.info("━━━ PIPELINE SUMMARY ━━━")
    all_ok = True
    for step, ok in results.items():
        status = "✓ OK" if ok else "✗ FAILED"
        log.info("  %s: %s", step.upper(), status)
        if not ok:
            all_ok = False

    if all_ok:
        log.info("All steps completed successfully.")
        sys.exit(0)
    else:
        log.warning("One or more steps failed — check logs above.")
        sys.exit(1)
