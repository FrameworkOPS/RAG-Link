# Website Status

**URL:** frameworkopsllc.com

## Current state (May 11, 2026)

- Live, basic build complete
- Pages: Home, Problem, Approach, How It Works, Tools, Services, Why Fractional
- Visual: Dark theme, green accent, monospace + sans typography
- Tech: Appears to be client-side rendered (SPA) — confirmed not crawlable by LLM web fetchers in current state

## Known issues

### Rendering (HIGH priority)

Site renders entirely client-side. This means:
- LLMs scraping for research (prospects using ChatGPT/Claude/Perplexity) can't read the site
- SEO is likely weak
- Social previews may be incomplete

**Fix:** Switch to server-side rendering or static site generation. If on Next.js, use SSR/SSG. If on Webflow/Framer, this should already work — investigate.

### Pricing — currently outdated (Week 1 fix)

Current site shows 11 offers across 3 tiers. Canonical offer ladder (per [[service-tiers]]) is 10 offers:

**KEEP / UPDATE:**
- AI Readiness Assessment $297
- Tech Stack Audit $497
- OPS Assessment $997 (Start Here)
- SOP Sprint $2,000 (flat)
- Automation Build Sprint $2,000 (flat)
- KPI Dashboard Build $2,000 (flat)
- Advisory $1,500/mo
- OPS Light $2,500/mo
- OPS Active $4,000/mo (mark as MOST COMMON)
- OPS Embedded $6,000/mo (30-40 hrs)

**KILL:**
- 90-Day OPS Roadmap ($2,000) — replaced by KPI Dashboard Build
- Any legacy/duplicate tiers beyond the 10 above (the old site carried an 11th)

### ICP language inconsistency

Site H1 says "$1M-$5M Home Service Companies." Final ICP is $1-3M (see [[icp-definition]]).

**Fix:** Update all ICP references to $1-3M.

## Pending additions

- Sales pages per offer (Week 2 deliverable)
- Daniel case study page (Week 6 deliverable)
- Discovery call booking flow (Cal.com or similar) integrated
- Intake form for prospects

## Related files
- [[offer-ladder]]
- [[icp-definition]]
- [[week-01-foundation]]
- [[week-02-sows]]
