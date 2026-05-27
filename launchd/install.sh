#!/bin/bash
# install.sh — Install Framework OPS daily automation agents on macOS
# Run once: bash ~/Documents/Framework-OPS/launchd/install.sh

set -e

LAUNCH_AGENTS="$HOME/Library/LaunchAgents"
FRAMEWORK_OPS="$HOME/Documents/Framework-OPS"

echo "Installing Framework OPS LaunchAgents..."

# ── Install dependencies ───────────────────────────────────────────────────
echo "→ Installing Python dependencies..."
pip3 install httpx "httpx[socks]" python-dotenv supabase --break-system-packages -q

# Fieldy extras (openai, anthropic, slack-sdk, requests)
if [ -f "$FRAMEWORK_OPS/fieldy/requirements_fieldy.txt" ]; then
    pip3 install -r "$FRAMEWORK_OPS/fieldy/requirements_fieldy.txt" \
        --break-system-packages -q
fi

echo "→ Python deps installed."

# ── Copy plists to LaunchAgents ────────────────────────────────────────────
mkdir -p "$LAUNCH_AGENTS"

cp "$FRAMEWORK_OPS/launchd/com.frameworkops.fathom.plist" "$LAUNCH_AGENTS/"
cp "$FRAMEWORK_OPS/launchd/com.frameworkops.fieldy.plist"  "$LAUNCH_AGENTS/"

echo "→ Plists copied to $LAUNCH_AGENTS"

# ── Load agents ────────────────────────────────────────────────────────────
launchctl unload "$LAUNCH_AGENTS/com.frameworkops.fathom.plist" 2>/dev/null || true
launchctl unload "$LAUNCH_AGENTS/com.frameworkops.fieldy.plist"  2>/dev/null || true

launchctl load "$LAUNCH_AGENTS/com.frameworkops.fathom.plist"
launchctl load "$LAUNCH_AGENTS/com.frameworkops.fieldy.plist"

echo ""
echo "✓ LaunchAgents installed and loaded."
echo ""
echo "Schedule:"
echo "  Fathom → daily at 7:00 AM  | log: ~/Library/Logs/frameworkops-fathom.log"
echo "  Fieldy → daily at 7:05 AM  | log: ~/Library/Logs/frameworkops-fieldy.log"
echo ""
echo "NEXT STEPS:"
echo "  Add Slack token to fieldy/.env if you want the daily digest:"
echo "     SLACK_BOT_TOKEN=xoxb-..."
echo "     SLACK_DIGEST_CHANNEL=C0B5RN4JSE7"
echo ""
echo "Test Fathom pipeline (dry run):"
echo "  cd $FRAMEWORK_OPS/fathom && python3 scheduled_fathom.py --dry-run"
echo ""
echo "Test Fieldy pipeline (dry run):"
echo "  cd $FRAMEWORK_OPS/fieldy && python3 scheduled_fieldy.py --dry-run"
