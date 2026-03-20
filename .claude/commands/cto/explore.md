# Explore Command

Fully understand a problem before writing any code. This is the checkpoint that prevents wasted work.

---

## Usage

```
/explore
```

Run this before any implementation. Think first, build second.

---

## Execution Steps

### Step 1: Context Gathering

**Check for existing workflow artifacts:**
```
Look for: projects/[project-name]/.dev-workflow/
If exists: Load prior artifacts, show "Resuming from: [last artifact]"
If not: Create directory structure
```

**Load project context:**
- Read project `CLAUDE.md` if it exists
- Identify tech stack, constraints, key files

### Step 2: Requirements Clarification

**Ask clarifying questions until requirements are unambiguous.**

Good questions to ask:
- What specific behavior are we changing?
- What should happen in edge cases?
- Are there existing patterns we should follow?
- What's the scope boundary — what's NOT included?
- Who are the stakeholders for this change?

**Continue asking until you can explain the requirement back clearly.**

### Step 3: Codebase Discovery

**Read relevant areas:**
- Files that will be affected
- Similar existing implementations
- Related tests
- Dependencies that might be impacted

**Use the Explore agent or Glob/Grep tools to:**
- Find files matching patterns
- Search for related code
- Understand existing architecture

### Step 4: Risk Assessment

**Identify:**
- Files that need modification
- Existing patterns to follow or break from
- Dependencies and potential breakage points
- Unknown areas needing more research
- Questions requiring human input

### Step 5: Confirmation

**Generate exploration summary and confirm understanding before proceeding.**

---

## Output Format

```markdown
# Exploration: [Feature/Bug Name]

**Project:** [Project name]
**Date:** [YYYY-MM-DD]
**Status:** Complete / Needs Clarification

---

## Understanding

[What we're building/fixing in plain language — 2-3 sentences]

---

## Affected Areas

| File/Module | Why Affected | Change Type |
|-------------|--------------|-------------|
| `path/to/file.ts` | [Reason] | Modify / Create / Delete |

---

## Existing Patterns

[How similar things are done in this codebase]

- **Pattern 1:** [Description + example location]
- **Pattern 2:** [Description + example location]

---

## Dependencies & Risks

| Dependency | Risk Level | What Could Break |
|------------|------------|------------------|
| [Component/Service] | High/Med/Low | [Consequence] |

---

## Open Questions

1. [Question needing human input]
2. [Question needing human input]

---

## Ready to Plan?

[ ] Yes — requirements clear, ready for `/create-plan`
[ ] No — need answers to open questions first

---

## Session Context

[Key discussion points, constraints identified, decisions made]
```

---

## Handoff

**Artifact saved:** `projects/[project-name]/.dev-workflow/exploration.md`

**Next step:** Run `/create-plan` when ready

**Key principle:** No planning until exploration is complete. Ask questions, don't assume.

---

## When to Use

- Starting a new feature
- Investigating a bug before fixing
- Any work that touches multiple files
- When requirements feel ambiguous
- Before writing any implementation code

---

## Anti-Patterns

**DON'T:**
- Skip exploration for "simple" changes (they rarely are)
- Start coding before confirming understanding
- Assume you know what the user wants
- Ignore existing patterns in the codebase
- Proceed with unanswered critical questions

**DO:**
- Ask clarifying questions aggressively
- Read existing code before proposing changes
- Surface risks early
- Confirm understanding explicitly
- Document decisions made during exploration
