# To Gamma

Publish any markdown file to Gamma as a presentation, document, or webpage.

---

## Usage

```
/to-gamma path/to/file.md               # Publish as presentation
/to-gamma path/to/file.md --title "X"   # Override title
/to-gamma path/to/file.md --dry-run     # Preview without publishing
/to-gamma path/to/file.md --format doc  # Publish as document
/to-gamma --test                        # Test API connection
```

---

## What It Does

1. Reads the markdown file
2. Validates structure (checks for `---` slide breaks)
3. Calls Gamma Generate API
4. Waits for async completion (~60-90 seconds)
5. Returns the Gamma URL

---

## Workflow

### Step 1: Preview (Optional)

```bash
python3 tools/gamma_create_presentation.py path/to/file.md --dry-run
```

### Step 2: Publish

```bash
python3 tools/gamma_create_presentation.py path/to/file.md
```

### Step 3: Edit in Gamma

Open the returned URL to customize design, add images, or refine content.

---

## Slide Structure Guidelines

Use `---` (horizontal rule) to create slide breaks:

```markdown
# Title Slide

Your opening content here

---

## Second Slide

Content for slide two

- Bullet point
- Another point

---

## Third Slide

More content...
```

**Key rules:**
- `---` on its own line = new slide
- First `# Heading` becomes the title
- Each section between `---` becomes one slide
- Gamma uses AI to style and add imagery automatically

---

## Output Example

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRESENTATION CREATED SUCCESSFULLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
URL: https://gamma.app/docs/Your-Presentation-abc123
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CLI Options

| Option | Description |
|--------|-------------|
| `file` | Path to markdown file (required unless --test) |
| `--dry-run`, `-n` | Preview structure without publishing |
| `--title`, `-t` | Override the presentation title |
| `--format`, `-f` | Output format: `presentation` (default), `document`, `webpage` |
| `--num-cards` | Specify exact number of slides |
| `--test` | Test Gamma API connection only |

---

## Environment Variables

Required in `.env`:

```bash
GAMMA_API_KEY=your-gamma-api-key
```

---

## Setup (One-Time)

1. Go to https://gamma.app/settings/developers
2. Create an API key
3. Add to `.env`: `GAMMA_API_KEY=your-key-here`

---

## Architecture

```
/to-gamma command
    ↓
.claude/commands/to-gamma.md (this skill)
    ↓
tools/gamma_create_presentation.py
    ↓
Gamma Generate API → Async generation → URL returned
```

---

## Format Comparison

| Format | Use Case |
|--------|----------|
| `presentation` | Slides for presenting (default) |
| `document` | Long-form content, reports |
| `webpage` | Shareable web pages |

---

## Quick Reference

```bash
# Test connection
python3 tools/gamma_create_presentation.py --test

# Dry run preview
python3 tools/gamma_create_presentation.py path/to/file.md --dry-run

# Publish as presentation (default)
python3 tools/gamma_create_presentation.py path/to/file.md

# Publish with custom title
python3 tools/gamma_create_presentation.py path/to/file.md --title "My Deck"

# Publish as document
python3 tools/gamma_create_presentation.py path/to/file.md --format document

# Publish as webpage
python3 tools/gamma_create_presentation.py path/to/file.md --format webpage
```
