# Recommended Tech Stack for Home Service Companies

## Guiding Principle

One tool that's fully implemented beats five tools with 20% adoption each. When evaluating or recommending a tech stack, the question is not "which software has the most features" — it's "which software will this team actually use, and what is the minimum viable stack to run this operation well?"

Build the stack in layers: FSM/CRM first (the operational core), then accounting integration, then communication, then automation. Don't add layer three until layer one is solid.

---

## Layer 1: Field Service Management (FSM) / CRM — The Core

The FSM is the most important tool in a home service company. It handles scheduling, dispatch, job management, estimates, invoices, and ideally customer history. Everything else plugs into it.

### ServiceTitan
**Best for:** $3M+ roofing, HVAC, plumbing, electrical companies scaling aggressively
**Strengths:** Most feature-complete FSM on the market. Best reporting and KPI tracking. Native payroll, marketing ROI tracking, dispatch board, flat-rate pricing. Strong for companies that need enterprise-level operations.
**Weaknesses:** High cost ($400–$800+/month depending on tier). Steep learning curve. Overkill for companies under $2M. Implementation takes 60–120 days to do properly. Sales process is aggressive.
**Price range:** $400–$1,500+/month; requires implementation fee

### Jobber
**Best for:** Landscaping, cleaning, smaller HVAC/plumbing companies; $500K–$5M range
**Strengths:** Intuitive UI, fast to implement, excellent mobile app, strong customer communication features, QBO integration. Best "startup FSM" — can be functional in a week.
**Weaknesses:** Weaker reporting than ServiceTitan. No flat-rate pricing natively. Limited for complex dispatch-heavy operations. Not built for multi-crew roofing.
**Price range:** $50–$250/month

### HouseCall Pro
**Best for:** Smaller service companies ($500K–$3M) that prioritize ease of use and customer experience features
**Strengths:** Consumer-grade UI, strong automated customer communication (confirmations, reminders, review requests), competitive pricing, solid dispatch board.
**Weaknesses:** Reporting is shallow. Not well-suited for complex job costing. Less powerful than ServiceTitan at scale.
**Price range:** $65–$250/month

### FieldEdge / Service Fusion / Workiz
**Use cases:** FieldEdge is HVAC/plumbing-specific and respected in those trades. Service Fusion offers competitive pricing with decent features for the range. Workiz is strong for smaller service companies and solo operators.

**Decision Framework:**
- Under $2M, growing: Jobber or HouseCall Pro
- $2M–$8M, service-heavy (HVAC, plumbing): FieldEdge or HouseCall Pro
- $3M+, roofing or multi-trade: ServiceTitan if willing to invest in implementation
- Already on a platform: do NOT switch unless it's costing more than the switch costs

---

## Layer 2: Accounting

### QuickBooks Online (QBO)
**Industry standard for home service under $20M.** Integrates natively with every major FSM. Bookkeepers and fractional CFOs all know it. The cost ($35–$100/month) is irrelevant.

**Critical:** QBO is only as good as the chart of accounts design and the discipline to code transactions correctly. The default QBO setup for a home service company is almost always wrong. A proper COA should separate revenue by service line, materials from labor in COGS, and have clear overhead categories.

Do not use QuickBooks Desktop in a new engagement — cloud-only from here forward.

### Alternatives
**Wave:** Free but limited. Adequate for solo operators just starting. No FSM integration. Do not recommend for clients over $500K.
**FreshBooks:** Better invoicing UX than QBO but weaker reporting. Not recommended for home service.
**Sage Intacct / NetSuite:** Enterprise-tier. Only relevant if client is $15M+ with complex multi-entity needs.

---

## Layer 3: Communication and Customer Experience

### Phone System
**Dialpad or RingCentral:** Cloud VOIP with call recording, routing, and analytics. Essential for companies that want to track lead source attribution and coach sales calls. Integrates with most CRMs.
**CallRail:** Best-in-class for call tracking and marketing attribution. Not a full phone system but a must-have if running Google Ads.

### Internal Communication
**Slack:** Best for teams >5 people. Creates channels for operations, dispatch, sales. Reduces text/email noise.
**Google Chat (Workspace):** Free if already on Google Workspace. Less powerful than Slack but adequate for small teams.
**Text/group text:** Works for very small teams but does not scale. No searchability, no integrations.

### Customer Communication
Best-in-class FSMs (HouseCall Pro, ServiceTitan) have this built in. If the FSM doesn't cover it, add:
- **Podium or NiceJob:** Review request automation, webchat, text messaging hub. Strong for driving Google reviews.

---

## Layer 4: HR and People

### ADP or Gusto (Payroll)
**Gusto:** Best for companies under 50 employees. Clean UI, benefits administration, direct deposit, W-2/1099 handling. $6–$12 per employee per month.
**ADP:** More powerful at scale (50+ employees). Higher cost, more complexity. Worth it at $10M+ with 40+ employees.

### Applicant Tracking
**Workable or Breezy HR:** Affordable ATS for companies that are actively hiring. Structured scorecards, interview guides, offer letters. $150–$300/month.
**Indeed + manual tracking:** Adequate for 2–5 hires per year. Below that threshold, no ATS is necessary.

---

## Layer 5: Automation and AI

See `automation-playbook.md` for full detail. Tools in this layer:
- **Zapier:** Easiest to implement for non-technical users. Connects FSM → QBO → communication tools. Higher cost at scale.
- **Make (formerly Integromat):** More powerful and cheaper than Zapier at volume. Requires slightly more technical setup.
- **n8n:** Open-source, self-hostable automation. Best for companies with technical resources or a fractional operator building custom flows. Free at self-hosted tier.
- **AI Agents (Claude API, ChatGPT API via n8n):** Emerging. Already viable for: lead triage, job summary generation, automated reporting narratives, customer service first response.

---

## Recommended Stack by Company Size

**$500K–$2M (Early Systems Stage)**
- FSM: Jobber or HouseCall Pro
- Accounting: QBO Simple Start
- Communication: Google Workspace
- HR: Gusto
- Automation: Zapier (basic tier)
- Total cost: ~$200–$400/month

**$2M–$8M (Scaling Operations Stage)**
- FSM: ServiceTitan or FieldEdge
- Accounting: QBO Plus
- Communication: Dialpad + CallRail + Slack
- HR: Gusto + Workable
- Automation: Make or Zapier
- Total cost: ~$1,000–$2,500/month

**$8M–$20M (Mature Operations Stage)**
- FSM: ServiceTitan (Enterprise)
- Accounting: QBO Advanced
- Communication: RingCentral + CallRail + Slack
- HR: ADP + Workable
- Automation: n8n + AI agents
- BI/Reporting: ServiceTitan dashboards + supplemental Looker Studio
- Total cost: ~$3,000–$6,000/month
