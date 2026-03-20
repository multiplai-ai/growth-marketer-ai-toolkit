# The CMO Strategy Suite: How It Works

A standard operating procedure for running the strategy workflow from intake to execution.

---

## What Is the Strategy Suite?

The CMO Strategy Suite is a sequence of six skills that take a business from "we need marketing" to "here's exactly what to say, to whom, where, and what it should look like."

Each skill builds on the one before it. The output of one becomes the input for the next. No skill is optional in a full engagement, but each can be run independently if upstream context is provided manually.

---

## The Six Skills in Order

1. Discovery & Intake
2. Positioning Strategy
3. ICP & Personas
4. Brand Strategy & Key Messages
5. Content Strategy
6. Design Systems

Think of it as a funnel: broad context narrows into specific, actionable marketing assets.

---

## Skill 1: Discovery & Intake

The mandatory starting point. This is where we collect everything about the business.

What the user provides:
- Business stage and primary goal
- Product description and customer details
- Current marketing tools, assets, and cadence
- Budget, timeline, and resource constraints
- Proof points and competitive intelligence

What it produces:
- A structured Discovery Artifact (markdown file) that every downstream skill reads from

Key principle: Messy, incomplete, stream-of-consciousness answers are fine. This is intake, not a presentation.

---

## Skill 2: Positioning Strategy

Builds competitive positioning using the Fletch PMM methodology.

What the user provides:
- Confirmation of the discovery context
- Input on competitive alternatives (not just direct competitors)
- Approval of a primary competitive anchor

What it produces:
- JTBD Competitive Landscape Map (all four alternative categories)
- Primary Anchor Selection with rationale
- Differentiation Analysis against the anchor
- Positioning Narrative at three levels: one-liner, elevator pitch, and homepage-ready copy

Key principle: Choose ONE primary anchor and commit. If you try to differentiate against everything, you differentiate against nothing.

---

## Skill 3: ICP & Personas

Defines the Ideal Customer Profile and buyer personas using workflow-based segmentation.

What the user provides:
- The core workflow the product supports
- Who performs it, how often, and what triggers it
- Problems with the current alternative
- Firmographic filters and buying signals

What it produces:
- Workflow Definition with width analysis
- ICP Statement (role + company type + workflow + alternative + problem)
- Buyer Persona Cards (user, champion, decision maker)
- Customer Journey Map (unaware through decision)
- Research & Validation Framework with interview scripts

Key principle: Workflow comes first. If they don't do the workflow your product supports, they won't buy, no matter how well they match your firmographics.

---

## Skill 4: Brand Strategy & Key Messages

Translates positioning into specific messaging with teeth.

What the user provides:
- The one angle they can win on
- Two most memorable specifics that prove it
- Brand personality, tone preferences, and voice guardrails

What it produces:
- Message Hierarchy (one main message + two supporting arguments)
- Key Messages by Persona and by Journey Stage
- USP Framework with prioritization matrix
- Proof Point Inventory mapped to claims
- Brand Voice Framework (we say / we don't say)
- Pricing Position (for SaaS products)

Key principle: One main message, two supporting arguments. You get 10 seconds, not 30 minutes.

---

## Skill 5: Content Strategy

Bridges brand positioning to weekly content production using the Emily Kramer / MKT1 content system.

What the user provides:
- Perception statements (what they want the audience to believe)
- Self-assessment of content creation and distribution capabilities
- Channel inventory with audience sizes
- Capacity and cadence preferences

What it produces:
- 3-5 Perception Statements tagged to funnel stages
- Content Pillars with funnel and perception mapping
- Fuel & Engine Diagnosis (creation vs. distribution balance)
- Distribution Tiers (Tier 1: every piece, Tier 2: select, Tier 3: strategic)
- Show Definitions (recurring content programs with formats and cadences)
- Monthly Theme Framework with rotation rubric
- 6-8 Content Principles

Key principle: Start with what you want people to believe (perceptions), not what you want to publish.

---

## Skill 6: Design Systems

Translates brand voice and positioning into a complete visual design system through a staged workflow.

What the user provides:
- Reference brands and anti-references
- Approval of a mood direction
- Selection of color palette and typography pairing

What it produces:
- Stage 1: Mood Direction (visual feel and energy, no colors yet)
- Stage 2: Locked Color Palette and Typography with preview HTML
- Stage 3: Full token architecture, component specs, pattern library, CSS custom properties, and Tailwind config

Key principle: Agree on feel before colors. Lock colors before building tokens. Each checkpoint prevents wasted work.

---

## How the Skills Connect

```
Discovery Intake
      |
      v
Positioning Strategy
      |
      v
ICP & Personas
      |
      v
Brand Strategy & Key Messages
      |
      v
Content Strategy       Design Systems
      |                      |
      v                      v
Content Calendar      Landing Pages
Writing               Product UI
Campaigns             Visual Content
```

Every skill reads from the ones above it. If you skip a step, the downstream skill either blocks you or proceeds with weaker foundations.

---

## What the User Does After the Suite

The strategy suite produces the foundation. Execution skills pick up from there:

Content Calendar: Uses pillars, shows, and themes to build a monthly publishing plan.

Writing: Uses brand voice, perception statements, and pillar definitions to produce weekly content.

Content Campaigns: Uses messaging, personas, and journey stages to build multi-channel campaigns.

Ads Planning: Uses positioning, ICP, and key messages to build paid advertising strategies.

Visual Content: Uses design tokens and brand voice to create infographics, diagrams, and frameworks.

SEO: Uses positioning and content pillars to build organic search strategy.

---

## Running the Suite: Step by Step

Step 1: Run /discovery-intake. Answer the five phases of questions. Get the discovery artifact.

Step 2: Run /positioning-strategy. Confirm the competitive landscape, choose a primary anchor, approve the differentiation and narrative.

Step 3: Run /icp-personas. Define the workflow, build ICP and personas, map the customer journey.

Step 4: Run /brand-strategy. Lock the message hierarchy, build persona-specific messaging, define brand voice.

Step 5: Run /content-strategy. Set perceptions, define pillars and shows, diagnose fuel vs. engine, set distribution tiers.

Step 6: Run /design-systems. Approve mood, lock palette and typography, build the full system.

---

## Time Expectations

Each skill is a focused conversation. Most require 2-4 rounds of input and review.

The full suite can be completed in a single working day if the user comes prepared with answers, or spread across a week if discovery requires internal research.

---

## What Makes This Different

Traditional approach: Hire an agency. Wait 6-8 weeks. Receive a PDF. Hope it's actionable.

This approach: Interactive, real-time strategy sessions. Each skill produces usable artifacts immediately. Every decision is made collaboratively, not behind closed doors.

The methodology is proven: Fletch PMM for positioning and messaging. Emily Kramer / MKT1 for content systems. Adapted into a repeatable, skill-driven workflow.

---

## Key Rules for Operators

1. Never skip discovery. Every downstream skill depends on it.
2. Capture customer language verbatim. Paraphrasing into marketing speak destroys the most valuable raw material.
3. Get checkpoint approvals. The user owns the strategic bets. Positioning anchor, primary message, mood direction, these are their calls to make.
4. Follow the dependency chain. Each skill reads from the one before it. Skipping steps weakens the output.
5. Artifacts are living documents. Strategy should be refreshed quarterly, not locked in stone.
