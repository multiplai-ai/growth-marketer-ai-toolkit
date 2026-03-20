# Content Brief

Generate SEO/AEO-optimized content briefs from a target keyword + topic. Runs SERP analysis, identifies content patterns, pulls brand context, and outputs a structured brief ready for `/writing` or SEO+AEO drafting.

**When to use:** Before writing any SEO/AEO-targeted article. The brief replaces guessing with data — what ranks, what's missing, and what angle makes our take worth reading.

**Input:** Target keyword + topic via `$ARGUMENTS` or conversation. Example: `/content-brief "virtual marketing team" for founders who can't afford a CMO`

**Output:** Structured brief saved to `content/briefs/brief-YYYY-MM-DD-{slug}.md`

---

## Workflow Overview

```
/content-brief runs:

1. PARSE INPUT        → Extract keyword, topic, intent from args
2. SERP ANALYSIS      → WebSearch top results, analyze patterns
3. CONTENT PATTERNS   → Formats, headings, word counts, gaps
4. BRAND CONTEXT      → Pull AirOps Brand Kit (optional) + local strategy
5. AEO TARGETS        → Questions AI engines surface for this topic
6. BRIEF OUTPUT       → Save structured brief to content/briefs/
```

---

# Step 1: Parse Input

Extract from `$ARGUMENTS` or ask the user:

- **Primary keyword** — the exact phrase to target (e.g., "virtual marketing team")
- **Topic context** — what angle or audience (e.g., "for B2B founders replacing agency spend")
- **Content type hint** — if the user specifies (Build Log, Tool Bench, standalone article). Default: standalone article.

If args are ambiguous, ask 1-2 clarifying questions:
- "What's the primary keyword you want to rank for?"
- "Who's the target reader — founders, CMOs, or marketers?"

Proceed with explicit assumptions if the user says "just go."

---

# Step 2: SERP Analysis

Run WebSearch for the primary keyword. Analyze the top 5-10 organic results.

### What to Capture

For each result in the top 10:

| Field | What to Note |
|-------|-------------|
| **Title** | Exact title tag |
| **URL / Domain** | Who ranks (brand authority signal) |
| **Format** | Listicle, how-to guide, comparison, definition, tool roundup, etc. |
| **Apparent word count** | Short (<1K), medium (1-2K), long (2K+) |
| **Key angle** | What's their hook or differentiator |

### Also Search For

Run 2-3 additional searches to fill gaps:

- `"{keyword}" + "how to"` — informational intent variants
- `"{keyword}" + "vs"` or `"{keyword}" + "alternatives"` — commercial intent variants
- `"{keyword}" + site:reddit.com` OR `"{keyword}" + site:linkedin.com` — community discussion signals

### Summarize

```markdown
## SERP Snapshot

**Dominant format:** [e.g., "Long-form how-to guides, 2,000+ words"]
**Who ranks:** [e.g., "HubSpot, Shopify, 2 niche blogs"]
**Content quality:** [e.g., "Generic — mostly SEO-optimized listicles, no real practitioner depth"]
**Gap identified:** [e.g., "Nobody covers this from a founder's POV with real cost data"]
```

---

# Step 3: Content Patterns

From the SERP analysis, extract patterns that inform the brief.

### Heading Analysis

List the most common H2/H3 headings across top results. Identify:
- **Table stakes headings** — what every competitor covers (must include or consciously skip)
- **Missing headings** — topics nobody covers well (opportunity)
- **Overused headings** — generic sections we can skip or reframe

### Format Decision

Based on SERP patterns, recommend a format:

| SERP Signal | Recommended Format |
|------------|-------------------|
| All listicles rank | Listicle (play the game) OR contrarian long-form (differentiate) |
| How-to guides dominate | Step-by-step guide with real examples |
| Comparison pages rank | Comparison with clear verdict |
| Thin content ranks | Long-form depth play — easy to outperform |
| Mixed formats | Match the top performer's format but add depth |

### Word Count Target

- If competitors are 800-1,200 words → target 1,800-2,200 (depth advantage)
- If competitors are 2,000+ words → match or exceed, but win on quality not length
- Never go below 1,500 for SEO/AEO-targeted pieces

---

# Step 4: Brand Context

Pull brand voice and strategic context to ensure the brief produces on-brand content.

### Local Strategy (Always Load)

Read these files (skip gracefully if not found):

1. `strategy/content-strategy.md` → pillars, perceptions, buyer segments
2. `strategy/brand-strategy.md` → message hierarchy, USPs
3. `voice-synthesis.md` → voice profile for tone guidance

Extract:
- Which **content pillar** this keyword maps to
- Which **perception statement** the article should reinforce
- Which **buyer segment** this targets
- **Voice blend** appropriate for the format

### AirOps Brand Kit (Optional — Not Blocking)

Try to pull Brand Kit context from AirOps MCP:

```
mcp__airops__get_brand_kit (ID: <your-brand-kit-id>)
```

If available, extract:
- Audiences and their priorities
- Content types and guidelines
- Writing rules
- Product lines and positioning

If AirOps MCP is not connected or the call fails: **skip and proceed.** Local strategy files are sufficient. Log: "AirOps Brand Kit: not available — using local strategy context."

---

# Step 5: AEO Question Targets

Identify 5-10 questions that AI engines (ChatGPT, Perplexity, Claude, Gemini) are likely to surface answers for on this topic.

### How to Find AEO Targets

1. **WebSearch:** `"{keyword}" questions` and `"people also ask" "{keyword}"`
2. **Infer from SERP:** What questions do the top-ranking articles answer in their content?
3. **Think like an AI user:** What would someone ask an AI assistant about this topic? These tend to be:
   - Definition questions ("What is X?")
   - Comparison questions ("X vs Y — which is better for Z?")
   - How-to questions ("How do I set up X?")
   - Evaluation questions ("Is X worth it for [audience]?")
   - Cost/ROI questions ("How much does X cost?")

### AEO Optimization Notes

For each question target, note:
- **Recommended answer format** — direct answer paragraph (2-3 sentences) that AI can extract cleanly
- **Where in the article** — which section should contain this answer
- **Structured data opportunity** — FAQ schema, HowTo schema, or none

### AirOps AEO Data (Optional)

If AirOps MCP is connected, check for existing AEO data:

```
mcp__airops__list_aeo_prompts — check if prompts exist for this keyword
mcp__airops__get_prompt_answers — pull existing AI citation data
```

If available, incorporate citation gaps and competitor mentions. If not available, skip.

---

# Step 6: Brief Output

Save the structured brief to `content/briefs/brief-YYYY-MM-DD-{slug}.md`.

Create the `content/briefs/` directory if it doesn't exist.

### Brief Template

```markdown
---
keyword: "{primary keyword}"
topic: "{topic description}"
created: YYYY-MM-DD
status: brief
pillar: "{content pillar}"
segment: "{target buyer segment}"
intent: "{search intent}"
---

# Content Brief: {Article Working Title}

## Target Keywords

**Primary:** {keyword} (estimated intent: {informational/commercial/navigational/transactional})
**Secondary:** {3-5 related keywords from SERP analysis}
**Long-tail:** {2-3 specific long-tail variants}

## Search Intent

**Classification:** {Informational / Commercial / Navigational / Transactional}
**User goal:** {What the searcher actually wants to accomplish}
**Funnel stage:** {Awareness / Consideration / Decision}

## Competitive Landscape

| Rank | Title | Domain | Format | Gap/Opportunity |
|------|-------|--------|--------|----------------|
| 1 | {title} | {domain} | {format} | {what they miss} |
| 2 | {title} | {domain} | {format} | {what they miss} |
| ... | ... | ... | ... | ... |

**Overall assessment:** {1-2 sentences on competitive quality and our opportunity}

## Recommended Content Structure

**Format:** {listicle / how-to guide / comparison / deep-dive essay}
**Target word count:** {range}

### Heading Outline

1. {H2: Opening section}
   - {Key points to cover}
2. {H2: Section 2}
   - {Key points to cover}
3. {H2: Section 3}
   - {Key points to cover}
...
N. {H2: What to do? — always last substantive section}

## AEO Question Targets

Answer these questions explicitly in the article (direct, extractable answers):

| # | Question | Answer Format | Section |
|---|----------|--------------|---------|
| 1 | {question} | {paragraph / list / table} | {which H2} |
| 2 | {question} | {paragraph / list / table} | {which H2} |
| ... | ... | ... | ... |

**Schema opportunity:** {FAQ / HowTo / None} — {note on implementation}

## Content Requirements

- **Word count:** {target range}
- **Internal links:** {specific articles/pages to link to, if known}
- **External links:** {types of sources to cite — research, tools, industry reports}
- **Images/visuals:** {what visuals would strengthen this piece — framework diagrams, screenshots, data viz}
- **CTA:** {recommended CTA based on pillar and funnel stage}

## Brand Voice Notes

- **Pillar:** {which content pillar this maps to}
- **Perception to reinforce:** {which perception statement}
- **Buyer segment:** {primary target}
- **Voice blend:** {ratio — e.g., 50% exploratory, 35% mechanism-focused, 15% wit}
- **Tone guidance:** {specific notes for this topic — e.g., "more mechanism-heavy, less personal story"}

## Differentiation Angle

**What makes our take unique:**
{2-3 bullets on how this piece differs from what already ranks. What do we know from real experience that competitors don't cover? What's the contrarian or practitioner angle?}

**Real experience to draw from:**
{Specific credentials, client work, or builds that give this piece authority}

---

## Next Steps

- [ ] Run `/writing` with this brief as input
- [ ] Or: Use SEO+AEO drafting workflow when available
- [ ] Review and adjust heading outline before drafting
```

### After Output

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brief generated.

- Keyword: {primary keyword}
- Intent: {search intent}
- Format: {recommended format}
- Word count: {target}
- AEO targets: {count} questions
- File: content/briefs/brief-YYYY-MM-DD-{slug}.md

Next: Run /writing with this brief, or review the heading outline first.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
