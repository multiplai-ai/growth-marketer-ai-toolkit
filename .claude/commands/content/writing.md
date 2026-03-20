# Writing

Flagship content creation skill for authentic, voice-driven content across Substack, LinkedIn, and Twitter. Run Saturday mornings (content spans Sat-Fri weekly cycle).

**Core principle:** Your authentic voice comes from YOUR inputs first. AI expands and shapes, never invents.

---

## Workflow Overview

```
/writing runs:

0. STRATEGY LOAD      → Pull content-strategy, calendar, brand-strategy context (if available)
1. VOICE CAPTURE      → Journal prompts OR pre-recorded transcript
2. READING SCAN       → Check Reading/Inbox for content ideas + research
3. PILLAR INFERENCE   → Derive best content pillar from inputs (pre-set if calendar loaded)
3.5 LEAD MAGNET       → Ideate promo asset (Loom, app, or downloadable)
4. CONTENT CREATION   → Editorial long-form + derivative posts (LinkedIn + Twitter)
5. OUTPUT             → Single markdown file ready for scheduling
6. PRODUCTION LOG     → Append entry to production log

Produces 5 pieces: 1 flagship article (Substack + Twitter) + 4 social posts (LinkedIn + Twitter)
Saturday + Monday posts ready before Saturday publish; Wednesday + Thursday finalized during the week
```

---

# Step 0: Strategy Load (Context Pull)

Pull upstream strategy context to inform content creation. **This step is automatic and silent** — if artifacts exist, load them. If not, skip gracefully and proceed as before.

### Check for Artifacts

Look for these files (all optional — none block the workflow):

1. **Content Strategy:** `{entity-dir}/strategy/content-strategy.md` (e.g., `strategy/content-strategy.md`)
   - Extract: content pillars (with funnel + perception mapping), content principles, perception statements

2. **Current Calendar:** `content/calendar-YYYY-MM.md` (current month)
   - Extract: monthly theme, this week's scheduled content, pillar assignment, GACCS brief

3. **Brand Strategy:** `{entity-dir}/strategy/brand-strategy.md` (e.g., `strategy/brand-strategy.md`)
   - Extract: message hierarchy (main message + supporting arguments), key messages by stage

### What Loads

```markdown
## Strategy Context (Auto-Loaded)

**Content Strategy:** [Loaded / Not found]
  → Pillars: [List if loaded]
  → Perceptions: [List if loaded]

**Calendar ([Month]):** [Loaded / Not found]
  → Theme: [Theme if loaded]
  → This week's pillar: [Pillar if loaded]
  → GACCS brief: [Available / Not available]

**Brand Strategy:** [Loaded / Not found]
  → Message hierarchy: [Available / Not available]
```

### Backward Compatibility

**If no upstream artifacts exist, this step is a no-op.** The skill runs exactly as it always has — Step 1 through Step 5, unchanged. Strategy context is additive, never required.

---

# Step 1: Voice Capture (Journal Prompts)

**This is the most important step.** Ask these questions and wait for real answers.

### Core Prompts (Ask All)

Present these prompts to the user and **wait for their responses**:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOICE CAPTURE — Weekly Content Inputs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Answer in your natural voice. Bullets, fragments, rambling — all good.
The messier the better. I'll shape it later.

1. WHAT CLICKED?
   What insight, realization, or "aha" moment did you have this week?
   (Could be from a meeting, conversation, article, or random shower thought)

2. WHAT FRUSTRATED YOU?
   Where did you see something broken, wrong, or inefficient?
   (Industry BS, bad advice, wasted effort, misaligned incentives)

3. WHAT DID YOU ACTUALLY SAY?
   Any memorable thing you said in a meeting or conversation that landed?
   (A framework you explained, pushback you gave, advice you offered)

4. WHAT ARE YOU BUILDING/TRYING?
   What are you actively working on that others might learn from?
   (Experiments, new approaches, tools, processes)

5. STORY SPARK?
   Any specific moment, conversation, or scenario worth telling?
   (Names changed, but real stories resonate)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Processing Voice Inputs

After user responds:
1. Identify the **strongest thread** — which response has the most energy/specificity?
2. Note **exact phrases** they used — these are voice gold
3. Flag **stories with stakes** — real scenarios beat abstractions
4. Mark **contrarian angles** — "everyone thinks X but actually Y"

### Alternative: Pre-Recorded Voice Input

If you've already recorded thoughts (Wispr Flow, voice memo, etc.), paste the transcript here instead of answering prompts.

**Processing pre-recorded input:**
1. Identify the **core thesis** — what's the main argument?
2. Extract **specific examples** — stories, analogies, data points
3. Note **voice phrases** — how you naturally frame ideas
4. Mark **emotional peaks** — where energy/conviction is highest

---

# Step 2: Reading Scan

Check the Reading/Inbox folder for content ideas and research.

### Process

1. Glob `Reading/Inbox/*.md`
2. Read each file's frontmatter and content summary
3. Filter to items saved in the last 14 days
4. Categorize by potential use:
   - **SPARK**: Could inspire a post angle or hook
   - **RESEARCH**: Data/evidence to support a point
   - **REACT**: Something to agree with, disagree with, or build on

### Display Format

```markdown
## Reading Queue — Content Potential

SPARK (could inspire this week's content):
  - "Article Title" — [one-line on why]
  - "Article Title" — [one-line on why]

RESEARCH (supporting evidence):
  - "Article Title" — [relevant stat or finding]

REACT (agree/disagree/build):
  - "Article Title" — [the take to react to]

No relevant items. (if nothing useful)
```

### Ask User

After displaying:
> "Any of these spark something for this week's content? Or should I focus purely on your voice capture inputs?"

---

# Step 3: Pillar Inference

Based on all inputs, determine the best content pillar for the week.

### Calendar-Aware Pillar (if calendar loaded in Step 0)

If the current month's content calendar was loaded and this week has a pillar pre-assigned:
- Display the pre-set pillar and this week's theme from the calendar
- Show: "Your calendar assigns **[Pillar]** for this week (theme: [Theme]). Use this, or override?"
- If user confirms, skip inference logic below and proceed to Step 3.5
- If user overrides, run inference logic as normal

### Content Pillars (from your playbook)

If content strategy was loaded in Step 0, use pillars from the entity's `strategy/content-strategy.md` instead of the defaults below. The strategy pillars include funnel stage and perception mappings.

**Default pillars (used when no content strategy exists):**

| Pillar | Signals in Inputs |
|--------|-------------------|
| **AI-Native Growth Systems** | Mentions of AI, ML, automation, tools, building, replacing manual work |
| **Healthcare Growth Playbooks** | Patient/physician engagement, compliance, healthcare-specific tactics |
| **Scaling-Stage Lessons** | What changes at $X revenue, hiring decisions, board-level topics |
| **Industry POV / Contrarian Takes** | Frustration with conventional wisdom, "everyone's wrong about X" |
| **Builder Stories / Behind the Scenes** | What you shipped, experiments, personal lessons, failures |

### Inference Logic

1. Score each pillar based on keyword/theme matches in:
   - Voice capture responses (weighted 3x)
   - Reading items flagged as SPARK
2. Present top 2 pillars with reasoning
3. Ask user to confirm or override

### Display Format

```markdown
## Pillar Recommendation

Based on your inputs, this week's content fits best in:

PRIMARY: [Pillar Name]
  → Why: [1-2 sentence explanation based on their inputs]

ALTERNATE: [Pillar Name]
  → Why: [1-2 sentence explanation]

Which pillar feels right for this week?
```

---

# Step 3.5: Lead Magnet & Promo Ideation

Based on the selected pillar and article topic, determine this week's Thursday promo.

### Process

1. **Check the rotation:** Is this an app-promo week or a new-magnet week?
   - If app-promo: Pick which app to promote and angle it to the week's topic
   - If new-magnet: Propose 2-3 lead magnet ideas (see types below)

2. **Lead magnet types:**

| Type | Example | Effort |
|------|---------|--------|
| **Loom mini-tutorial** | "3-min walkthrough: setting up [specific thing]" | Low |
| **Checklist/Scorecard** | "Rate your PLG readiness: 10-point checklist" | Low |
| **Template/Worksheet** | "Engagement metrics audit template (Sheets)" | Low-Med |
| **Mini-guide (2-4 pages)** | "The 5-minute guide to [specific tactic]" | Medium |
| **Infographic (downloadable)** | High-res version of Wednesday's visual | Low |
| **Swipe file/Examples** | "7 real examples of [thing] that work" | Low |
| **Decision framework** | Flowchart or decision tree | Low-Med |

3. **Standing app rotation (for app-promo weeks):**
   - **Stonesite OS** app
   - **Cursor CMO** app
   - **Home School OS** app
   - Any new standalone mini-applets/tools built that week

4. **Output:** Present recommendation with type, title, description, and which app (if app week). User confirms.

### Display Format

```markdown
## Lead Magnet / Promo Recommendation

This week's Thursday promo:

TYPE: [App Promo / Loom Tutorial / Checklist / etc.]
TITLE: "[Title]"
DESCRIPTION: [1-2 sentences on what it is and how it ties to the article]
APP (if applicable): [App name]
KEYWORD: [Comment keyword for engagement, e.g., "AUDIT"]

Confirm or suggest changes?
```

---

# Step 4: Content Creation

Generate the editorial long-form piece and derivative posts across LinkedIn + Twitter.

### Strategic Alignment (if strategy context loaded in Step 0)

If content strategy and/or brand strategy were loaded, use them as guardrails during creation:

- **Message hierarchy:** The main message and supporting arguments from brand strategy should inform (not dictate) the article's core argument. Content should reinforce these messages, not contradict them.
- **Perception statements:** Check which perception this week's pillar serves. The content should move readers toward that perception.
- **30% juice rule:** If the calendar or strategy flags this as a product-focused week, lean into it. If not, keep product mentions incidental (not the focus).
- **Monthly theme:** If a calendar theme is loaded, this week's content should connect to it, even tangentially.

**These guardrails are advisory, not rigid.** If the voice capture inputs pull in a different direction, follow the energy. Authenticity beats strategic alignment every time. But when the inputs are ambiguous, lean toward the strategy.

### Publishing Schedule (Sat–Fri Cycle)

| Day | Content | Platform(s) | Must be ready by |
|-----|---------|-------------|-----------------|
| **Saturday** | Flagship article + article promo posts | Substack + Twitter (article) + LinkedIn + Twitter (promo) | Saturday AM |
| **Monday** | Interactive engagement post | LinkedIn + Twitter | Saturday (batch) |
| **Wednesday** | Infographic / Visual | LinkedIn + Twitter | Day-of OK |
| **Thursday** | Lead magnet / App promo | LinkedIn + Twitter | Day-of OK |

**Key rules:**
- Saturday flagship and Monday engagement post must be ready before Saturday publish
- Wednesday and Thursday can be finalized during the week
- Flagship article publishes to BOTH Substack and Twitter (as long-form article) every Saturday
- All derivative posts go to BOTH LinkedIn and Twitter (adapted for each platform's tone)
- The following Saturday starts a new cycle

### Editorial Long-Form (Substack Flagship)

**Target length:** 1,800-2,100 words (7-minute read)
**Format:** Flowing essay prose with headers (3-5 headers)
**Tone:** Pensive, exploratory, reflective

**Voice blend for this format:**
- 50% exploratory, reflective, "fellow learner" stance
- 35% mechanism-thinking, density, calm confidence
- 15% wit as teaching tool (sparingly)

**Structure:**
1. **Opening hook (2-3 paragraphs)** — Start with an observation, story, or question that creates tension. Don't rush to the thesis.
2. **Development (6-10 paragraphs)** — Explore the idea from multiple angles. Let it breathe. Use transitional prose, not headers.
3. **Mechanism section (2-3 paragraphs)** — Explain WHY this works, not just what to do
4. **Grounding examples (2-3 paragraphs)** — Specific stories, names changed, real stakes
5. **"What to do?" section (2-3 paragraphs)** — ALWAYS the last header. Actionable next steps the reader can take immediately. Include resources from the author AND external experts/tools/articles. This closes every article.
6. **Closing (1-2 paragraphs)** — Optional brief forward-looking thought or genuine question after the action steps

**Paragraph rhythm:**
- Short paragraphs (1-3 sentences) with white space
- Some paragraphs develop ideas across 4-5 sentences
- Let ideas breathe — don't rush the reader
- Vary sentence length: mix 8-word punches with 25-word explorations

**Voice markers to use:**
- "I've been sitting with this idea..."
- "What strikes me about..."
- "The more I think about it..."
- "Here's the thing..."
- "What I've learned..."
- Questions mid-paragraph that you then answer

**AI tells to NEVER use:**
- Em-dashes (use commas, parentheses, or restructure the sentence)
- Sentence fragments for emphasis
- Bullet points or numbered lists (weave into prose)
- Headers every 100-200 words (use 3-5 total, not more)
- Staccato rhythm (point, point, point)
- Starting consecutive paragraphs with "The" or "This"
- Starting more than 2 sentences with "I" in a paragraph

### Saturday — Flagship Article + Promo (Substack + Twitter article + LinkedIn + Twitter promo)

- Flagship article publishes to Substack and Twitter (as long-form article)
- Accompanying promo posts on LinkedIn and Twitter
- Promo: punchy angle, links to full piece
- LinkedIn promo: 100-200 words, professional tone
- Twitter promo: 1-2 tweets, sharper/punchier, may thread

### Monday — Interactive Engagement (LinkedIn + Twitter)

Engages followership directly. Examples:
- Poll: "Are you seeing the same thing? Agree/disagree?"
- Pre-post concept: "Working on next week's piece about X. What's your experience?"
- Challenge: "Try this one thing this week and report back"
- Hot take for debate

**Goal:** Comments and conversation, not link clicks.
- LinkedIn version: 50-150 words, conversational
- Twitter version: Single tweet or short thread, more provocative

### Wednesday — Infographic / Visual (LinkedIn + Twitter)

- A visual that *supports* the article's core idea (not just promotes it)
- Framework diagram, process flow, data visualization, or 2x2 matrix
- Reference `/visual-content` skill for creation
- Should stand alone as valuable even without reading the article
- LinkedIn version: Image + 50-150 word caption
- Twitter version: Image + 1-2 tweet caption

### Thursday — Lead Magnet / App Promo (LinkedIn + Twitter)

Rotating between two types:

**Type A: Loom Mini-Tutorial (most weeks)**
- Short Loom video showing how to do something very specific
- Tied to the week's article topic
- Format: "I recorded a 3-min walkthrough of [specific thing]. Comment '[keyword]' and I'll send you the link."
- User sends Loom link to commenters after engagement

**Type B: App Promotion (2x/month minimum)**
- Promote one of the standing apps on a rotation:
  - **Stonesite OS** app
  - **Cursor CMO** app
  - **Home School OS** app
  - Any new standalone mini-applets/tools built that week
- Format: "I built this [app/tool] so you don't have to. Comment '[keyword]' to get access."

**Rotation rule:** At least 2 Thursdays per month should promote apps. The other Thursdays use Loom tutorials or other lead magnets (checklists, templates, etc.).

- LinkedIn version: 100-250 words, professional framing
- Twitter version: 1-2 tweets, more casual/builder-voice

### Voice Preservation Rules

**NEVER:**
- Invent stories or examples the user didn't provide
- Add generic advice they didn't express
- Use phrases like "In my experience..." unless they said those words
- Add emojis, hashtags, or engagement bait

**ALWAYS:**
- Use their exact phrases when possible
- Keep their tone (direct, builder-mindset, action-oriented)
- Ground insights in specifics they provided
- End with questions they'd actually want answered

---

## Voice Profile

Load your voice profile and exemplars before writing. Create a voice-synthesis.md with your brand's tone, style patterns, and anti-patterns.

---

## Voice Reference Library

Detailed voice analysis and exemplars are in:
- `voice-synthesis.md` — Overall blend
- `voice-samples/` — Individual voice reference analyses
- `voice-exemplars/social/` — Social post examples
- `voice-exemplars/long-form/` — Long-form examples

**Quick reference for format selection:**
| Format | Primary Voice | Blend |
|--------|---------------|-------|
| Editorial/Substack | Exploratory | 50% exploratory, 35% mechanism-focused, 15% wit |
| LinkedIn post | Sharp + substantive | 40% wit, 40% mechanism, 20% exploratory |
| Quick takes/X | Wit-forward | 60% wit, 25% mechanism, 15% exploratory |

---

# Step 5: Output

Generate a single markdown file with all content.

### File Location

`content/flagship-YYYY-MM-DD.md`

### File Format

```markdown
---
title: Flagship Content — Week of [Date]
pillar: [Selected Pillar]
status: draft
created: YYYY-MM-DD
schedule: Sat-Fri
---

# Flagship Content — Week of [Month Day]

## This Week's Theme
[One sentence summary of the core idea]

---

## Saturday — Flagship Article (Substack + Twitter Article)

**Pillar:** [Pillar Name]
**Publish:** Saturday AM to Substack + Twitter (long-form article)

### Article

[Full flagship article content here — 1,800-2,100 words, ending with "What to do?" section]

### Saturday Promo — LinkedIn

[100-200 word promo post linking to article]

### Saturday Promo — Twitter

[1-2 tweet promo linking to article]

---

## Monday — Interactive Engagement (LinkedIn + Twitter)

**Must be ready:** Before Saturday publish (batch with flagship)

### LinkedIn Post

[50-150 word engagement post — poll, challenge, hot take, or pre-post concept]

### Twitter Post

[Single tweet or short thread — more provocative version]

---

## Wednesday — Visual / Infographic (LinkedIn + Twitter)

**Can be finalized:** Day-of OK

### Visual
[Description of visual to create — reference /visual-content skill]

### LinkedIn Caption

[50-150 word caption for visual]

### Twitter Caption

[1-2 tweet caption for visual]

---

## Thursday — Lead Magnet / App Promo (LinkedIn + Twitter)

**Can be finalized:** Day-of OK
**Type:** [Loom Tutorial / App Promo / Checklist / etc.]
**Keyword:** [Comment keyword]

### LinkedIn Post

[100-250 word lead magnet or app promo post]

### Twitter Post

[1-2 tweet version]

---

## Lead Magnet Creation Plan

**Asset:** [Title of lead magnet or app being promoted]
**Type:** [Loom video / Checklist / Template / App promo]
**To build this week:** [What needs to be created or prepared]
**Tie to article:** [How it connects to this week's theme]

---

## Source Material

### Voice Capture (Raw Inputs)
[Copy of user's journal prompt responses]

### Reading Items Used
[List of Reading/Inbox items referenced]

---

## Notes for Next Week
[Any threads worth developing, reactions to track, follow-up angles]
```

### After Output

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Flagship content created

- Pillar: [Pillar Name]
- Posts: 5 pieces (1 flagship article on Substack + Twitter + 4 social posts across LinkedIn + Twitter)
- File: content/flagship-YYYY-MM-DD.md
- Schedule: Saturday + Monday posts ready before Saturday publish; Wednesday + Thursday can be finalized during the week

Next steps:
1. Review and edit all posts for voice
2. Publish flagship to Substack + Twitter as article on Saturday AM
3. Schedule LinkedIn + Twitter posts (Mon/Wed/Thu)
4. Record Loom / build lead magnet (if applicable this week)
5. Set reminder to engage first 60 min after each post

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

# Step 6: Production Log

After content is generated, append an entry to the production log. This creates a running record of what's been produced, enabling the content calendar to track coverage and the content strategy to assess pillar rotation.

### File Location

`content/production-log.md`

### Log Entry Format

Append the following entry to the file (create the file if it doesn't exist):

```markdown
## Week of [YYYY-MM-DD]

- **Pillar:** [Selected pillar]
- **Theme:** [Monthly theme, if calendar loaded; otherwise "—"]
- **Flagship:** [Article title]
- **Derivatives:** [Count] pieces (LinkedIn, Twitter, visual, promo)
- **Lead magnet:** [Type + title]
- **Calendar alignment:** [On-theme / Override / No calendar]
- **File:** `content/flagship-YYYY-MM-DD.md`
```

### Backward Compatibility

If no content strategy or calendar exists, log entries still get written — they just show "—" for theme and "No calendar" for alignment. The log is useful regardless of whether upstream artifacts exist.

---

# Quality Checklist

## All Formats

Before finalizing, verify:

- [ ] Hook would make YOU stop scrolling
- [ ] At least one specific number, name, or detail
- [ ] Reads like something you'd actually say
- [ ] No corporate buzzwords or generic advice
- [ ] Ends with a question you genuinely want answered
- [ ] Each derivative post is distinct (not just shorter flagship)
- [ ] Content aligns with monthly theme and perception goals (if calendar/strategy loaded)

## Editorial Long-Form (Additional Checks)

Before finalizing editorial/Substack pieces:

- [ ] Word count is 1,800-2,100 words
- [ ] No em-dashes anywhere (use commas, parentheses, or restructure)
- [ ] No bullet points or numbered lists (woven into prose)
- [ ] 3-5 section headers, last one is always "What to do?"
- [ ] Average paragraph length: 2-4 sentences
- [ ] Sentence length varies (mix short punches with longer explorations)
- [ ] Ideas develop over paragraphs, not just stated
- [ ] Reads like an essay, not an outline
- [ ] Could imagine reading this in The Atlantic or Lenny's Newsletter
- [ ] Hook creates tension/curiosity, doesn't rush to thesis

---

# Quick Actions

After running /writing, common follow-ups:

- "Make the hook more contrarian" → Rewrites hook with sharper angle
- "Add more of my voice to [post]" → Shows where to insert their phrases
- "Turn flagship into carousel" → Reformats as 6-8 slides
- "This doesn't sound like me" → Re-extracts from voice capture inputs
- "Schedule these" → Instructions for Buffer/LinkedIn scheduler
