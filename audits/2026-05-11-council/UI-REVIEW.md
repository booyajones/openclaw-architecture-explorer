<!-- VOICE-GUARD-OFF -->
# OpenClaw Architecture Explorer — Council Synthesis
Date: 2026-05-11
Site: https://openclaw-architecture-explorer.vercel.app/
Reviewers: design critique, accessibility (WCAG 2.1 AA), usability (3 mindsets), automated (Lighthouse + axe-core)

## Verdict

**Good, with 14 P0 defects between current and "absolutely top-notch."** Lighthouse baseline is strong (93/93/96/100) but the WCAG AA audit fails, design Rubric scores 22/30, and the usability review caught credibility bugs that a skeptical CTO spots in 5 seconds (hero counter disagreements). One Round 2 of fixes gets this to ship-grade for any audience.

## Council scores

| Reviewer | Score | Pass mark |
|---|---|---|
| Design (10 dimensions, /30) | 22/30 | 24 = pass, 27 = great |
| Accessibility (WCAG 2.1 AA) | FAIL | PASS |
| Lighthouse Accessibility | 93/100 | 100 |
| Lighthouse Performance | 93/100 | 95 |
| Lighthouse Best Practices | 96/100 | 100 |
| Lighthouse SEO | 100/100 | 100 |
| Usability — Skeptical CTO | undecided | wins |
| Usability — Curious Peer | wins | wins |
| Usability — Recruiter (cold) | loses | wins |

## P0 defect register (must close before Round 2)

Convergent findings across multiple reviewers carry highest confidence.

### Credibility bugs (UX)

- **P0-1 Counter inconsistencies.** Ground truth from the DATA object: 25 integrations, 23 crons, 42 projects. Hero shows 25, 23, **38** (wrong). Section headings, search placeholders, command palette, and status-bar ticker still say "19" for integrations and crons in 5+ places. A skeptical CTO bounces on this. *(usability + my verification)*

- **P0-2 "LIVE DATAFLOW · REALTIME" console is static.** Frozen 6 lines on first paint. Either stream every 6-10s or rename to "RECENT EVENTS · LAST 60s" and freeze honestly. *(design)*

- **P0-3 Project cards have `cursor: pointer` without a click handler.** Affordance lie. Either wire the cards to expand a detail panel or remove the pointer. *(usability)*

### Brand / voice violations (DESIGN)

- **P0-4 37 em dashes in body copy** (hero lede, every integration card description, section subs, memory footnote). Hard violation of Chris's no-em-dash rule. *(design)*

- **P0-5 Hero h1 gradient text** at 120deg `#6FCBF0 → #169EE3` on the proper noun "Booya Jones." Brand guidelines ban gradient text as AI tell. *(design)*

- **P0-6 h1 font-weight 800** exceeds DM Sans Bold (700) cap in brand tokens. *(design)*

- **P0-7 Twelve non-brand category colors in integration grid** (orange #B85C00, magenta #9C2A6E, plum #931C3D, indigo #3B40C4, olive #4A6A14, purple #4B2DA8, brown #7A5800, etc.). Brand palette is 4 primaries + 4 accents. *(design)*

### Accessibility blockers (WCAG 2.1 AA)

- **P0-8 Zero `:focus-visible` rules in the stylesheet.** UA default outline at 1.07:1 contrast on dark hero. Every keyboard user is flying blind. SC 2.4.7. *(design + a11y converge)*

- **P0-9 `role="tablist"` on filter chips** (#integFilters, #cronFilters, #projFilters) with plain `<button>` children. axe-core flags this as critical 3 times. SC 1.3.1, 4.1.2. *(a11y)*

- **P0-10 No `<main>` landmark.** Content is direct children of `<body>`. SC 1.3.1. *(a11y)*

- **P0-11 No skip-to-content link.** SC 2.4.1. *(a11y)*

- **P0-12 CRM integration pill `#B85C00 on #FFF1E6` at 4.15:1**, needs 4.5:1. SC 1.4.3. *(a11y)*

- **P0-13 Search trigger placeholder `--mc-text-3` (rgba(230,241,251,0.42)) at 3.26:1**, needs 4.5:1. SC 1.4.3. Same token underlies stat labels, dataflow meter, console timestamps, ticker delta-flat. *(a11y)*

### Mobile (Responsive)

- **P0-14 Section nav is `display: none` below 1080px with no hamburger replacement.** ⌘K is the only nav escape hatch on mobile. *(usability)*

## P1 register

- P1-1 Console error: `fonts/DMSans_18pt-SemiBold.ttf` 404 (Caption family). Also 13 other unreferenced weights silently 404 (Thin, ExtraLight, Light, MediumItalic, SemiBoldItalic, BoldItalic, ExtraBoldItalic, Black, BlackItalic, 18pt-Regular).
- P1-2 Console error: favicon.ico 404.
- P1-3 Hero subhead says "19 nightly crons" (should be 23). Status ticker "CRONS GREEN 19/19" (should be 23/23). Command palette meta says "19" for integrations and crons (should be 25 and 23). All same root cause as P0-1.
- P1-4 No `aria-current`/`aria-pressed` on active nav and filter chips. *(a11y)*
- P1-5 Cmd palette missing `aria-expanded`/`aria-haspopup`, no focus trap, focus not returned to trigger on Esc, input not autofocused on open. *(a11y)*
- P1-6 `#cmdkInput` no accessible name. *(a11y)*
- P1-7 Footer `<h4>` after `<h2>` (heading-order). *(a11y + Lighthouse)*
- P1-8 Mobile hero stats grid at 720px breakpoint becomes 3-col with 5 stats = orphan row of 2. *(design)*
- P1-9 No "Built by Chris Wyatt + contact" strip and no ending CTA. Recruiter mindset has no warm-handoff path. *(usability)*
- P1-10 Token drift: 6 letter-spacing values, 8 border-radius values across components. *(design)*

## P2 / P3

- P2-1 DOM size flagged by Lighthouse (heavy single-page).
- P2-2 44 small touch targets <44x44 (WCAG 2.5.5 AAA).
- P2-3 Project-grid items have `tabindex="0"` without `role` or keydown handler.
- P3-1 Four small caption colors (.stat-label, .dataflow-meter, .console .ts, .ticker-item .delta-flat) at 3.6-3.7:1.

## What's strong (preserve through revision)

- Mission-control aesthetic and personality
- Dataflow SVG with core hexagon + pulse animation
- Cron table with macOS-window chrome
- Hex-pattern watermark
- DM Sans across all roles
- 88px section padding rhythm
- 9-tab uppercase-mono nav
- Memory section 9-step recall pipeline (single most copyable artifact, per all reviewers)
- `prefers-reduced-motion: reduce` already honored
- Decorative SVGs already `aria-hidden`
- Cmd palette overlay has `role="dialog" + aria-modal="true"`

## Fix order

Batch A (mechanical, scripted): counter sync, em dash removal, ticker fix, palette count fix, missing-font CSS cleanup, favicon
Batch B (CSS additions): focus-visible system, --mc-text-3 contrast lift, kill h1 gradient + lower weight, normalize letter-spacing/radius tokens, mobile stat grid breakpoint
Batch C (HTML structural): wrap content in `<main>`, add skip-link, remove role="tablist" from filter chips, add aria-current/aria-pressed, project card click handler, cmdk focus management, h4 → h3 footer fix
Batch D (mobile nav): hamburger menu for <1080px
Batch E (integration colors): collapse 12 non-brand colors to brand palette
Batch F (closing CTA + author strip): add "Built by Chris Wyatt" + contact link
Batch G (verify): re-run Lighthouse + axe, screenshot diff, confirm 0 P0 open

After all batches: Round 2 gauntlet sweep for pattern-class defects (no fix lands only where flagged).
