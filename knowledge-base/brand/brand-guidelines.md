---
type: brand-reference
status: active
version: 1.0
last_updated: 2026-06-01
tags: [brand, identity, logo, color, typography, voice]
supersedes: brand.md (v0, frameworkopsllc.com-derived)
pdf_source: brand/brand-book-v1.0.pdf
note: Canonical single source of truth for Framework / Ops identity. Visual brand book is brand-book-v1.0.pdf in the same folder. Overrides all previous brand documents for logos and colors.
---

# Framework / Ops — Brand Guidelines

> Canonical brand reference for Framework / Ops. This document is the single source of truth for identity, color, typography, voice, and asset usage. It is written to be ingested by a retrieval system (RAG): each section is self-contained, headings are explicit, and values are stated in full rather than cross-referenced. When any downstream material conflicts with this document, this document wins.

- **Document:** Brand Guidelines v1.0
- **Last updated:** May 2026
- **Owner:** Framework / Ops
- **Status:** Active

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

## 8. Web tokens (developer handoff)

### 8.1 CSS custom properties
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

### 8.2 Tailwind config
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
      },
      fontFamily: {
        sans: ['Geist', 'ui-sans-serif', 'system-ui'],
        mono: ['Geist Mono', 'ui-monospace'],
      },
    },
  },
};
```

### 8.3 Favicon
```html
<link rel="icon" type="image/svg+xml" href="/assets/mark-constellation.svg">
```

---

## 9. Apparel & merchandise (gear)

The Constellation mark is the hero on gear: it embroiders cleanly, screen-prints in one color, and reads at small apparel sizes.

### 9.1 General print specs
- **Embroidery:** Constellation mark only. Minimum 2″ (51mm) wide. Pantone **2245 C** for emerald, Pantone **539 C** for ink. Drop the three dots below ¾″.
- **Screen print:** One color preferred — Bone on Ink garments, Ink on Bone garments. Two-color (emerald mark on contrasting body) for premium runs.
- **Vinyl:** Die-cut to the mark silhouette + 2mm safe edge. Single-color only; avoid full-color vinyl.
- **Substrates:** Avoid pure-white garments. Use Bone heather, natural cotton, or Ink so the brand reads warm, not corporate.

### 9.2 Recommended sample hat
- **Style:** Unstructured 6-panel "dad cap" (reference: Richardson 320 or equivalent).
- **Material:** 100% cotton twill, garment-washed.
- **Body color:** Ink navy, matched to Pantone 539 C.
- **Closure:** Adjustable strap, antique brass buckle.
- **Decoration:** Flat embroidery (no 3D/puff), single-color emerald thread matched to Pantone 2245 C (approx. Madeira Polyneon #1751/#1851).
- **Placement:** Centered on the front panels; mark 2″ tall; top of mark ⅝″ (16mm) below the bill seam; center seam runs through the mark's center; cells aligned parallel to the brim.
- **Backing:** Tear-away, 2.5oz, fully removed.
- **Alternate colorways:** Bone (natural cotton) and Khaki (structured 6-panel canvas, trade-site), both with the Ink mark.

### 9.3 Acceptance criteria (QC)
- Mark centered front ±2mm; ⅝″ down from bill seam ±2mm.
- Mark exactly 2″ × 2″ ±1.5mm.
- Emerald thread reads as `#14B981` in daylight — not blue-shifted, not olive.
- No loose threads, skips, or puckering over 0.5mm.
- Each of the three signal dots reads as a distinct circle.
- Rounded corners visible on all six cells; visible gutter between every cell.
- Tear-away backing fully removed; no needle holes outside the embroidery footprint; bill pre-curved and symmetrical.

---

## 10. Asset inventory

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

## 11. Quick-reference summary

- **Mark:** Constellation — 3×3 emerald grid, 6 cells + 3 dots. File: `assets/mark-constellation.svg`.
- **Wordmark:** `framework/ops` — Geist Mono 500, lowercase, emerald slash, no spaces around slash.
- **Primary colors:** Ink `#07182B`, Emerald `#14B981`.
- **Emerald on dark, small:** use Emerald Bright `#34D9A2` below ~40px.
- **Typefaces:** Geist (sans), Geist Mono (mono).
- **Color ratio:** 60 Ink/Bone · 30 neutral · 10 Emerald.
- **Voice:** operational, not aspirational — concrete, measured, plain.
- **Tagline:** "We build the ops layer home-service companies actually run on."
- **Min mark size:** 16px screen / 2″ embroidery; drop the 3 dots below the floor.

---

*End of Framework / Ops Brand Guidelines v1.0.*
