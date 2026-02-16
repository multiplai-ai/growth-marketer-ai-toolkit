# Installation Guide

This guide walks you through setting up the Growth Marketer AI Toolkit in your project.

## Prerequisites

### Required

- **Claude Code CLI** — Install from [claude.ai/code](https://claude.ai/code)
- **Git** — For cloning and version control

### Optional (for tools)

- **Python 3.9+** — Required for Python tools
- **OpenAI API key** — For `llm_router.py` (OpenAI models)
- **Anthropic API key** — For `llm_router.py` (Claude models)
- **Google Cloud service account** — For `sheets_publish.py`

## Installation Methods

### Method 1: Copy Individual Skills (Recommended)

Copy only the skills you need:

```bash
# Create .claude/commands directory in your project
mkdir -p your-project/.claude/commands

# Copy ads audit system
cp -r growth-marketer-ai-toolkit/.claude/commands/ads your-project/.claude/commands/

# Copy other skills as needed
cp growth-marketer-ai-toolkit/.claude/commands/marketing/seo-audit.md your-project/.claude/commands/
cp growth-marketer-ai-toolkit/.claude/commands/utilities/prompt-optimizer.md your-project/.claude/commands/
```

### Method 2: Clone Entire Repo

Use this if you want all skills and tools:

```bash
git clone https://github.com/YOUR_USERNAME/growth-marketer-ai-toolkit.git
cd growth-marketer-ai-toolkit
```

### Method 3: Use as Submodule

Add to an existing project as a git submodule:

```bash
git submodule add https://github.com/YOUR_USERNAME/growth-marketer-ai-toolkit.git .skills
```

## Configuration

### 1. Environment Variables

If using the Python tools, create a `.env` file in your project root:

```bash
# LLM Router (pick one or both)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# Google Sheets Publisher
GOOGLE_SERVICE_ACCOUNT_PATH=~/.config/google-service-account.json
GOOGLE_SHEETS_ID=your-spreadsheet-id
```

### 2. Python Dependencies

Install required packages:

```bash
pip install -r tools/requirements.txt
```

Or install individually:

```bash
# For llm_router.py
pip install openai anthropic

# For sheets_publish.py
pip install gspread google-auth

# For time_comparisons.py
pip install pandas numpy
```

### 3. Google Sheets Setup (if using sheets_publish.py)

1. Create a Google Cloud project
2. Enable Google Sheets API
3. Create a service account and download JSON key
4. Share your target spreadsheet with the service account email
5. Set `GOOGLE_SERVICE_ACCOUNT_PATH` to the JSON key location
6. Set `GOOGLE_SHEETS_ID` to your spreadsheet ID (from the URL)

### 4. LLM Router Configuration (if using llm_router.py)

Create `config/model-routing-config.json`:

```json
{
  "default_model": "claude",
  "models": {
    "claude": {
      "provider": "anthropic",
      "api_model_id": "claude-sonnet-4-20250514",
      "max_tokens": 4096,
      "temperature": 0.7
    },
    "gpt-4": {
      "provider": "openai",
      "api_model_id": "gpt-4",
      "max_tokens": 4096,
      "temperature": 0.7
    }
  },
  "task_routing": {
    "insight_generation": {"model": "claude", "provider": "anthropic"},
    "narrative_writing": {"model": "claude", "provider": "anthropic"},
    "code_generation": {"model": "gpt-4", "provider": "openai"}
  }
}
```

## Customization

### Adding Your Voice Profile

1. Open `.claude/commands/content/writing.md`
2. Fill in the "Your Voice Profile" section with your characteristics
3. Optionally, use `templates/voice-system-template.md` for a detailed analysis framework

### Creating Your CLAUDE.md

1. Copy `templates/CLAUDE.md.template` to your project root as `CLAUDE.md`
2. Fill in your specific information
3. Claude Code will read this file for project context

### Modifying Industry Templates

The ads planning skill uses industry-specific templates. To customize:

1. Navigate to `.claude/commands/ads/industry-templates/`
2. Edit the relevant template (e.g., `saas.md`, `ecommerce.md`)
3. Add your industry-specific recommendations and benchmarks

## Verifying Installation

### Test Skills

```bash
# Start Claude Code
claude

# Test a skill (won't run full audit, just loads the skill)
/ads

# You should see the skill loaded with available commands
```

### Test Tools

```bash
# Test LLM router
python tools/llm_router.py --test

# Test Google Sheets connection
python tools/sheets_publish.py --test
```

## Troubleshooting

### "Skill not found"

- Verify `.claude/commands/` directory exists
- Check file permissions
- Restart Claude Code

### "API key not found"

- Verify `.env` file exists in project root
- Check environment variable names match exactly
- Restart your terminal/shell

### "Google Sheets connection failed"

- Verify service account JSON exists at specified path
- Check spreadsheet is shared with service account email
- Verify spreadsheet ID is correct

### Python import errors

- Run `pip install -r tools/requirements.txt`
- Verify Python version is 3.9+

## Updating

### If using git clone

```bash
cd growth-marketer-ai-toolkit
git pull origin main
```

### If using submodule

```bash
git submodule update --remote
```

## Uninstalling

Simply remove the copied files:

```bash
rm -rf .claude/commands/ads
rm -rf tools/
```

## Support

- **Issues:** [GitHub Issues](https://github.com/YOUR_USERNAME/growth-marketer-ai-toolkit/issues)
- **Discussions:** [GitHub Discussions](https://github.com/YOUR_USERNAME/growth-marketer-ai-toolkit/discussions)
