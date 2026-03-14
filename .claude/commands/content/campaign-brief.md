---
name: campaign-brief
description: >
  Interactive GACCS campaign brief generator. Walks you through Goals, Audience,
  Creative, Channels, and Success metrics with clarifying questions. Outputs a
  structured brief that feeds directly into creative production, media buying,
  or AI-assisted ad generation. Use when user says "campaign brief", "creative brief",
  "ad brief", "GACCS", "brief a campaign", or "plan a campaign".
---

# Campaign Brief (GACCS)

Interactive campaign brief generator based on Emily Kramer's GACCS format — Goals, Audience, Creative, Channels, Success metrics — with additions for AI-assisted production workflows.

**What this does:** Asks you questions section by section, captures your answers, and outputs a structured brief that any designer, media buyer, copywriter, or LLM can use to produce campaign assets without guessing.

**Why it matters:** Most creative production fails because the brief was bad — vague goals, undefined audience, no success criteria. This skill forces the conversation that prevents rework.

---

## Workflow Overview

```
/campaign-brief runs:

1. CONTEXT       → What are we briefing? Campaign name, product, initiative.
2. GOALS         → Business objective, campaign objective, KPIs.
3. AUDIENCE      → Who, what they care about, what stage they're at.
4. CREATIVE      → Format, key message, tone, mandatory elements.
5. CHANNELS      → Where it runs, platform constraints, budget.
6. SUCCESS       → How we measure, when we evaluate, kill/scale criteria.
7. OUTPUT        → Structured brief saved to file.
```

---

# Step 1: Context

Before diving into GACCS, establish what we're briefing.

Ask the user:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN BRIEF — Let's build this.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

First, the basics:

1. CAMPAIGN NAME
   What are we calling this? (Working title is fine.)

2. PRODUCT / SERVICE / INITIATIVE
   What are we promoting? Be specific.

3. CONTEXT
   Why now? What's the trigger — a launch, a seasonal moment,
   a competitive move, a board mandate?

4. EXISTING ASSETS
   Do you already have positioning docs, brand guidelines,
   a copy bank, or past campaigns to reference?
   (If yes, point me to them.)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Wait for the user's answers before proceeding.

If they mention existing strategy docs, positioning, or brand guidelines — read those files to inform the rest of the brief. This context makes every subsequent answer sharper.

---

# Step 2: Goals

Ask the user:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
G — GOALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. BUSINESS OBJECTIVE
   What business outcome does this campaign serve?
   (Revenue target, pipeline, market entry, retention, etc.)

2. CAMPAIGN OBJECTIVE
   What does THIS campaign specifically need to accomplish?
   Pick one:
   □ Awareness    — get in front of new people
   □ Consideration — move known prospects closer to a decision
   □ Conversion   — drive a specific action (demo, signup, purchase)
   □ Retention    — re-engage or expand existing customers

3. SPECIFIC TARGETS
   Put a number on it. Examples:
   - "50 demo requests in 30 days"
   - "2,000 landing page visits at <$5 CPC"
   - "15% open rate lift on re-engagement email"

   "Drive awareness" is not a goal. What would make you call
   this campaign a success in 30/60/90 days?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Wait for answers. If the user gives vague goals ("increase brand awareness"), push back once:

> "What would make you feel like awareness actually increased? More site traffic? More inbound? More LinkedIn DMs? Let's make it measurable so we know when it's working."

---

# Step 3: Audience

Ask the user:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A — AUDIENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. PRIMARY AUDIENCE
   Who is the ONE person this campaign is for?
   (Title, company size, industry, seniority — be specific.)

2. THEIR SITUATION
   What's happening in their world right now?
   What pain, frustration, or goal is top of mind?

3. THEIR OBJECTIONS
   What would make them scroll past this? What do they
   NOT believe, or what have they been burned by before?

4. JOURNEY STAGE
   Where are they when they see this?
   □ Unaware    — don't know they have the problem
   □ Problem-aware — know the pain, exploring solutions
   □ Solution-aware — comparing options
   □ Product-aware  — know you, need a reason to act

5. SECONDARY AUDIENCE (optional)
   Anyone else who needs to see this? (CFO who approves,
   team who influences, partner who refers.)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Wait for answers. The "objections" question is the most important one here — it determines what the creative needs to overcome.

---

# Step 4: Creative

Ask the user:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
C — CREATIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. FORMAT(S)
   What are we making? Check all that apply:
   □ Static image ads (feed, story, display)
   □ Video ads
   □ Carousel ads
   □ Landing page
   □ Email sequence
   □ Social posts (organic)
   □ Blog / article
   □ Other: ___

2. KEY MESSAGE
   If the audience remembers ONE thing, what is it?
   (One sentence. Not a tagline — the core argument.)

3. PROOF POINTS
   What evidence supports that message?
   (Stats, case studies, testimonials, credentials, awards.
   The more specific, the better the creative.)

4. TONE / ENERGY
   How should this feel? Examples:
   - Confident and direct (not aggressive)
   - Warm and educational (not salesy)
   - Urgent and specific (not hype-y)
   - Technical and precise (not cold)

5. MANDATORY ELEMENTS
   Anything that MUST appear?
   (Logo, legal disclaimer, specific CTA button text,
   brand colors, partner logos, compliance copy.)

6. CREATIVE REFERENCES (optional)
   Anything you've seen that's close to what you want?
   (Competitor ads you like, past campaigns that worked,
   visual references, tone examples.)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Wait for answers. If the user has a copy bank or brand guidelines, note which headlines/messages to prioritize.

---

# Step 5: Channels

Ask the user:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
C — CHANNELS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. PRIMARY CHANNEL(S)
   Where does this run first?
   □ LinkedIn Ads    □ Meta Ads (FB/IG)    □ Google Ads
   □ TikTok Ads      □ YouTube Ads         □ Microsoft Ads
   □ Email           □ Organic social      □ Website/landing page
   □ Other: ___

2. SECONDARY CHANNELS
   Where else does it get distributed after primary?

3. BUDGET
   What's the spend? (Total campaign budget, or monthly.)
   If unknown: what range are we working with?

4. TIMELINE
   When does this launch? When does it end?
   Any fixed dates (event, product launch, seasonal)?

5. PLATFORM CONSTRAINTS
   Anything we need to watch for?
   - Character limits (LinkedIn: 150 intro chars before fold)
   - Format specs (Meta story safe zones, Google RSA limits)
   - Audience targeting approach (ABM list, lookalike, broad)
   - Existing pixel/tracking setup status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Wait for answers.

---

# Step 6: Success Metrics

Ask the user:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S — SUCCESS METRICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. LEADING INDICATORS
   What early signals tell us this is working?
   (CTR, engagement rate, landing page conversion, email opens.)

2. LAGGING INDICATORS
   What downstream results matter?
   (Pipeline generated, revenue attributed, retention rate.)

3. REPORTING CADENCE
   How often do we check?
   □ Daily (launch week)  □ Weekly  □ Bi-weekly  □ Monthly

4. KILL CRITERIA
   What would make you turn this off?
   (e.g., "CPA above $X after 2 weeks" or
   "less than Y conversions after $Z spend")

5. SCALE CRITERIA
   What would make you increase spend?
   (e.g., "CPA below $X with volume headroom" or
   "3x ROAS sustained for 2 weeks")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Wait for answers. The kill/scale criteria are what separate a real brief from a wishlist.

---

# Step 7: Output

Compile all answers into the structured brief below. Save to the user's preferred location — suggest `briefs/brief-YYYY-MM-DD-{campaign-slug}.md` or ask where they want it.

## Brief Template

```markdown
---
campaign: "{campaign name}"
product: "{product/service}"
objective: "{awareness|consideration|conversion|retention}"
created: YYYY-MM-DD
status: brief
---

# Campaign Brief: {Campaign Name}

## Context
{Why now — trigger, background, initiative.}

## Goals

**Business objective:** {business outcome}
**Campaign objective:** {awareness/consideration/conversion/retention}
**Specific targets:**
- {measurable target 1}
- {measurable target 2}

## Audience

**Primary:** {who — title, company, industry, seniority}
**Their situation:** {what's top of mind, pain/goal}
**Their objections:** {what would make them scroll past}
**Journey stage:** {unaware / problem-aware / solution-aware / product-aware}
**Secondary:** {if applicable}

## Creative

**Formats:** {list of formats}
**Key message:** {one sentence — the core argument}
**Proof points:**
- {evidence 1}
- {evidence 2}
- {evidence 3}
**Tone:** {how it should feel}
**Mandatory elements:** {logo, disclaimers, CTA text, etc.}
**References:** {if any}

## Channels

**Primary:** {channel(s)}
**Secondary:** {channel(s)}
**Budget:** {amount and timeframe}
**Timeline:** {launch → end, key dates}
**Platform constraints:** {specs, targeting, tracking notes}

## Success Metrics

**Leading indicators:** {early signals}
**Lagging indicators:** {downstream results}
**Reporting cadence:** {frequency}
**Kill criteria:** {when to turn it off}
**Scale criteria:** {when to increase spend}

---

## Production Checklist

- [ ] Brief approved by stakeholder(s)
- [ ] Copy bank / headlines prepared
- [ ] Visual assets gathered (logos, screenshots, backgrounds)
- [ ] Landing page / destination ready
- [ ] Tracking / pixels configured
- [ ] Campaign built in platform
- [ ] QA review complete
- [ ] Launch
```

### After Output

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brief complete.

Campaign: {name}
Objective: {type}
Primary channel: {channel}
Budget: {amount}
Launch: {date}

Saved to: {file path}

Next steps:
- Review and get stakeholder approval
- Build copy bank from the key message + proof points
- Gather creative assets per the production checklist
- Set up tracking before launch

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Usage Notes

- **This is a conversation, not a form.** Ask each section, wait for answers, then move on. Don't dump all questions at once.
- **Push back on vagueness.** "Increase awareness" needs a number. "Everyone" is not an audience. The brief is only as good as the specificity of the answers.
- **If the user has existing strategy docs** (positioning, ICP profiles, brand guidelines), read them first. Pre-fill what you can and confirm with the user instead of asking from scratch.
- **The brief feeds everything downstream.** Creative production, media buying, copy generation, AI-assisted ad creation — they all read this document. Gaps here become problems later.
- **Adapt the depth to the situation.** A $500 test campaign doesn't need the same rigor as a $50K product launch. Match the brief's thoroughness to the stakes.
