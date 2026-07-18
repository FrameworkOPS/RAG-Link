---
title: AI and Automation Playbook — Framework OPS
date: 2026-05-27
source: manual
type: wiki
tags: [framework-ops, wiki, automation, ai, n8n, zapier, make, home-service, playbook]
---

# AI and Automation Playbook — Framework OPS

## Philosophy

At $5M revenue with 20 employees, a home service company is spending roughly $80K–$150K per year on manual tasks that could be partially or fully automated. The highest-value targets are repetitive, rules-based processes where timing and consistency matter: follow-up, confirmations, reminders, reviews, and reporting.

Automation does not replace people — it removes the low-value tasks that distract people from high-value work.

**Framework OPS approach:** Build one automation, let it run for 2–4 weeks, confirm it works, then build the next one. Automation debt (broken flows no one monitors) is worse than no automation. The sequence matters more than the speed.

---

## Priority Tier 1: High Impact, Low Complexity

Build these first. Each delivers measurable ROI quickly.

### 1. Lead Response / Follow-Up Automation

**Problem:** Leads not contacted within 5 minutes convert at 10x the rate of leads contacted after 30 minutes. Most home service companies take 30 minutes to 24 hours.

**Automation:** New lead (web form, Google LSA, paid ad) → immediate SMS + email to prospect → if no response in 2 hours, second message → if no response in 24 hours, create task in FSM for manual follow-up.

**Tools:** Zapier/Make + Twilio (SMS) + FSM webhook. Or native to HouseCall Pro/ServiceTitan for connected lead sources.

**Expected lift:** 15–30% increase in estimate scheduling rate from existing lead volume.

**Build time:** 2–4 hours for a competent builder.

---

### 2. Appointment Confirmation and Reminders

**Problem:** No-shows and "forgot about you" cancellations cost 1–3% of total scheduled capacity.

**Automation:** 48-hour confirmation SMS/email asking customer to confirm → 2-hour day-of reminder with tech name and arrival window → if customer doesn't respond to confirmation, dispatcher flagged to call manually.

**Tools:** Most FSMs (HouseCall Pro, ServiceTitan, Jobber) have this native. If not: Zapier + Twilio.

**Expected lift:** 30–50% reduction in no-shows and late cancellations.

---

### 3. Invoice and Payment Follow-Up

**Problem:** Invoices sitting unpaid extend DSO and create cash flow drag. Manual collection calls take admin time.

**Automation:** Invoice sent automatically at job completion via FSM → if unpaid at 3 days: reminder SMS/email → if unpaid at 7 days: second reminder + phone call task assigned → if unpaid at 14 days: overdue notice with payment link.

**Tools:** Native to most FSMs. Integrate with Stripe or Square for payment link. QBO for AR reconciliation.

**Expected lift:** 5–10 day reduction in DSO for the average invoice. At $5M revenue with 35-day current DSO, this recovers significant working capital.

---

### 4. Review Request Automation

**Problem:** Most customers who have a good experience don't leave reviews unless asked. Most companies don't ask consistently.

**Automation:** 24–48 hours after job completion and invoice paid → personalized SMS asking for Google review with direct link → if customer clicked but didn't review, one follow-up 72 hours later.

**Tools:** NiceJob or Podium ($200–$400/month, purpose-built). Or build in Make/Zapier + FSM.

**Expected lift:** 3–5x increase in monthly review volume. Compounding effect on local SEO over 6–12 months.

---

## Priority Tier 2: High Impact, Medium Complexity

These deliver significant value but require more setup time or integration work.

### 5. Automated Weekly Reporting

**Problem:** Owner spends 2–4 hours per week manually compiling revenue, close rate, and job cost data. Or doesn't do it at all — no visibility.

**Automation:** Scheduled weekly query of FSM data + QBO → compile into Google Sheet or dashboard → send summary email/Slack to owner every Monday morning with key metrics.

**Metrics to include:** Revenue vs. goal (week and MTD), jobs completed, close rate, gross margin (if job costing is clean), AR balance.

**Tools:** Make or n8n + FSM API + QBO API + Google Sheets API. ServiceTitan has scheduled reports natively.

**Time saved:** 2–4 hours/week.

---

### 6. Hiring Funnel Automation

**Problem:** Job applicants apply on Indeed and wait days for a response. Top candidates take other offers. Manual screening is time-consuming.

**Automation:** Indeed application → Zapier trigger → automated acknowledgment email with pre-screening questionnaire (Google Form) → qualified candidates automatically receive calendar link to schedule phone screen.

**Tools:** Indeed webhook/RSS + Zapier + Google Forms + Calendly.

**Expected lift:** 40–60% reduction in time to first phone screen.

---

### 7. Seasonal Reactivation Campaigns

**Problem:** Past customers who haven't booked in 12+ months are low-hanging revenue. No one has time to manually contact 500 past customers.

**Automation:** Monthly or quarterly, pull customers from FSM where last job date > 12 months → send personalized reactivation SMS/email → suppress active customers and unsubscribes.

**Expected lift:** 3–8% reactivation rate. At 500 cold contacts and $500 average job, that's $7,500–$20,000 in revenue per campaign.

---

## Priority Tier 3: Emerging AI Automation

These are newer and require more technical setup but are increasingly viable.

### 8. AI-Powered Lead Triage

**Problem:** Not all leads are equal. Dispatchers spend time on tire-kickers, wrong-area requests, and low-budget jobs.

**Automation:** Lead comes in via web form or inbound call transcript → sent to AI model with prompt that categorizes urgency, scope, likelihood to convert → high-quality leads routed immediately, low-quality leads given lower-priority follow-up.

**Tools:** n8n + Claude API or OpenAI API. Twilio for call transcription.

**Maturity:** Viable for technically capable teams or with a builder's help.

---

### 9. AI Job Summary for Techs

**Problem:** Field techs spend 15–30 minutes on admin after each job.

**Automation:** Tech dictates a 60-second voice note at job closeout → AI transcribes and generates structured job notes → auto-populates FSM job notes field.

**Tools:** OpenAI Whisper (transcription) + Claude/GPT for formatting → FSM API.

---

### 10. Automated P&L Commentary

**Problem:** Monthly financials reviewed but no one writes the narrative explaining variances. Owner lacks context for decisions.

**Automation:** QBO API pulls monthly P&L → sends to AI model with prior month for comparison → generates 3–5 sentence narrative summary of key variances → delivered in the weekly report email.

**Tools:** QBO API + n8n + Claude API.

**Note:** Chance runs a version of this for himself via the Framework OPS RAG and Claude integration.

---

## Implementation Sequence

**Month 1:** Lead response automation + appointment confirmations
**Month 2:** Review requests + invoice follow-up
**Month 3:** Weekly reporting automation
**Month 4+:** Reactivation campaigns, hiring automation, AI tools (lead triage, job summaries)

---

## Tool Selection Guide

| Tool | Best for | Cost | Technical bar |
|---|---|---|---|
| **Zapier** | Simple integrations, non-technical client teams | $20–$200/mo (task-based pricing) | Low |
| **Make (Integromat)** | Complex multi-step flows, better value at volume | $10–$100/mo | Medium |
| **n8n** | Open source, AI agent integration, maximum flexibility | Free (self-hosted) or $20/mo cloud | Medium-High |
| **HouseCall Pro native** | Appointment confirmations, review requests, basic follow-up | Included in FSM cost | Very low |
| **ServiceTitan native** | Reporting, marketing automation for ST customers | Included in FSM cost | Low |
| **NiceJob / Podium** | Review automation specifically | $200–$400/mo | Very low |

**Decision rule:** If the FSM already does it, don't build it in Zapier. If Zapier does it cleanly, don't build it in n8n. Use the lowest-complexity tool that gets the job done — operational complexity you don't need is technical debt.

---

## How Framework OPS Uses Automation Internally

Framework OPS practices what it sells. Chance runs the following automations in his own practice:

**Meeting capture pipeline:**
- Fathom records every client call
- Fathom transcript → n8n pipeline → format and chunk → Voyage AI embed → Supabase ingest
- Result: every client meeting is searchable via the RAG within hours of the call ending

**Weekly reporting:**
- Planned: QBO API + Mercury → weekly financial summary → delivered to Chance via Slack

**ClickUp integration:**
- Fathom meeting summary → n8n → ClickUp task creation for action items
- LinkedIn content queue → ClickUp calendar

**AI assistance:**
- Claude (via FastMCP + Supabase RAG) has full context of every client meeting, all playbooks, all wikis
- Used for: drafting proposals, answering client questions with context, building automation flows

---

## Common Automation Failures to Avoid

1. **Building automations before the manual process is stable.** If the team doesn't do the process consistently by hand, the automation will amplify the inconsistency. Document and stabilize the process first.

2. **No monitoring or error handling.** Automations break silently. Every automation needs a notification when it fails. At minimum: Slack or email alert when a workflow errors.

3. **Automating the wrong things first.** Companies that automate their expense reports before their lead follow-up have misaligned priorities. Follow the Tier 1 → 2 → 3 sequence.

4. **No ownership.** Someone on the client's team needs to own each automation. Not just "Chance set it up" — someone internal who can troubleshoot a broken Zap or Make scenario.

5. **Over-engineering.** An n8n flow with 40 nodes to replace a 5-minute task is not a win. Automation should reduce cognitive load on the team, not transfer it to the automation itself.

---

## AI Tooling Landscape (2026)

Relevant AI tools for home service operations and how Framework OPS evaluates them:

| Tool | Use case | Status |
|---|---|---|
| **Claude API (Anthropic)** | Document generation, meeting summaries, P&L commentary, lead triage, RAG retrieval | Production — Chance uses this daily |
| **Fathom** | Meeting transcription and summary | Production — all client calls |
| **Fieldy** | Wearable ambient AI capture | Active — field use |
| **n8n + Claude** | AI agent workflows for clients | Active builds |
| **OpenAI Whisper** | Voice-to-text for tech job summaries | Viable, being tested |
| **ChatGPT / GPT-4** | Alternative to Claude for some client workflows | Evaluated case-by-case |

**Framework OPS position:** Claude API is the default AI layer. The RAG + FastMCP architecture means every AI-assisted action in the practice has full context of client history, benchmarks, and playbooks. This is the core technical advantage over a generic AI assistant.

---

## Related Files
- Automation playbook (client-facing): knowledge-base/playbooks/automation-playbook.md
- Client tech stack recommendations: knowledge-base/playbooks/tech-stack-home-service.md
- Framework OPS internal tech stack: Wiki/tech-stack.md
