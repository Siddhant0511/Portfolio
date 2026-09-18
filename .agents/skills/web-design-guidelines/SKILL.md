---
name: web-design-guidelines
description: Web design best practices for the portfolio project — responsive, accessible, performant, on-brand
---

# Web Design Guidelines

Reference: https://vercel.com/design

## Principles

- **Mobile-first**: Design for the smallest screen first, then enhance
- **Accessible**: WCAG AA minimum — contrast, focus states, semantic HTML, alt text
- **Performant**: Minimal JS, lazy assets, fast first paint (critical for QR-scan use case)
- **On-brand**: Follow DESIGN.md tokens faithfully — no deviation on color, type, spacing

## Responsive Breakpoints

| Breakpoint | Width | Target |
|------------|-------|--------|
| Mobile | < 736px | Primary (QR scan from CV) |
| Tablet | 736–980px | Secondary |
| Desktop | > 980px | Review/editing |

## Accessibility Checklist

- `prefers-reduced-motion` fallback for all animations
- Keyboard-focusable interactive elements (buttons, links, cards)
- `aria-label` on icon-only controls
- Sufficient color contrast in both light and dark themes
- `alt` text on all images

## Typography Rules

- Satoshi for display headlines and large numbers
- Geist for body text (16-17px, 1.6-1.75 line-height)
- Geist Mono for data and labels (`.label`: uppercase, 0.08em letter-spacing)
- Never mix more than 2 typefaces in one component
- Full token set lives in DESIGN.md (v2)

## This Project

The portfolio targets recruiters scanning a QR from a printed CV — mobile performance and 5-second credibility are the primary constraints. Every addition must pass: *"Does this help a recruiter decide I'm credible in under 5 seconds?"*
