# To Notion

Publish any markdown file to Notion database for collaboration and commenting.

---

## Usage

```
/to-notion path/to/file.md               # Publish file
/to-notion path/to/file.md --dry-run     # Preview only
/to-notion path/to/file.md --title "X"   # Override title
/to-notion --test                        # Test connection
```

---

## What It Does

1. Reads the markdown file
2. Extracts title from first H1 heading (or uses filename)
3. Converts markdown → Notion blocks (preserving links, formatting)
4. Creates a page in your Notion database with `Stage: Editing`
5. Returns the page URL

---

## Workflow

### Step 1: Preview (Optional)

```bash
python3 tools/notion_publish.py path/to/file.md --dry-run
```

### Step 2: Publish

```bash
python3 tools/notion_publish.py path/to/file.md
```

### Step 3: Collaborate

Open the Notion page URL and edit/comment with collaborators.

---

## Output Example

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTION PUBLISH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

File: projects/Social Media Strategy/content-playbook.md
Title: Content Playbook

✓ Published successfully

Page URL: https://notion.so/abc123...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Supported Markdown

| Element | Converts To |
|---------|-------------|
| `# Heading` | Heading 1 |
| `## Heading` | Heading 2 |
| `### Heading` | Heading 3 |
| `- bullet` | Bulleted list |
| `1. numbered` | Numbered list |
| `[text](url)` | Hyperlink |
| `**bold**` | Bold text |
| `` ```code``` `` | Code block |
| `> quote` | Quote block |
| `---` | Divider |
| paragraphs | Paragraphs |

---

## CLI Options

| Option | Description |
|--------|-------------|
| `file` | Path to markdown file (required) |
| `--dry-run`, `-n` | Preview without publishing |
| `--title`, `-t` | Override the page title |
| `--test` | Test Notion connection only |

---

## Environment Variables

Required in `.env`:

```bash
NOTION_API_KEY=ntn_XXXXX...
NOTION_DATABASE_ID=your-database-id
```

---

## Setup (One-Time)

1. Go to https://www.notion.so/my-integrations
2. Create new integration, copy the secret → `NOTION_API_KEY`
3. Open your target database in Notion
4. Click ⋯ → Connections → Connect to your integration
5. Copy database ID from URL → `NOTION_DATABASE_ID`

---

## Architecture

```
/to-notion command
    ↓
.claude/commands/to-notion.md (this skill)
    ↓
tools/notion_publish.py
    ↓
Notion API → Page created with Stage: Editing
```

---

## Quick Reference

```bash
# Test connection
python3 tools/notion_publish.py --test

# Publish with auto-detected title
python3 tools/notion_publish.py path/to/file.md

# Publish with custom title
python3 tools/notion_publish.py path/to/file.md --title "My Custom Title"

# Preview only
python3 tools/notion_publish.py path/to/file.md --dry-run
```
