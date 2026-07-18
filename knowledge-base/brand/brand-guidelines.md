---
type: brand-reference
status: active
version: 1.1
last_updated: 2026-06-04
tags: [brand, identity, logo, color, typography, voice, collateral, spreadsheets, charts]
supersedes: brand.md (v0, frameworkopsllc.com-derived)
pdf_source: brand/brand-book-v1.0.pdf
note: Canonical single source of truth for Framework / Ops identity and collateral. The visual PDF brand book is retained as the v1.0 identity reference; this Markdown file governs all collateral, spreadsheet, chart, and sales-document work.
---

# Framework / Ops — Brand Guidelines

> Canonical brand reference for Framework / Ops. This document is the single source of truth for identity, color, typography, voice, and asset usage. It is written to be ingested by a retrieval system (RAG): each section is self-contained, headings are explicit, and values are stated in full rather than cross-referenced. When any downstream material conflicts with this document, this document wins.

- **Document:** Brand Guidelines v1.1
- **Last updated:** June 2026
- **Owner:** Framework / Ops
- **Status:** Active
- **PDF reference:** `brand-book-v1.0.pdf` remains the visual reference for the core identity. Where the PDF conflicts with this Markdown file, this Markdown file wins.

---

## 1. Brand at a glance

**Framework / Ops** is a fractional consulting practice that helps home-service companies (HVAC, plumbing, electrical, and similar trades) leverage automation and AI. The work is embedded and operational: build the systems an operator runs on — dispatch, jobs, follow-up, AI triage — then hand them over.

- **Name (written):** Framework / Ops (in prose) · `framework/ops` (in interfaces, headers, the wordmark)
- **Name (spoken):** "Framework Ops"
- **Category:** Fractional automation & AI consulting for home-service operators
- **Tone:** Operational and dependable — closer to Stripe or Datadog than to a creative agency. Precise, measured, plain-spoken.
- **Primary mark:** Constellation (a 3×3 cubed grid in emerald)
- **Primary wordmark:** `framework/ops` set in Geist Mono, lowercase, with an emerald slash
- **Core colors:** Ink navy `#07182B` and Emerald `#14B981`
- **Core typefaces:** Geist (sans) and Geist Mono (mono)
- **Collateral style:** Clean operating documents: dense enough for a contractor to use, polished enough to justify premium advisory pricing.

**One-line positioning:** We build the ops layer home-service companies actually run on.

---

## 2. The mark — "Constellation"

The primary brand mark is called **Constellation**. It is a 3×3 grid built from six solid rounded-square cells plus three smaller circular "signal" dots arranged along the bottom-right diagonal. It reads as a system at work: most modules built and in place, three signals actively transmitting.

### 2.1 Concept
- The 3×3 grid descends from the company's original logo concept and is retained deliberately — this is evolution, not reinvention.
- Solid cells represent built framework. The three dots represent live operational signals.
- The mark is fully emerald and works as a standalone symbol; it does not require the wordmark to be legible.

### 2.2 Geometry (construction)
The mark is drawn on a **200 × 200 unit** square canvas.

- **Cell size:** 48 × 48 units
- **Cell corner radius:** 10 units
- **Gutter between cells:** 8 units
- **Signal dot radius:** 9 units
- **Cell positions (top-left x, y):** (20,20) (76,20) (132,20) · (20,76) (76,76) · (20,132)
- **Dot center positions (cx, cy):** (156,100) · (100,156) · (156,156)
- **Fill:** single flat fill, Emerald `#14B981`, 100% opacity (no gradients, no strokes, no effects)

### 2.3 SVG source (canonical)
```svg
<svg width="512" height="512" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="48" height="48" rx="10" fill="#14B981"/>
  <rect x="76" y="20" width="48" height="48" rx="10" fill="#14B981"/>
  <rect x="132" y="20" width="48" height="48" rx="10" fill="#14B981"/>
  <rect x="20" y="76" width="48" height="48" rx="10" fill="#14B981"/>
  <rect x="76" y="76" width="48" height="48" rx="10" fill="#14B981"/>
  <circle cx="156" cy="100" r="9" fill="#14B981"/>
  <rect x="20" y="132" width="48" height="48" rx="10" fill="#14B981"/>
  <circle cx="100" cy="156" r="9" fill="#14B981"/>
  <circle cx="156" cy="156" r="9" fill="#14B981"/>
</svg>
```
The vector master file is `assets/mark-constellation.svg`.

### 2.4 Color on different surfaces
- **On light surfaces (Bone, Paper):** Emerald `#14B981`.
- **On dark surfaces (Ink):** Emerald `#14B981` at large sizes; switch to **Emerald Bright `#34D9A2`** below ~40px so the cells stay sharp against navy.
- The mark may also be rendered in single-color **Ink** (on light) or **Bone** (on dark) where one-color reproduction is required (e.g. embossing, single-thread embroidery on a contrasting garment).

### 2.5 Clear space
Reserve clear space equal to **one cell width (48 units, ≈ the width of one module)** on all four sides of the mark. No type, rules, seams, imagery, or other marks may enter that frame.

### 2.6 Minimum size
- **Screen:** 16px is the absolute floor for the full mark.
- **Embroidery / physical:** 2 inches (51mm) wide is the floor — below this the three signal dots collapse.
- **Simplified mark:** below the minimum, drop the three dots and use the six cells only. This is the approved sub-minimum substitute (pins, tiny patches, sub-16px favicons).

### 2.7 Don'ts
- Do not recolor individual cells or dots (the mark is single-color).
- Do not rotate, skew, or stretch the mark; preserve the square aspect ratio.
- Do not add shadows, glows, bevels, or other effects.
- Do not rearrange the cells or move the dots.
- Do not place the mark on a busy photo without a solid Ink or Bone backing shape.
- Do not outline the cells (no strokes).

---

## 3. The wordmark

The wordmark is **`framework/ops`** set in **Geist Mono**, **weight 500 (Medium)**, **all lowercase**.

### 3.1 Setting
- **Family:** Geist Mono
- **Weight:** 500 (Medium)
- **Case:** lowercase, always
- **Tracking:** −2%
- **Leading:** 100%
- **Slash:** the `/` is always Emerald `#14B981`. There are no spaces around it.

### 3.2 Slash rules
- The slash is functional, not decorative — it is the bridge between *framework* (what you build) and *ops* (what you run), and it is the one place emerald always appears in the wordmark.
- Use the standard ASCII forward slash `/`. Never substitute the Unicode division slash, a hyphen, or a pipe.
- Never set the slash in a neutral color; it is always emerald.

### 3.3 Written vs spoken
- **In interfaces, headers, navigation, the wordmark:** `framework/ops` (lowercase, with slash).
- **In running prose:** "Framework Ops" or "Framework / Ops" is acceptable.
- **Spoken:** "Framework Ops."

---

## 4. Lockups

There are five approved lockups. Use the horizontal lockup roughly 80% of the time.

1. **Horizontal (primary):** Constellation mark to the left of the `framework/ops` wordmark, vertically centered. Gap between mark and wordmark ≈ 0.3× the mark height. Default for nav bars, headers, decks, email.
2. **Horizontal reversed:** Same, on Ink or dark surfaces — wordmark in Bone, mark in Emerald, slash in Emerald.
3. **Stacked:** Mark centered above the wordmark. For square crops, avatars, social, square print.
4. **Mark only:** Constellation alone. Favicons, app icons, monograms, stickers, embroidery.
5. **Wordmark only:** `framework/ops` alone. Email signatures, body-text contexts, invoices, watermarks where the mark would be too loud.

**Lockup rules**
- Never recreate the lockup by eye — use the spacing above.
- Never swap the typeface of the wordmark.
- Keep the mark and wordmark in a single shared color on a given surface (mark emerald, wordmark ink/bone), with the slash always emerald.

---

## 5. Color system

The palette keeps the original navy + emerald spirit, tuned for ownership and stratified with proper neutrals. Twelve roles. Do not invent new values — if a use case doesn't fit, reuse the nearest token's role and adjust opacity.

### 5.1 Ink scale (dark / primary)
| Name | Token | Hex | RGB | Role |
|---|---|---|---|---|
| Ink | `--fo-ink` | `#07182B` | 7, 24, 43 | Primary brand. Backgrounds, dark surfaces, body text on light bg. |
| Ink Deep | `--fo-ink-deep` | `#030B17` | 3, 11, 23 | Full-bleed / abyss. Footers, hero darks, splash. |
| Surface | `--fo-surface` | `#0F2940` | 15, 41, 64 | Elevated card on Ink. Inputs, sidebars, panels. |
| Hairline | `--fo-hairline` | `#1B3A57` | 27, 58, 87 | 1px borders on Ink. Dividers, subtle separation. |

### 5.2 Emerald (accent)
| Name | Token | Hex | RGB | Role |
|---|---|---|---|---|
| Emerald | `--fo-emerald` | `#14B981` | 20, 185, 129 | Primary accent. The slash, status, buttons, links, the mark. |
| Emerald Bright | `--fo-emerald-bright` | `#34D9A2` | 52, 217, 162 | Highlight on dark. Hover, glow, small marks on Ink, charts. |
| Emerald Deep | `--fo-emerald-deep` | `#047857` | 4, 120, 87 | Pressed / underline / dark-mode link. |

### 5.3 Neutrals
| Name | Token | Hex | RGB | Role |
|---|---|---|---|---|
| Bone | `--fo-bone` | `#F4F4EE` | 244, 244, 238 | Reverse fg on Ink. Soft cards on Paper. Warm, not stark white. |
| Paper | `--fo-paper` | `#FAFAF7` | 250, 250, 247 | Default light page background. |
| Fog | `--fo-fog` | `#D9DDD5` | 217, 221, 213 | 1px borders on light. Dividers, table rules. |
| Graphite | `--fo-graphite` | `#4A5868` | 74, 88, 104 | Secondary text on light. |
| Ash | `--fo-ash` | `#8893A1` | 136, 147, 161 | Tertiary text on dark. Captions, metadata. |

### 5.4 Usage ratio
Roughly **60 / 30 / 10**: 60% Ink or Bone (background), 30% neutrals (Surface, Fog, Graphite, Ash), 10% Emerald. Emerald is a scalpel — aim for one moment of accent per view. Never fill large areas with Emerald.

### 5.5 Accessibility / contrast
- Bone on Ink — 14.8:1 — passes AAA
- Ink on Bone — 14.8:1 — passes AAA
- Emerald on Ink — 6.4:1 — passes AA (use as accent, not body copy)
- Graphite on Paper — 7.2:1 — passes AAA
- Ash on Ink — 5.1:1 — passes AA
Emerald is AA-Large only against some backgrounds; never set long body copy in Emerald.

---

### 5.6 Functional colors for data and warnings
Use these only for charts, dashboards, spreadsheet warnings, and decision states. They are **not** brand colors and should not appear in logos, hero treatments, apparel, or broad page backgrounds.

| Name | Token | Hex | Use |
|---|---|---|---|
| Warning | `--fo-warning` | `#B7791F` | Marginal fit, budget pressure, aging AR, schedule risk |
| Danger | `--fo-danger` | `#C2410C` | No-Go flags, critical margin leakage, cash risk, broken handoff |
| Blue Signal | `--fo-blue-signal` | `#2563EB` | Neutral comparison series, secondary chart line, non-financial volume metric |
| Violet Signal | `--fo-violet-signal` | `#7C3AED` | Third chart series only when needed |

**Usage rules**
- Positive performance uses Emerald or Emerald Deep.
- Negative performance uses Danger, not red-tinted Emerald.
- Caution uses Warning.
- Neutral benchmark/comparison lines use Graphite, Ash, or Blue Signal.
- Never use more than four series colors in a client-facing chart. If the chart needs more than four colors, the chart is trying to say too much.

---

## 6. Typography

Two families, both open-source from Vercel.

### 6.1 Families
- **Geist (sans)** — primary. Everything readable: display, headings, body, UI.
- **Geist Mono** — the operational layer: the wordmark, code, identifiers, status, labels, overlines, metadata.

Web import:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap">
```

### 6.2 Type roles (Geist sans)
| Role | Size | Weight | Tracking |
|---|---|---|---|
| Display | 48–56px+ | 600 | −4% |
| H1 | 32px | 600 | −3.5% |
| H2 | 22px | 500 | −2.5% |
| Body | 15–16px | 400 | 0 |
| Small / overline | 12px | 500 | +2%, uppercase |

### 6.3 Type roles (Geist Mono)
| Role | Weight | Tracking | Notes |
|---|---|---|---|
| Wordmark | 500 | −2% | lowercase; emerald slash |
| Overline | 500 | +22% | uppercase; often emerald |
| Status | 500 | 0 | with emerald dot glyph |
| Code | 400 | 0 | — |

### 6.4 Type scale (web)
`xs` 12 · `sm` 14 · `base` 16 · `lg` 19 · `xl` 24 · `2xl` 32 · `display` 56 (px). Headings ≥24px take −2.5% tracking or tighter.

---

## 7. Voice & tone

Framework / Ops sounds **operational, not aspirational.** Three principles:

1. **Concrete.** Name the system. "We rebuilt their dispatch routing." Not "we transformed operations." Specifics build trust.
2. **Measured.** Numbers over adjectives. "Cut follow-up from 48h to 2h" beats "blazing fast." If you can't measure it, soften the claim.
3. **Plain.** Read it out loud. If a contractor wouldn't say it on a job site, rewrite. No "leverage," no "synergize," no "best-in-class."

### 7.1 Sounds like us
- "We build the ops layer home-service companies actually run on."
- "Fractional. Embedded for 90 days. Then you own it."
- "Dispatch routing rebuilt. AI triage on inbound. Done."

### 7.2 Does not sound like us
- "Leveraging cutting-edge AI to transform operations."
- "Unlock your team's true potential."
- "End-to-end synergistic solutions."

### 7.3 Vocabulary
- **Prefer:** build, run, embed, operator, system, dispatch, follow-up, triage, measurable, fractional, hand it over.
- **Avoid:** leverage, synergy, transform, revolutionary, best-in-class, unlock, empower, seamless (as filler), cutting-edge.

---

## 8. Sales and delivery collateral

Framework / Ops collateral should look like operating infrastructure, not a marketing brochure. The client should feel like the document could be used in a Monday leadership meeting, not just admired and filed away.

### 8.1 Core collateral types

| Asset | Primary job | Format | Design pattern |
|---|---|---|---|
| Customer journey map | Show how a prospect moves from first touch to kickoff | PDF, Docx, slide, or web export | Horizontal stage map with decision gates and owner/client responsibilities |
| Offer sheet | Explain one offer, one next step, one price | One-page PDF | Top diagnosis, middle deliverables, bottom investment and next step |
| OPS Assessment | Diagnose operating gaps and rank fixes | 4-6 page PDF/docx | Scored dimensions, problem cost, 30/60/90 priorities |
| Proposal | Convert diagnostic into one recommended path | 4-6 page PDF/docx | What we heard, what it costs, what we will build, investment |
| Spreadsheet model | Let Chance manipulate real numbers | XLSX / Google Sheets | Inputs on left/top, outputs on right/top, assumptions separated from results |
| Sales tracker | Track prospects without CRM bloat | XLSX / Google Sheets | Dense table, status flags, next action, follow-up date |

### 8.2 Page structure
- **Use one clear job per page.** If a page explains the journey, do not also sell all services.
- **Lead with the operator's situation.** Start with revenue stage, margin leak, cash strain, owner bottleneck, lead response, dispatch, job costing, callbacks, or sales handoff.
- **Keep the brand quiet.** Use the mark or wordmark once per page unless the asset is a cover.
- **Use Ink for anchors, Paper/Bone for working surface, Emerald for the one action or positive signal.**
- **No decorative pattern fills.** The Constellation mark is a logo, not wallpaper.
- **No generic icons unless they clarify workflow.** Prefer labels like "Discovery," "Diagnostic," "Proposal," "Kickoff," "30-day install."

### 8.3 Customer journey maps
Use this structure for Framework / Ops sales and onboarding journey visuals:

| Stage | Label | Owner/client action | Framework / Ops action | Gate |
|---|---|---|---|---|
| 1 | Discovery | Owner names revenue, pain, budget, urgency | Qualify ICP and red flags | Go / No-Go |
| 2 | Intake | Owner submits written intake and access list | Review revenue, margin, tech stack, org chart | Enough data to diagnose |
| 3 | OPS Assessment | Owner attends 90-minute diagnostic | Score gaps and quantify cost | Diagnosis accepted |
| 4 | Proposal | Owner reviews one recommended path live | Present scope, timeline, investment, ROI | 7-day decision |
| 5 | Agreement | Owner signs and pays first month | Schedule kickoff, collect access | Paid kickoff |
| 6 | First 90 days | Owner/team implements with Chance | Install systems, SOPs, dashboard, cadence | 90-day review |

Design rules:
- Use a horizontal six-stage map on landscape pages and a vertical six-stage stack on mobile or portrait pages.
- Each stage gets one primary action and one gate. Do not crowd the map with every task.
- Use Emerald only for current/complete/Go states.
- Use Warning for stalled intake or missing data.
- Use Danger only for No-Go or blocked implementation.
- Show the OPS Assessment as the gateway. Do not visually imply prospects skip straight from discovery to retainer.

### 8.4 Proposal and assessment pages
- Use a restrained cover: Ink background, Bone title, small Emerald mark, one sentence of context.
- Do not open with Chance's bio. Open with the client's operating condition.
- Every problem block should include the observed symptom, the likely root cause, and the cost at that revenue level.
- Every scope block should name the deliverable: "13-week cash flow model," "job costing dashboard," "sales-to-production handoff SOP," "Monday review cadence."
- Include a "Not in scope" box in Graphite/Bone styling. This protects margin and reduces hand-wavy scope creep.
- ROI pages must show downside, conservative case, and upside in that order. Never show upside alone.

### 8.5 Spreadsheet styling
Framework / Ops spreadsheets should feel like operator tools, not finance-department art projects.

| Element | Style |
|---|---|
| Workbook cover / first tab | Ink header, wordmark, short usage note, last updated date |
| Input cells | Bone fill, Ink text, Fog border, label in Graphite |
| Required inputs | Thin Emerald left border or small Emerald status dot |
| Assumption cells | Paper fill, Graphite label, mono note where helpful |
| Output cells | Ink fill, Bone text, Emerald value only when positive |
| Warning outputs | Warning fill at 12-18% tint, Ink text, explicit reason |
| No-Go outputs | Danger fill at 10-14% tint, Ink text, no vague label |
| Protected/formula cells | Light Fog fill, Graphite text, locked where possible |
| Section headers | Ink text, 12px Geist Mono uppercase, +22% tracking |
| Tables | 1px Fog borders, no heavy grid, zebra rows only if table has 12+ rows |

Workbook rules:
- Inputs, assumptions, lookups, and outputs must be visually distinct.
- Never hide critical assumptions. If implementation rate is 65%, show it.
- Use freeze panes on sales trackers and pricing models.
- Use data validation for stage/status fields.
- Use plain English flags: "Go," "Wait," "No-Go," "Budget risk," "Missing gross margin."
- The retainer affordability flag must be visually obvious when monthly retainer exceeds 15% of monthly net profit.

### 8.6 Charts and dashboards
- Use Ink or Graphite for axes and labels. Use Fog for gridlines.
- Use Emerald for actual performance when it is good or on track.
- Use Graphite/Ash for benchmarks.
- Use Warning and Danger only for decisions or variance that needs action.
- Label the chart in the title. "Gross margin gap by month" is better than "Margin."
- Put the takeaway above the chart in one sentence.
- Avoid donut charts for operating metrics. Use bars, lines, scorecards, and variance tables.
- Do not chart more than 12 months unless the trend is the point.

### 8.7 Sales-document tone
Use field-level words: job costing, callbacks, DSO, draw schedule, FSM, dispatch, close rate, gross margin, lead response, production handoff, weekly review. Avoid imported SaaS language like "customer lifecycle," "revenue engine," or "activation" unless the audience is specifically a software or marketing client.

---

## 9. PDF and export production

### 9.1 PDF source of truth
The v1.0 PDF brand book is a visual reference, not the editable source. For future brand-book updates, rebuild from an editable source file and export a new PDF instead of manually editing the PDF.

### 9.2 PDF export requirements
- Text must remain selectable and copy cleanly. Avoid letterspacing implementations that make words extract as "shiptoday" or "oneidentity."
- Every export should pass a visual render check: no clipped text, no overlapping type, no broken glyphs, no low-contrast captions.
- Include document title, version, last updated date, and owner in the file properties where the tool allows it.
- For client PDFs, use filenames in this pattern: `Framework-OPS_[Client-or-Asset]_[YYYY-MM-DD].pdf`.
- For internal brand PDFs, use versioned filenames: `brand-book-v1.1.pdf`, not `brand-book-final.pdf`.

### 9.3 Accessibility basics
- Do not rely on Emerald alone to communicate status. Pair color with labels like "Go," "Wait," "No-Go," or "Budget risk."
- Keep body text at 10.5pt minimum in PDF/docx exports.
- Use real tables for tabular data in docx where practical; screenshots of spreadsheets are allowed only when the visual layout is the deliverable.

---

## 10. Web tokens (developer handoff)

### 10.1 CSS custom properties
```css
:root {
  /* Color · Ink scale */
  --fo-ink:           #07182B;
  --fo-ink-deep:      #030B17;
  --fo-surface:       #0F2940;
  --fo-hairline:      #1B3A57;

  /* Color · Emerald */
  --fo-emerald:        #14B981;
  --fo-emerald-bright: #34D9A2;
  --fo-emerald-deep:   #047857;

  /* Color · Neutral */
  --fo-bone:      #F4F4EE;
  --fo-paper:     #FAFAF7;
  --fo-fog:       #D9DDD5;
  --fo-graphite:  #4A5868;
  --fo-ash:       #8893A1;

  /* Functional data states */
  --fo-warning:       #B7791F;
  --fo-danger:        #C2410C;
  --fo-blue-signal:   #2563EB;
  --fo-violet-signal: #7C3AED;

  /* Type */
  --fo-font-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --fo-font-mono: 'Geist Mono', ui-monospace, 'JetBrains Mono', Menlo, monospace;

  /* Radius */
  --fo-r-sm: 6px;
  --fo-r-md: 10px;
  --fo-r-lg: 16px;
  --fo-r-xl: 22px;

  /* Shadow */
  --fo-shadow-sm: 0 1px 2px rgba(7,24,43,.06);
  --fo-shadow-md: 0 6px 18px -8px rgba(7,24,43,.18);
  --fo-shadow-lg: 0 24px 48px -16px rgba(7,24,43,.32);
}

body {
  font-family: var(--fo-font-sans);
  background: var(--fo-paper);
  color: var(--fo-ink);
}
```

### 10.2 Tailwind config
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        ink:    { DEFAULT: '#07182B', deep: '#030B17',
                  surface: '#0F2940', hairline: '#1B3A57' },
        emerald:{ DEFAULT: '#14B981', bright: '#34D9A2', deep: '#047857' },
        bone:   '#F4F4EE',
        paper:  '#FAFAF7',
        fog:    '#D9DDD5',
        graphite:'#4A5868',
        ash:    '#8893A1',
        warning:'#B7791F',
        danger: '#C2410C',
        blueSignal: '#2563EB',
        violetSignal: '#7C3AED',
      },
      fontFamily: {
        sans: ['Geist', 'ui-sans-serif', 'system-ui'],
        mono: ['Geist Mono', 'ui-monospace'],
      },
    },
  },
};
```

### 10.3 Favicon
```html
<link rel="icon" type="image/svg+xml" href="/assets/mark-constellation.svg">
```

---

## 11. Apparel & merchandise (gear)

The Constellation mark is the hero on gear: it embroiders cleanly, screen-prints in one color, and reads at small apparel sizes.

### 11.1 General print specs
- **Embroidery:** Constellation mark only. Minimum 2″ (51mm) wide. Pantone **2245 C** for emerald, Pantone **539 C** for ink. Drop the three dots below ¾″.
- **Embroidery style:** Flat embroidery only. Do not use 3D/puff embroidery for the Constellation mark; puff distorts the small signal dots and rounded cell corners.
- **Screen print:** One color preferred — Bone on Ink garments, Ink on Bone garments. Two-color (emerald mark on contrasting body) for premium runs.
- **Vinyl:** Die-cut to the mark silhouette + 2mm safe edge. Single-color only; avoid full-color vinyl.
- **Substrates:** Avoid pure-white garments. Use Bone heather, natural cotton, or Ink so the brand reads warm, not corporate.

### 11.2 Recommended sample hat
- **Style:** Unstructured 6-panel "dad cap" (reference: Richardson 320 or equivalent).
- **Material:** 100% cotton twill, garment-washed.
- **Body color:** Ink navy, matched to Pantone 539 C.
- **Closure:** Adjustable strap, antique brass buckle.
- **Decoration:** Flat embroidery (no 3D/puff), single-color emerald thread matched to Pantone 2245 C (approx. Madeira Polyneon #1751/#1851).
- **Placement:** Centered on the front panels; mark 2″ tall; top of mark ⅝″ (16mm) below the bill seam; center seam runs through the mark's center; cells aligned parallel to the brim.
- **Backing:** Tear-away, 2.5oz, fully removed.
- **Alternate colorways:** Bone (natural cotton) and Khaki (structured 6-panel canvas, trade-site), both with the Ink mark.

### 11.3 Acceptance criteria (QC)
- Mark centered front ±2mm; ⅝″ down from bill seam ±2mm.
- Mark exactly 2″ × 2″ ±1.5mm.
- Emerald thread reads as `#14B981` in daylight — not blue-shifted, not olive.
- No loose threads, skips, or puckering over 0.5mm.
- Each of the three signal dots reads as a distinct circle.
- Rounded corners visible on all six cells; visible gutter between every cell.
- Tear-away backing fully removed; no needle holes outside the embroidery footprint; bill pre-curved and symmetrical.

---

## 12. Asset inventory

All paths are relative to the brand project root.

| File | Description |
|---|---|
| `assets/mark-constellation.svg` | **Primary mark.** Constellation, single-color emerald, 200×200 viewBox. Production-ready; the only file an embroiderer needs (they digitize a stitch file from it). |
| `assets/mark-pulse-ink.svg` | Earlier "Pulse" mark, ink fill (superseded by Constellation; retained for reference). |
| `assets/mark-pulse-bone.svg` | Earlier "Pulse" mark, bone fill (superseded). |
| `assets/lockup-horizontal-ink.svg` | Horizontal lockup, ink type (note: requires Geist Mono to render the wordmark; for print-perfect output, render from HTML/CSS with the font loaded and outline to paths). |
| `assets/lockup-horizontal-bone.svg` | Horizontal lockup, bone type. |
| `assets/favicon.svg` | SVG favicon. |

**Note on the primary mark:** the current approved primary mark is **Constellation** (`assets/mark-constellation.svg`). The "Pulse" marks were an earlier exploration and are superseded; use Constellation everywhere.

---

## 13. Quick-reference summary

- **Mark:** Constellation — 3×3 emerald grid, 6 cells + 3 dots. File: `assets/mark-constellation.svg`.
- **Wordmark:** `framework/ops` — Geist Mono 500, lowercase, emerald slash, no spaces around slash.
- **Primary colors:** Ink `#07182B`, Emerald `#14B981`.
- **Emerald on dark, small:** use Emerald Bright `#34D9A2` below ~40px.
- **Typefaces:** Geist (sans), Geist Mono (mono).
- **Color ratio:** 60 Ink/Bone · 30 neutral · 10 Emerald.
- **Voice:** operational, not aspirational — concrete, measured, plain.
- **Collateral:** operator tools first — proposals, journey maps, assessments, and spreadsheets should be dense, clear, and decision-oriented.
- **Charts:** Emerald for good/on-track, Warning for marginal, Danger for No-Go/critical, Graphite/Ash for benchmarks.
- **Tagline:** "We build the ops layer home-service companies actually run on."
- **Min mark size:** 16px screen / 2″ embroidery; drop the 3 dots below the floor.
- **Gear:** flat embroidery only; no 3D/puff on the Constellation mark.

---

*End of Framework / Ops Brand Guidelines v1.1.*
