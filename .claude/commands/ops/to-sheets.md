# To Sheets

Publish markdown tables to Google Sheets, preserving all columns (unlike Notion's block limits).

---

## Usage

```
/to-sheets path/to/file.md               # Publish all tables
/to-sheets path/to/file.md --dry-run     # Preview only
/to-sheets path/to/file.md --sheet-name "My Data"   # Custom worksheet name
/to-sheets --test                        # Test connection
```

---

## What It Does

1. Reads the markdown file
2. Finds all markdown tables (pipe-delimited `|`)
3. Extracts headers and data rows
4. Creates or updates a worksheet in your Google Sheet
5. Returns the sheet URL

---

## Workflow

### Step 1: Preview (Optional)

```bash
python3 tools/sheets_publish.py path/to/file.md --dry-run
```

Shows: tables found, column count, row count, first few rows.

### Step 2: Publish

```bash
python3 tools/sheets_publish.py path/to/file.md
```

### Step 3: Share

Open the Google Sheet URL and share/edit as needed.

---

## Output Example

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GOOGLE SHEETS PUBLISH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

File: outputs/skills-table-blog-post.md
Tables found: 6
  1. Task Management: 3 columns, 5 rows
  2. Daily Operations: 3 columns, 3 rows
  ...

✓ Published successfully

Worksheet: Task Management
Rows written: 6

Sheet URL: https://docs.google.com/spreadsheets/d/abc123.../edit#gid=0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## CLI Options

| Option | Description |
|--------|-------------|
| `file` | Path to markdown file (required) |
| `--dry-run`, `-n` | Preview without publishing |
| `--sheet-name`, `-s` | Override the worksheet name |
| `--test` | Test Google Sheets connection only |

---

## Environment Variables

Required in `.env`:

```bash
GOOGLE_SERVICE_ACCOUNT_PATH=~/.config/google-service-account.json
GOOGLE_SHEETS_ID=your-spreadsheet-id
```

---

## Setup (One-Time)

### 1. Create Google Cloud Service Account

1. Go to https://console.cloud.google.com/
2. Create a project (or use existing)
3. Enable **Google Sheets API**: APIs & Services → Enable APIs → Search "Google Sheets API" → Enable
4. Create service account: IAM & Admin → Service Accounts → Create
5. Download JSON key file → save as `~/.config/google-service-account.json`

### 2. Share Target Spreadsheet

1. Create a new Google Sheet (or use existing)
2. Click Share → paste the service account email (from JSON file, looks like `xxx@project.iam.gserviceaccount.com`)
3. Give it **Editor** access
4. Copy the spreadsheet ID from the URL: `https://docs.google.com/spreadsheets/d/{THIS_PART}/edit`
5. Add to `.env` as `GOOGLE_SHEETS_ID`

---

## Architecture

```
/to-sheets command
    ↓
.claude/commands/to-sheets.md (this skill)
    ↓
tools/sheets_publish.py
    ↓
Google Sheets API → Worksheet created/updated
```

---

## Quick Reference

```bash
# Test connection
python3 tools/sheets_publish.py --test

# Publish with auto-detected worksheet name
python3 tools/sheets_publish.py path/to/file.md

# Publish with custom worksheet name
python3 tools/sheets_publish.py path/to/file.md --sheet-name "Q1 Data"

# Preview only
python3 tools/sheets_publish.py path/to/file.md --dry-run
```

---

## When to Use This vs /to-notion

| Use Case | Tool |
|----------|------|
| Need all columns (>3-4 cols) | `/to-sheets` |
| Need filtering, sorting, formulas | `/to-sheets` |
| Need collaboration on prose | `/to-notion` |
| Need database properties | `/to-notion` |
