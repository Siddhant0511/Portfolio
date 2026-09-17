import { getCollection, type CollectionEntry } from 'astro:content';

export type Work = CollectionEntry<'work'>;

export async function getWork(): Promise<Work[]> {
  const entries = await getCollection('work', ({ data }) => !data.draft);
  return entries.sort((a, b) => a.data.order - b.data.order);
}

export function workHref(entry: Work | string) {
  const id = typeof entry === 'string' ? entry : entry.id;
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/work/${id}/`;
}

/** Resolve a link from frontmatter: absolute URLs pass through, site paths get the base prefix. */
export function resolveLink(href: string) {
  if (/^https?:\/\//.test(href)) return href;
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${href.replace(/^\//, '')}`;
}
