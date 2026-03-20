# Growth Marketer AI Toolkit

A modular collection of Claude Code skills for growth marketers. 65 skills across 6 components — use them all or pick the components you need.

## Installation

### Full Toolkit

```bash
git clone https://github.com/multiplai-ai/growth-marketer-ai-toolkit.git
cp -r growth-marketer-ai-toolkit/.claude/commands/* your-project/.claude/commands/
```

### Single Component

Only want ads? Or just the strategy suite? Copy individual directories:

```bash
# Just the ads audit system
cp -r growth-marketer-ai-toolkit/.claude/commands/ads your-project/.claude/commands/

# Just the strategy suite
cp -r growth-marketer-ai-toolkit/.claude/commands/strategy your-project/.claude/commands/

# Mix and match
cp -r growth-marketer-ai-toolkit/.claude/commands/content your-project/.claude/commands/
cp -r growth-marketer-ai-toolkit/.claude/commands/cto your-project/.claude/commands/
```

Skills are available as `/component:skill-name` in Claude Code (e.g., `/ads:ads-google`, `/strategy:positioning-strategy`).

## Components

### 1. Strategy Suite (8 skills)

Full marketing strategy pipeline — from discovery through design systems.

| Skill | What it does |
|-------|-------------|
| `/strategy:discovery-intake` | Structured discovery and client intake process |
| `/strategy:positioning-strategy` | Competitive positioning and market differentiation |
| `/strategy:brand-strategy` | Brand voice, key messages, value props, proof points, USPs |
| `/strategy:icp-personas` | Ideal customer profiles and buyer personas |
| `/strategy:content-strategy` | Content pillars, formats, cadence, distribution plan |
| `/strategy:design-systems` | Design system creation and documentation |
| `/strategy:design-extract` | Reverse-engineer design tokens from a live URL |
| `/strategy:strategy-suite-sop` | How the strategy suite works (start here) |

**Best for:** Starting a new brand, onboarding a client, building a strategy foundation.

### 2. Content Production (9 skills)

Write, plan, produce, and QC content at scale.

| Skill | What it does |
|-------|-------------|
| `/content:writing` | Voice-driven long-form and social content creation |
| `/content:content-brief` | Structured content briefs from strategy inputs |
| `/content:content-calendar` | Monthly content calendar with cadence and themes |
| `/content:content-campaign` | Multi-channel campaign planning and execution |
| `/content:produce` | End-to-end content production pipeline |
| `/content:cro` | CRO audit for webpages and landing pages |
| `/content:seo-qc` | SEO/AEO quality check for draft articles |
| `/content:visual-content` | Generate shareable infographics, diagrams, frameworks |
| `/content:ai-tool-review` | Product-review style AI tool evaluation articles |

**Best for:** Content teams, solo marketers scaling output, agency content ops.

### 3. Ads Audit System (13 skills)

Full multi-platform paid advertising audit and optimization.

| Skill | What it does |
|-------|-------------|
| `/ads:ads` | Full multi-platform audit with parallel analysis |
| `/ads:ads-google` | Google Ads deep analysis (Search, PMax, YouTube) |
| `/ads:ads-meta` | Meta Ads deep analysis (FB, IG, Advantage+) |
| `/ads:ads-youtube` | YouTube Ads specific analysis |
| `/ads:ads-linkedin` | LinkedIn Ads deep analysis (B2B, Lead Gen) |
| `/ads:ads-tiktok` | TikTok Ads deep analysis (Creative, Shop, Smart+) |
| `/ads:ads-microsoft` | Microsoft/Bing Ads deep analysis |
| `/ads:ads-creative` | Cross-platform creative quality audit |
| `/ads:ads-landing` | Landing page quality assessment |
| `/ads:ads-budget` | Budget allocation and bidding strategy review |
| `/ads:ads-plan` | Strategic ad planning with industry templates |
| `/ads:ads-competitor` | Competitor ad intelligence analysis |
| `/ads:ads-audit` | Full account audit with health scoring |

**Included:** 12 reference docs (scoring, benchmarks, bidding strategies, platform specs, compliance) + 11 industry templates (SaaS, e-commerce, B2B enterprise, healthcare, finance, agency, and more).

**Best for:** PPC managers, agencies running audits, anyone managing ad spend.

### 4. Distribution (1 skill)

| Skill | What it does |
|-------|-------------|
| `/distribution:seo` | SEO audit with GSC/GA4 data analysis |

### 5. Ops (5 skills)

Marketing operations and utility workflows.

| Skill | What it does |
|-------|-------------|
| `/ops:growth-operator-hiring` | Growth operator hiring framework and interview rubrics |
| `/ops:scrape-website` | Scrape blog index pages to markdown for analysis |
| `/ops:to-gamma` | Export content to Gamma presentations |
| `/ops:to-sheets` | Export data to Google Sheets |
| `/ops:to-notion` | Export content to Notion |

**Best for:** Hiring growth roles, moving content between platforms.

### 6. CTO / Dev Workflow (6 skills)

Structured development lifecycle for building marketing tools and automations.

| Skill | What it does |
|-------|-------------|
| `/cto:explore` | Understand codebase and requirements |
| `/cto:build-workflow` | Create new skills, agents, or hybrid workflows |
| `/cto:dev-process` | Full dev lifecycle orchestrator |
| `/cto:document` | Generate and update documentation |
| `/cto:learning-opportunity` | Turn problems into structured learning |
| `/cto:prompt-optimizer` | Transform rough prompts into optimized versions |

**Best for:** Marketers building their own tools, prompt engineering, automation development.

## Quick Start

1. **Copy the skills** you want into your project's `.claude/commands/` directory
2. **Run a skill** in Claude Code: `/ads:ads-google`, `/strategy:discovery-intake`, etc.
3. **Customize** — skills reference generic paths like `strategy/`, `content/`, `voice-synthesis.md`. Create these in your project to match your brand.

### Customization Tips

- **Voice profile:** The `/content:writing` skill works best with a `voice-synthesis.md` file describing your brand's tone and style. Use `templates/voice-system-template.md` to create one.
- **Strategy inputs:** Content skills reference strategy outputs (positioning, brand strategy, ICP). Run the strategy suite first, or point the skills at your existing strategy docs.
- **Industry templates:** Edit `ads/industry-templates/` to match your business vertical.

## Tools (`tools/`)

Python scripts for deterministic execution:

| Tool | Description |
|------|-------------|
| `llm_router.py` | Route prompts to OpenAI or Anthropic based on task type |
| `sheets_publish.py` | Publish markdown tables to Google Sheets |
| `time_comparisons.py` | MTD pacing, weekly pace, period-over-period calculations |

```bash
pip install -r tools/requirements.txt
```

## File Structure

```
growth-marketer-ai-toolkit/
├── .claude/commands/
│   ├── strategy/              # 8 strategy skills
│   ├── content/               # 9 content production skills
│   ├── ads/                   # 13 ad audit skills
│   │   ├── references/        #   12 reference docs
│   │   └── industry-templates/#   11 industry templates
│   ├── distribution/          # 1 SEO skill
│   ├── ops/                   # 5 operations skills
│   └── cto/                   # 6 dev workflow skills
├── tools/                     # Python utilities
├── templates/                 # Starter templates
└── examples/                  # Example outputs
```

## Changelog

### v2.0.0 (2026-03-20)
- Reorganized into 6 modular components (strategy, content, ads, distribution, ops, cto)
- Added strategy suite: discovery, positioning, brand strategy, ICP, content strategy, design systems, design extract
- Added content production: writing, briefs, calendars, campaigns, produce, CRO, SEO QC, visual content, AI tool reviews
- Added ops: hiring, scrape, export utilities (Gamma, Sheets, Notion)
- Updated CTO skills: build-workflow, dev-process, prompt-optimizer
- Updated all ads skills to latest versions
- 65 total skill files (up from 27 in v1.0)

### v1.0.0 (2026-02-16)
- Initial public release
- 13 ad audit skills, SEO/CRO, dev workflow, content writing, utilities

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- Python 3.9+ (for tools)

## Contributing

Contributions welcome! Fork, branch, PR.

## License

MIT License — see [LICENSE](LICENSE)

## Author

[Hanna Huffman](https://linkedin.com/in/hannahuffman) — Founder, MultiplAI Growth Systems

Built with [Claude Code](https://claude.ai/code)
