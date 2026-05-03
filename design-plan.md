# OpenClaw Architecture Explorer v2 — Design Plan

## Problems with v1 (current page)

1. **All content behind clicks** — nothing visible at a glance; you must click each component to see its details
2. **Process flow is buried** — "Message Data Flow" section exists but is collapsed, same pattern as everything else
3. **No holistic visual** — no way to see the full message lifecycle (user → channel → gateway → agent → LLM → back) as one continuous diagram
4. **Click-to-reveal is clunky** — expansion is animated but each click only reveals one small section

## Design Principles

- **One-glance architecture**: The core process flow must be visible without any interaction
- **Layered but connected**: Show layers stacked vertically with arrows/connections between them
- **Progressive disclosure**: Click/hover reveals details but doesn't hide the overall picture
- **Clean, premium dark theme**: Consistent with open-source tool aesthetic, good typography, spacious

## Layout

```
┌──────────────────────────────────────────────────┐
│ Stats Bar: 378K lines | 2188 files | 38 ext | │
│           10+ channels | 4 apps                 │
├──────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────────── MESSAGE FLOW ──────────────┐  │
│  │                                             │  │
│  │  User ─▶ Channel ─▶ Routing ─▶ Gateway ─▶│  │
│  │                                    │        │  │
│  │                                    ▼        │  │
│  │                              Agent ─▶ LLM  │  │
│  │                                    │        │  │
│  │                                    ▼        │  │
│  │                           Tool Policy       │  │
│  │                                    │        │  │
│  │                                    ▼        │  │
│  │                             Sandbox         │  │
│  │                                    │        │  │
│  │                                    ▼        │  │
│  │                          Result → Agent     │  │
│  │                                             │  │
│  │  Response: LLM ─▶ Subscribe ─▶ Gateway     │  │
│  │                    ─▶ Channel ─▶ User       │  │
│  └─────────────────────────────────────────────┘  │
│                                                    │
│  ┌───────────── ARCHITECTURE LAYERS ────────────┐  │
│  │                                               │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │ USER SURFACES: CLI · Web UI · TUI       │  │  │
│  │  │ macOS · iOS · Android                │  │  │
│  │  └──────────────┬──────────────────────────┘  │  │
│  │                 ▼                              │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │ CHANNELS: WhatsApp · Telegram · Discord  │  │  │
│  │  │ Slack · Signal · iMessage · 20+ ext   │  │  │
│  │  └──────────────┬──────────────────────────┘  │  │
│  │                 ▼                              │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │ GATEWAY: Server · Routing · Sessions     │  │  │
│  │  │ Auth · Hooks                             │  │  │
│  │  └──────────────┬──────────────────────────┘  │  │
│  │                 ▼                              │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │ AGENT LAYER: Pi Runner · Tools · Skills  │  │  │
│  │  │ Sandbox · Sub-Agents                     │  │  │
│  │  └──────────────┬──────────────────────────┘  │  │
│  │                 ▼                              │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │ INFRA: Memory · Config · Plugins         │  │  │
│  │  │ Media · Security · Infra Utility       │  │  │
│  │  └──────────────┬──────────────────────────┘  │  │
│  │                 ▼                              │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │ PROVIDERS: Anthropic · OpenAI · Google   │  │  │
│  │  │ Ollama · 15+ more                        │  │  │
│  │  └─────────────────────────────────────────┘  │  │
│  └─────────────────────────────────────────────┘  │
│                                                    │
│  ┌───────────── MODULE REFERENCE ───────────────┐  │
│  │  Grid of cards: each module with name,       │  │
│  │  file count, path, description. Inline       │  │
│  │  expand for details.                         │  │
│  └─────────────────────────────────────────────┘  │
│                                                    │
│  ┌───────────── EXTENSIONS ────────────────────┐  │
│  │  Grouped by type: Channels · AI Tools       │  │
│  │  Memory · Auth                               │  │
│  └─────────────────────────────────────────────┘  │
│                                                    │
│  ┌───────────── TECH STACK ────────────────────┐  │
│  │  Language, Build, Test, Lint, etc.          │  │
│  └─────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

## Technical Implementation

- Single-file static HTML (zero dependencies, loads from any static host)
- No build step, no JS frameworks
- CSS Grid + Flexbox for layout
- Custom SVG arrows for process flow (no external library)
- CSS transitions for hover/expand interactions
- Dark theme with OpenClaw-inspired color palette (#043886 navy, #169ee3 bright blue accent)
- Deploy via GitHub Pages from the `booyajones/openclaw-architecture-explorer` repo

## Interactive Behaviors

- Process flow diagram: always visible, no click needed
- Architecture layers: hover highlights connected components, click expands details inline
- Module reference: grid of cards, click to expand description inline
- Extensions: filterable/searchable card grid

## What Makes It Better Than v1

| Aspect | v1 (Pincer) | v2 (this design) |
|--------|-------------|------------------|
| Process flow visibility | Hidden behind click | Always visible hero section |
| Layer relationships | Isolated cards | Connected vertical stack with arrows |
| Module details | Separate overlay/page | Inline expand within same view |
| At-a-glance understanding | Requires 6+ clicks | One glance shows full picture |
| Extension browsing | Long flat list | Categorized grid |
| Tech stack | Separate section | Compact reference table |
