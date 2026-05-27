# OpenClaw Architecture Explorer

Interactive deep-dive into the [OpenClaw](https://openclaw.ai) internal architecture, modules, and data flow.

**Live site:** [pincer.patrykgolabek.dev/openclaw-architecture/](https://pincer.patrykgolabek.dev/openclaw-architecture/)

Built by [Patryk Golabek](https://github.com/PatrykQuantumNomad) as part of [Pincer Ops](https://pincer.patrykgolabek.dev/) — a GitOps-driven Kubernetes platform for deploying OpenClaw at scale.

## Documentation

- **[Scaling Guide](scaling-guide.md)** — Hardware requirements, concurrency patterns, and architecture recommendations for 2 to 200+ simultaneous jobs

## Overview

The Architecture Explorer visualizes the full OpenClaw stack:

- **User-Facing Surfaces** — CLI, Web UI, TUI, macOS/iOS/Android apps
- **Messaging Channels** — WhatsApp, Telegram, Discord, Slack, Signal, iMessage, LINE, and 20+ more via extensions
- **Gateway (Core Engine)** — WebSocket server, routing, sessions, auth, hooks
- **AI Agent Layer** — Pi-embedded runner, tools, skills, sandbox, sub-agents
- **Infrastructure & Storage** — Memory (SQLite+Vec), config, plugins, media, security
- **AI Model Providers** — Anthropic, OpenAI, Google, Ollama, and 15+ more

## Source

The source code for the Pincer Ops project (including this explorer):

- **GitHub:** [PatrykQuantumNomad/pincer-ops](https://github.com/PatrykQuantumNomad/pincer-ops)
- **License:** MIT

## Quick Start (to deploy Pincer Ops)

```bash
# Fork on GitHub first, then:
git clone https://github.com/<your-username>/pincer-ops.git
cd pincer-ops
make setup-repo
make up          # Bootstraps Kinder cluster + ArgoCD + OpenClaw
make status      # Check all apps are Synced
make openclaw-onboard   # Configure LLM provider keys
```
