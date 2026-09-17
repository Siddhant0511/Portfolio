# Portfolio | Siddhant Morye

Portfolio for **Siddhant Morye**, PGDM candidate in Analytics & Operations at Great Lakes Institute of Management, Gurgaon.

Live: https://siddhant0511.github.io/Portfolio/

## Stack

Astro 7 with React islands, Tailwind CSS v4, Motion, MDX. Design system and rules are in [DESIGN.md](DESIGN.md).

## Develop

```bash
npm install
npx astro dev --background   # http://localhost:4321/Portfolio/
npx astro dev stop
npm run build                # static output in dist/
```

## Where things live

| Path | What |
|---|---|
| `src/pages/index.astro` | Home page |
| `src/pages/work/[slug].astro` | Case file template |
| `src/content/work/*.mdx` | One case study per file (frontmatter + body) |
| `src/components/site/` | Home page sections, header, footer |
| `src/components/case/` | Chart and diagram kit used inside case studies |
| `src/components/ui/` | Motion components from Magic UI and motion-primitives |
| `src/lib/site.ts` | Profile data: contact, experience, education, awards, tools |
| `src/data/` | Chart data computed from the original project datasets |
| `src/assets/` | Portrait and project artefacts (optimised at build) |
| `public/demos/` | Live prototypes: TezCredit and VitalChain |
| `legacy/index.html` | Previous single-file version of the site |

## Adding a case file

1. Create `src/content/work/<slug>.mdx` with the frontmatter fields defined in `src/content.config.ts`.
2. Write the body with `##` sections (they build the contents sidebar) and components from `src/components/case/`.
3. Internship entries appear in the featured bento; competitions and academic work appear in the filterable index.

## Résumé button

Put an up-to-date PDF at `public/resume.pdf` and set `resume: 'resume.pdf'` in `src/lib/site.ts`.

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages. In the repository settings, Pages must use **GitHub Actions** as its source.
