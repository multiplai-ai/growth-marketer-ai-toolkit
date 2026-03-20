# Brand Strategy & Key Messages

Build brand voice, key messages, value propositions, proof points, and USPs using the Positioning System. Produces messaging architecture that connects positioning to tactical execution.

**When to use:** After positioning strategy and ICP/personas are defined. This skill translates positioning into specific messaging that can be used across channels.

**Prerequisites:** Run `/positioning-strategy` and `/icp-personas` first, or have positioning context ready.

---

## Philosophy

This skill is **opinionated**. It produces messaging with teeth, not generic platitudes.

**Core principles:**

1. **Differentiation-first, not capability-first.** Lead with what makes you different from the anchor, not what you do. Features and capabilities come second.

2. **One main message, two supporting arguments.** You get 10 seconds, not 30 minutes. Choose ONE angle you can win on and defend it with memorable specifics.

3. **Shut up.** When asked "What is your product?", give a direct answer and stop. Don't monologue about market landscapes and technology shifts.

4. **Business outcomes are unspecific.** "Increase revenue" and "reduce costs" mean nothing — every company claims them. Say what you actually are and do.

---

## Workflow Overview

```
/brand-strategy runs:

1. FOUNDATION CHECK  → Load positioning and ICP context
2. MESSAGE HIERARCHY → Build main message + supporting arguments
3. KEY MESSAGES      → Create messaging per persona/stage
4. USP FRAMEWORK     → Define unique selling propositions
5. PROOF POINTS      → Assemble evidence for claims
6. BRAND VOICE       → Define tone, style, personality
7. PRICING POSITION  → Position pricing (if SaaS)
```

---

# Phase 1: Load Foundation Context

Before building brand strategy, load discovery, positioning, and ICP context.

### Check for Discovery Artifact

Look for: `projects/[project-name]/discovery-intake.md`

**If found:**
Extract:
- Customer language (verbatim — critical for voice)
- Customer evidence (feeds proof points)
- Competitive intel

**If not found:**
Display: "I need business context first. Please run `/discovery-intake` to collect the foundation."
Stop and wait.

### Check for Positioning Artifact

Look for: `projects/[project-name]/positioning-strategy.md`

**If found:**
Extract:
- Primary anchor
- One-sentence positioning
- Core differentiation

**If not found:**
Display: "Brand strategy requires positioning. Please run `/positioning-strategy` first."
Stop and wait.

### Check for ICP Artifact

Look for: `projects/[project-name]/icp-personas.md`

**If found:**
Extract:
- Primary persona
- Secondary personas
- Journey stages

**If not found:**
Display: "I recommend running `/icp-personas` first so messaging is persona-specific. Proceed without ICP context? [Yes/No]"

If user says yes, proceed with discovery + positioning only.

---

# Phase 2: Message Hierarchy

Build the central message architecture using the "one main message, two supporting arguments" framework.

### The Message Clarity Test

A clear message answers ONE of these questions in 5 seconds:

| Question | What It Tests |
|----------|---------------|
| "Which of my tools does this replace?" | Category clarity (using product as reference) |
| "Which tasks in my job would this help with?" | Workflow clarity (using JTBD as reference) |

If your hero message doesn't answer either question, it's not clear enough.

### Main Message Workshop

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE HIERARCHY — Building the Core
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. WHAT IS THE ONE ANGLE YOU CAN WIN ON?
   Not 10 things. ONE thing.
   This becomes your main message.

2. WHAT ARE THE TWO MOST MEMORABLE SPECIFICS?
   Not features. Specifics that prove the main message.
   These become your supporting arguments.

3. WHAT'S YOUR "TELL A FRIEND" EXPLANATION?
   If a customer explains you to a colleague, what do they say?
   No jargon. No buzzwords. Natural language.

4. WHAT'S THE PROBLEM WITH THE ALTERNATIVE?
   (From positioning anchor)
   Specific pain, not abstract complaints.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Message Hierarchy Output

```markdown
## Message Hierarchy

**Main Message:**
[The ONE angle you can win on — clear, specific, memorable]

**Supporting Argument 1:**
[Specific proof/capability that defends the main message]

**Supporting Argument 2:**
[Second specific proof/capability]

**"Tell a Friend" Explanation:**
"[Product] is [what it is] that [what it does] for [who]."

**Problem with Alternative:**
[Anchor] [creates this problem]. [Specific pain]. [Impact].

**Clarity Test:**
- Does this answer "which tool does it replace"? [Yes/No]
- Does this answer "which tasks does it help with"? [Yes/No]
```

### Example (Good vs. Bad)

```markdown
❌ BAD (outcome-focused, unspecific):
"Increase your revenue with AI-powered solutions"

❌ BAD (hedging with 10+ things):
"Sales automation, lead scoring, email tracking, pipeline management, forecasting, reporting..."

✅ GOOD (one main message, two specifics):
Main: "We help sales teams book more meetings"
Supporting 1: "AI writes personalized emails in your voice"
Supporting 2: "Auto-follows up when prospects go silent"
```

---

# Phase 3: Key Messages by Persona/Stage

Build specific messaging for different audiences and journey stages.

### Persona-Specific Messages

For each persona identified in ICP:

```markdown
## Key Messages — [Persona Name]

**What they care about:** [Their top priority / how they're measured]

**Hook:** [What gets their attention — the problem they feel]

**Value prop:** [What makes them lean in — specific to their role]

**Differentiator:** [Why you vs. the alternative — relative to anchor]

**Proof:** [What makes them believe — evidence they'd trust]

**Objection handler:** [Their biggest concern → your response]
```

### Stage-Specific Messages

For each journey stage:

| Stage | Audience Mindset | Message Focus |
|-------|------------------|---------------|
| **Unaware** | Doesn't know they have the problem | Lead with problem (not solution) |
| **Problem Aware** | Knows problem, not seeking solution | Amplify pain, introduce possibility |
| **Solution Aware** | Evaluating options | Differentiate from alternatives |
| **Product Aware** | Evaluating you specifically | Build confidence, address objections |
| **Decision** | Ready to act | Remove friction, clear next step |

```markdown
## Messages by Journey Stage

### Unaware → Problem Aware
**Message:** [Focus on the problem, not your solution]
**Example headline:** "[Problem] is costing [audience] [specific cost]"

### Problem Aware → Solution Aware
**Message:** [Introduce the category/approach]
**Example headline:** "[Audience] are switching from [old way] to [new approach]"

### Solution Aware → Product Aware
**Message:** [Differentiate from anchor]
**Example headline:** "Unlike [anchor], [Product] [key differentiator]"

### Product Aware → Decision
**Message:** [Remove objections, clear next step]
**Example headline:** "[Action] — [benefit] in [timeframe]"
```

---

# Phase 4: USP Framework

Define Unique Selling Propositions — the specific things only you can claim.

### USP vs. Value Prop vs. Feature

| Type | Definition | Example |
|------|------------|---------|
| **Feature** | What the product has/does | "AI-powered email writer" |
| **Capability** | What the feature lets users do | "Write personalized emails at scale" |
| **Benefit** | Why the capability matters | "Book more meetings with less effort" |
| **USP** | Benefit + why only you deliver it | "Book 3x more meetings — our AI trained on 10M winning emails" |

### USP Development Framework

For each potential USP:

```markdown
## USP: [Name]

**Feature:** [What is the thing?]

**Capability:** [What does it let users do?]

**Benefit:** [Why does that matter?]

**Why Only Us:** [What makes this unique to you?]

**Proof:** [Evidence that supports the claim]

**One-Liner:** [Feature] lets you [capability], so you [benefit].
```

### USP Prioritization

Rank USPs by:

| Criterion | Question |
|-----------|----------|
| **Differentiation** | Can competitors claim this? |
| **Importance** | Does the ICP care about this? |
| **Provability** | Can you back it up with evidence? |
| **Memorability** | Will they remember it? |

```markdown
## USP Priority Matrix

| USP | Differentiation | Importance | Provability | Memorability | Priority |
|-----|-----------------|------------|-------------|--------------|----------|
| [USP 1] | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] | [1-3] |
| [USP 2] | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] | [1-3] |

**Primary USP:** [The one to lead with]
**Secondary USPs:** [Supporting claims]
```

---

# Phase 5: Proof Points

Assemble evidence that supports your claims.

### Types of Proof

| Type | Strength | Best For |
|------|----------|----------|
| **Customer quotes** | High | Emotional resonance, relatability |
| **Case studies** | High | Complex value props, B2B sales |
| **Performance data** | High | Quantifiable claims |
| **Logos** | Medium | Social proof, credibility |
| **Awards/recognition** | Medium | Category validation |
| **Expert endorsements** | Medium | Technical credibility |
| **Methodology/approach** | Lower | "How we do it" differentiation |

### Proof Inventory

```markdown
## Proof Point Inventory

### Customer Quotes
- [Quote 1] — [Customer name/title, if permissioned]
- [Quote 2]

### Case Studies
- [Company]: [Before metric] → [After metric] ([% improvement])

### Performance Data
- [Metric]: [Specific number with context]

### Logos
- [Notable customers by segment]

### Other Proof
- [Awards, integrations, certifications, etc.]

### Proof Gaps
- [Claims that need evidence]
- [Research/data needed]
```

### Matching Proof to Claims

```markdown
## Proof Mapping

| Claim | Best Proof | Where to Use |
|-------|------------|--------------|
| [Main message] | [Proof type + specific] | Homepage, sales deck |
| [Supporting argument 1] | [Proof type + specific] | Feature page |
| [USP 1] | [Proof type + specific] | Case study, ads |
```

---

# Phase 6: Brand Voice

Define the tone, style, and personality of communication.

### Voice Discovery Questions

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRAND VOICE — Defining Personality
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. IF YOUR BRAND WERE A PERSON, WHO WOULD THEY BE?
   (Colleague? Expert? Friend? Guide?)

2. WHAT 3 ADJECTIVES DESCRIBE YOUR TONE?
   (Confident, not arrogant. Friendly, not casual. Etc.)

3. WHAT WOULD YOUR BRAND NEVER SAY?
   (Buzzwords? Hype? Formal language?)

4. HOW DOES YOUR AUDIENCE TALK?
   (Technical jargon? Plain English? Industry-specific?)

5. WHAT BRANDS DO YOU ADMIRE (NOT IN YOUR SPACE)?
   (Helps identify tone models)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Brand Voice Framework

```markdown
## Brand Voice

**Voice Character:**
[We are a [role] who [approach/attitude]. We speak like [reference].]

**Tone Attributes:**
| Attribute | What It Means | Example |
|-----------|---------------|---------|
| [Attribute 1] | [Definition] | [Sample phrase] |
| [Attribute 2] | [Definition] | [Sample phrase] |
| [Attribute 3] | [Definition] | [Sample phrase] |

**We Say:**
- [Preferred phrasing 1]
- [Preferred phrasing 2]

**We Don't Say:**
- [Avoided phrasing 1] → Instead: [Alternative]
- [Avoided phrasing 2] → Instead: [Alternative]

**Voice Examples:**

| Context | ❌ Not This | ✅ This |
|---------|-------------|---------|
| Homepage hero | [Bad example] | [Good example] |
| Email subject | [Bad example] | [Good example] |
| Error message | [Bad example] | [Good example] |
```

### Voice Consistency Rules

```markdown
## Voice Guardrails

**Always:**
- [Rule 1: e.g., "Use second person (you, your)"]
- [Rule 2: e.g., "Lead with the benefit, not the feature"]
- [Rule 3: e.g., "Use customer language, not marketing speak"]

**Never:**
- [Anti-rule 1: e.g., "Use 'leverage', 'synergy', 'cutting-edge'"]
- [Anti-rule 2: e.g., "Lead with business outcomes alone"]
- [Anti-rule 3: e.g., "Use superlatives without proof"]

**Escalation Words (Use Sparingly):**
- [Words to use carefully: "revolutionary", "game-changing", "best"]
```

---

# Phase 7: Pricing Position (SaaS Only)

If applicable, position pricing within the messaging strategy.

### Pricing Strategy Questions

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRICING POSITION — Strategic Framing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. WHERE DO YOU WANT TO BE POSITIONED ON PRICE?
   - Premium (higher than competitors)
   - Market rate (similar to competitors)
   - Value/Challenger (lower than competitors)

2. WHAT'S YOUR PRIMARY VALUE METRIC?
   (What do customers pay for? Users, usage, outcomes?)

3. HOW DOES PRICING SUPPORT POSITIONING?
   (Does price reinforce differentiation? Accessibility?)

4. WHAT ANCHORS SHOULD CUSTOMERS COMPARE TO?
   (Alternative costs: agencies, internal hires, other tools)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Pricing Position Output

```markdown
## Pricing Position

**Strategy:** [Premium / Market / Value]

**Rationale:** [Why this position supports the overall brand]

**Value Metric:** [What they pay for]

**Price Anchoring:**
"Compare to [anchor] at [anchor price]. [Product] delivers [benefit] for [your price]."

**Pricing Page Messages:**
- Headline: [Value-focused, not price-focused]
- Subhead: [What they get, not what they pay]
- CTA: [Action-oriented]
```

---

# Output Artifacts

### Primary Output File

Save to: `projects/[project-name]/brand-strategy.md`

If no project name: `products/cursor-cmo/marketing/outputs/brand-strategy-[company-name].md`

### Output Structure

```markdown
---
title: Brand Strategy & Key Messages — [Company/Product Name]
framework: Positioning System
created: YYYY-MM-DD
status: draft
prerequisites: positioning-strategy.md, icp-personas.md
---

# Brand Strategy & Key Messages — [Company/Product Name]

## Executive Summary
[2-3 sentences: Main message, primary USP, voice character]

---

## 1. Message Hierarchy
[From Phase 2]

## 2. Key Messages by Persona
[From Phase 3 — persona-specific messaging]

## 3. Key Messages by Stage
[From Phase 3 — journey-stage messaging]

## 4. USP Framework
[From Phase 4 — prioritized USPs with proof]

## 5. Proof Points
[From Phase 5 — inventory and mapping]

## 6. Brand Voice
[From Phase 6 — voice framework and guardrails]

## 7. Pricing Position
[From Phase 7 — if applicable]

---

## Next Steps

This brand strategy connects to:
- **Marketing Channel Strategy** — Where to deploy these messages
- **Asset Creation** — Content and campaigns using this messaging
- **Homepage/Website** — Direct application of message hierarchy

---

## Methodology Notes

Built using Positioning System:
- Message Hierarchy (One main message + supporting arguments)
- Differentiation-first messaging
- Feature → Capability → Benefit framework
- USP prioritization (Differentiation, Importance, Provability, Memorability)
- Journey-stage message adaptation
```

---

# Quality Checklist

Before finalizing, verify:

- [ ] Main message answers "what tool does this replace" OR "what tasks does this help with"
- [ ] Message hierarchy has ONE main message (not 5-10)
- [ ] Supporting arguments are specific (not generic capabilities)
- [ ] USPs are actually unique (competitors can't claim them)
- [ ] Proof points exist for major claims
- [ ] Brand voice is specific enough to guide real writing
- [ ] No buzzword bingo: "leverage," "synergy," "cutting-edge," "revolutionary"
- [ ] Messages connect back to positioning anchor and ICP

---

# Anti-Patterns (Never Do)

**DON'T:**
- Lead with business outcomes ("increase revenue")
- List 10+ features/use cases (that's hedging)
- Create voice guidelines so generic anyone could use them
- Skip proof points ("we'll add those later")
- Try to speak to everyone simultaneously
- Use jargon your customers don't use

**DO:**
- Pick ONE main message and defend it
- Make messaging specific to the positioning anchor
- Include "We say / We don't say" examples
- Map proof to claims
- Create persona-specific variations
- Use customer language, not marketing speak

---

# Quick Actions

After running `/brand-strategy`:

- "Sharpen the main message" → Rewrites for more punch
- "Add persona messaging for [role]" → Creates persona-specific variant
- "Generate proof points for [claim]" → Identifies evidence needed
- "Create voice examples for [channel]" → Applies voice to specific format
- "Develop pricing page messaging" → Pricing-specific copy framework
- "Export to Notion" → Formats for Notion page creation
