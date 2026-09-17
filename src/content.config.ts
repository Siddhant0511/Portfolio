import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const metric = z.object({
  /** Numeric value animates with a ticker; omit for text-only metrics such as "Zero". */
  value: z.number().optional(),
  display: z.string().optional(),
  prefix: z.string().optional(),
  suffix: z.string().optional(),
  decimals: z.number().optional(),
  label: z.string(),
});

const work = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/work' }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      fileId: z.string(),
      order: z.number(),
      group: z.enum(['internship', 'competition', 'academic']),
      org: z.string(),
      context: z.string(),
      period: z.string(),
      year: z.string(),
      role: z.string(),
      team: z.string().optional(),
      summary: z.string(),
      problem: z.string(),
      tools: z.array(z.string()),
      tags: z.array(z.string()),
      metrics: z.array(metric).min(2).max(4),
      /** Raster cover for image-led tiles and social cards; chart-led projects draw an SVG cover instead. */
      cover: image().optional(),
      coverAlt: z.string().optional(),
      award: z.string().optional(),
      links: z.array(z.object({ label: z.string(), href: z.string() })).default([]),
      draft: z.boolean().default(false),
    }),
});

export const collections = { work };
