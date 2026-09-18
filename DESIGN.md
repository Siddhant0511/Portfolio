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

Defined as CSS variables in `src/styles/global.css` and exposed to Tailwind through `@theme inline`, so every utility (`bg-surface`, `text-muted`, `border-line`) resolves from one place.

### Colour
| Token | Light (site) | Inverted panel | Use |
|---|---|---|---|
| `bg` | `#f4f4f1` | `#0e0f11` | Page background |
| `surface` | `#fbfbf9` | `#15161a` | Cards, figures, bands |
| `surface-2` | `#eaeae6` | `#1c1e22` | Image wells, subtle fills |
| `ink` | `#121315` | `#ecece8` | Primary text, emphasis blocks |
| `ink-2` | `#393c41` | `#c4c6ca` | Body copy |
| `muted` | `#62666d` | `#8f939a` | Captions, labels |
| `line` / `line-strong` | `#dcdcd6` / `#bdbdb6` | `#25272b` / `#3a3d42` | Hairlines, neutral chart marks |
| `accent` | `#e4561b` | `#ff6a2c` | Signal orange: highlights, key bars, markers |
| `accent-ink` | `#b0400b` | `#ff8a57` | Accent for small text, and for any accent fill sitting under light text |

`accent` is bright enough to fail WCAG AA behind light text: `bg` on `accent` is only 3.38:1. Any button that fills with the accent and keeps light text uses `accent-ink` instead, which is 5.32:1. `accent` stays the fill for icon-only targets and graphic marks, where the 3:1 bar for non-text applies.

The site is light only: `<html>` carries `data-theme="light"` and there is no switcher. The second column is not a dark theme, it is the palette for sections that deliberately invert. A section opts in with `data-theme="dark"`, which also turns on the `dark:` variant inside it. The contact band is the only one that does.

Charts are monochrome plus the accent: neutral marks in `line-strong`, the point of the chart in `accent`.

### Type
| Role | Face | Notes |
|---|---|---|
| Display | **Satoshi** (weights 400, 500, 700, 900) | Headlines, name, big numbers. Tracking -0.03 to -0.04em; the name sits at 700 |
| Body | **Geist** | Running text 16-17px, line-height 1.6-1.75 |
| Data / labels | **Geist Mono** | Metrics, file IDs, axis labels, `.label` (uppercase, 0.08em tracking) |

Fonts are self-hosted through Astro's font API with preloads and metric-matched fallbacks: Satoshi via the `fontshare` provider (discrete weights only, a variable range returns nothing), Geist and Geist Mono via the `local` provider pointing at the installed Fontsource files.

### Shape and space
- Corners are square. Containers, buttons and chips use no rounding.
- Hairline borders separate content; shadows only on lifted elements (grid tiles on hover, phone screenshots).
- Tile containers (the case-file grid and the Ashok Leyland bento) carry `line-strong`, not `line`. Their surface sits lighter than the page, so a `line` hairline left them floating without an edge. Dividers inside a tile stay on `line`.
- Container: `max-w-88rem`, gutters 16 / 24 / 40px. Sections breathe at 80-112px vertically.
- A fixed, non-interactive film-grain layer adds texture at 3.5-5% opacity.

---

## 3. Page structure

Header: the nav sits in the middle column of a `1fr auto 1fr` grid, so it is centred on the page rather than on the space left between the wordmark and the buttons.

### Home (`src/pages/index.astro`)
1. **Hero**: eyebrow, name in display type with an accent full stop, 19-word lead, two CTAs (magnetic primary). Portrait inside a "drawing sheet" frame with registration marks and a four-cell title block. From lg up the sheet matches the name block exactly, top and bottom: the portrait is absolutely positioned inside its well so it contributes nothing to intrinsic sizing, which lets the row be sized by the text column and the well take whatever height is left once the title block is placed. Below lg the well keeps a 4:5 portrait crop.
2. **Four systems for one truck plant**: bento of the Ashok Leyland case files, each tile with a different real visual (phone screens, tenure chart, sync timeline, tyre photos). On hover the tile lifts onto a tinted shadow, an accent rule draws along the bottom edge, the title nudges right and the phone screens fan out one after another.
3. **More case files**: filterable grid (All / Case competitions / Academic), four tiles per row at xl, stepping down to one on mobile. Each tile carries a generated thumbnail, its title and its headline number, and the metric rule is pinned to the bottom of the cell so the rules line up across a row. Hovering slides the problem statement up from inside the tile.
4. **Experience**: sticky heading, scroll-drawn timeline, internship entry links to its four case files.
5. **About**: editorial statement, capabilities in an asymmetric 1 + 2 tile split (never three equal cards), full-width centred academic record, the page's only marquee (tools).
6. **Beyond the classroom**: awards and leadership ledger.
7. **Contact**: dark closing band, large email with copy button, LinkedIn. The "process?" line carries a 0.0156em indent, because Satoshi gives lowercase p a smaller left side bearing than H and L and its stem otherwise sits left of the lines around it. Round letters that should overhang, like the S of "Siddhant", are left alone.

### Case file (`src/pages/work/[slug].astro`)
Header (file ID, group, title, summary, role / context / team / when) → key-numbers band → two columns: sticky "On this page" contents with tools and live links on the left, the MDX body on the right → previous / next.

A 2px accent reading-progress bar sits under the header (CSS scroll-driven animation).

Case bodies follow a narrative: problem → approach → what the data showed → recommendation → impact.

---

## 4. Motion

Two tiers, all disabled or reduced under `prefers-reduced-motion`.

**Ambient**
- Hero: name lines rise from a mask, the portrait uncovers itself with a `clip-path` wipe and settles out of a slow push-in, supporting elements fade up in sequence.
- Section headings rise from behind their own edge once, on first view (`[data-mask]`, staggered per line).
- `[data-reveal]` elements fade and rise 14px once when they enter the viewport (IntersectionObserver).
- Bars, columns and dumbbell gaps grow from zero on reveal; line charts draw left to right via `clip-path`.
- Number tickers count up once when visible.
- Experience: the timeline rule draws itself (scroll-driven), and each role's node scales up and fills with the accent as it arrives.
- Case studies: each section rule draws itself on scroll (`animation-timeline: view()`), and a 2px progress bar tracks reading.

**Interactive**
- Magnetic primary CTA, bento tiles lift on hover, tyre photos go from grayscale to colour with a scan line.
- Nav links wipe an accent underline in from the left.
- Work grid: filter pill slides between options (`layoutId`), tiles re-flow on filter. On hover a tile lifts, its accent rule wipes in, the arrow fills and the problem statement slides up from the bottom edge. Every affordance is anchored inside the tile, so nothing tracks the cursor and nothing can be clipped at the viewport edge.
- Case contents: the sidebar marker slides to the section being read; zoomable artefacts scale slightly under the cursor.
- Astro view transitions morph a case title from its tile into the case page header.

Every one of these is gated behind `prefers-reduced-motion: no-preference`, and the masked reveals only apply once JS has added `.js`, so text is never stuck invisible.

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

Case-file thumbnails are generated, not screenshotted: `scripts/gen-thumbs.py` renders one SVG per case file into `public/thumbs/` from that project's own data (grid SCADA series, default-rate matrix, fatigue rates, Kraljic coordinates), in the site palette with a single accent on the point of the chart. Each chart carries the project's own vocabulary (model names, loan purposes, Kraljic quadrants, journey steps) so the tile reads as that project rather than as an abstract shape. Labels use a generic monospace stack, because an SVG loaded through `<img>` cannot reach the site's web fonts. The source artefacts are Power BI and matplotlib exports in purple, magenta and green, which break the one-accent lock and turn to mush at 317px. Re-run the script after changing a case file's numbers. The whole set is about 20KB.

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
