# Portfolio Design Doc — Siddhant Morye

**Type:** Single-page HTML portfolio, linked via QR code on CV
**Audience:** Recruiters / interview panels, mostly opening on a phone right after scanning a printed QR
**Job the page has to do:** In under 5 seconds, read as *credible MBA candidate* — then reward a slower read with evidence of real analytical + technical depth (Ops & Analytics specialization, Ashok Leyland SIP, self-built AI tooling).

---

## 1. Creative direction

MBA portfolios default to one of two clichés: the "consulting deck" (navy, serif logo-mark, generic stock icons) or the "developer portfolio" (dark mode, terminal font, neon accent). You're neither — you're an Ops & Analytics candidate who happens to build real software (dashboards, RAG pipelines, CNN classifiers) as a strategic edge, not as a hobby flex. The design should read that tension honestly: **boardroom discipline, shop-floor precision.**

The grounding metaphor: your internship lived inside *plant documentation* — work orders, shift registers, gate passes, a plant literally called "Plant 2004." That world already has a visual language: manifest numbers, stamped headers, tight tabular data, hairline rules. We borrow that vernacular — quietly, not literally (no fake rubber-stamp textures) — and pair it with clean editorial typography so it still reads as *personal brand*, not *cosplay industrial.*

**Signature element:** Projects are shown as compact **case-file cards** (like a manifest index). Clicking one doesn't navigate to a new page — it *opens the file*: the card expands in place into a full case study, contents staggering in like a dossier being pulled and unfolded (metrics count up, a process line draws itself, sections slide in from the card's edge). This is where your one motion "risk" lives — everywhere else stays quiet and disciplined.

---

## 2. Design tokens

### Color
| Name | Hex | Use |
|---|---|---|
| Paper | `#F5F4F0` | Page background — warm off-white, not cream-terracotta cliché |
| Ink | `#171A1C` | Primary text, dark surfaces (case-file expanded view) |
| Graphite | `#5B6570` | Secondary text, captions, meta |
| Signal Amber | `#D98A2B` | Single accent — used like a hazard-stripe / gauge-needle, never decorative |
| Steel | `#2E4457` | Secondary accent — data, charts, links |
| Hairline | `#DAD6CC` | Borders, dividers, table rules |

Rule: Amber only ever marks *one thing per screen* (an active state, a key metric, the hovered card). If two elements are amber at once, dial one back to Steel.

### Type
| Role | Typeface | Notes |
|---|---|---|
| Display | **Fraunces** (serif, weight 500–600, slight optical sizing) | Headlines, name, section titles — gives editorial warmth against the industrial data language |
| Body | **Inter** | All running text, 16–18px base, 1.55 line-height |
| Data / Labels | **IBM Plex Mono** | Manifest IDs, dates, metrics, tags, nav labels — small caps, letter-spacing 0.04em |

Type scale (base 16px): 12 / 14 / 16 / 20 / 28 / 40 / 64 — display headline only ever uses 40 or 64.

### Spacing & shape
- 8px base unit, section rhythm on 96px (desktop) / 56px (mobile)
- Radius: 2px everywhere (cards, buttons) — sharp enough to feel like a printed card, not a soft app
- Shadows: none by default; on hover/expand use a single hard offset shadow (`4px 4px 0 rgba(23,26,28,0.12)`) — reads as a card lifting off a stack, not a generic drop-shadow

---

## 3. Page structure (wireframe)

```
┌───────────────────────────────────────────┐
│ MORYE, S.        [PGDM · OPS & ANALYTICS]  │  ← sticky micro-header, mono
├───────────────────────────────────────────┤
│                                             │
│   Siddhant Morye                           │  ← Fraunces 64
│   Operations & Analytics · GLIM '27        │
│   [Ashok Leyland SIP — Alwar Plant 2004]   │  ← one-line credibility stamp
│                                             │
│   [view case files ↓]                      │
├───────────────────────────────────────────┤
│  ABOUT / ACADEMICS                         │
│  ─ short profile paragraph                 │
│  ─ academic record: PGDM specialization,   │
│    coursework highlights, GLIM             │
│  ─ meta strip: location, focus areas       │
├───────────────────────────────────────────┤
│  EXPERIENCE                                │
│  ─ Ashok Leyland SIP — role, dates, scope  │
│  ─ (any prior internship/work if relevant) │
├───────────────────────────────────────────┤
│  CASE FILES (projects)                     │
│  ┌──────────┐ ┌──────────┐                 │
│  │ FILE-01  │ │ FILE-02  │  ← manifest grid │
│  │ Grievance│ │Contractor│                 │
│  └──────────┘ └──────────┘                 │
│  ┌──────────┐ ┌──────────┐                 │
│  │ FILE-03  │ │ FILE-04  │                 │
│  │Time Office│ │ AL-TICS │                 │
│  └──────────┘ └──────────┘                 │
│  (click → full-screen expansion, see §4)   │
├───────────────────────────────────────────┤
│  CAPABILITIES                              │
│  ─ ops/analytics tools, AI-build stack,    │
│    a quiet nod to the "strategic + technical│
│    bridge" positioning                     │
├───────────────────────────────────────────┤
│  CONTACT                                   │
│  ─ email / phone / LinkedIn, resume link   │
└───────────────────────────────────────────┘
```

Numbering note: "FILE-01…04" is earned here, not decorative — your four SIP workstreams really were run and reported as discrete numbered project chapters, so a manifest ID is honest structure, not template dressing.

---

## 4. Motion system

Two tiers only — ambient (quiet, everywhere) and the signature interaction (bold, one place).

**Ambient (quiet, restrained):**
- Page load: micro-header and headline fade/rise 12px, staggered 80ms — under 500ms total, never a showy intro
- Scroll reveals: sections fade/rise once, 4px, no bounce, no repeat-on-rescroll
- Hover on case-file cards: card lifts 2px, hard shadow appears, manifest ID underlines in amber — all under 150ms

**Signature — opening a case file (this is where the motion budget goes):**
1. Click on a card → card's bounding box begins scaling/morphing to fill the viewport (shared-element transition, ~450ms ease)
2. Background dims to Ink, rest of grid recedes
3. Once expanded, contents stagger in over ~350ms:
   - Manifest header (project name, role, timeframe) slides in first
   - Key metrics count up from 0 (e.g. absenteeism % reduced, cycle time cut) — numbers only, no icons
   - A single process/flow line draws itself left-to-right under the metrics (stroke-dashoffset animation) — represents the actual before→after workflow, not decoration
   - Body sections (problem / approach / outcome) slide in from the right edge, one after another, 60ms stagger
4. Close (X or Esc) reverses the same transition back to the grid — never a hard cut

Keep this sequence identical across all four case files so it reads as a system, not four one-off effects.

**Reduced motion:** All of the above degrades to instant opacity crossfades if `prefers-reduced-motion` is set — no exceptions.

---

## 5. Content notes
- About section: 2–3 sentences max, written in plain first-person, no "results-driven professional" language. Say what you actually do (ops + analytics, building AI tools as a strategic lens).
- Each case file needs: one-line problem, your specific role, method/tools used, and a real outcome metric wherever you have one — recruiters skim for the metric.
- Capabilities section is the one place to mention the self-built tooling (local LLMs, RAG, dashboards) — framed as *why an MBA who can also build* is useful, not as a developer resume.

---

## 6. Build plan (part by part, as requested)

1. **Shell + tokens** — HTML structure, CSS variables for the token system above, type loaded, sticky micro-header, base layout for all sections (no motion yet)
2. **Hero + About/Academics** — static, responsive, content in
3. **Case-file component (built once)** — the card + expansion system fully working end-to-end with placeholder content for a single file, motion tuned and confirmed
4. **Populate remaining case files** — one at a time, reusing the confirmed component: FILE-01 → 02 → 03 → 04
5. **Experience + Capabilities + Contact** — static sections, consistent styling
6. **Polish pass** — mobile check (QR-scan-on-phone is the primary path), keyboard focus states, reduced-motion fallback, final self-critique against §1

---

## 7. Open assumptions (flag if wrong)
- Four case files = the four SIP workstreams (Grievance Platform, Contractor Absenteeism, Time Office Rectification, AL-TICS). Swap in different projects if you'd rather feature something else.
- Single scrolling page, no router — matches QR/CV use case (one link, fast load, no dead ends).
- No photo in hero by default — type-led per the direction above; easy to add a small photo in the micro-header if you want a face attached to the name.