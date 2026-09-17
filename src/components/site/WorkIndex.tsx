import { useEffect, useMemo, useRef, useState } from 'react';
import {
  AnimatePresence,
  LayoutGroup,
  motion,
  useMotionValue,
  useReducedMotion,
  useSpring,
} from 'motion/react';
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
  tags: string[];
};

type Filter = 'all' | 'competition' | 'academic';

const filters: { key: Filter; label: string }[] = [
  { key: 'all', label: 'All' },
  { key: 'competition', label: 'Case competitions' },
  { key: 'academic', label: 'Academic' },
];

export default function WorkIndex({ items }: { items: IndexItem[] }) {
  const [filter, setFilter] = useState<Filter>('all');
  const [active, setActive] = useState<string | null>(null);
  const [canHover, setCanHover] = useState(false);
  const reduceMotion = useReducedMotion();
  const listRef = useRef<HTMLUListElement>(null);

  const x = useMotionValue(0);
  const y = useMotionValue(0);
  const sx = useSpring(x, { stiffness: 260, damping: 30, mass: 0.6 });
  const sy = useSpring(y, { stiffness: 260, damping: 30, mass: 0.6 });

  useEffect(() => {
    const mq = window.matchMedia('(hover: hover) and (pointer: fine) and (min-width: 1024px)');
    const update = () => setCanHover(mq.matches);
    update();
    mq.addEventListener('change', update);
    return () => mq.removeEventListener('change', update);
  }, []);

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
  const activeItem = visible.find((i) => i.id === active);

  const onMove = (e: React.PointerEvent) => {
    x.set(e.clientX + 24);
    y.set(e.clientY + 24);
  };

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

      <ul ref={listRef} className="relative" onPointerMove={canHover ? onMove : undefined} onPointerLeave={() => setActive(null)}>
        <AnimatePresence initial={false} mode="popLayout">
          {visible.map((item) => (
            <motion.li
              key={item.id}
              layout={reduceMotion ? false : 'position'}
              initial={reduceMotion ? false : { opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              exit={reduceMotion ? { opacity: 0 } : { opacity: 0, y: -8 }}
              transition={{ duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
              className="border-b border-line"
            >
              <a
                href={item.href}
                onPointerEnter={() => setActive(item.id)}
                onFocus={() => setActive(item.id)}
                onBlur={() => setActive(null)}
                className="group relative grid grid-cols-[3.75rem_1fr_auto] items-start gap-x-4 gap-y-1 py-5 transition-colors sm:grid-cols-[5rem_1fr_auto] sm:py-6 lg:grid-cols-[6rem_minmax(0,1fr)_minmax(0,20rem)_4rem_2.5rem] lg:items-center"
              >
                <span
                  aria-hidden="true"
                  className="absolute -bottom-px left-0 h-px w-full origin-left scale-x-0 bg-accent transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:scale-x-100 group-focus-visible:scale-x-100 motion-reduce:transition-none"
                />
                <span className="pt-1 font-mono text-xs text-muted transition-colors group-hover:text-accent-ink lg:pt-0">
                  {item.fileId}
                </span>
                <span className="min-w-0">
                  <span className="flex items-center gap-2 font-display text-xl leading-tight font-semibold tracking-[-0.025em] transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:translate-x-1.5 sm:text-2xl">
                    {item.title}
                    {item.award && (
                      <span className="inline-flex shrink-0 items-center gap-1 border border-accent/40 bg-accent-soft px-1.5 py-0.5 font-mono text-[10px] font-normal tracking-[0.06em] text-accent-ink uppercase">
                        <TrophyIcon className="size-3" aria-hidden="true" />
                        {item.award}
                      </span>
                    )}
                  </span>
                  <span className="mt-1 block text-sm text-muted">
                    {item.org}, {item.context}
                  </span>
                </span>
                <span className="col-start-3 row-start-1 pt-1 text-right font-mono text-xs text-muted lg:col-start-4 lg:pt-0">
                  {item.year}
                </span>
                <span className="hidden flex-wrap justify-end gap-1.5 lg:col-start-3 lg:row-start-1 lg:flex">
                  {item.tags.slice(0, 2).map((t) => (
                    <span key={t} className="border border-line px-2 py-0.5 text-xs text-ink-2">
                      {t}
                    </span>
                  ))}
                </span>
                <span className="hidden size-10 place-items-center justify-self-end border border-line transition-colors duration-300 group-hover:border-accent group-hover:bg-accent group-hover:text-white lg:col-start-5 lg:grid">
                  <ArrowUpRightIcon className="size-4" aria-hidden="true" />
                </span>
              </a>
            </motion.li>
          ))}
        </AnimatePresence>
      </ul>

      {canHover && (
        <motion.div
          aria-hidden="true"
          className="pointer-events-none fixed top-0 left-0 z-40"
          style={{ x: reduceMotion ? x : sx, y: reduceMotion ? y : sy }}
        >
          <AnimatePresence>
            {activeItem && (
              <motion.div
                key={activeItem.id}
                initial={{ opacity: 0, scale: 0.94, rotate: -1.5 }}
                animate={{ opacity: 1, scale: 1, rotate: 0 }}
                exit={{ opacity: 0, scale: 0.96 }}
                transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
                className="w-80 border border-line-strong bg-surface p-5 shadow-[0_24px_60px_-24px_rgb(var(--shadow-tint)/0.45)]"
              >
                <div className="flex items-center justify-between">
                  <span className="font-mono text-[11px] tracking-[0.08em] text-accent-ink uppercase">{activeItem.fileId}</span>
                  <span className="font-mono text-[11px] tracking-[0.08em] text-muted uppercase">{activeItem.year}</span>
                </div>
                <p className="mt-4 font-display text-4xl leading-none font-semibold tracking-[-0.04em]">
                  {activeItem.metric.value}
                </p>
                <p className="mt-2 text-sm text-ink-2">{activeItem.metric.label}</p>
                <p className="mt-4 border-t border-line pt-3 text-sm leading-snug text-muted">{activeItem.problem}</p>
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>
      )}
    </div>
  );
}
