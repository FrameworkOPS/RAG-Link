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

Current site shows 11 offers across 3 tiers. New offer ladder (per [[offer-ladder]]) is 6 offers:

**KEEP:**
- OPS Assessment $997
- SOP Sprint $2,000 (flat — kill the range)
- Automation Build $2,000 (flat — kill the range)
- OPS Light $2,000/mo
- OPS Active $3,500/mo (mark as MOST COMMON)
- OPS Embedded — change from $6,500/30-40hr to $5,500/25-30hr

**KILL:**
- AI Readiness Score ($297)
- Tech Stack Audit ($497)
- 90-Day OPS Roadmap ($2,000)
- OPS Advisory ($1,200/mo)

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
