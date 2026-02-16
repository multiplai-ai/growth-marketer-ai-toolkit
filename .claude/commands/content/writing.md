---
name: writing
description: >
  Flagship content creation skill for authentic, voice-driven LinkedIn content.
  Runs through voice capture, reading scan, pillar inference, content creation,
  and outputs a single markdown file ready for scheduling. Use when user says
  "write content", "create post", "LinkedIn content", "flagship content", or
  "weekly writing".
---

# Writing

Flagship content creation skill for authentic, voice-driven LinkedIn content. Run Monday mornings (90 min).

**Core principle:** Your authentic voice comes from YOUR inputs first. AI expands and shapes, never invents.

---

## Workflow Overview

```
/writing runs:

1. VOICE CAPTURE    → Journal prompts OR pre-recorded transcript
2. READING SCAN     → Check Reading/Inbox for content ideas + research
3. PILLAR INFERENCE → Derive best content pillar from inputs
4. CONTENT CREATION → Editorial long-form + derivative posts
5. OUTPUT           → Single markdown file ready for scheduling
```

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

### Content Pillars (Customize These)

| Pillar | Signals in Inputs |
|--------|-------------------|
| **[YOUR PILLAR 1]** | [What keywords/themes suggest this pillar] |
| **[YOUR PILLAR 2]** | [What keywords/themes suggest this pillar] |
| **[YOUR PILLAR 3]** | [What keywords/themes suggest this pillar] |
| **[YOUR PILLAR 4]** | [What keywords/themes suggest this pillar] |
| **[YOUR PILLAR 5]** | [What keywords/themes suggest this pillar] |

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

# Step 4: Content Creation

Generate the editorial long-form piece and 2-3 derivative posts.

### Editorial Long-Form (Newsletter Flagship)

**Target length:** 1,800-2,100 words (7-minute read)
**Format:** Flowing essay prose with minimal headers (2-3 max)
**Tone:** Pensive, exploratory, reflective

**Structure:**
1. **Opening hook (2-3 paragraphs)** — Start with an observation, story, or question that creates tension. Don't rush to the thesis.
2. **Development (6-10 paragraphs)** — Explore the idea from multiple angles. Let it breathe. Use transitional prose, not headers.
3. **Mechanism section (2-3 paragraphs)** — Explain WHY this works, not just what to do
4. **Grounding examples (2-3 paragraphs)** — Specific stories, names changed, real stakes
5. **Closing (2-3 paragraphs)** — Forward-looking implication or genuine question

**Paragraph rhythm:**
- Short paragraphs (1-3 sentences) with white space
- Some paragraphs develop ideas across 4-5 sentences
- Let ideas breathe — don't rush the reader
- Vary sentence length: mix 8-word punches with 25-word explorations

**AI tells to NEVER use:**
- Em-dashes (use commas, parentheses, or restructure the sentence)
- Sentence fragments for emphasis
- Bullet points or numbered lists (weave into prose)
- Headers every 100-200 words
- Staccato rhythm (point, point, point)
- Starting consecutive paragraphs with "The" or "This"
- Starting more than 2 sentences with "I" in a paragraph

### Derivative Posts (Tuesday-Thursday)

**Tuesday — Quick Take (50-150 words)**
- One punchy angle from the flagship idea
- Opinionated, fast to read
- End with a question or hot take

**Wednesday — Framework or Data Point (100-250 words)**
- Distill flagship into a visual framework OR
- Pull one specific stat/data point and unpack it
- "Here's what I'd do" action list format works

**Thursday — Story or Example (150-300 words)**
- Tell the flagship idea through a specific scenario
- Real names removed, but real stakes
- "It was [moment] when [thing happened]..."

### Voice Preservation Rules

**NEVER:**
- Invent stories or examples the user didn't provide
- Add generic advice they didn't express
- Use phrases like "In my experience..." unless they said those words
- Add emojis, hashtags, or engagement bait

**ALWAYS:**
- Use their exact phrases when possible
- Keep their tone (match voice profile below)
- Ground insights in specifics they provided
- End with questions they'd actually want answered

---

## Your Voice Profile

*Fill this section with your own voice characteristics. See `templates/voice-system-template.md` for a full framework.*

### Voice DNA

| Quality | Description | How It Shows Up |
|---------|-------------|-----------------|
| **[QUALITY 1]** | [What this means for you] | [Specific patterns] |
| **[QUALITY 2]** | [What this means for you] | [Specific patterns] |
| **[QUALITY 3]** | [What this means for you] | [Specific patterns] |
| **[QUALITY 4]** | [What this means for you] | [Specific patterns] |

### Social Post Voice

**Core characteristics:**
- [YOUR CHARACTERISTIC 1]
- [YOUR CHARACTERISTIC 2]
- [YOUR CHARACTERISTIC 3]
- [YOUR CHARACTERISTIC 4]

**Hooks that work for you:**
- [YOUR HOOK PATTERN 1]
- [YOUR HOOK PATTERN 2]
- [YOUR HOOK PATTERN 3]

**Anti-patterns (never do):**
- Engagement bait ("Like if you agree!")
- Hashtag soup (max 2-3, end of post only)
- Empty openers ("I've been thinking a lot about...")
- Self-congratulation disguised as humility

**AI-tell anti-patterns (these are dead giveaways — kill on sight):**
- Perfect parallel bullet lists where every item has the same structure/length (real people are messier)
- Em-dash + rhetorical question chains ("Gather site context — with what structure?") — this pattern screams LLM
- Thesis-statement closers that package the lesson in a bow ("That's the gap in X: they Y without Z")
- Formulaic closing questions pretending to be curiosity ("What [thing] have you [done]?")
- Spec-sheet formatting in personal posts (numbered improvements, tables of before/after)
- Consultant jargon packaging ("operational depth," "operating system for delivering X")
- Hook → Framework → Friction → Fixes → Lesson → Question template structure
- Teaser bait openers ("It was missing something critical." / "What I found surprised me.")
- Every section mirroring perfectly — real observations are asymmetric

### Long-Form Voice

**Core characteristics:**
- [YOUR LONG-FORM CHARACTERISTIC 1]
- [YOUR LONG-FORM CHARACTERISTIC 2]
- [YOUR LONG-FORM CHARACTERISTIC 3]

**Opening techniques that work for you:**
- [YOUR OPENER 1]
- [YOUR OPENER 2]

**Closing techniques:**
- Summary of key takeaways (3-5 bullets)
- Specific next steps for reader
- Forward-looking implication
- Genuine question that invites dialogue

### Voice Test (Ask Yourself)

1. Would I actually say this in a meeting?
2. Is every sentence doing work?
3. Can I point to a specific example?
4. Does the ending give them something to do?
5. Would I cringe reading this in 6 months?

---

# Step 5: Output

Generate a single markdown file with all content.

### File Location

`content/flagship-YYYY-MM-DD.md` (or your preferred content directory)

### File Format

```markdown
---
title: Flagship Content — Week of [Date]
pillar: [Selected Pillar]
status: draft
created: YYYY-MM-DD
---

# Flagship Content — Week of [Month Day]

## This Week's Theme
[One sentence summary of the core idea]

---

## Monday — Flagship Post (Anchor)

**Pillar:** [Pillar Name]
**Format:** [Text / Carousel]
**Best posting time:** Monday 9:00 AM

### Post

[Full flagship post content here]

---

## Tuesday — Quick Take

**Best posting time:** Tuesday 8:30 AM

### Post

[Quick take content]

---

## Wednesday — Framework/Data Point

**Best posting time:** Wednesday 10:00 AM

### Post

[Framework or data point content]

---

## Thursday — Story/Example

**Best posting time:** Thursday 9:00 AM

### Post

[Story/example content]

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

✓ Flagship content created

- Pillar: [Pillar Name]
- Posts: 4 (1 flagship + 3 derivatives)
- File: content/flagship-YYYY-MM-DD.md

Next steps:
1. Review and edit for voice
2. Schedule in Buffer/LinkedIn
3. Set reminder to engage first 60 min after each post

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

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

## Editorial Long-Form (Additional Checks)

Before finalizing editorial/newsletter pieces:

- [ ] Word count is 1,800-2,100 words
- [ ] No em-dashes anywhere (use commas, parentheses, or restructure)
- [ ] No bullet points or numbered lists (woven into prose)
- [ ] Maximum 2-3 section headers total
- [ ] Average paragraph length: 2-4 sentences
- [ ] Sentence length varies (mix short punches with longer explorations)
- [ ] Ideas develop over paragraphs, not just stated
- [ ] Reads like an essay, not an outline
- [ ] Hook creates tension/curiosity, doesn't rush to thesis

---

# Quick Actions

After running /writing, common follow-ups:

- "Make the hook more contrarian" → Rewrites hook with sharper angle
- "Add more of my voice to [post]" → Shows where to insert their phrases
- "Turn flagship into carousel" → Reformats as 6-8 slides
- "This doesn't sound like me" → Re-extracts from voice capture inputs
- "Schedule these" → Instructions for Buffer/LinkedIn scheduler
