# Audit System

The productized OPS Assessment ($997) delivery system. Built Weeks 4-5.

## Goal

Take manual audit delivery (10-12 hours per client) down to 4-6 hours through templating and automation.

## Components

### 1. Structured intake form

**Tool:** Tally or Typeform
**Linked to:** ClickUp Sales & Pipeline (auto-creates lead record)

**Fields collected:**
- Company info (name, revenue range, sub-vertical, employee count, geography)
- Owner background and goals
- Current tech stack
- Current team structure
- Top 3 operational pain points
- Recent attempts to fix
- Specific outcomes hoped for from audit

### 2. Scoring rubric

10 operational dimensions, scored 1-5:

1. Lead intake
2. Sales handoff
3. Scheduling
4. Job execution
5. Quality control
6. Collections
7. Customer follow-up
8. Hiring / onboarding
9. Financial close
10. Owner dependency

**Scoring guide:**
- 1 = Nonexistent / chaotic / owner does it all manually
- 2 = Some process but inconsistent / undocumented
- 3 = Documented but not consistently followed
- 4 = Documented + followed but not optimized
- 5 = Optimized + improving

Each dimension gets a written assessment + score + top 1-2 recommendations.

### 3. Interview scripts

Standard question sets per dimension. Used in 90-min discovery call + 3 stakeholder interviews (owner + 2 team members).

### 4. Report generator

Inputs: Intake form responses + interview notes
Output: 15-25 page branded PDF audit deliverable

**Structure:**
- Executive summary (1 page)
- Scored rubric visualization (1 page)
- Findings by dimension (8-10 pages)
- Prioritized recommendations (3-5 pages)
- 90-day roadmap (2-3 pages)
- Optional: Scoped proposal for Phase 1 Implementation (last page)

**Technology:** Markdown templates + Pandoc → PDF, or programmatic Google Doc generation via Drive API.

### 5. Findings review call

Pre-built deck template. 60-min structured walkthrough. Ends with optional Phase 1 Implementation proposal.

## Delivery timeline

- Day 0: Discovery call (90 min)
- Day 1-2: Intake form sent, completed
- Day 3-5: Stakeholder interviews (3 × 30-45 min)
- Day 8-10: Analysis + draft report
- Day 12: Internal review (Chance polishes)
- Day 14: Delivery call + report shipped

Total client-facing time: ~6 hours. Total Chance time: 4-6 hours (post-system build).

## Pricing rationale

$997 at 4-6 hours = $165-250/hr effective. Margin is tight intentionally per [[pricing-strategy]] — this is reputation-building pricing.

Year 2 target price: $2,500 (still under most fractional COO assessment pricing).

## Audit → Phase 1 conversion

Target: 50-60% of audits convert to OPS Active retainer or Implementation engagement.

If under 40%, the audit isn't selling the next step. Likely issues:
- Recommendations too vague to act on
- No clear roadmap → owner doesn't know what to do
- Phase 1 proposal too expensive relative to perceived audit value

## Related files
- [[offer-ladder]]
- [[week-04-generator-p2]]
- [[week-05-audit-recap]]
