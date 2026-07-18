---
title: Daniel / William — Client Acquisition & Automation Review
date: 2026-05-26
participants: [Chance Peare, Daniel Kalinin]
source: fathom
type: meeting
url: https://fathom.video/calls/688071219
tags: [daniel, lead-statement, client-acquisition, automation, l10]
---

# Daniel / William — Client Acquisition & Automation Review
**Date:** May 26, 2026
**Participants:** Chance Peare (William Peare), Daniel Kalinin
**Recording:** [View on Fathom](https://fathom.video/calls/688071219)

---

## Summary

Progress and next-steps review for Daniel's Lead Statement engagement. Two revenue-generating systems are now live — a B2B outreach campaign targeting tax firms, and a daily contractor-license scraper feeding the Close CRM. The Claude copywriting pipeline is functional and the immediate next build is integrating Higgsfield to generate video ads from scripts. Client acquisition is the stated #1 priority; Upwork profile needs updating to match the higher-ticket positioning.

---

## Key Takeaways

- **B2B Outreach is launching:** Personalized GammaDocs + Loom video targeting tax firms with 50+ Google reviews. Metric benchmark: 1 client per 200 outreaches. Tracking via UTM → Calendly → ClickUp GammaDoc ID. Non-responders enter cold email sequence via Smart Lead.
- **Home Service Lead Gen is live:** Daily scraper pulling new CA/OR/WA contractor licenses → Close CRM → sales rep (Daniel's fiancé's brother). Model: $97/mo, LTV projection 25–40 months, high upsell potential. Railway hosting 24/7.
- **Claude Copywriting Pipeline is functional:** Brief → Ideation → QA → Scripting → QA → ClickUp task. Daniel feeds repeated feedback to train the model. Next step: integrate Higgsfield for video generation.
- **Immediate priorities:** Client acquisition, video automation pipeline completion, Upwork profile update for higher-ticket positioning.

---

## Topics

### Client Acquisition Strategy

**Goal:** Drive immediate cash flow through new client acquisition.

**B2B Outreach — Tax Firms**
- Target: Established firms with 50+ Google reviews
- Package: $6k/quarter
- Method: Personalized GammaDocs + Loom video + 10 ad examples per outreach
- Tracking: UTM parameters linking Calendly bookings to GammaDoc ID in ClickUp
- Follow-up: Non-responders enter cold email sequence via Smart Lead
- Benchmark: 1 client per 200 outreaches (Daniel's stated assumption — needs validation as data comes in)

**Home Service Lead Gen**
- Mechanism: Daily scraper pulling new contractor licenses from CA, OR, WA state databases
- Destination: Close CRM → sales rep (Daniel's fiancé's brother)
- Pricing model: $97/mo
- LTV assumption: 25–40 months (conservative end of that range is more realistic at this stage)
- Infrastructure: Railway for 24/7 hosting, Supabase for data storage

### Automation & Systems

**Claude Copywriting Pipeline (Live)**
- Flow: Brief → Ideation → QA → Scripting → QA → ClickUp task creation
- Daniel is iterating with repeated feedback to improve model output quality
- Current state: functional; refinement ongoing

**Video Generation Pipeline (Next Build)**
- Flow: Claude dissects script into 10-second chunks → Higgsfield generates video → files saved to Google Drive
- Open research question: whether Claude can view video output to auto-flag and regenerate out-of-sync clips
- This is the completion milestone for the automation build before moving to the next project

**Infrastructure Stack**
- Railway: 24/7 server hosting for the lead scraper
- Supabase: data storage layer
- Claude Remote Routines (Max plan, 15/day): scheduled server-side task execution
- Claude Live Artifacts: real-time dashboards

---

## Action Items

- [ ] **Daniel** — Update Upwork profile to attract higher-ticket clients
- [ ] **Daniel** — Record and send ≥50 personalized GammaDoc/Loom outreaches to tax firms
- [ ] **Daniel** — Test the Close CRM integration for the home service lead-gen project
- [ ] **Daniel** — Complete the Claude-to-Higgsfield video automation pipeline
- [ ] **Daniel** — Call leads from contractor list to validate scraper accuracy

---

## Transcript

> *Note: Transcript source file was unavailable at ingest time (temp path expired). Full recording available at [fathom.video/calls/688071219](https://fathom.video/calls/688071219).*
