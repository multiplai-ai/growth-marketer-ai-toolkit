# Growth Marketer AI Toolkit

A collection of Claude Code skills and tools for growth marketers. Audit ad accounts, plan campaigns, and create content with AI-powered workflows.

## Installation

### Option 1: Plugin Marketplace (Recommended)

Add this toolkit as a Claude Code plugin marketplace:

```
/plugin marketplace add multiplai-ai/growth-marketer-ai-toolkit
/plugin install growth-marketer-toolkit@growth-marketer-toolkit
```

Skills are then available as `/growth-marketer-toolkit:ads`, `/growth-marketer-toolkit:seo-audit`, etc.

### Option 2: Manual Copy

```bash
# Clone and copy skills to your project
git clone https://github.com/multiplai-ai/growth-marketer-ai-toolkit.git
cp -r growth-marketer-ai-toolkit/.claude/commands/* your-project/.claude/commands/
```

Skills are then available as `/ads`, `/seo-audit`, etc. (shorter names, but requires manual updates).

## What's Inside

### Skills (`.claude/commands/`)

Skills are markdown-based workflows that Claude Code executes. Invoke them with `/skill-name` in Claude Code.

#### Ads Audit System (13 skills)

Full multi-platform paid advertising audit and optimization:

| Skill | Description |
|-------|-------------|
| `/ads audit` | Full multi-platform audit with parallel analysis |
| `/ads google` | Google Ads deep analysis (Search, PMax, YouTube) |
| `/ads meta` | Meta Ads deep analysis (FB, IG, Advantage+) |
| `/ads youtube` | YouTube Ads specific analysis |
| `/ads linkedin` | LinkedIn Ads deep analysis (B2B, Lead Gen) |
| `/ads tiktok` | TikTok Ads deep analysis (Creative, Shop, Smart+) |
| `/ads microsoft` | Microsoft/Bing Ads deep analysis |
| `/ads creative` | Cross-platform creative quality audit |
| `/ads landing` | Landing page quality assessment |
| `/ads budget` | Budget allocation and bidding strategy review |
| `/ads plan <type>` | Strategic ad planning with industry templates |
| `/ads competitor` | Competitor ad intelligence analysis |

**Reference docs included:** Scoring system, benchmarks, bidding strategies, budget allocation, platform specs, conversion tracking, compliance, and platform-specific audit checklists.

**Industry templates:** SaaS, e-commerce, local service, B2B enterprise, info products, mobile app, real estate, healthcare, finance, agency.

#### Marketing (2 skills)

| Skill | Description |
|-------|-------------|
| `/seo-audit` | SEO audit with GSC/GA4 data analysis |
| `/cro-audit` | CRO audit for webpages and landing pages |

#### Growth (2 skills)

| Skill | Description |
|-------|-------------|
| `/hiring` | Growth operator hiring framework and interview rubrics |
| `/learning` | Learning opportunity identification |

#### Dev Workflow (6 skills)

Structured software development workflow:

| Skill | Description |
|-------|-------------|
| `/explore` | Understand codebase and requirements |
| `/create-plan` | Break work into phased implementation plan |
| `/execute` | Build with phase-by-phase implementation |
| `/review` | Self-check against quality checklist |
| `/peer-review` | Analyze external code review feedback |
| `/document` | Update docs and README |

#### Content (1 skill)

| Skill | Description |
|-------|-------------|
| `/writing` | Voice-driven content creation for LinkedIn |

#### Utilities (2 skills)

| Skill | Description |
|-------|-------------|
| `/prompt-optimizer` | Transform rough prompts into optimized versions |
| `/create-skill` | Create new skills with proper structure |

### Tools (`tools/`)

Python scripts for deterministic execution:

| Tool | Description |
|------|-------------|
| `llm_router.py` | Route prompts to OpenAI or Anthropic based on task type |
| `sheets_publish.py` | Publish markdown tables to Google Sheets |
| `time_comparisons.py` | MTD pacing, weekly pace, period-over-period calculations |

### Templates (`templates/`)

| Template | Description |
|----------|-------------|
| `voice-system-template.md` | Framework for creating your voice profile |
| `dev-workflow.md` | One-pager explaining the dev workflow |
| `CLAUDE.md.template` | Template for project-level Claude Code instructions |

## Quick Start

### 1. Install the toolkit

```
/plugin marketplace add multiplai-ai/growth-marketer-ai-toolkit
/plugin install growth-marketer-toolkit@growth-marketer-toolkit
```

### 2. Run a skill

```
/growth-marketer-toolkit:ads audit
```

### 3. (Optional) Install tool dependencies

If using the Python tools in `tools/`:

```bash
pip install -r tools/requirements.txt
```

Create `.env` for API access:

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_SERVICE_ACCOUNT_PATH=~/.config/google-service-account.json
GOOGLE_SHEETS_ID=your-spreadsheet-id
```

## Customization

### Voice Profile

The `/writing` skill needs your voice profile. Fill out the blank sections in `.claude/commands/content/writing.md` or use `templates/voice-system-template.md` to create a detailed profile.

### Industry Templates

The `/ads plan` skill uses industry-specific templates. Edit the templates in `.claude/commands/ads/industry-templates/` to match your business.

### CLAUDE.md

Create a `CLAUDE.md` in your project root to give Claude Code context about your project. Use `templates/CLAUDE.md.template` as a starting point.

## File Structure

```
growth-marketer-ai-toolkit/
├── README.md
├── INSTALLATION.md
├── LICENSE
├── .claude-plugin/              # Marketplace config
│   ├── plugin.json
│   └── marketplace.json
├── .claude/commands/
│   ├── ads/                      # 13 ad audit skills
│   │   ├── ads.md                # Main orchestrator
│   │   ├── ads-google.md
│   │   ├── ads-meta.md
│   │   ├── ...
│   │   ├── references/           # 12 reference docs
│   │   └── industry-templates/   # 11 industry templates
│   ├── marketing/
│   │   ├── seo-audit.md
│   │   └── cro-audit.md
│   ├── growth/
│   │   ├── hiring.md
│   │   └── learning.md
│   ├── dev-workflow/
│   │   ├── explore.md
│   │   ├── create-plan.md
│   │   ├── execute.md
│   │   ├── review.md
│   │   ├── peer-review.md
│   │   └── document.md
│   ├── content/
│   │   └── writing.md
│   └── utilities/
│       ├── prompt-optimizer.md
│       └── create-skill.md
├── tools/
│   ├── llm_router.py
│   ├── sheets_publish.py
│   ├── time_comparisons.py
│   └── requirements.txt
├── templates/
│   ├── voice-system-template.md
│   ├── dev-workflow.md
│   └── CLAUDE.md.template
└── examples/
    ├── ads-audit-example.md
    └── seo-audit-example.md
```

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- Python 3.9+ (for tools)
- API keys for OpenAI and/or Anthropic (for `llm_router.py`)
- Google service account (for `sheets_publish.py`)

## Contributing

Contributions welcome! Please:

1. Fork the repo
2. Create a feature branch
3. Submit a PR with a clear description

## License

MIT License — see [LICENSE](LICENSE)

## Author

[Hanna Huffman](https://linkedin.com/in/hannahuffman) — Growth Marketing Leader

Built with [Claude Code](https://claude.ai/code)
