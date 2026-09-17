# Portfolio Project | Siddhant Morye

Handoff context for the v2 redesign (September 2026). Design system: `DESIGN.md`. Setup and structure: `README.md`.

## What changed from v1
- Rebuilt from a single hand-written `index.html` (now in `legacy/`) into Astro 7 + React islands + Tailwind v4 + Motion.
- New visual language: drawing-sheet details, Bricolage Grotesque / Geist / Geist Mono, signal-orange accent, light and dark themes.
- Case files moved from modal dossiers to dedicated pages, one per project, written in MDX.
- Expanded from 4 internship projects to 13 case files: 4 Ashok Leyland workstreams, 3 case competitions, 6 academic projects.
- Charts are drawn from the source data (NLDC SCADA, StreamMax, credit dataset) or from figures stated in the reports. Several v1 numbers that did not appear in the SIP report were removed.
- TezCredit and VitalChain prototypes are hosted in `public/demos/`, with screenshots captured from the running apps.

## Post-launch revisions (18 September 2026)
- Display face changed from Bricolage Grotesque to **Satoshi** (Fontshare provider, discrete weights). Bricolage package removed.
- Hero: tighter portrait crop, full institute name, job title now "Summer Intern, Analytics & Operations" (HR dropped).
- The four-number proof strip under the hero was removed; the hero now flows straight into the work section.
- Academic record table is centre-aligned.
- Added a motion layer: masked heading reveals, portrait wipe, timeline node fills, nav and row underline wipes, sliding contents marker, self-drawing case section rules, hover zoom on zoomable artefacts.
- CI fix: TypeScript pinned to 6.x, because `@astrojs/check` peers on ^5 || ^6 and the 7.x install broke `npm ci` in the Pages workflow.

## Case files
| ID | Slug | Source material |
|---|---|---|
| AL-01 | grievance-platform | SIP report and presentation |
| AL-02 | contractor-absenteeism | SIP report, presentation, report figures |
| AL-03 | time-office | SIP report and presentation |
| AL-04 | al-tics | SIP report, presentation, tyre images |
| CC-01 | vguard-bess | Executive summary, NLDC SCADA CSVs, BESS charts, SBU model inputs |
| CC-02 | quantum-trial | Crest Analytics deck and script |
| CC-03 | finception-credit-risk | Deck, Power BI export, cleaned credit dataset |
| AC-01 | streammax-fatigue | Power BI dashboard, deck, dataset |
| AC-02 | tezcredit | Prototype and presentation script |
| AC-03 | vitalchain | Prototype and presentation script |
| AC-04 | butterfly-valves | SSP deck |
| AC-05 | printcraft-erp | Capstone presentation, Odoo audit screenshots, BPMN swimlanes |
| AC-06 | novatel-erp | Individual ERP design report and Bizagi models |

## Open items to confirm
- Exact personal role in group projects (Finception, StreamMax, TezCredit, VitalChain, SSP, PrintCraft) and in V-Guard; currently worded conservatively.
- V-Guard competition result, if any, to add as an award badge.
- An updated résumé PDF that includes the Ashok Leyland internship, to enable the résumé button.
- First-person About copy should be read and adjusted to Siddhant's own voice.

## Rules
1. No em dashes or en dashes in visible copy.
2. One accent colour; charts are neutral plus accent.
3. Every metric traces to a source; projections are labelled.
4. WCAG AA contrast, visible focus, reduced-motion fallbacks.
