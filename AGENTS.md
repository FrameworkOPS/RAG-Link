# Framework OPS — Project Instructions

This file is the operating context for any Codex session working in this repo. Read it before doing anything else. It governs business context, voice, file conventions, financial guardrails, and the pricing-modeling workstream that's active right now.

---

## 1. Who This Project Is

**Framework OPS LLC** is a fractional COO consulting practice serving home service companies ($2M–$20M revenue: roofing, HVAC, plumbing, electrical, landscaping, pest, painting, garage door, pool). Founder is **Chance Peare** — currently a sitting COO at a large roofing company, BBA/MBA, 10+ years of org leadership. Framework OPS is **just launching**. It is not an established firm with a book of business. Treat every recommendation as pre-revenue: low ego, conservative assumptions, no fictional case studies.

**Differentiator:** Lived home-service operator experience (not borrowed expertise) + heavy lean into AI/automation as a value driver.

**Banking:** Mercury. **Bookkeeping:** QBO. **Knowledge base:** Obsidian vault rooted at `knowledge-base/`.

---

## 2. Repo Map — Where Things Live

| Path | What's there | When to touch |
|---|---|---|
| `knowledge-base/business/` | Service tiers, ICP, engagement process, proposal/onboarding/diagnostic templates, LinkedIn positioning, ClickUp client scaffold | Source of truth for offer, pricing, ICP, and client project structure. Edit here when business strategy shifts. |
| `knowledge-base/playbooks/` | Industry benchmarks (roofing, HVAC), KPI library, SOP framework, automation playbook, cash flow, tech stack, top 10 problems | Reference material for client work and content. Update when benchmarks change or new playbooks are needed. |
| `knowledge-base/clients/` | Per-client briefs (e.g., `daniel-lead-statement-brief.md`) | Create one per active engagement using `_templates/client-brief-template.md`. Living docs. |
| `knowledge-base/meetings/` | Meeting notes by client | Use `_templates/meeting-notes-template.md`. |
| `knowledge-base/_templates/` | Obsidian templates: SOP, client brief, meeting notes | Use these. Don't reinvent structure. |
| `backend/` `frontend/` `supabase/` `copilot/` | RAG/chat app over the KB (FastAPI + Next.js + Supabase + Voyage + Anthropic) | Technical infra. Leave alone unless explicitly asked. |

When you create a new doc, **place it in the right folder and use the matching template**. The Obsidian vault is rooted at `knowledge-base/` — anything outside that path won't show up in the vault.

---

## 3. Service Menu (Current Pricing — Source of Truth)

Pricing is in `knowledge-base/business/service-tiers.md`. Summary:

**Entry / Trust Builders** (defined deliverables, foot-in-the-door)
- AI Readiness Assessment — $297
- Tech Stack Audit — $497
- OPS Assessment — $997 ⭐ (credits to retainer Month 1 if signed within 30 days)

**Productized Sprints** (fixed scope, 2–4 weeks)
- SOP Sprint — $1,500–$2,500
- Automation Build Sprint — $1,500–$3,000
- 90-Day Roadmap Sprint — $2,000–$3,500

**Retainers** (ongoing fractional COO)
- Advisory — $1,500/mo, 3-mo min, 4–6 hrs
- Light — $2,500/mo, 3-mo min, 8–12 hrs
- **Active — $4,000/mo, 6-mo min, 15–20 hrs** ⭐ most common
- Embedded — $6,000/mo, 6–12 mo min, 30–40 hrs

**Add-ons:** On-site days $1,500–$2,500, automation builds $750–$2,000, SOP packages $1,500–$2,500, tech-stack implementation $2,000–$5,000.

**Rules:** Don't discount to close — scope down instead. Don't present multiple tiers in a proposal — do the diagnostic, then propose one tier. Don't propose without completing the OPS Assessment / diagnostic.

---

## 4. Ideal Client Profile (Use This to Pressure-Test Everything)

- $2M–$20M revenue; sweet spot $2M–$8M (80% of pipeline)
- Owner-operator, still in the weeds, decision maker
- 5–75 employees, at least one office staffer to implement with
- Home service trades only — **NOT** remodeling/GC, retail, manufacturing, franchise units
- Three or more of these buying triggers: declining gross margin, owner approves every estimate, near-miss on payroll, key-person departure, unused software, no vacation in 2+ years, recent failed COO/ops hire

**Disqualifiers:** Pre-revenue/<$1M, consultant carousel history, owner won't implement, active turnaround (losing money), ego-locked owner. Detail in `knowledge-base/business/fractional-coo-ideal-client.md`.

---

## 5. Voice, Tone, and Working Style

Chance's stated preferences — these override any default Codex personality:

- **Straight answers, no fluff.** Don't agree to be agreeable. If you don't have data, say so.
- **Always pessimistic on financial forecasting and scaling projections.** Solo founders overestimate close rates and underestimate ramp time. Stress-test every revenue assumption.
- **Operator language, not consultant language.** "Job costing," "callbacks," "DSO," "draw schedule," "FSM" — use the vocabulary in `playbooks/`. Avoid corporate jargon ("synergy," "leverage best practices," "holistic," "ecosystem").
- **No bullet-list reports unless asked.** Prose for analysis; tables for comparisons; bullets only when actually listing items.
- **Specific over vague.** "Improve operations" is banned. "Build a 13-week rolling cash flow model in Google Sheets, train the office manager, install a Monday review cadence — delivered by Day 45" is the standard.
- **Quantify the cost of every problem you name.** Naming "no job costing" isn't enough — say what it costs at this revenue level.

When drafting client-facing content (proposals, LinkedIn posts, emails): follow `knowledge-base/business/linkedin-positioning.md` and `proposal-structure.md`. No AI-flavored writing — this audience is hands-on and will spot it.

---

## 6. Active Workstream: Pricing Model to Determine Client Needs at Launch

**The current priority.** Chance is launching the practice and needs a pricing model that answers, for any inbound prospect:
1. Can this client afford a Framework OPS engagement at the tier that would actually fix their problem?
2. Which tier (Advisory / Light / Active / Embedded — or Entry product / Sprint) is the right starting point given their revenue, gross profit, owner pain, and implementation capacity?
3. What's the conservative ROI math we can show in the proposal?

### Inputs the model needs from a prospect
Pulled from the discovery call + pre-intake form (`engagement-process.md` Stage 1–2):
- Annual revenue (trailing 12 months)
- Gross margin % (or COGS structure if unknown)
- Net profit % (or estimated)
- Employee count + office staff count
- Owner hours/week (proxy for delegation infrastructure)
- Trade vertical (roofing / HVAC / plumbing / etc. — drives benchmark lookup)
- Top 3 stated problems (mapped to the 10 in `playbooks/home-service-common-problems.md`)
- Tech stack maturity (FSM in use? job costing live? KPI dashboard?)
- Budget range (asked directly per the discovery call SOP)

### Outputs the model needs to produce
- **Affordability check:** retainer cost as % of monthly gross profit and % of monthly net profit. Flag if retainer > 15% of monthly net.
- **Tier recommendation:** Entry product / Sprint / Advisory / Light / Active / Embedded — with rationale tied to revenue band and pain profile.
- **Conservative ROI range:** value creation estimate using benchmark gap math (e.g., current GM% vs. trade benchmark from `playbooks/`), explicitly capped at the conservative end. Never quote upside without quoting downside.
- **Go / No-Go / Wait flag:** Go (fit), No-Go (disqualified), Wait (right industry, wrong stage — keep warm).

### Modeling guardrails (non-negotiable)
- **Pessimistic by default.** Use the low end of every benchmark range in `playbooks/roofing-operations-benchmarks.md` and `hvac-operations-benchmarks.md`. Assume client implements 60–70% of recommendations, not 100%. Assume ramp time is double what the optimistic case suggests.
- **Capacity math, not aspiration math.** Chance can realistically deliver ~3 Active retainers + 1 Embedded simultaneously while still COO at the roofing company. Solo capacity ceiling is the binding constraint, not market demand.
- **Year-1 revenue projections cap at 50% of "fully booked."** New consulting practices undersell, miss-close, and have sales cycles of 2–4 weeks minimum. Model accordingly.
- **No customer LTV math borrowed from SaaS.** Home-service fractional COO retainers run 6–18 months realistically, not "forever." Model churn at 30%+ annually.
- **The OPS Assessment ($997) is the gateway product**, not the retainer. Most pipeline math should run through Entry → Sprint or Entry → Retainer, not direct-to-retainer.

### Use of code/tools for the pricing model
- **xlsx skill** for the working model — Chance needs to manipulate inputs himself. Build it as a spreadsheet with input cells, lookup tables (benchmarks per trade), and output cells.
- **docx skill** for the narrative explainer Chance can hand to a prospect or use internally.
- **No Python scripts as deliverables** unless Chance asks for code. He's the operator using this, not a developer running a CLI.

When you start pricing-model work in a new session, default to: load `knowledge-base/business/service-tiers.md` and `knowledge-base/business/fractional-coo-ideal-client.md`, plus the relevant benchmark playbook for the trade in question, before touching the spreadsheet.

---

## 7. Engagement Process — How Real Client Work Flows

Detailed in `knowledge-base/business/engagement-process.md`. Six stages, 2–4 weeks contact to kickoff:
1. **Discovery call** (30–45 min) — mutual qualify against ICP
2. **Pre-diagnostic intake** (written form, 60–90 min of client time)
3. **Operational diagnostic** (90 min + doc review, paid if standalone, included in retainer)
4. **Proposal** (4–6 pages, PDF, walked through live, 7-day expiration)
5. **Agreement + kickoff** (within 5 business days of signed + paid)
6. **Ongoing:** 30-day diagnostic phase → 60-day quick wins → 90-day review

**Hard rules:** No proposal without a completed diagnostic. No kickoff without signed agreement AND first month's payment. No open-ended proposals.

---

## 8. Client Work Defaults

When working on a client account in `knowledge-base/clients/<client>/`:

- Read the client brief in full before suggesting anything
- Apply the client's stated tech stack — don't propose new platforms unless there's a gap the current stack can't fill
- Use the priority order in the brief (e.g., for Daniel: capacity → consistency → financial clarity)
- Conservative financial projections always — stress-test conversion rates, close rates, ramp times
- Don't recommend hiring before systems are documented
- Don't recommend automation before the manual process is stable

For meeting notes, use `_templates/meeting-notes-template.md`. For new client briefs, use `_templates/client-brief-template.md`.

---

## 9. Content + LinkedIn Defaults

Per `knowledge-base/business/linkedin-positioning.md`:
- 3–5 posts/week, mostly text-only or carousels
- 80% educational/story content, 20% or less explicit positioning
- Content pillars: industry benchmarks (35%), field stories (30%), tactical how-to (25%), POV/contrarian (10%)
- Use specific numbers and named tools (ServiceTitan, QBO, Mercury, Make, etc.). Generic content gets ignored
- Don't write motivational content. Don't post AI-flavored prose. This audience reads through that

For any content draft: use the **marketing:draft-content** skill if heavy lift, but match the operator voice in `playbooks/` — not generic marketing voice.

---

## 10. What NOT to Do

- Don't invent client case studies or testimonials. Framework OPS is launching — there is no portfolio yet.
- Don't quote upside ROI without quoting the conservative case alongside it.
- Don't recommend tools that aren't in `playbooks/tech-stack-home-service.md` without strong justification.
- Don't propose retainer tiers as a menu in a proposal. Diagnose, then propose one.
- Don't write proposals or content over 6 pages without a clear reason — busy operators don't read them.
- Don't touch the `backend/`, `frontend/`, or `supabase/` code unless explicitly asked.
- Don't add documentation/README files unprompted.

---

## 11. File Conventions

- Markdown only inside `knowledge-base/`. Obsidian renders it; PDF/docx exports happen on demand for client deliverables.
- All KB files use frontmatter when the template has it. Preserve `type:`, `tags:`, and `last_updated:` fields.
- New client artifacts: `knowledge-base/clients/<client-slug>/` — brief at the top, meeting notes, working docs nested below.
- Deliverables for prospects/clients (xlsx, docx, pdf): build in workspace, save to workspace folder root for Chance to grab.

---

## 12. Quick Reference — When Stuck

| Question | File to read first |
|---|---|
| What's the price? | `knowledge-base/business/service-tiers.md` |
| Is this a real client? | `knowledge-base/business/fractional-coo-ideal-client.md` |
| How does the sale flow? | `knowledge-base/business/engagement-process.md` |
| How do I write the proposal? | `knowledge-base/business/proposal-structure.md` |
| What does "good" look like for this trade? | `knowledge-base/playbooks/<trade>-operations-benchmarks.md` |
| What KPIs matter? | `knowledge-base/playbooks/home-service-kpi-library.md` |
| What's the real problem they have? | `knowledge-base/playbooks/home-service-common-problems.md` |
| What tools should they use? | `knowledge-base/playbooks/tech-stack-home-service.md` |
| What automation matters first? | `knowledge-base/playbooks/automation-playbook.md` |
| How do I onboard a new client? | `knowledge-base/business/onboarding-checklist.md` |
| How is client work structured in ClickUp? | `knowledge-base/business/clickup-client-scaffold.md` |

## Framework OPS brand system

Treat `DESIGN_SYSTEM.md` and `design/brand/brand-system.json` as core product
knowledge. Apply them to every branded or interactive surface. The July 2026
UI/UX handoff governs v1.1 implementation corrections and supersedes
conflicting v1.0 interaction rules. Use the checked-in semantic tokens; do not
invent visual values in components. Do not claim `ui-verified` until responsive,
WCAG 2.2 AA, state, microcopy, and AI-trust requirements have been tested.
