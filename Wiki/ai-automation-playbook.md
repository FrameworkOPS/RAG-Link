---
title: AI & Automation Playbook
date: 2026-05-27
source: manual
type: wiki
tags: [ai, automation, playbook, home-services, tech-stack, implementation]
---

# AI & Automation Playbook

## Framework OPS Automation Philosophy
Every client engagement includes at least one automation or AI implementation. This is a differentiator — not an add-on. The goal is to reduce manual labor, increase data visibility, and let the owner/leadership team focus on high-value decisions.

## Home Service Company Automation Stack (Typical Buildout)

### Tier 1 — Quick Wins (First 30 Days)
1. **Automated job completion notifications** — CRM trigger → text/email to customer
2. **Lead routing automation** — New inbound lead → assign to rep → notify in Slack/Teams
3. **Invoice follow-up sequences** — Unpaid invoice aging → automated reminder sequence
4. **Daily ops digest** — Pull KPIs from CRM/job management → Slack message to leadership
5. **Scheduling gap alerts** — Calendar + job board integration → flag crew downtime

### Tier 2 — Process Automation (30–90 Days)
1. **Estimate-to-job conversion** — Approved estimate → auto-create job, schedule crew, trigger materials order
2. **Technician check-in/check-out** — GPS + job management → auto-log hours, trigger completion workflow
3. **Customer review requests** — Job closed → automated Google/Trustpilot review request (timing-optimized)
4. **Payroll prep automation** — Timecard data → formatted for ADP/Gusto processing
5. **AR aging report** — Weekly automated report to owner with overdue balance list

### Tier 3 — AI Implementation (60–180 Days)
1. **AI call analysis** — Record inbound calls → AI summary + sentiment → flag at-risk customers
2. **Estimate assistant** — AI reads job photos + scope → draft estimate + materials list
3. **Internal knowledge base** — RAG system with SOPs, pricing, policies → answer employee questions
4. **Lead scoring** — AI scores inbound leads by likelihood to close + job size
5. **Performance coaching** — AI analyzes technician data → flag coaching opportunities for managers

## Common Tools by Function
| Function | Tool Options |
|----------|-------------|
| CRM / Job Management | ServiceTitan, Jobber, HouseCall Pro, FieldEdge |
| Automation platform | Zapier, Make (Integromat), n8n (self-hosted) |
| AI assistant | Claude (Anthropic), GPT-4, industry-specific models |
| Communication | Slack, Teams, Ringcentral |
| Reporting | Looker Studio, Power BI, custom QBO dashboards |
| RAG/Knowledge base | Supabase + pgvector + Claude (Framework OPS stack) |

## RAG Knowledge Base (Framework OPS Signature)
Chance's flagship AI implementation for clients:
- Ingest SOPs, training docs, pricing guides, FAQs into Supabase pgvector
- Connect to Claude via MCP server
- Employees can ask natural language questions → get accurate answers from company knowledge base
- Reduces onboarding time, reduces management overhead for repetitive questions

## AI Tool Selection Criteria
When evaluating AI tools for a client:
1. **Data security**: Will proprietary data leave the company? (Critical for acquirers)
2. **Integration**: Does it connect to existing CRM/job management?
3. **Training curve**: Will the crew actually use it?
4. **ROI timeline**: Measurable impact within 90 days or deprioritize
5. **Vendor stability**: Is this a startup that may shut down?

## Automation Red Flags
- Client wants to automate before core process is documented → Document first
- Automation built on unstable data (bad CRM hygiene) → Clean data first
- Tool selected by owner without ops input → Evaluate fit before committing
- Over-automating customer touchpoints → Keep human moments human
