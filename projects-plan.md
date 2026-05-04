# Architecture Explorer — Projects Section Plan

## Design Principles

- **Mirror the existing page style**: gold-accent cards, inline data-driven rendering
- **Categorize by purpose, not by tool**: avoid "Salesforce project" or "BigQuery project"
- **Allow multi-tagging**: one project can span business + personal (e.g., Finexio analysis lives in both)
- **Visual grouping with color-bounded cards** matching the cron tag pattern

## Definitions

- **Project**: A named workstream with a definable scope, active over a period of weeks or months. Has a clear owner and output.
- **Process**: An ongoing, recurring activity (e.g., BDR reports, competitor watch) that is tracked separately from finite projects.
- **Status**: Active (current work), Ongoing (maintenance mode, recurring), or Archive (completed or deprecated).

## Proposed Taxonomy

### 1. Finexio Operations (FINEXIO)
Ongoing CSO work: dashboards, reporting, pipeline analysis, marketing campaigns, and platform maintenance at Finexio.

| Project | Description |
|---------|-------------|
| BDR Executive Dashboard v2 | Sales pipeline, call analytics, rep heatmaps on Vercel |
| BDR Executive Reports | Weekly/monthly BDR performance reports and archives |
| Data Engine | BigQuery → Salesforce → Power BI semantic layer and analysis |
| Marketing Dashboard | Campaign metrics, HubSpot email stats, content performance |
| Finexio ROI Calculator | Prospect-facing ROI model on finexio.com |
| Finexio Website | finexio.com Webflow CMS, pages, collections |
| Finexio Brand Assets | Logos, color palettes, brand guidelines |
| Finexio Portal / Rebuild | Finexio portal redesign efforts |

### 2. Diligence & M&A (FINEXIO)
Discrete M&A advisory work and PE diligence responses. Each is a finite project with a clear start and end.

| Project | Description |
|---------|-------------|
| Project Franklin | Blackstone/M3 acquisition of Finexio — deal structure, economics, positioning |
| Blackstone Diligence | PE diligence responses, QA sessions, data room analysis |
| M3 Payments Analysis | M3 hospitality platform, payment rail displacement, AvidXchange competition |
| Birchstreet Analysis | Birchstreet buyer analysis, fee structures, penetration modeling |
| Visa BYOC & VARM | Visa bring-your-own-card and Visa Accounts Receivable Match diligence |
| VARM Integration | VARM tech analysis and integration planning |

### 3. Project Phoenix (FINEXIO) [ARCHIVED]
Internal restructuring analysis — completed April 2026. Kept in taxonomy as reference.

| Project | Description |
|---------|-------------|
| Phoenix Headcount Model | Staffing optimization, cost analysis, scenario planning |
| Phoenix Decision Memos | Executive decision memos, board-level communication |
| Phoenix Manifesto | Strategic vision document |

### 4. Personal Brand & Content (PERSONAL)
Public writing, LinkedIn presence, personal websites. Ongoing content pipeline with weekly cadence.

| Project | Description |
|---------|-------------|
| LinkedIn Newsletter | Sunday deep-dive, Monday rapid-fire, Friday newsletter — 3 weekly crons |
| LinkedIn Content Pipeline | Research → draft → gauntlet → post pipeline |
| Chris Executive Site | chriswyatt.dev — personal brand site on Vercel |
| Intel Dashboard | intel.chriswyatt.dev — thought leadership dashboard |
| Research & Analysis | Industry research, trend analysis, long-form writing |

### 5. Job Search (PERSONAL) [ACTIVE]
Executive transition planning. Time-sensitive — daily/weekly activity cadence.

| Project | Description |
|---------|-------------|
| Job Search | C-level (CSO/CRO/COO/President) at healthcare+fintech |
| Target Company Watcher | Automated monitoring of top-20 target companies |
| Weekly Briefing | Sunday synthesis of market intel and positioning |
| Resume & Materials | Ramp doc, executive summaries, positioning docs |

### 6. ErrorCodeFixes.com (PERSONAL) [ONGOING]
Side project — monetized content site. Maintenance mode with periodic content updates.

| Project | Description |
|---------|-------------|
| ErrorCodeFixes Site | Cloudflare Pages site at errorcodefixes.com |
| SEO & Content | Content priority, SEO audit, article pipeline |
| Affiliate Monetization | Impact.com integration |
| GA4 Analytics | Traffic tracking and content performance |
| Brand & Redesign | Brand identity, redesign plan |
| Social Media | Automated posts, discovery optimization |

### 7. OpenClaw Infrastructure (PERSONAL) [ONGOING]
The AI gateway itself — maintenance, architecture upgrades, skills development. Continuous evolution.

| Project | Description |
|---------|-------------|
| Architecture Explorer | This page — deployment documentation |
| Wiki & Memory System | Obsidian vault, LanceDB, knowledge graph |
| Gateway Operations | Upgrades, restarts, MCP config, cron management |
| Skills & Tools | 49 skills from ClawHub, custom skill development |
| Claude Code Integration | Desktop app setup, CLI integration, cowork mode |
| Gauntlet / Council | Dual-LLM evaluation pipeline for quality gating |

### 8. Finexio Analysis (FINEXIO)
Data-intensive analysis projects supporting Finexio decision-making.

| Project | Status | Description |
|---------|--------|-------------|
| Finexio Financial Analysis | Active | Deep-dive revenue, volume, fee, customer analysis |
| PBIP Data Model | Active | Power BI semantic model reverse-engineering and documentation |
| Contract Inventory | Active | Finexio supplier contract terms extraction and analysis |
| Forecast Model | Ongoing | Finexio revenue forecasting model maintenance and scenario planning |
| Supplier Opportunity | Archive | Supplier-level opportunity assessment project (completed) |

### 9. Research & Writing (PERSONAL)
Independent research, analysis, and quality evaluation.

| Project | Status | Description |
|---------|--------|-------------|
| Competitor Watch | Ongoing | Automated competitive intelligence tracking (Finexio + personal) |
| Gauntlet Evaluations | Ongoing | 30+ dual-LLM evaluations across decks, plans, writing, decisions |
| Industry Research | Active | Healthcare fintech market research, trend analysis |
| SOTA Model Tracking | Ongoing | State-of-the-art model comparison and readiness tracking |

## Display Format

The projects section will render as a grid of category groups. Each group has:
- A heading with a color-coded tag (FINEXIO / PERSONAL / MIXED)
- A subtitle explaining the category
- A nested grid of project cards with name + 1-line description

Cards are click-expandable (same accordion pattern as the integration cards in v1) for more detail.

## Implementation

- 100% static HTML + inline JS data, same as the rest of the page
- DATA.projects object keyed by category
- Render function creates category sections with nested cards
- Zero new dependencies

---

**Ready for council review.**
