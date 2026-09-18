import { useMemo, useState } from 'react';
import { AnimatePresence, LayoutGroup, motion, useReducedMotion } from 'motion/react';
import { ArrowUpRightIcon, TrophyIcon } from '@phosphor-icons/react';
import { cn } from '@/lib/utils';

export type IndexItem = {
  id: string;
  href: string;
  fileId: string;
  title: string;
  org: string;
  context: string;
  year: string;
  group: 'competition' | 'academic' | 'internship';
  problem: string;
  metric: { value: string; label: string };
  award?: string;
  /** Generated from the case file's own data, see scripts/gen-thumbs.py. */
  thumb: string;
};

type Filter = 'all' | 'competition' | 'academic';

const filters: { key: Filter; label: string }[] = [
  { key: 'all', label: 'All' },
  { key: 'competition', label: 'Case competitions' },
  { key: 'academic', label: 'Academic' },
];

export default function WorkIndex({ items }: { items: IndexItem[] }) {
  const [filter, setFilter] = useState<Filter>('all');
  const reduceMotion = useReducedMotion();

  const visible = useMemo(
    () => (filter === 'all' ? items : items.filter((i) => i.group === filter)),
    [filter, items],
  );
  const counts = useMemo(
    () => ({
      all: items.length,
      competition: items.filter((i) => i.group === 'competition').length,
      academic: items.filter((i) => i.group === 'academic').length,
    }),
    [items],
  );

  return (
    <div>
      <div className="flex flex-wrap items-center justify-between gap-4 border-b border-line pb-4">
        <LayoutGroup id="work-filter">
          <div role="group" aria-label="Filter case files" className="flex flex-wrap gap-1">
            {filters.map((f) => {
              const selected = filter === f.key;
              return (
                <button
                  key={f.key}
                  type="button"
                  aria-pressed={selected}
                  onClick={() => setFilter(f.key)}
                  className={cn(
                    'relative flex h-9 cursor-pointer items-center gap-2 px-3 text-sm transition-colors',
                    selected ? 'text-bg' : 'text-ink-2 hover:text-ink',
                  )}
                >
                  {selected && (
                    <motion.span
                      layoutId="filter-pill"
                      className="absolute inset-0 bg-ink"
                      transition={reduceMotion ? { duration: 0 } : { type: 'spring', stiffness: 420, damping: 36 }}
                    />
                  )}
                  <span className="relative">{f.label}</span>
                  <span className={cn('relative font-mono text-[11px]', selected ? 'text-bg/70' : 'text-muted')}>
                    {counts[f.key]}
                  </span>
                </button>
              );
            })}
          </div>
        </LayoutGroup>
        <p className="label" aria-live="polite">
          Showing {visible.length} of {items.length}
        </p>
      </div>

      <ul className="mt-8 grid grid-cols-1 gap-x-5 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        <AnimatePresence initial={false} mode="popLayout">
          {visible.map((item) => (
            <motion.li
              key={item.id}
              layout={reduceMotion ? false : 'position'}
              initial={reduceMotion ? false : { opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={reduceMotion ? { opacity: 0 } : { opacity: 0, scale: 0.97 }}
              transition={{ duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
              className="h-full"
            >
              {/* Fills the stretched grid cell so the metric rules line up across a row. */}
              <a href={item.href} className="tile group flex h-full flex-col">
                <div className="tile-plate relative aspect-[5/4] overflow-hidden border border-line bg-surface">
                  {/* Drawn from this project's own numbers, in the site palette. */}
                  <img
                    src={item.thumb}
                    alt=""
                    loading="lazy"
                    decoding="async"
                    className="tile-img size-full object-cover"
                  />

                  <div className="pointer-events-none absolute inset-x-0 top-0 flex items-start justify-between gap-2 p-4">
                    <span className="flex min-w-0 items-center gap-2">
                      <span className="font-mono text-[11px] tracking-[0.08em] text-accent-ink uppercase">
                        {item.fileId}
                      </span>
                      {item.award && (
                        <span className="inline-flex shrink-0 items-center gap-1 border border-accent/40 bg-accent-soft px-1.5 py-0.5 font-mono text-[10px] tracking-[0.06em] text-accent-ink uppercase">
                          <TrophyIcon className="size-3" aria-hidden="true" />
                          {item.award}
                        </span>
                      )}
                    </span>
                    <span className="font-mono text-[11px] tracking-[0.08em] text-muted uppercase">{item.year}</span>
                  </div>

                  {/* Anchored inside the tile, so it can never be clipped by the viewport the
                      way the old cursor-following card was at the bottom of the list. */}
                  <div
                    aria-hidden="true"
                    className="tile-pop absolute inset-x-0 bottom-0 border-t border-line bg-surface-2 px-4 py-3.5"
                  >
                    <p className="line-clamp-3 text-[12.5px] leading-snug text-ink-2">{item.problem}</p>
                  </div>

                  <span
                    aria-hidden="true"
                    className="tile-rule absolute inset-x-0 bottom-0 h-px origin-left bg-accent"
                  />
                </div>

                <div className="mt-4 mb-3 flex items-start justify-between gap-3">
                  <div className="min-w-0">
                    <h3 className="font-display text-lg leading-tight font-semibold tracking-[-0.025em] text-balance">
                      {item.title}
                    </h3>
                    <p className="mt-1 text-[13px] leading-snug text-muted">
                      {item.org}, {item.context}
                    </p>
                  </div>
                  <span className="tile-arrow mt-0.5 grid size-8 shrink-0 place-items-center border border-line text-ink-2">
                    <ArrowUpRightIcon className="size-4" aria-hidden="true" />
                  </span>
                </div>

                <p className="mt-auto flex items-baseline gap-2 border-t border-line pt-3">
                  <span className="font-display text-xl leading-none font-semibold tracking-[-0.03em]">
                    {item.metric.value}
                  </span>
                  <span className="min-w-0 flex-1 text-[12.5px] leading-snug text-muted">{item.metric.label}</span>
                </p>
              </a>
            </motion.li>
          ))}
        </AnimatePresence>
      </ul>
    </div>
  );
}
