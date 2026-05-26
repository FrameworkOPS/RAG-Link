# Deferred to Phase 2 (Months 3-6, Post-Launch)

These ideas are explicitly NOT being built in the 60-day plan. Listed here so they don't get accidentally pulled forward and so the rationale is preserved.

## SOP Generator from Recorded Videos

**Concept:** Feed a Loom/Fathom recording of an operator doing a task → output a clean SOP draft in standard format, with decision points flagged.

**Why deferred:** Useful, but doesn't directly close clients. Build after 3+ engagements have generated enough recordings to test against real-world variance.

## Second Brain Sync

**Concept:** Fathom transcripts + Gmail + ClickUp + Drive piped into a searchable index Chance can query.

**Why deferred:** Highest-leverage build for a disorganized operator, but complex. Requires multiple API integrations + vector DB. Build after volume justifies (3+ active clients = enough data to make worth indexing).

## N8N Workflow Auditor

**Concept:** Reads exported workflow JSON, flags single points of failure, missing error handling, hardcoded values, security issues.

**Why deferred:** Useful for client audits, but only matters when auditing 5+ N8N implementations. Most $1-3M ICP doesn't have N8N yet.

## Client-Facing Dashboards

**Concept:** Take CSV export from ServiceTitan, Housecall Pro, Jobber, etc. → build ops dashboard.

**Why deferred:** High value but high build cost. Wait until 3+ clients are asking for the same metrics — then build the right thing.

## AI Chatbot on Website

**Concept:** Lead qualification chatbot for inbound prospects.

**Why deferred:** Inbound volume at 400 connections + 60 days outreach will be near zero. Solving a problem that doesn't exist yet.

## Other tempting builds to NOT pull forward

- Roofing/HVAC-specific KPI calculators
- Proposal generator from discovery questionnaire
- Automated LinkedIn content generator
- ROI calculators for prospects
- Industry benchmark dashboards
- Slack-integrated client portal

## Rule for deciding to pull forward

A Phase 2 build can be promoted to Phase 1 only if:
1. A paying client has explicitly asked for it, AND
2. Building it would meaningfully accelerate that engagement, AND
3. It's reusable across at least 2 future clients

Otherwise it waits.

## Related files
- [[60-day-overview]]
- [[build-philosophy]]
