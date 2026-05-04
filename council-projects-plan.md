# Council Evaluation: Architecture Explorer Projects Section Plan

## Evaluator: Claude Opus 4.7 (Technical)

### PHASE 1: EVIDENCE CERTIFICATE

PREMISES:
- P1: The artifact is a plan for adding a "Projects" section to a static HTML page documenting Chris Wyatt's OpenClaw deployment
- P2: Stated constraints: must match existing page style (gold-accent cards, inline data-driven rendering), support multi-tagging (FINEXIO/PERSONAL/MIXED), be 100% static HTML + inline JS
- P3: The deployment environment is Vercel from a GitHub repo; audience is Chris (operational owner)

EXECUTION TRACE:
- Happy path: Plan approved → HTML DATA.projects object written → render function creates category sections → deployed → viewed
- Primary failure mode: Category overlap/ambiguity — projects that span categories end up duplicated or arbitrarily assigned, causing confusion about where to find a given project
- Edge case: A project changes category over time (e.g., "Finexio Financial Analysis" starts as FINEXIO but becomes personal reference work when Chris leaves Finexio). The taxonomy has no "archived" or "transitioned" handling.

EVIDENCE INVENTORY:
- Correctness: The 8 categories map cleanly to what I know of Chris's work. FINEXIO (3 categories + some of MIXED), PERSONAL (4 categories + some of MIXED), MIXED (1 category). The split is about 50/50 which matches the AGENTS.md doctrine.
- Completeness: Covers 30+ named projects. Missing: the actual concrete criteria for what goes in each category — is it by funding source? by data access? by time allocation? The plan says "by purpose, not by tool" but doesn't define how to disambiguate edge cases.
- Maintainability: The category structure is clear and hierarchical. Adding a new project is obvious (pick the best-fit category). Removing Finexio projects when Chris leaves means deleting 3 categories worth of data.
- Verification: The plan mentions no mechanism to verify the project list is complete or current.

STRONGEST ASPECT: The 8-category taxonomy is well-balanced and easy to navigate. The FINEXIO/PERSONAL/MIXED tagging integrates cleanly with the existing cron tagging system.

BIGGEST RISK: Ambiguity at category boundaries. "Finexio Financial Analysis" sits under "Analysis & Research (MIXED)" but could reasonably be under "Finexio Core." The plan doesn't give clear assignment rules.

### PHASE 2: SCORING

**Correctness: 78/100**
The plan correctly identifies the major workstreams. The 3-category split (FINEXIO/PERSONAL/MIXED) matches the deployment's existing convention. Deduction: "Finexio ROI Calculator" and "Finexio Website" are listed as Finexio Core projects but are effectively web development projects. The line between "Finexio Core" and "Personal Brand & Content" could be clearer for cross-cutting work like the marketing dashboard.

**Security/failure containment: 65/100**
Not applicable in the traditional sense — this is a content plan, not code. However, the plan doesn't address what happens when the taxonomy is wrong or projects need re-categorization. The "archived" edge case is unhandled. If Chris transitions from Finexio, 3 categories of projects become irrelevant — the plan should specify whether those get hidden, removed, or tagged.

**Completeness: 72/100**
The project list is comprehensive. Missing: (1) no entry criteria for each category, (2) no "other" or "miscellaneous" bucket for projects that don't fit neatly, (3) the Analysis & Research category is a catch-all that blends Finexio-specific analysis with personal research — this should be split or given clearer internal structure.

**Maintainability: 82/100**
Strong structure. Adding a project requires editing one DATA array. Category names are concise. The MIXED tag handles cross-cutting work well. The main weakness: no guidance on how to re-categorize when project context changes (e.g., Competitor Watch goes from FINEXIO-only to personal reference post-transition).

**Verification: 55/100**
No verification criteria. The plan doesn't define "done" for the implementation. No acceptance criteria for the section. No mechanism to validate the project list against the actual git history, memory records, or file system. The council would have to manually spot-check.

### FATAL FLAWS: None found.

### Pre-mortem
If this plan ships as-is and fails, the most likely reason: category ambiguity forces project entries to be duplicated across categories or arbitrarily assigned, making the section less useful than a simple flat list.

### Overall: 72/100 — REVISE

### PHASE 3: CONSISTENCY CHECK
All scores consistent with Phase 1 traces. Correctness 78 reflects the category boundary ambiguity noted in the risk section. Maintainability 82 is the strongest score, reflecting the clear hierarchical structure.

---

## Evaluator: GPT-5.4 (Technical)

### PHASE 1: EVIDENCE CERTIFICATE

PREMISES:
- P1: A categorization plan for ~30 projects spanning 6+ months of work
- P2: Design constraints: static HTML, gold-accent style, FINEXIO/PERSONAL/MIXED tags
- P3: Must survive Chris's transition from Finexio (40-50% of integrations become inactive)

EXECUTION TRACE:
- Happy path: 8 clear categories, each with 2-6 projects, rendered as expandable cards
- Failure mode: Projects with ambiguous ownership (e.g., "Finexio Financial Analysis" — is this FINEXIO work or personal analysis?) get double-listed, and the user sees the same project in two places
- Edge case: Post-Finexio transition — the plan correctly calls out that 3 categories become irrelevant but doesn't specify the transition mechanism

EVIDENCE INVENTORY:
- Strong: Real project names, real descriptions, clear tag assignments
- Weak: No definition of what qualifies as a "project" vs. "task" vs. "workstream" — is "competitor watch" a project or an ongoing process?
- Missing: No total project count, no completion status indicators, no date ranges

### PHASE 2: SCORING

**Correctness: 75/100**
The project inventory matches what I can observe from the workspace. The taxonomy is sensible. Deduction: "Analysis & Research" is too broad — it collects gauntlet runs, contract inventory, supplier analysis, and financial modeling under one roof. These are different work types with different audiences.

**Security/failure containment: 60/100**
No rollback plan if the taxonomy proves wrong. No graceful degradation for projects that span categories. The multi-tag support is mentioned but not designed — if a project appears in two categories, which one is canonical?

**Completeness: 68/100**
Missing: (1) date ranges for projects (when was each active?), (2) status indicators (active/complete/archived), (3) a definition of "project" vs. "ongoing process" — some items like "Competitor Watch" and "BDR Executive Reports" are ongoing processes, not finite projects with a beginning and end.

**Maintainability: 80/100**
Clean structure, easy to add new projects. The MIXED tag is a good catch-all. Could benefit from a flat project name-to-category mapping rather than requiring the reader to scan all 8 categories to find a specific project.

**Verification: 50/100**
No criteria for "complete." No checklist for verifying the project list is exhaustive. No mechanism to detect stale or orphaned projects.

### FATAL FLAWS: None found.

### Pre-mortem
If this plan is implemented as-is, the most likely failure: "Analysis & Research" becomes a grab-bag of 8+ unrelated items, diluting the value of the taxonomy. Users scan the first few categories, don't find what they're looking for, and give up.

### Overall: 68/100 — REVISE

### PHASE 3: CONSISTENCY CHECK
Consistent. The scores reflect the inventory findings: the taxonomy is strong at the category level but needs refinement on edge cases and verification.

---

## CHAIRMAN SYNTHESIS

**FINAL SCORE: 70/100 — REVISE**

### Evaluator agreement
Both judges agree: the taxonomy is well- structured and the project inventory is comprehensive. Both flagged "Analysis & Research" as too broad and the lack of entry/exit criteria for categories.

### Key revisions needed (per both judges)
1. Split "Analysis & Research (MIXED)" into two: "Finexio Analysis (FINEXIO)" and "Research & Writing (PERSONAL)"
2. Rename "Finexio Core" to "Finexio Operations (FINEXIO)" for clarity
3. Add project status (active / ongoing / archived) as a subtle indicator
4. Define what qualifies as a "project" vs. an ongoing process

### Verdict: REVISE — implement the 4 changes above, then proceed to build.
