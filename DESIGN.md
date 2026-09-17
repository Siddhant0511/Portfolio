# Portfolio Design Doc | Siddhant Morye (v2)

**Type:** Multi-page portfolio (home + one page per case file), linked by QR code from the CV
**Audience:** Recruiters and interview panels, often on a phone right after scanning a printed QR
**Job of the site:** In five seconds, read as a credible Analytics & Operations candidate. On a slower read, prove depth with real data, real artefacts and clear reasoning.

---

## 1. Creative direction

**Minimal, but not bland.** An architect turned analyst: the site borrows the discipline of a drawing sheet (hairline rules, title blocks, registration marks, mono labels) and pairs it with a confident grotesk display face and one warm signal colour.

Design read used for every decision: *personal portfolio for recruiters, editorial-industrial language, Astro + Tailwind v4 + Motion islands, restrained motion, real artefacts.*

Dials (taste skill): `DESIGN_VARIANCE 6`, `MOTION_INTENSITY 5`, `VISUAL_DENSITY 4`.

Rules that hold everywhere:
- Real material over decoration: screenshots, photos and charts come from the actual projects. No stock images, no div-based fake UIs.
- Every number traces to a source document or dataset. Projections are labelled as targets or estimates.
- One accent colour, used to mark the single most important thing in a view.
- No em dashes or en dashes in visible copy. Use commas, colons, periods or hyphens.

---

## 2. Tokens

Defined as CSS variables in `src/styles/global.css` and exposed to Tailwind through `@theme inline`, so every utility (`bg-surface`, `text-muted`, `border-line`) switches with the theme.

### Colour
| Token | Light | Dark | Use |
|---|---|---|---|
| `bg` | `#f4f4f1` | `#0e0f11` | Page background |
| `surface` | `#fbfbf9` | `#15161a` | Cards, figures, bands |
| `surface-2` | `#eaeae6` | `#1c1e22` | Image wells, subtle fills |
| `ink` | `#121315` | `#ecece8` | Primary text, emphasis blocks |
| `ink-2` | `#393c41` | `#c4c6ca` | Body copy |
| `muted` | `#62666d` | `#8f939a` | Captions, labels |
| `line` / `line-strong` | `#dcdcd6` / `#bdbdb6` | `#25272b` / `#3a3d42` | Hairlines, neutral chart marks |
| `accent` | `#e4561b` | `#ff6a2c` | Signal orange: highlights, key bars, markers |
| `accent-ink` | `#b0400b` | `#ff8a57` | Accent for small text (contrast safe) |

Theme: follows `prefers-color-scheme`, with a manual toggle saved to `localStorage`. The contact band pins `data-theme="dark"` so it stays a dark closing panel in both modes.

Charts are monochrome plus the accent: neutral marks in `line-strong`, the point of the chart in `accent`.

### Type
| Role | Face | Notes |
|---|---|---|
| Display | **Bricolage Grotesque** (variable, `opsz` 96) | Headlines, names, big numbers. Tracking -0.03 to -0.04em |
| Body | **Geist** | Running text 16-17px, line-height 1.6-1.75 |
| Data / labels | **Geist Mono** | Metrics, file IDs, axis labels, `.label` (uppercase, 0.08em tracking) |

Fonts are self-hosted through Astro's font API (`local` provider pointing at the installed Fontsource files) with preloads and metric-matched fallbacks.

### Shape and space
- Corners are square. Containers, buttons and chips use no rounding.
- Hairline borders separate content; shadows only on floating elements (hover preview, phone screenshots).
- Container: `max-w-88rem`, gutters 16 / 24 / 40px. Sections breathe at 80-112px vertically.
- A fixed, non-interactive film-grain layer adds texture at 3.5-5% opacity.

---

## 3. Page structure

### Home (`src/pages/index.astro`)
1. **Hero**: eyebrow, name in display type with an accent full stop, 19-word lead, two CTAs (magnetic primary). Portrait inside a "drawing sheet" frame with registration marks and a four-cell title block.
2. **Proof strip**: four animated numbers (rows engineered, loans profiled, plant systems, case files).
3. **Four systems for one truck plant**: bento of the Ashok Leyland case files, each tile with a different real visual (phone screens, tenure chart, sync timeline, tyre photos).
4. **More case files**: filterable index (All / Case competitions / Academic). On desktop a preview card follows the cursor with the project's headline metric.
5. **Experience**: sticky heading, scroll-drawn timeline, internship entry links to its four case files.
6. **About**: editorial statement, capabilities, academic record, the page's only marquee (tools).
7. **Beyond the classroom**: awards and leadership ledger.
8. **Contact**: dark closing band, large email with copy button, LinkedIn.

### Case file (`src/pages/work/[slug].astro`)
Header (file ID, group, title, summary, role / context / team / when) → key-numbers band → two columns: sticky "On this page" contents with tools and live links on the left, the MDX body on the right → previous / next.

A 2px accent reading-progress bar sits under the header (CSS scroll-driven animation).

Case bodies follow a narrative: problem → approach → what the data showed → recommendation → impact.

---

## 4. Motion

Two tiers, all disabled or reduced under `prefers-reduced-motion`.

**Ambient**
- Hero lines rise from a mask on load (CSS), supporting elements fade up in sequence.
- `[data-reveal]` elements fade and rise 14px once when they enter the viewport (IntersectionObserver).
- Bars, columns and dumbbell gaps grow from zero on reveal; line charts draw left to right via `clip-path`.
- Number tickers count up once when visible.

**Interactive**
- Magnetic primary CTA, bento tiles lift on hover, tyre photos go from grayscale to colour with a scan line.
- Work index: filter pill slides between options (`layoutId`), rows re-flow, cursor-following preview.
- Astro view transitions morph a case title from its tile into the case page header.

---

## 5. Component kit

`src/components/case/` (server-rendered Astro, zero client JS unless noted):

| Component | Use |
|---|---|
| `Figure` | Titled, captioned frame with optional source line |
| `Bars` | Horizontal bars, no background tracks, optional dashed reference |
| `Columns` | Vertical columns with direct labels and reference line |
| `LineChart` | Stretchable SVG plot, HTML labels, bands, refs, points, fill-to-average |
| `Dumbbell` | Two values per row (train vs test, group A vs B) |
| `Heatmap` | Rate matrix, accent tint plus printed values |
| `Flow` | Process or system flow, horizontal on desktop, vertical on phones, failure edges |
| `Tiers` | Graded cards (triage levels, root-cause layers) |
| `Steps` | Numbered frameworks and roadmaps |
| `Compare` | Before / after by dimension |
| `Stats`, `MetricValue` | Supporting numbers with tickers and screen-reader values |
| `DataTable`, `Matrix`, `Callout` | Tables, 2x2 positioning, one key insight |
| `Gallery` | Real screenshots and photos, phone layout, click-to-zoom dialog |
| `Tabs` | Accessible tabs (arrow keys), all panels visible without JS |

`src/components/ui/` holds components pulled from Magic UI and motion-primitives (the libraries 21st.dev lists), adapted to the tokens and reduced motion: `number-ticker` (all animated metrics), `marquee` (tools band), `magnetic` (hero CTA). `text-effect` is installed but not yet used.

---

## 6. Content rules

- Case files live in `src/content/work/*.mdx`; frontmatter (schema in `src/content.config.ts`) drives cards, the index and page headers.
- Each case needs: one-line problem, specific role, method and tools, and an outcome metric.
- Group roles that are not documented are stated as "group member"; confirm and sharpen them before sharing widely.
- Chart data comes from `src/data/*.json`, computed from the original datasets, or from numbers stated in the project documents.
- About copy is first person, plain, and free of "results-driven" language.

---

## 7. Stack

Astro 7, React 19 islands, Tailwind CSS v4 (Vite plugin), Motion 13, MDX, Phosphor icons, sitemap. Deployed to GitHub Pages under `/Portfolio` by `.github/workflows/deploy.yml`. The previous single-file site is kept in `legacy/`.
