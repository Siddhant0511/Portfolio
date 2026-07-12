---
name: tailwind-4-docs
description: Tailwind CSS v4 reference — utility classes, responsive design, custom config for the portfolio project
---

# Tailwind CSS v4

Docs: https://tailwindcss.com/docs

## Key Concepts (v4)

- **CSS-first config**: Use `@import "tailwindcss"` in your CSS entry point
- **No `tailwind.config.js` needed** — custom values via `@theme` directive
- **Utility classes**: `flex`, `grid-cols-2`, `p-4`, `text-lg`, `font-bold`, etc.
- **Responsive prefixes**: `sm:`, `md:`, `lg:`, `xl:`, `2xl:`
- **Dark mode**: `dark:` prefix (if enabled)
- **Arbitrary values**: `w-[300px]`, `bg-[#123456]`

## Common Utilities for This Project

| Purpose | Classes |
|---------|---------|
| Layout | `container mx-auto px-4` |
| Flex | `flex items-center justify-between gap-4` |
| Grid | `grid grid-cols-1 md:grid-cols-2 gap-4` |
| Typography | `font-sans text-base leading-relaxed` |
| Spacing | `p-4 py-8 mt-4 mb-2 space-y-4` |
| Borders | `border border-gray-200 rounded` |
| Colors | `text-gray-600 bg-white hover:bg-gray-50` |

## Custom Theme (@theme)

```css
@import "tailwindcss";
@theme {
  --color-paper: #F5F4F0;
  --color-ink: #171A1C;
  --color-amber: #D98A2B;
}
```

When building new components, reference `DESIGN.md` for the project's design tokens.
