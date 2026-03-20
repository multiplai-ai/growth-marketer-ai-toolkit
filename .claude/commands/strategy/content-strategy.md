# Content Strategy

Build a comprehensive content strategy connecting positioning, brand-strategy, and ICP upstream to content production downstream. Uses the Content System.

**When to use:** When building a content strategy that bridges brand positioning to weekly content production. Quarterly refresh cadence.

**Prerequisites:** Run `/positioning-strategy`, `/brand-strategy`, and `/icp-personas` first for best results. Can proceed without them.

---

## Philosophy

This skill is **opinionated**. It follows the Content System — battle-tested across 130+ articles and frameworks. The goal is a content strategy that connects what you believe (positioning) to what you publish (weekly content).

**Core principles:**
1. **Perceptions before content.** What do you want people to believe about you? Content serves perception shifts, not just topics.
2. **Shows, not feeds.** Recurring content programs with clear cadences beat ad-hoc posting.
3. **Fuel and engine must balance.** Creating content without distribution is a tree falling in an empty forest.
4. **Default to less.** Better to publish 3 excellent pieces than 7 mediocre ones. Quality compounds.

---

## Workflow Overview

```
/content-strategy runs:

1. LOAD FOUNDATION    → Read positioning, brand-strategy, ICP, voice-synthesis
2. PERCEPTIONS        → Create 3-5 narrative statements from customer POV
3. CONTENT PILLARS    → Define 3-5 pillars with funnel + perception mapping
4. FUEL & ENGINE      → Diagnose creation vs. distribution balance
5. DISTRIBUTION TIERS → Define Tier 1/2/3 with actual channels
6. SHOW DEFINITIONS   → Define recurring content programs with cadences
7. MONTHLY THEMES     → Build theme selection rubric
8. CONTENT PRINCIPLES → Synthesize 6-8 guiding principles
```

---

# Phase 1: Load Foundation

Before building content strategy, load all upstream strategy artifacts.

### Check for Strategy Artifacts

Look for these files in order:

1. **Positioning:** `strategy/positioning-strategy.md`
2. **Brand Strategy:** `strategy/brand-strategy.md`
3. **ICP/Personas:** `strategy/icp-personas.md`

**If all found:**
Extract and display summary:
- One-sentence positioning
- Primary anchor and differentiation
- Message hierarchy (main message + supporting arguments)
- Primary persona
- Voice character

Confirm: "I've loaded your strategy foundation. Ready to build content strategy?"

**If some missing:**
Display which artifacts exist and which are missing. For each missing:
- Positioning: "No positioning found. I'll work from your inputs, but recommend running `/positioning-strategy` for stronger foundations."
- Brand Strategy: "No brand strategy found. Message hierarchy will be built from scratch."
- ICP: "No ICP found. Content will be less persona-targeted."
- Voice: "No voice profile found. Voice consistency won't be enforced."

Proceed with what's available — warn but don't block.

---

# Phase 2: Perceptions Workshop

**This is the critical insight most content strategists miss.**

Perceptions are NOT positioning statements. Positioning is how you frame yourself. Perceptions are what you want to live in your audience's mind — stated from THEIR point of view.

### The Distinction

| Type | Perspective | Example |
|------|------------|---------|
| **Positioning** | Your voice | "We help growth teams automate engagement" |
| **Perception** | Customer's mind | "They understand the real bottleneck in scaling growth — it's not more tactics, it's better systems" |

### Perceptions Workshop

Present this to the user:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERCEPTIONS WORKSHOP — What Should Live in Their Mind?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Imagine your ideal reader after 6 months of consuming your content.
What do they BELIEVE about you? Complete these sentences:

1. "[Your name] is the person who ___"
2. "When I think about [your topic], I think of [your name] because ___"
3. "I follow [your name] because they ___"
4. "Unlike other [category] voices, [your name] ___"
5. "The thing I always tell people about [your name] is ___"

Don't overthink it. Write what you WANT them to say.
If you have positioning artifacts, I'll pre-fill suggestions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Pre-Fill Logic

If positioning and brand-strategy artifacts exist:
- Generate 3-5 suggested perception statements from the positioning, message hierarchy, and differentiation
- Present them as starting points: "Based on your positioning, here are suggested perceptions. Edit, add, or replace:"

### Processing Perceptions

After user responds:
1. Refine into 3-5 clean perception statements
2. Tag each with the funnel stage it primarily serves (Awareness, Consideration, Decision)
3. Identify which perceptions are strongest (most specific, most differentiated)

### Display Format

```markdown
## Perception Statements

| # | Perception | Funnel Stage | Strength |
|---|-----------|-------------|----------|
| 1 | "[Perception statement]" | Awareness | Strong / Needs work |
| 2 | "[Perception statement]" | Consideration | Strong / Needs work |
| 3 | "[Perception statement]" | Decision | Strong / Needs work |

**Primary perception to reinforce:** [The #1 thing you want people to believe]

Confirm or adjust?
```

---

# Phase 3: Content Pillars

Define the 3-5 content pillars that organize all content production.

### Seeding from Existing

If writing.md pillars exist (check lines 129-137 of the writing skill), seed from them:
- AI-Native Growth Systems
- Healthcare Growth Playbooks
- Scaling-Stage Lessons
- Industry POV / Contrarian Takes
- Builder Stories / Behind the Scenes

These are starting points. This phase enriches them with funnel stage mapping and perception mapping.

### Pillar Enrichment Framework

For each pillar:

```markdown
## Pillar: [Name]

**Description:** [1-2 sentences — what topics fall here]

**Funnel Focus:** [Primary funnel stage this pillar serves]
- Awareness: Attracts new audience, builds recognition
- Consideration: Establishes expertise, builds trust
- Decision: Drives conversion, removes objections

**Perception Served:** [Which perception statement(s) this pillar reinforces]

**Content Types:** [What formats work best for this pillar]
- Long-form articles
- Quick takes / hot takes
- Frameworks / visuals
- Case studies
- Tutorials / how-tos

**Frequency Target:** [How often to publish in this pillar — e.g., 1-2x/month]

**Example Topics:**
- [Topic 1]
- [Topic 2]
- [Topic 3]
```

### Pillar Balance Check

After defining all pillars, verify:
- At least 1 pillar serves each funnel stage
- No more than 30% of pillars are product/decision-focused (the "30% juice rule")
- Each perception statement is served by at least 1 pillar
- Total frequency across all pillars matches realistic production capacity

### Display Format

```markdown
## Content Pillars

| Pillar | Funnel Stage | Perception | Frequency | Balance |
|--------|-------------|-----------|-----------|---------|
| [Name] | Awareness | P1, P3 | 2x/month | ✓ |
| [Name] | Consideration | P2 | 1-2x/month | ✓ |
| [Name] | Decision | P4 | 1x/month | ✓ (under 30%) |

**Balance Assessment:** [OK / Warning — with explanation if warning]

Confirm pillars or adjust?
```

---

# Phase 4: Fuel & Engine Assessment

Diagnose the balance between content creation (fuel) and distribution (engine).

### The Diagnostic

Most creators have one of these problems:
- **All fuel, no engine:** Great content nobody sees
- **All engine, no fuel:** Great distribution with nothing worth distributing
- **Mismatched octane:** Content quality doesn't match channel expectations

### Assessment Workshop

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FUEL & ENGINE — Honest Diagnostic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rate each honestly (1-5, where 5 = excellent):

FUEL (Content Creation):
1. How consistent is your publishing cadence? ___
2. How differentiated is your content from others in your space? ___
3. How much of your content comes from real experience vs. research? ___
4. How well does your content connect to business goals? ___

ENGINE (Distribution):
5. How strong is your organic reach (followers, subscribers)? ___
6. How active are you in distributing content after publishing? ___
7. How much content do you repurpose/redistribute vs. create new? ___
8. Do you have any paid amplification? ___

ALIGNMENT:
9. Does your best content reach your target audience? ___
10. Can you trace content to business outcomes (leads, conversations)? ___

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Diagnosis Logic

After user responds:
- Fuel score: Average of Q1-4
- Engine score: Average of Q5-8
- Alignment score: Average of Q9-10

Present diagnosis:

```markdown
## Fuel & Engine Diagnosis

**Fuel Score:** [X/5] — [Strong / Adequate / Weak]
**Engine Score:** [X/5] — [Strong / Adequate / Weak]
**Alignment Score:** [X/5] — [Strong / Adequate / Weak]

**Diagnosis:** [One of:]
- "All fuel, no engine" — You're creating good content but nobody sees it. Priority: distribution.
- "All engine, no fuel" — You have reach but content isn't strong enough. Priority: content quality.
- "Mismatched" — Content and distribution aren't aligned. Priority: channel-content fit.
- "Balanced" — Good foundation. Priority: optimization and scaling.
- "Starting from scratch" — Low on both. Priority: establish one show, one channel, be consistent.

**Top 3 Recommendations:**
1. [Specific action based on diagnosis]
2. [Specific action based on diagnosis]
3. [Specific action based on diagnosis]
```

---

# Phase 5: Distribution Tier Defaults

Define how content gets distributed using a tiered approach.

### Distribution Tier Framework

```markdown
## Distribution Tiers

### Tier 1 — Owned Channels (Every Piece)
These are the channels where every piece of content gets published or promoted:
- [Channel 1 — e.g., Substack newsletter]
- [Channel 2 — e.g., LinkedIn personal profile]
- [Channel 3 — e.g., Twitter/X]

### Tier 2 — Extended Distribution (Select Pieces)
Channels where strong pieces get additional distribution:
- [Channel — e.g., LinkedIn newsletter]
- [Channel — e.g., Cross-post to Medium/other platforms]
- [Channel — e.g., Community shares (specific communities)]

### Tier 3 — Amplification (Strategic Pieces Only)
Reserved for highest-impact content:
- [Channel — e.g., LinkedIn Thought Leader Ads]
- [Channel — e.g., Paid newsletter sponsorships]
- [Channel — e.g., Podcast guest pitches referencing content]
- [Channel — e.g., Email outreach to specific people]
```

### Channel Inventory Workshop

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHANNEL INVENTORY — Where Do You Publish?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

List all channels you currently use or plan to use:

OWNED (you control these):
- [List channels: newsletter, blog, social profiles, podcast, etc.]

EARNED (you contribute to these):
- [Communities, guest posts, podcast appearances, etc.]

PAID (you pay for reach):
- [Ads, sponsorships, boosted posts, etc.]

For each, note:
- Current audience size (approximate)
- Posting frequency
- Engagement quality (comments, replies, shares)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

After user responds, organize into tiers. Recommend defaults based on the Fuel & Engine diagnosis.

---

# Phase 6: Show Definitions

Define recurring content programs ("shows") with clear formats and cadences.

### Shows vs. Feeds

| Type | Description | Example |
|------|-------------|---------|
| **Show** | Recurring, expected, branded format | "Saturday essay on Substack" |
| **Feed** | Ad-hoc, reactive, no set schedule | Random LinkedIn posts |

Shows build audience expectations and compound. Feeds don't.

### Seed from Writing Schedule

If the writing skill schedule exists, seed from the existing Sat/Mon/Wed/Thu cadence:

| Day | Show | Format | Platform |
|-----|------|--------|----------|
| Saturday | Flagship Essay | Long-form article (1,800-2,100 words) | Substack + Twitter |
| Monday | Engagement Post | Poll / hot take / challenge | LinkedIn + Twitter |
| Wednesday | Visual Framework | Infographic / diagram | LinkedIn + Twitter |
| Thursday | Lead Magnet / Promo | Tutorial / app promo | LinkedIn + Twitter |

### Show Definition Template

For each show:

```markdown
## Show: [Name]

**Format:** [What type of content]
**Platform(s):** [Where it publishes]
**Cadence:** [How often — weekly, biweekly, monthly]
**Day/Time:** [When it publishes]
**Length:** [Word count or duration]
**Pillar Rotation:** [Which pillars this show draws from]

**What Makes It a Show:**
- [Consistent format]
- [Audience expects it]
- [Has a clear purpose in the strategy]

**Success Metrics:**
- [What good looks like for this show]
```

### Show Portfolio Assessment

After defining shows:
- Total weekly production load: [X pieces]
- Pillar coverage: Does every pillar have at least 1 show?
- Capacity check: Is this sustainable? (Max recommended: 5 pieces/week)

---

# Phase 7: Monthly Theme Framework

Build a system for selecting monthly themes that keep content cohesive without being repetitive.

### Theme Selection Rubric

Each month, select a theme based on three factors:

| Factor | Weight | Question |
|--------|--------|----------|
| **Pillar Rotation** | 40% | Which pillar hasn't been featured recently? |
| **Perception Reinforcement** | 35% | Which perception needs the most reinforcement right now? |
| **Timeliness** | 25% | Is there something happening in the market/industry that creates urgency? |

### Theme Definition Template

```markdown
## Monthly Theme Template

**Month:** [Month Year]
**Theme:** [Theme name — specific enough to guide, broad enough for 4 weeks]
**Pillar:** [Primary pillar this theme falls under]
**Perception Served:** [Which perception statement this reinforces]
**Timeliness Hook:** [Why now? What makes this timely?]

**Anchor Piece:** [The flagship content piece for the month]
**Supporting Angles:**
- Week 1: [Angle]
- Week 2: [Angle]
- Week 3: [Angle]
- Week 4: [Angle]
```

### Rotation Tracking

```markdown
## Pillar Rotation Tracker

| Pillar | Last Featured | Months Since | Priority |
|--------|--------------|-------------|----------|
| [Pillar 1] | [Month] | [N] | [High/Med/Low] |
| [Pillar 2] | [Month] | [N] | [High/Med/Low] |
```

---

# Phase 8: Content Principles

Synthesize 6-8 guiding principles from content frameworks + voice profile.

### Auto-Synthesize Principles

Draw from:
1. Content frameworks (default to less, no dead ends, 30% juice rule)
2. Voice profile (if loaded)
3. Fuel & Engine diagnosis
4. Perception priorities

### Principle Format

```markdown
## Content Principles

These principles guide all content decisions. When in doubt, refer here.

### 1. [Principle Name]
**What it means:** [1-2 sentences]
**In practice:** [Specific example of applying this principle]
**Violation looks like:** [What breaking this principle looks like]

### 2. Default to Less
**What it means:** Publish fewer, better pieces. Quality compounds; quantity dilutes.
**In practice:** Max 5 new pieces per week. If you can't make it excellent, don't publish it.
**Violation looks like:** Publishing 7 mediocre posts because "consistency."

### 3. No Dead Ends
**What it means:** Every piece of content should lead somewhere — another piece, a resource, a conversation, a next step.
**In practice:** Every article ends with "What to do?" section. Every social post has a clear next action.
**Violation looks like:** A LinkedIn post that makes a point but gives the reader nowhere to go.

### 4. The 30% Juice Rule
**What it means:** At most 30% of content should be product-focused or conversion-oriented. The rest builds trust and audience.
**In practice:** In a 4-week month with 16 posts, max 5 should mention your product/service directly.
**Violation looks like:** Every post being a thinly veiled pitch.

[Continue for 6-8 total principles]
```

---

# Output Artifacts

### Primary Output File

Save to: `strategy/content-strategy.md`

### Output Structure

```markdown
---
title: Content Strategy — [Name / Brand]
framework: Content System
created: YYYY-MM-DD
status: draft
cadence: quarterly-refresh
upstream: positioning-strategy, brand-strategy, icp-personas
downstream: content-calendar, writing
---

# Content Strategy — [Name / Brand]

## Executive Summary
[3-5 sentences: What this strategy does, key perceptions, pillar count, show cadence, primary diagnosis]

---

## 1. Perception Statements
[From Phase 2]

## 2. Content Pillars
[From Phase 3 — with funnel + perception mapping]

## 3. Fuel & Engine Diagnosis
[From Phase 4]

## 4. Distribution Tiers
[From Phase 5]

## 5. Show Definitions
[From Phase 6 — with cadences and platforms]

## 6. Monthly Theme Framework
[From Phase 7 — rubric + rotation tracker]

## 7. Content Principles
[From Phase 8]

---

## Next Steps

This content strategy connects to:
- **Content Calendar** (`/content-calendar`) — Monthly calendar built from this strategy
- **Content Campaign** (`/content-campaign`) — Campaign briefs for launches and series
- **Writing** (`/writing`) — Weekly content production using these pillars and themes

---

## Methodology Notes

Built using Content System:
- Perceptions framework
- Content Pillars with funnel mapping
- Fuel & Engine diagnostic
- Distribution Tiers (1/2/3)
- Shows vs. Feeds
- Monthly Themes with rotation rubric
- Content Principles (default to less, no dead ends, 30% juice rule)
```

---

# Quality Checklist

Before finalizing, verify:

- [ ] Perceptions are stated from the customer's POV (not your positioning language)
- [ ] Each pillar maps to a funnel stage AND at least one perception
- [ ] No more than 30% of pillars are product/decision-focused
- [ ] Fuel & Engine diagnosis is honest (not aspirational)
- [ ] Distribution tiers use real channels with real audience sizes
- [ ] Shows have clear cadences and formats (not vague "post regularly")
- [ ] Monthly theme rubric balances rotation, perception reinforcement, and timeliness
- [ ] Principles are specific enough to guide real decisions (not platitudes)
- [ ] Total weekly production load is realistic (max 5 new pieces)
- [ ] Strategy connects upstream (positioning) to downstream (calendar, writing)

---

# Anti-Patterns (Never Do)

**DON'T:**
- Skip perceptions and jump straight to "what topics should we write about"
- Build pillars that are just topic categories with no strategic intent
- Rate yourself 5/5 on Fuel & Engine (nobody is — be honest)
- Define distribution tiers without knowing actual audience sizes
- Create 7+ shows when you can barely sustain 3
- Treat monthly themes as rigid constraints vs. focusing lenses
- Write principles that any brand could claim ("be authentic")

**DO:**
- Start with what you want people to believe (perceptions), not what you want to publish
- Map every pillar to both a funnel stage and a perception
- Be brutally honest about creation capacity vs. distribution reach
- Seed from existing writing schedule and pillars (don't reinvent)
- Make principles specific enough that violating them is obvious
- Build for quarterly refresh — this is a living document

---

# Quick Actions

After running `/content-strategy`:

- "Refresh perceptions" → Re-runs Phase 2 with new inputs
- "Add a new pillar" → Walks through pillar enrichment for a new topic area
- "Re-diagnose fuel & engine" → Re-runs Phase 4 assessment
- "Update distribution tiers" → Re-runs Phase 5 with new channels
- "Add a new show" → Defines a new recurring content program
- "Generate themes for next quarter" → Uses rubric to suggest 3 monthly themes
- "Export to Notion" → Formats for Notion page creation
