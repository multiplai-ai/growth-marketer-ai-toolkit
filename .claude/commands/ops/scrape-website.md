---
name: scrape-website
description: Scrape articles from blog index pages and save as markdown files to Library/
---

# Website Scraper Skill

Scrapes articles from blog index pages (like Graphite.io/five-percent, Growth-memo.com) and saves them as markdown files.

## Tool Location

`tools/web_scraper.py`

## Prerequisites

- Python 3.10+
- Playwright (`playwright install chromium` if not already done)
- trafilatura (`pip install trafilatura`)

## Basic Usage

```bash
# Scrape all articles from an index page
python tools/web_scraper.py "<index_url>" "<output_dir>"

# Example: Graphite's 5% blog
python tools/web_scraper.py "https://graphite.io/five-percent" "Library/Graphite-5-Percent/"
```

## Common Options

| Option | Description |
|--------|-------------|
| `--limit N` | Only scrape first N articles (for testing) |
| `--substack` | Substack mode: auto-navigate to /archive |
| `--link-selector "CSS"` | Custom CSS selector for article links |
| `--delay N` | Seconds between page loads (default: 1.5) |
| `--no-skip-existing` | Re-scrape articles already in output dir |

## Examples

### Substack blogs
```bash
python tools/web_scraper.py "https://www.growth-memo.com" "Library/Growth-Memo/" --substack
```

### Custom link selector
```bash
python tools/web_scraper.py "https://site.com/blog" "Library/Site/" --link-selector "article a.title"
```

### Test with limit
```bash
python tools/web_scraper.py "https://site.com" "Library/Test/" --limit 3
```

## Output Format

Articles are saved as markdown with YAML frontmatter:

```markdown
---
source: https://example.com/article-slug
scraped: 2026-02-16
title: "Article Title Here"
author: "Author Name"
date: 2026-01-15
---

# Article Title Here

Article content in markdown...
```

## How It Works

1. **Navigate** to the index URL (or /archive for Substack)
2. **Scroll** to load all article links (handles infinite scroll)
3. **Filter** links to find articles (configurable patterns + smart defaults)
4. **Deduplicate** against already-scraped URLs
5. **For each article:**
   - Navigate to page
   - Extract content via trafilatura (handles boilerplate removal)
   - Save as markdown with frontmatter
6. **Report** success/error counts

## Troubleshooting

### "No article links found"
- The site may use unusual markup. Try:
  1. Open the page in browser, inspect article links
  2. Use `--link-selector "your-selector"` with a CSS selector that matches

### Paywalled content
- The scraper will get whatever's visible without login
- Articles requiring authentication will have minimal content

### Rate limiting
- Increase `--delay` if you're getting blocked
- The default 1.5s is usually safe

### Content extraction issues
- trafilatura handles most sites well
- For very unusual layouts, content may be incomplete
- Check the markdown output and consider manual cleanup if needed

## Deduplication

The scraper checks existing files in the output directory and skips URLs that have already been scraped (based on the `source:` frontmatter field). Use `--no-skip-existing` to force re-scraping.

## Expected Behavior

- Creates output directory if it doesn't exist
- Sanitizes filenames (removes special characters, limits length)
- Handles duplicate filenames with -1, -2 suffix
- Continues on individual article failures
- Reports errors at the end
