<!-- VOICE-GUARD-OFF -->
# OpenClaw Architecture Explorer, Usability & Task-Completion Audit
**URL:** https://openclaw-architecture-explorer.vercel.app/
**Auditor:** Claude Opus 4.7 (1M)
**Date:** 2026-05-11
**Method:** Playwright MCP, three mindset passes (desktop 1440x900, mobile 375x812), source inspection.

---

## Snapshot of what the page actually shows

- **Hero H1:** "Meet Booya Jones."
- **Subhead:** "Chris Wyatt's personal AI assistant, callsign Booya Jones, deployed as Wyattbot on top of OpenClaw. A single Node.js process on EC2, fanning Slack messages out across LLMs, CRMs, data warehouses, and 19 nightly crons. All live, all in conversation."
- **Pillbox stats:** HOST EC2 t3.medium / NODE v24.13.1 / BUILD v2026.4.15 / UPTIME 41d 07:00:09
- **CTAs:** "Trace a request" (anchor to #flow) plus Cmd+K palette
- **Stat row:** 49 SKILLS / 23 CRONS / 25 INTEGRATIONS / 5 PROVIDERS / 38 PROJECTS
- **Right of hero:** animated dataflow SVG (sources to Wyattbot core to targets) with a live-feed console block
- **Eight content sections:** Lifecycle / Integrations / Crons / Providers / Projects / Memory / Stack / Architecture

---

## Mindset 1: Skeptical CTO

**Held past 10 seconds?** Y. The pillbox of HOST / NODE / BUILD / UPTIME and the live-pulsing dataflow SVG read as signal, not chrome. "A single Node.js process on EC2" is the kind of constraint a CTO respects. Uptime of 41 days on a personal stack is credible without being absurd.

**First 3 questions at 30s:**
1. "What does this actually do in a business context? Is this a toy or is it replacing real work?"
2. "What are the cron uptimes hiding? 99.62 to 99.97 percent looks too clean. Where do I see failures, retries, the time someone dropped a token?"
3. "How does this scale beyond one EC2 box? What's the failure mode when t3.medium hits memory?"

**Did the tabs answer?**
- Lifecycle (good): six concrete steps with port number, library name, model name. The CTO sees "ws :18789" and "Bolt SDK in socket mode" and trusts it.
- Crons (good but suspicious): 23 jobs with 7-day uptimes and sparklines. Problem: every job is 99.6 to 99.9 percent. No red. No flapping. That reads "synthetic" to a hostile reader.
- Integrations (mostly good): 25 systems with concrete scopes ("w_member_social scope", "Service account", "OAuth + SA"). Real engineering vocabulary.
- Stack (good): "TypeBox runtime validation", "ACP sub-agent spawning", "Hybrid retrieval vector 0.7 + BM25 0.3 + FTS, Jina rerank, recencyWeight 0.15". This is the page that wins a CTO.
- Architecture (good but flat): six layers in a static block. No interactive drill-down.

**Where the CTO bounces or yawns:**
- The provider mix shows traffic percentages (DeepSeek 70 percent, Anthropic 12 percent) but no cost, no latency, no token volume. A CTO wants $/day or tokens/day to anchor scale.
- No "this replaced X hours of manual work" or "this saves $Y/month." Without an outcome, it stays an architecture diagram.
- The 5 providers section is one screen of cards with three model names each. No reason given for why a task routes to one vs another.

**What would have hooked harder:**
- One real failure story. "Memory truncation incident, May 3. Found via Layer 3 audit, fixed in bootstrapMaxChars from 25000 to 32000." That single anecdote converts a hostile CTO faster than any uptime number.
- A live "today" metric: "Tokens consumed today: 4.2M. Slack threads handled: 31. Crons fired: 18/19."
- One paragraph at the top of Architecture explaining why the gateway is one process and not microservices. Defend the choice.

**Verdict:** **Undecided, leaning win.** The technical density is real and the vocabulary is correct. The clean uptime numbers and absence of cost/outcome data are the two things that keep the skeptic from fully converting.

---

## Mindset 2: Curious AI-tinkerer peer

**Held past 10 seconds?** Y, hard. The dataflow SVG plus "OpenClaw v2026.4.15" plus an unusual stack (DeepSeek primary, Pi Agent, LanceDB hybrid retrieval) is exactly the bait this audience can't ignore.

**First 3 questions at 30s:**
1. "What is Pi Agent? @mariozechner/pi-* is this open source or proprietary?"
2. "How is the memory layer actually composed? Three tiers, can I steal that pattern?"
3. "Can I see the code? Is there a repo, a SKILL.md template, a hook recipe?"

**Did the tabs answer?**
- Memory section is the **best section on the site**. The 9-step recall pipeline (Query embedding, Vector cosine, BM25, FTS, Jina cross-encoder rerank, Recency decay, Access reinforcement, Score thresholds, Inject as context) with weights and parameters is exactly what a peer wants to copy. "+15.4% measured precision lift today" is the kind of specific number that tells me you actually run evals.
- Stack section delivers: TypeBox, ACP, pnpm workspaces, Pi Agent runtime, Bolt + grammY for multi-channel. Each is a specific, googleable choice.
- Lifecycle answers question 1 partially. "pi-agent · 49 skills" appears as step 03 but no link to docs or repo.
- The "Source on GitHub" link in the header (`github.com/booyajones/wyattbot-architecture-explorer`) is *the site repo*, not the bot repo. The peer wants the bot repo, which is private.

**Where the peer bounces or gets bored:**
- Projects section is a flat 38-card catalog grouped into 9 categories. After the first two categories the eye glazes. Cards have a sub-title (e.g., "BQ to SF to Power BI") but no link, no expandable detail. Click cursor is set to pointer but nothing happens on click. **Broken affordance.**
- Provider section is the weakest for this audience: no comparison framework, no "why I route X to Y", no routing config snippet.
- Integrations is a grid of 25 logos and one-line scopes. Could be a CSV. Add 2 or 3 with the actual prompt or MCP config visible and it transforms.

**What would have hooked harder:**
- A "skill anatomy" mini-section: pick one of the 49 skills and show its SKILL.md frontmatter plus reference structure. Peers want patterns to steal.
- Make the Memory pipeline interactive: click a step and a callout shows the actual config block from `memory-lancedb-pro`.
- One callout: "Want this stack? Here's the minimum repo to bootstrap your own." Even if it's a teaser link.

**Verdict:** **Wins.** The memory section alone justifies the URL. They'll bookmark this and screenshot the recall pipeline for their team Slack.

---

## Mindset 3: Recruiter / hiring manager

**Held past 10 seconds?** Conditional Y. A senior recruiter for an AI/exec role sees "Mission Control" and the OpenClaw build number and registers "this person builds, ships, operates." A generic recruiter sees jargon and bounces.

**First 3 questions at 30s:**
1. "Who is this person and what role do they want? Is this a portfolio or a product?"
2. "What does this person do for a living, is the day job at Finexio or is OpenClaw the day job?"
3. "Where's the resume, contact info, or 'work with me' CTA?"

**Did the tabs answer?**
- Projects section is the closest to a resume: it shows Finexio Operations (CSO work), P3 Diligence & M&A (Project Franklin / Blackstone / M3 Payments), Project Phoenix (April 2026 restructuring), Personal Brand & Content, Career Development. **The "Career Development" project literally says "Executive transition search for a C-level role at the healthcare + fintech intersection."** That's the answer to "what role" but it's buried 5 sections deep and only visible if you keep scrolling.
- No bio, no headshot, no link to chriswyatt.dev, no contact button anywhere I could find. The GitHub link goes to the site repo, not to a profile.
- No timeline ("Started OpenClaw Jan 2026", "41 days uptime since...") to ground how recent or how serious this is.

**Where the recruiter bounces:**
- Hero says "Meet Booya Jones." For a recruiter this is opaque branding. Booya Jones is the bot. The person is Chris Wyatt and that name appears only inside the subhead paragraph.
- After 30 seconds they have not seen a single human-readable outcome ("led X", "shipped Y", "saved $Z"). They've seen infrastructure.
- No clear "next step." A recruiter wants a button. There isn't one.

**What would have hooked harder:**
- A small bio strip near the hero: "Built by Chris Wyatt, CSO/CPO at Finexio. Looking for [role]. Contact / LinkedIn / chriswyatt.dev."
- One outcomes panel: "What this stack has produced in 41 days" with 3 or 4 concrete deliverables (PRDs shipped, BDR dashboards live, decks generated).
- "Talk to me" CTA in the header. Even a mailto.

**Verdict:** **Loses on a cold pass. Wins if the recruiter already knows who Chris is.** This page assumes context. A hiring manager landing here from a LinkedIn link with "look at what I built" will convert. A recruiter cold-searching will not.

---

## Mental model assessment: Booya / Wyattbot / OpenClaw, taught in 30s?

**Partial.** The page tries to teach the distinction through the H1 plus subhead:
- **Booya Jones** = the assistant identity / callsign
- **Wyattbot** = the deployed instance
- **OpenClaw** = the gateway / runtime

The subhead actually nails it in one sentence: "Chris Wyatt's personal AI assistant, callsign Booya Jones, deployed as Wyattbot on top of OpenClaw."

But this only lands if you read the subhead carefully. Visually, the H1 says "Meet Booya Jones" while the header logo says "Booya Jones / Wyattbot · OpenClaw v2026.4.15" and the eyebrow above the H1 says "MISSION CONTROL · WYATTBOT ARCHITECTURE EXPLORER · 2026." Four names, three concepts, fighting for primacy.

**Fix:** A tiny three-pill explainer right below the H1, "BOOYA JONES (persona) · WYATTBOT (deployment) · OPENCLAW (runtime)", would resolve this in under five seconds.

---

## Proof of life: do the counters connect to anything?

- **49 skills:** referenced again at L02 in Architecture ("49 Skills") and at step 03 of Lifecycle ("pi-agent · 49 skills"). Not clickable. No drill-down to the skill list.
- **23 crons:** matches the cron section count, but the hero subhead and the cmd+K palette index both say "19 nightly crons." **Three different numbers for the same thing on one page.**
- **25 integrations:** matches the integration filter "ALL25", but the section heading says "19 systems on the wire." **Two numbers in the same section.**
- **5 providers:** matches the provider section, fully consistent.
- **38 projects:** projects filter shows "ALL42" instead. **Fourth counter mismatch.**

So four of five hero counters have at least one stale-copy contradiction elsewhere on the page. None of them are clickable to filter or expand. This is the single biggest credibility leak on the site.

---

## Story arc

**Mostly flat catalog with a strong opening.**

There's a clear *opening*: hero plus dataflow plus stats row. There's no clear *middle climax* and no *closing call to action*. The eight sections read as a tab-organized inventory rather than a story.

The closest thing to an arc:
1. **Hook** (Hero), "this is what runs"
2. **The path** (Lifecycle), "this is how a request flows"
3. **The network** (Integrations), "this is who it talks to"
4. **The work** (Crons + Projects), "this is what it does"
5. **The brain** (Memory), "this is how it remembers"
6. **The bones** (Stack + Architecture), "this is what holds it up"

That ordering is actually pretty good. The site loses the arc because (a) there's no transition copy between sections to carry the reader and (b) there's no ending. The page just stops after Architecture.

**Fix:** Add a closing section. Either a "What's next on the roadmap" preview or a "Talk to me / fork the stack / read the write-up" landing strip. Right now the reader hits the bottom of Architecture and has no instruction for what to do next.

---

## Top 5 usability gaps plus fixes

### 1. Counter inconsistencies (hero vs sections vs palette vs subhead)
**Gap:** 23 vs 19 crons, 25 vs 19 integrations, 38 vs 42 projects. Subhead says "19 nightly crons." Four out of five stat counters have at least one contradiction.
**Fix:** Hoist the counts into JS constants computed from the data arrays. Bind hero stats, section headings, filter pills, and subhead text to the same source. One PR, big trust win.

### 2. Hero stats and section headings are not clickable
**Gap:** "49 SKILLS" is the most curiosity-inducing number on the page. Clicking it does nothing.
**Fix:** Make each hero stat scroll to its section and pre-apply a default filter. Bonus: clicking "23 CRONS" scrolls to crons and pulses the cron table.

### 3. Project cards have pointer cursor but no click behavior
**Gap:** 38 cards (and 9 category headers) signal interactivity that doesn't exist. Tested: cursor is "pointer", no click handler fires.
**Fix:** Either remove pointer cursor or attach a modal or expandable with one paragraph plus tech stack plus status badge per project.

### 4. No human / no contact path
**Gap:** The recruiter mindset can't find a name, role, or contact CTA on first scroll. Chris's name appears once in the subhead.
**Fix:** Tiny "Built by Chris Wyatt · CSO/CPO at Finexio · chriswyatt.dev · LinkedIn" strip in the footer or below hero. Optional "Work with me" mailto in header.

### 5. No mobile navigation
**Gap:** At 375px the section nav is `display: none` with no hamburger replacement. CmdK is the only way to jump between sections, and the cmd+K affordance is unobvious on touch.
**Fix:** Replace the hidden desktop nav with a mobile hamburger that opens a section list, or auto-show the cmd+K palette label as "Sections" on touch devices.

---

## Memorability test: what would each mindset remember in 24h?

**Skeptical CTO:** "Single Node process on EC2, 41 days uptime, hybrid retrieval with Jina rerank, DeepSeek primary at 70 percent. Pretty solid for a personal stack. Wanted to see cost numbers."

**Curious peer:** "Three-tier memory: LanceDB plus Obsidian wiki plus bootstrap context, 9-step recall pipeline with vector 0.7 BM25 0.3 plus rerank. Stealing that. Also, Pi Agent is a thing apparently."

**Recruiter:** "Some kind of personal AI bot. Don't remember the person's name. Don't remember if there was a contact button."

The peer is the only mindset that retains specific, actionable detail. The CTO retains tone, not facts. The recruiter retains nothing.

---

## Failure modes per mindset

- **CTO bounces if:** they look for cost / tokens / latency and find only uptime. Or if they click "23 CRONS" and nothing happens.
- **Peer bounces if:** they're impatient and don't scroll to Memory. The first three sections are good but not unique; the unique value is below the fold.
- **Recruiter bounces if:** they hit the hero, fail to find a name and a CTA, and back out. This happens at second 8.

---

## One-line site verdict

**Good, with three fix-this-firsts that move it to top-notch:** sync the counters, give the stats and cards actual click behavior, and add a one-line "who built this and how to reach them" strip near the hero.

---

## Appendix: artifacts captured

- `openclaw-hero-desktop.png`, 1440x900 hero
- `openclaw-cmdk-open.png`, command palette open state
- `openclaw-mobile-hero.png`, 375x812 mobile hero
- Pre-existing: `openclaw-desktop-viewport.png`, `openclaw-mobile-viewport.jpeg`, `openclaw-tablet-viewport.jpeg`, `openclaw-desktop-fullpage.jpeg`

## Appendix: console health

1 console error on initial load (not surfaced to user). Worth diagnosing but not blocking. No horizontal overflow at 375px. CmdK opens cleanly on both desktop and mobile.
