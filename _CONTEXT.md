# Portfolio Project — Siddhant Morye

Single-page portfolio for **Siddhant Morye** (PGDM Candidate, Analytics & Operations, Great Lakes Institute of Management, Gurgaon). Architect-turned-analyst. Matches `DESIGN.md` (boardroom discipline + shop-floor precision).

## File Registry
- `index.html` — Core unified single-page portfolio
- `DESIGN.md` — Active design tokens, typography scale, and layout guidelines
- `_CONTEXT.md` — Active handoff context and token-efficient history
- `Siddhant_Morye_Resume.pdf` — Resume asset
- `img/photo.jpg` — Face avatar image

## Implemented Architecture & Milestones

### 1. Hero & Navigation
- **Sticky Frosted Header**: Added a sticky navigation header (`backdrop-filter: blur(12px)`) with anchor links (`#about`, `#experience`, `#qualifications`, `#case-files`, `#capabilities`, `#contact`). 
- **Header Mobile Adaptation**: Centers navigation links and hides secondary links (`Qualifications`, `Capabilities`) on viewports under `736px` to fit 4 primary tabs on a single line with **zero wrapping or horizontal scrolling**.
- **Hero Metadata**: Grouped avatar photo, name, and meta details into a vertical flex stack, center-aligned to the full name. Replaced bullet divider dot with a thin pipe (`|`) and removed down-scroll arrow icons.

### 2. Experience Timeline (Ashok Leyland & Kembhavi)
- **Role Update**: Kembhavi Architecture Foundation entry corrected to *Architectural Intern*.
- **Text Justification**: Set all text copy (timeline paragraphs and bullet lists) to `text-align: justify` without horizontal character width limits (`max-width`) to fill cards.
- **Bullet Elements**: Custom list markers updated from hyphens (`-`) to standard round bullets (`•`).

### 3. Qualifications (Swapped Position)
- **Visual Swap**: Re-ordered Qualifications section directly above the Case Files section.
- **Table Alignment**: Right-aligned both the "Year" table header (`th:last-child`) and row cells to prevent misalignment.
- **Mobile Stack Cards**: Collapses the qualifications table below `600px` into vertical profile cards, hiding headers and formatting grades/years cleanly.

### 4. Case Files (Interactive Dossiers)
- **FLIP Expansion**: Shared-element modal transition. Clicking a manifest card scales the box to fill the viewport, fading backgrounds to Ink and displaying a dark dossier overlay.
- **Staggered Content**: Counts metrics from 0, draws SVG process flowlines (left-to-right), traps focus, and closes via ESC/Close keys. Honors `prefers-reduced-motion`.

### 5. Academic Block & Course Grid
- **Single-Line Title**: Locked `PGDM | Analytics & Operations` to a single line on desktop/tablet (`white-space: nowrap`) with matching fluid text size.
- **Course Grid**: Restructured courses flexbox into a uniform 2-column grid layout (collapsing to single-column under `480px`).

### 6. Minimal Accent Panel Coloration
Introduced subtle background tints (`rgba` < 4%) to layout panels to break the flat grey blandness:
- **Steel Blue**: Academics (`rgba(46, 68, 87, 0.025)`), timeline items, and tags.
- **Signal Amber**: Case cards (`rgba(217, 138, 43, 0.015)`) deepening on hover.
- **Muted Graphite**: Recognition items and capability cards.

### 7. Standalone HTML Architecture & GitHub Pages
- **Astro Boilerplate Purge**: Reverted all Astro integrations and modules to restore a clean, serverless local workspace consisting solely of HTML, CSS, and vanilla JS. Removed the local Astro skill.
- **GitHub Pages Deploy**: Renamed the entry page to `index.html` and configured remote origin tracking for `https://github.com/Siddhant0511/Portfolio.git` on the `main` branch to host the static portfolio live at `https://siddhant0511.github.io/Portfolio/`.
- **Full Viewport Optimization**: Removed the page container max-width limit and paragraph width constraints in the About segment, ensuring the page content scales to fully utilize widescreen displays without empty side margins.

## Active Rules & Guidelines
1. **Never** use em-dashes (`—`) in text copy; use pipes (`|`), commas, or hyphens.
2. Maintain single color accent (Amber `#D98A2B`) and strict corner radius (2px) throughout.
3. Every button or text block must maintain a minimum WCAG AA contrast ratio against background panels.

