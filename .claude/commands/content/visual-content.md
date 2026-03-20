---
name: visual-content
description: Generate shareable visuals (infographics, diagrams, frameworks) from content. Creates HTML that renders as visual, user screenshots for PNG. Uses personal brand styling from visual-brand-guide.md.
---

# /visual-content — Shareable Visual Generator

Create shareable visuals that help readers understand frameworks, processes, and mental models. Outputs HTML for browser preview; user screenshots for final PNG.

## When to Use

- Visualizing a framework or methodology from an article
- Creating a process flow or step-by-step diagram
- Making a comparison visual (before/after, old/new)
- Designing a 2x2 decision matrix
- Distilling a mental model into a single visual

## Inputs

User provides ONE of:
1. **Content excerpt** — Paste of article section with framework/concept
2. **Framework description** — "I want to visualize the 3 stages of X"
3. **Existing article path** — Path to markdown file to analyze

## Workflow

### Phase 1: Content Analysis

**1.1 Identify Visual Type**

| Type | Indicators | Best For |
|------|-----------|----------|
| **Framework** | Named methodology, 3-6 components, pillars | Revenue Levers, Story Stack |
| **Process** | Sequential steps, "first...then...finally" | Workflows, how-tos |
| **Matrix** | Two dimensions, quadrants, tradeoffs | Decision frameworks |
| **Comparison** | Before/after, old/new, this vs that | Transformation stories |
| **Mental Model** | Single concept, one big idea | Key insight, aha moment |
| **Checklist/Reference Card** | Multiple categories, action items, dense info | AI SEO checklist, tool comparison, cheat sheets |
| **Spoke/Radial Diagram** | Central concept with branches, hub-and-spoke | Topic maps, capability breakdowns |
| **Layered Pyramid/Stack** | Hierarchy, progression, stacked levels | Marketing layers, maturity models |

**1.2 Extract Elements**

For each type, identify:
- **Title** — What is this framework called?
- **Sections/Steps** — What are the components?
- **Labels** — Brief text for each element
- **Relationships** — How do elements connect?

### Phase 1.5: Visual Exemplar Review

**Before generating any HTML, review reference graphics for design inspiration.**

1. Read at least 3 images from `visual-exemplars/social-graphics/` using the Read tool
2. Identify which exemplars are closest to the visual type you're building (framework, comparison, checklist, etc.)
3. Note specific design qualities to emulate:
   - **Layout density** — how much whitespace vs content?
   - **Typography hierarchy** — headline weight, label sizing, description text
   - **Color restraint** — most exemplars use 1-2 accent colors on a clean white/cream base
   - **Information architecture** — how is complex info organized? (cards, pills/chips, numbered sections, arrows)
   - **Format** — portrait (1080x1350) works well for information-dense graphics; landscape (1200x675) for simpler frameworks

This step is **non-negotiable** — the same way the writing skill requires reading voice exemplars before drafting. The exemplars show what "good" looks like in practice, beyond what the templates alone can capture.

---

### Phase 2: Generate HTML

**2.1 Load Brand Tokens**

Brand tokens vary by entity. Before generating any HTML, load tokens in this priority order:

1. **Check if working on a specific entity.** If the user specifies an entity or the context makes it clear:
   - **First:** Check for entity-specific tokens at `{entity-dir}/creative/tokens.json`. If found, this is the source of truth — use colors, typography, spacing, textures, and shape values from this file. Also load `{entity-dir}/creative/brand-guide.md` for rules and anti-patterns.
   - **Fallback:** If no `tokens.json` exists, load the brand profile from the entity's brand directory
   - Use the entity's color palette, typography, and texture rules instead of the personal brand defaults below
2. **Default (personal brand content):** Read `visual-brand-guide.md` for current brand tokens, typography, and layout principles.

> **Note:** Entities with a complete creative foundation will have `tokens.json` with machine-readable values for every design decision. Use these exact values — do not approximate or substitute.

**2.2 Design Principles (apply to every graphic)**

- Use **Poppins** (weight 800) for headlines, **Inter** for body text
- Headline size: **48-56px minimum**, weight 800, letter-spacing: -0.03em
- Card titles: 22-28px Poppins weight 700
- Labels: 11-13px, weight 600, uppercase, 0.1em letter-spacing
- **Add emoji icons** (32-36px) to each card, step, or quadrant for whimsy
- **Add organic blob shapes** — use `::before`/`::after` pseudo-elements with asymmetric `border-radius` and low-opacity accent fill
- **NO wave decorations. NO gradient backgrounds on the container itself.**
- Use solid backgrounds: `#FFE6C8` (warm cream), `#FFFFFF` (white), or `#101010` (dark)
- Accent color (`#EE5A29`) in **maximum 1-2 elements** per graphic (e.g., one top-border + step numbers)
- Text color: `#101010` (headlines), `#666666` (secondary/descriptions)
- Cards: white background, 1px `#E0E0E0` border, **16-18px border-radius** (soft, friendly) — no heavy shadows
- Watermark: `@yourbrand` (bottom-right, 12px, weight 600, opacity 0.4)
- Accent bar: 4px `#EE5A29` along bottom edge

**2.3 Select Template**

Based on visual type, use the appropriate template from Phase 3.

**2.4 Customize Content**

Replace placeholder text with extracted content:
- Title and subtitle
- Section labels and descriptions
- Step numbers and text
- Quadrant labels
- Comparison points

**2.5 Select Dimensions**

| Platform | Dimensions | Use Case |
|----------|------------|----------|
| LinkedIn | 1200 x 675 | Simple frameworks, mental models, comparisons |
| Square | 1080 x 1080 | Instagram, carousel |
| Portrait | 1080 x 1350 | Information-dense graphics: checklists, reference cards, layered diagrams |

Default to LinkedIn (1200x675) for simple visuals. Use Portrait (1080x1350) for information-dense types like checklists, reference cards, and multi-section graphics — most high-performing exemplars use a tall format.

### Phase 3: HTML Templates

Use these templates. Include the CSS inline (reference `tools/visual_templates/base-styles.css` for the full stylesheet).

---

#### Template 1: Framework Diagram

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; }

    .container {
      width: 1200px;
      height: 675px;
      background: #FFE6C8;
      padding: 56px;
      position: relative;
      display: flex;
      flex-direction: column;
    }

    .title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 48px;
      font-weight: 700;
      color: #101010;
      margin-bottom: 8px;
      letter-spacing: -0.03em;
    }

    .subtitle {
      font-size: 17px;
      color: #666666;
      margin-bottom: 40px;
    }

    .framework-grid {
      display: flex;
      gap: 20px;
      flex: 1;
    }

    .framework-item {
      flex: 1;
      background: #FFFFFF;
      border-radius: 12px;
      padding: 28px;
      border: 1px solid #E0E0E0;
      border-top: 3px solid #EE5A29;
      display: flex;
      flex-direction: column;
    }

    .item-number {
      font-size: 11px;
      font-weight: 600;
      color: #666666;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-bottom: 12px;
    }

    .item-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 22px;
      font-weight: 700;
      color: #101010;
      margin-bottom: 12px;
      letter-spacing: -0.02em;
    }

    .item-desc {
      font-size: 14px;
      color: #666666;
      line-height: 1.5;
    }

    .watermark {
      position: absolute;
      bottom: 24px;
      right: 32px;
      font-size: 12px;
      font-weight: 600;
      color: #101010;
      opacity: 0.5;
    }

    .accent-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: #EE5A29;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="title">{{FRAMEWORK_TITLE}}</div>
    <div class="subtitle">{{FRAMEWORK_SUBTITLE}}</div>

    <div class="framework-grid">
      <div class="framework-item">
        <div class="item-number">01</div>
        <div class="item-title">{{ITEM_1_TITLE}}</div>
        <div class="item-desc">{{ITEM_1_DESC}}</div>
      </div>

      <div class="framework-item">
        <div class="item-number">02</div>
        <div class="item-title">{{ITEM_2_TITLE}}</div>
        <div class="item-desc">{{ITEM_2_DESC}}</div>
      </div>

      <div class="framework-item">
        <div class="item-number">03</div>
        <div class="item-title">{{ITEM_3_TITLE}}</div>
        <div class="item-desc">{{ITEM_3_DESC}}</div>
      </div>

      <div class="framework-item">
        <div class="item-number">04</div>
        <div class="item-title">{{ITEM_4_TITLE}}</div>
        <div class="item-desc">{{ITEM_4_DESC}}</div>
      </div>
    </div>

    <div class="accent-bar"></div>
    <div class="watermark">@yourbrand</div>
  </div>
</body>
</html>
```

**Variants:**
- 3 items: Remove one `framework-item` div
- 5-6 items: Add more items, reduce padding/font sizes

---

#### Template 2: Process Flow

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; }

    .container {
      width: 1200px;
      height: 675px;
      background: #FFFFFF;
      padding: 56px;
      position: relative;
      display: flex;
      flex-direction: column;
    }

    .title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 48px;
      font-weight: 700;
      color: #101010;
      margin-bottom: 48px;
      text-align: center;
      letter-spacing: -0.03em;
    }

    .process-flow {
      display: flex;
      align-items: center;
      justify-content: center;
      flex: 1;
      gap: 12px;
    }

    .step {
      background: #FFFFFF;
      border-radius: 12px;
      padding: 32px 24px;
      border: 1px solid #E0E0E0;
      text-align: center;
      width: 220px;
    }

    .step-number {
      width: 44px;
      height: 44px;
      background: #EE5A29;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 20px;
      font-weight: 700;
      margin: 0 auto 16px;
    }

    .step-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 20px;
      font-weight: 700;
      color: #101010;
      margin-bottom: 8px;
      letter-spacing: -0.02em;
    }

    .step-desc {
      font-size: 13px;
      color: #666666;
      line-height: 1.4;
    }

    .arrow {
      color: #E0E0E0;
      font-size: 28px;
      font-weight: 300;
    }

    .watermark {
      position: absolute;
      bottom: 24px;
      right: 32px;
      font-size: 12px;
      font-weight: 600;
      color: #101010;
      opacity: 0.5;
    }

    .accent-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: #EE5A29;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="title">{{PROCESS_TITLE}}</div>

    <div class="process-flow">
      <div class="step">
        <div class="step-number">1</div>
        <div class="step-title">{{STEP_1_TITLE}}</div>
        <div class="step-desc">{{STEP_1_DESC}}</div>
      </div>

      <div class="arrow">→</div>

      <div class="step">
        <div class="step-number">2</div>
        <div class="step-title">{{STEP_2_TITLE}}</div>
        <div class="step-desc">{{STEP_2_DESC}}</div>
      </div>

      <div class="arrow">→</div>

      <div class="step">
        <div class="step-number">3</div>
        <div class="step-title">{{STEP_3_TITLE}}</div>
        <div class="step-desc">{{STEP_3_DESC}}</div>
      </div>

      <div class="arrow">→</div>

      <div class="step">
        <div class="step-number">4</div>
        <div class="step-title">{{STEP_4_TITLE}}</div>
        <div class="step-desc">{{STEP_4_DESC}}</div>
      </div>
    </div>

    <div class="accent-bar"></div>
    <div class="watermark">@yourbrand</div>
  </div>
</body>
</html>
```

---

#### Template 3: 2x2 Matrix

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; }

    .container {
      width: 1200px;
      height: 675px;
      background: #FFE6C8;
      padding: 48px;
      position: relative;
      display: flex;
      flex-direction: column;
    }

    .title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 44px;
      font-weight: 700;
      color: #101010;
      margin-bottom: 32px;
      text-align: center;
      letter-spacing: -0.03em;
    }

    .matrix-wrapper {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    .matrix {
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: 1fr 1fr;
      gap: 2px;
      background: #E0E0E0;
      border-radius: 12px;
      overflow: hidden;
      width: 600px;
      height: 400px;
    }

    .quadrant {
      background: #FFFFFF;
      padding: 28px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }

    .quadrant-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 20px;
      font-weight: 700;
      color: #101010;
      margin-bottom: 8px;
      letter-spacing: -0.02em;
    }

    .quadrant-desc {
      font-size: 13px;
      color: #666666;
      line-height: 1.4;
    }

    .quadrant.highlight {
      background: rgba(238, 90, 41, 0.12);
    }

    .quadrant.highlight .quadrant-title {
      color: #EE5A29;
    }

    .axis-label {
      position: absolute;
      font-size: 11px;
      font-weight: 600;
      color: #666666;
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }

    .axis-x-left { left: 80px; bottom: 60px; }
    .axis-x-right { right: 80px; bottom: 60px; }
    .axis-y-top { top: 100px; left: 50px; writing-mode: vertical-rl; transform: rotate(180deg); }
    .axis-y-bottom { bottom: 100px; left: 50px; writing-mode: vertical-rl; transform: rotate(180deg); }

    .watermark {
      position: absolute;
      bottom: 24px;
      right: 32px;
      font-size: 12px;
      font-weight: 600;
      color: #101010;
      opacity: 0.5;
    }

    .accent-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: #EE5A29;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="title">{{MATRIX_TITLE}}</div>

    <div class="matrix-wrapper">
      <div class="axis-label axis-y-top">{{Y_AXIS_HIGH}}</div>
      <div class="axis-label axis-y-bottom">{{Y_AXIS_LOW}}</div>
      <div class="axis-label axis-x-left">{{X_AXIS_LOW}}</div>
      <div class="axis-label axis-x-right">{{X_AXIS_HIGH}}</div>

      <div class="matrix">
        <div class="quadrant">
          <div class="quadrant-title">{{Q1_TITLE}}</div>
          <div class="quadrant-desc">{{Q1_DESC}}</div>
        </div>
        <div class="quadrant highlight">
          <div class="quadrant-title">{{Q2_TITLE}}</div>
          <div class="quadrant-desc">{{Q2_DESC}}</div>
        </div>
        <div class="quadrant">
          <div class="quadrant-title">{{Q3_TITLE}}</div>
          <div class="quadrant-desc">{{Q3_DESC}}</div>
        </div>
        <div class="quadrant">
          <div class="quadrant-title">{{Q4_TITLE}}</div>
          <div class="quadrant-desc">{{Q4_DESC}}</div>
        </div>
      </div>
    </div>

    <div class="accent-bar"></div>
    <div class="watermark">@yourbrand</div>
  </div>
</body>
</html>
```

---

#### Template 4: Comparison

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; }

    .container {
      width: 1200px;
      height: 675px;
      background: #FFFFFF;
      padding: 56px;
      position: relative;
      display: flex;
      flex-direction: column;
    }

    .title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 48px;
      font-weight: 700;
      color: #101010;
      margin-bottom: 40px;
      text-align: center;
      letter-spacing: -0.03em;
    }

    .comparison {
      display: flex;
      gap: 32px;
      flex: 1;
    }

    .column {
      flex: 1;
      border-radius: 12px;
      padding: 32px;
    }

    .column-old {
      background: #FFFFFF;
      border: 2px dashed #E0E0E0;
    }

    .column-new {
      background: rgba(238, 90, 41, 0.08);
      border: 2px solid #EE5A29;
    }

    .column-header {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 14px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .column-old .column-header { color: #666666; }
    .column-new .column-header { color: #EE5A29; }

    .column-header .icon {
      font-size: 18px;
    }

    .items {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 15px;
      color: #101010;
      line-height: 1.4;
    }

    .item .bullet {
      font-size: 18px;
      line-height: 1;
      margin-top: 2px;
    }

    .column-old .bullet { color: #E0E0E0; }
    .column-new .bullet { color: #EE5A29; }

    .watermark {
      position: absolute;
      bottom: 24px;
      right: 32px;
      font-size: 12px;
      font-weight: 600;
      color: #101010;
      opacity: 0.5;
    }

    .accent-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: #EE5A29;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="title">{{COMPARISON_TITLE}}</div>

    <div class="comparison">
      <div class="column column-old">
        <div class="column-header">
          <span class="icon">✗</span>
          {{OLD_HEADER}}
        </div>
        <div class="items">
          <div class="item"><span class="bullet">—</span> {{OLD_ITEM_1}}</div>
          <div class="item"><span class="bullet">—</span> {{OLD_ITEM_2}}</div>
          <div class="item"><span class="bullet">—</span> {{OLD_ITEM_3}}</div>
          <div class="item"><span class="bullet">—</span> {{OLD_ITEM_4}}</div>
        </div>
      </div>

      <div class="column column-new">
        <div class="column-header">
          <span class="icon">✓</span>
          {{NEW_HEADER}}
        </div>
        <div class="items">
          <div class="item"><span class="bullet">→</span> {{NEW_ITEM_1}}</div>
          <div class="item"><span class="bullet">→</span> {{NEW_ITEM_2}}</div>
          <div class="item"><span class="bullet">→</span> {{NEW_ITEM_3}}</div>
          <div class="item"><span class="bullet">→</span> {{NEW_ITEM_4}}</div>
        </div>
      </div>
    </div>

    <div class="accent-bar"></div>
    <div class="watermark">@yourbrand</div>
  </div>
</body>
</html>
```

---

#### Template 5: Mental Model

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; }

    .container {
      width: 1200px;
      height: 675px;
      background: #101010;
      padding: 64px;
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }

    .label {
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      color: #EE5A29;
      margin-bottom: 24px;
    }

    .main-text {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 52px;
      font-weight: 700;
      color: #FFFFFF;
      line-height: 1.15;
      letter-spacing: -0.03em;
      max-width: 900px;
      margin-bottom: 32px;
    }

    .highlight {
      color: #EE5A29;
    }

    .accent-line {
      width: 60px;
      height: 3px;
      background: #EE5A29;
      border-radius: 2px;
      margin: 32px 0;
    }

    .supporting {
      font-size: 18px;
      color: rgba(255, 255, 255, 0.6);
      max-width: 700px;
      line-height: 1.5;
    }

    .watermark {
      position: absolute;
      bottom: 24px;
      right: 32px;
      font-size: 12px;
      font-weight: 600;
      color: rgba(255, 255, 255, 0.4);
    }

    .accent-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: #EE5A29;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="label">{{LABEL}}</div>
    <div class="main-text">{{MAIN_TEXT_BEFORE}} <span class="highlight">{{MAIN_TEXT_HIGHLIGHT}}</span> {{MAIN_TEXT_AFTER}}</div>
    <div class="accent-line"></div>
    <div class="supporting">{{SUPPORTING_TEXT}}</div>

    <div class="accent-bar"></div>
    <div class="watermark">@yourbrand</div>
  </div>
</body>
</html>
```

---

### Phase 4: Save & Preview

**4.1 Generate Filename**

Format: `visual-{type}-{timestamp}.html`

Example: `visual-framework-2026-02-16-143022.html`

**4.2 Save Location**

Save HTML to: `.tmp/visuals/`

**4.3 Provide Preview Instructions**

Tell user:
```
Visual saved to: .tmp/visuals/visual-framework-2026-02-16-143022.html

To preview:
1. Open the file in your browser (Cmd+O or drag to browser)
2. Take a screenshot (Cmd+Shift+4, select area)
3. Save PNG to: projects/Social Media Strategy/visuals/
```

### Phase 5: Social Copy (Optional)

If user wants to share the visual, suggest:

**LinkedIn format:**
```
[Hook — what problem this solves]

[1-2 sentence context]

[Framework name or key insight]

Save this for later. ↓

#marketing #growth #frameworks
```

---

## Visual Exemplar Library

Reference graphics live in `visual-exemplars/social-graphics/`. These are real high-performing social graphics that demonstrate what "good" looks like. Add new exemplars to this folder over time as you find them.

**Key patterns across the exemplars:**
- Clean white/cream backgrounds with 1-2 accent colors max
- Bold, heavy-weight headlines (often 40-56px black)
- Strong information hierarchy: headline → section labels → body text → footer
- Generous whitespace even in dense layouts
- Card/pill/chip elements for organizing concepts
- Footer bars with CTA or attribution text
- Portrait format (tall) for information-dense graphics
- Minimal decoration — content does the heavy lifting

## Brand Reference

Brand tokens vary by entity. Load the correct profile before generating visuals.

**Entity-specific brands:** Load from `the entity's brand directory` — this overrides the defaults below.

**Default (personal brand):**
See `visual-brand-guide.md` for the full brand system.

**Quick reference (personal brand defaults):**
- **Palette:** `#101010` (ink), `#FFE6C8` (cream), `#FFFFFF` (white), `#EE5A29` (accent), `#666666` (gray), `#E0E0E0` (borders)
- **Fonts:** Poppins (headlines, weight 800), Inter (body)
- **Headlines:** 48-56px, weight 800, letter-spacing -0.03em
- **Icons:** Emoji per card/step (32-36px) for playful anchoring
- **Shapes:** Organic blob decorations via CSS pseudo-elements
- **Watermark:** `@yourbrand`
- **Accent bar:** 3px `#EE5A29` bottom edge

---

## Example Usage

**Input:**
```
Create a visual for the SAT Framework:
- Skills: Markdown SOPs that define what to do
- Agents: AI decision-makers that coordinate
- Tools: Python scripts that execute
```

**Output:**
Framework diagram with 3 components, saved to `.tmp/visuals/`

---

## Checklist

- [ ] Identify visual type from content
- [ ] Review 3+ visual exemplars from `visual-exemplars/social-graphics/`
- [ ] Read `visual-brand-guide.md` for brand tokens
- [ ] Extract title, sections, labels
- [ ] Select template and dimensions
- [ ] Generate HTML with Poppins (headlines) + Inter (body) fonts
- [ ] Add emoji icons to each card/step/quadrant
- [ ] Add organic blob shape decoration (CSS pseudo-element)
- [ ] Verify: headlines 48px+, no waves, no gradient backgrounds, accent used sparingly
- [ ] Watermark says `@yourbrand`
- [ ] Save to `.tmp/visuals/`
- [ ] Provide preview instructions
- [ ] (Optional) Suggest social copy
