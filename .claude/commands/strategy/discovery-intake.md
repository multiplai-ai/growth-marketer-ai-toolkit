# Discovery & Intake

Comprehensive intake that collects all business context upfront. This is the mandatory entry point for the Cursor CMO suite — run this first, then positioning, ICP, brand strategy, and channel strategy.

**When to use:** Before running any other Cursor CMO skill. This skill produces the artifact that all downstream skills read from.

---

## Philosophy

This skill is **opinionated**. It collects everything upfront so you don't repeat yourself across skills.

**Core principle:** Strategy work requires context. The more you share now, the better the recommendations. Messy, incomplete, stream-of-consciousness answers are fine — this is intake, not a presentation.

---

## Workflow Overview

```
/discovery-intake runs:

1. BUSINESS CONTEXT   → Stage, goals, one-sentence description
2. PRODUCT & CUSTOMERS → What you offer, who buys, why they choose you
3. CURRENT STATE      → Tools, channels, past marketing efforts
4. CHALLENGES         → Pain points, budget, timeline, resources
5. ASSETS & EVIDENCE  → Proof points, content, competitive intel
6. OUTPUT             → Generate structured discovery artifact
```

---

# Phase 1: Business Context

Establish the fundamentals: who you are, where you are, and where you want to go.

### Core Business Questions

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DISCOVERY INTAKE — Business Context
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Answer in your natural voice. Bullets, fragments, incomplete thoughts — all fine.
The messier, the more useful.

1. COMPANY/PRODUCT NAME
   What are we building positioning for?

2. STAGE
   Where are you on the journey?
   - Idea stage (pre-product)
   - Building (product in development)
   - Launched (live, early users)
   - Revenue (paying customers)
   - Scaling (growth mode)

3. PRIMARY GOAL FOR THE NEXT 6 MONTHS
   What's the ONE thing that matters most right now?
   - Finding product-market fit?
   - Getting first customers?
   - Increasing revenue?
   - Raising funding?
   - Something else?

4. ONE-SENTENCE DESCRIPTION
   How would you describe your product to someone at a party?
   No jargon, no buzzwords — just plain language.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Processing Phase 1 Inputs

After user responds:
1. Capture **exact company/product name** (will use throughout all skills)
2. Note **stage** — this changes what advice is relevant
3. Identify **primary goal** — this is the filter for all recommendations
4. Save **one-sentence description** — raw material for positioning

---

# Phase 2: Product & Customers

Understand what you offer, who buys, and why they choose you.

### Product & Customer Questions

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DISCOVERY INTAKE — Product & Customers
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5. WHAT DOES YOUR PRODUCT DO?
   Describe it like you would to a friend who works in tech but doesn't know your space.
   What does someone actually DO with it?

6. WHO ARE YOUR CURRENT/TARGET CUSTOMERS?
   - Who's buying today? (titles, company types, sizes)
   - Who do you WANT to be buying?
   - Any specific verticals or industries?
   - B2B, B2C, or both?

7. WHAT WORKFLOW DOES YOUR PRODUCT SUPPORT?
   What job is someone trying to do when they use your product?
   Be specific about the task, not the business outcome.
   (e.g., "send cold emails at scale" not "grow revenue")

8. HOW DO CUSTOMERS DESCRIBE YOU?
   When happy customers explain your product to someone else, what words do they use?
   What problem do they say you solve?
   Any specific phrases that keep coming up?
   (If you don't have customers yet, how do early users/beta testers describe it?)

9. WHAT DO PEOPLE DO TODAY WITHOUT YOU?
   How are they currently solving this problem?
   - Manual processes?
   - Cobbled-together tools?
   - Agencies?
   - Direct competitor?
   - Nothing (they just live with the pain)?

10. WHY DO CUSTOMERS CHOOSE YOU?
    When someone signs up or buys, what's the #1 reason?
    What's the tipping point?
    (If pre-revenue, why do early users say they'd pay?)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Processing Phase 2 Inputs

After user responds:
1. Identify the **core workflow** they enable
2. Note **exact phrases** from customer descriptions (voice gold for brand strategy)
3. List all **alternatives mentioned** (feeds into competitive positioning)
4. Flag the **stated reason customers choose them** (validates differentiation)
5. Note **customer titles/roles** (feeds into ICP development)

---

# Phase 3: Current Marketing State

Understand what's been tried, what exists, and what tools are in play.

### Current State Questions

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DISCOVERY INTAKE — Current Marketing State
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

11. MARKETING DONE SO FAR
    What marketing have you tried? What worked, what didn't?
    - Content (blog, social, newsletter)?
    - Paid ads (Google, Meta, LinkedIn)?
    - SEO?
    - Events/conferences?
    - Partnerships?
    - Cold outreach?
    - Word of mouth?
    - Nothing yet?

12. TOOLS BEING USED
    What's in your current stack?
    - CRM: (HubSpot, Salesforce, Notion, spreadsheet, none)?
    - Email: (Mailchimp, ConvertKit, Loops, custom)?
    - Analytics: (GA4, Mixpanel, Amplitude, PostHog)?
    - Ads: (Google Ads, Meta Ads, LinkedIn Ads)?
    - Other marketing tools?

13. EXISTING BRAND ASSETS
    What do you already have?
    - Logo/visual identity?
    - Brand guidelines?
    - Messaging doc or positioning statement?
    - Website copy?
    - Pitch deck?
    - Sales materials?

14. CURRENT MARKETING CADENCE
    How often are you doing marketing?
    - Daily posting?
    - Weekly newsletter?
    - Monthly campaigns?
    - Sporadic/when we remember?
    - Nothing consistent?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Processing Phase 3 Inputs

After user responds:
1. Note **what's been tried** — avoid recommending dead ends
2. Identify **existing tools** — work within the stack, not against it
3. Catalog **existing assets** — build on what exists, don't recreate
4. Understand **current cadence** — realistic about capacity

---

# Phase 4: Challenges & Constraints

Surface the pain points, budget reality, timeline pressure, and resource limitations.

### Challenges Questions

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DISCOVERY INTAKE — Challenges & Constraints
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

15. BIGGEST MARKETING CHALLENGE
    What's the #1 thing blocking your marketing right now?
    - Don't know where to start?
    - Know what to do but no time?
    - Tried things but nothing worked?
    - Can't articulate what makes us different?
    - No budget?
    - No people?
    - Something else?

16. BUDGET REALITY
    What can you actually spend on marketing?
    - $0 (bootstrapped, sweat equity only)
    - <$1K/month (coffee money)
    - $1-5K/month (modest budget)
    - $5-20K/month (real budget)
    - $20K+/month (serious investment)

    Are you willing to spend on tools/ads, or is this purely organic/time-based?

17. TIMELINE PRESSURE
    When do you need results?
    - Yesterday (urgent, existential)
    - Next 30 days (launch coming, deadline)
    - Next quarter (building toward something)
    - No rush (building for the long term)

18. RESOURCES AVAILABLE
    Who's doing the marketing work?
    - Just me (founder doing everything)
    - Small team (1-2 people, part-time on marketing)
    - Marketing person/team (dedicated resource)
    - Agency/contractors (outsourced)
    - Mix of the above

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Processing Phase 4 Inputs

After user responds:
1. Identify **primary blocker** — strategy must address this directly
2. Note **budget constraints** — keeps recommendations realistic
3. Flag **timeline pressure** — affects tactical vs strategic mix
4. Understand **capacity** — determines execution feasibility

---

# Phase 5: Assets & Evidence

Collect proof points, performance data, existing content, and competitive intelligence.

### Assets Questions

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DISCOVERY INTAKE — Assets & Evidence
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

19. CUSTOMER EVIDENCE
    What proof do you have that customers love you?
    - Testimonials or quotes?
    - Case studies?
    - NPS scores?
    - Retention data?
    - Reviews (G2, Capterra, Product Hunt)?
    - Nothing yet?

20. PERFORMANCE DATA
    What metrics do you track? What do you know about what works?
    - Conversion rates?
    - Traffic sources?
    - Email open/click rates?
    - Trial-to-paid conversion?
    - Churn rate?
    - Not tracking anything yet?

21. EXISTING CONTENT
    What content exists that we could build on?
    - Blog posts?
    - Social content?
    - Videos?
    - Webinars?
    - Guides/ebooks?
    - Nothing substantial?

22. COMPETITIVE INTELLIGENCE
    What do you know about competitors?
    - Who are the main competitors?
    - What do they do well?
    - What do they do poorly?
    - How do customers compare you?
    - Pricing relative to competition?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Processing Phase 5 Inputs

After user responds:
1. Catalog **proof points** — essential for credibility in messaging
2. Note **performance baselines** — needed for measuring improvement
3. Inventory **content assets** — opportunities to repurpose
4. Map **competitive landscape** — feeds into positioning strategy

---

# Phase 6: Output Generation

Compile all inputs into a structured discovery artifact that downstream skills can reference.

### Generate the Discovery Artifact

```markdown
---
title: Discovery Intake — [Company/Product Name]
created: YYYY-MM-DD
status: complete
---

# Discovery Intake — [Company/Product Name]

## Executive Summary
[2-3 sentence summary: what they do, who they serve, primary goal, biggest challenge]

---

## 1. Business Context

**Company/Product:** [Name]
**Stage:** [Stage]
**Primary 6-Month Goal:** [Goal]
**One-Sentence Description:** [Description]

---

## 2. Product & Customers

**What the product does:**
[Summary of product functionality]

**Current/target customers:**
- Titles: [List]
- Company types: [List]
- Industries: [List]
- B2B/B2C: [Answer]

**Core workflow supported:**
[The job to be done]

**Customer language:**
[Exact phrases customers use — gold for messaging]

**Current alternatives:**
- [Alternative 1]
- [Alternative 2]
- [Alternative 3]

**Why customers choose them:**
[The tipping point/key reason]

---

## 3. Current Marketing State

**Marketing tried:**
- [What worked]
- [What didn't]

**Current stack:**
- CRM: [Tool]
- Email: [Tool]
- Analytics: [Tool]
- Ads: [Tool]
- Other: [Tools]

**Existing assets:**
- [Asset 1]
- [Asset 2]
- [Asset 3]

**Current cadence:** [Frequency]

---

## 4. Challenges & Constraints

**Primary challenge:** [The #1 blocker]

**Budget:** [Range and willingness to spend]

**Timeline:** [Urgency level]

**Resources:** [Who's doing the work]

---

## 5. Assets & Evidence

**Customer evidence:**
- [Proof point 1]
- [Proof point 2]

**Performance data:**
- [Metric 1]: [Value]
- [Metric 2]: [Value]

**Content inventory:**
- [Content type 1]
- [Content type 2]

**Competitive intelligence:**
- Main competitors: [List]
- Relative positioning: [Summary]

---

## Next Steps

This discovery intake connects to:
- **Positioning Strategy** (/positioning-strategy) — Build competitive positioning from JTBD mapping
- **ICP & Personas** (/icp-personas) — Deep dive into target customer definition
- **Brand Strategy** (/brand-strategy) — Voice, visual identity, messaging architecture

---

## Raw Inputs (Reference)

[Include the full Q&A transcript for context preservation]
```

### Save Location

Save to: `projects/[project-name]/discovery-intake.md`

If no project name is specified, ask for one or use: `products/cursor-cmo/marketing/outputs/discovery-intake-[company-name].md`

---

# Execution Instructions

### How to Run This Skill

1. **Present Phase 1 questions** — Wait for response
2. **Present Phase 2 questions** — Wait for response
3. **Present Phase 3 questions** — Wait for response
4. **Present Phase 4 questions** — Wait for response
5. **Present Phase 5 questions** — Wait for response
6. **Generate output artifact** — Save to specified location
7. **Recommend next skill** — Based on their primary goal

### Pacing

- Ask ONE phase at a time
- Wait for user response before proceeding
- If they want to skip a section, note it and move on
- If answers are thin, probe with follow-up questions

### Follow-Up Probes

Use these when answers are too brief:

**For vague customer descriptions:**
> "Can you give me a specific example of a customer and how they use the product?"

**For unclear differentiation:**
> "If a customer was comparing you to [alternative they mentioned], what would you say?"

**For missing proof points:**
> "Even informal feedback counts — any Slack messages, tweets, or email replies that show customers love it?"

**For unclear goals:**
> "If you had to pick ONE metric that tells you marketing is working, what would it be?"

---

# Quality Checklist

Before finalizing, verify:

- [ ] All 5 phases have responses (even if some are "don't know yet")
- [ ] Company/product name is captured exactly
- [ ] Stage is clearly identified
- [ ] Primary goal is specific and actionable
- [ ] Customer language is captured verbatim (not paraphrased)
- [ ] Alternatives/competitors are listed
- [ ] Budget and resource constraints are realistic
- [ ] Output file is saved to correct location
- [ ] Next skill recommendation is relevant to their goal

---

# Anti-Patterns (Never Do)

**DON'T:**
- Skip phases because "we can figure it out later"
- Accept "we sell to everyone" as a customer answer
- Paraphrase customer language into marketing speak
- Assume tools or assets exist without asking
- Rush through intake to get to "the fun strategy stuff"
- Combine all questions into one massive block

**DO:**
- Ask one phase at a time
- Capture customer language verbatim
- Note what's missing or unclear
- Be explicit about constraints (budget, time, people)
- Ask follow-up probes when answers are thin
- Generate a clean, structured artifact that other skills can read

---

# Quick Actions

After running `/discovery-intake`:

- "Run positioning strategy" → Proceeds to `/positioning-strategy` with this context
- "Run ICP & personas" → Proceeds to `/icp-personas` with this context
- "Run brand strategy" → Proceeds to `/brand-strategy` with this context
- "What should I run next?" → Recommends based on their primary goal
- "Export to Notion" → Formats for Notion page creation
