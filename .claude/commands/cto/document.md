# Document Command

Update documentation after code changes to keep AI context current.

---

## Usage

```
/document
```

Run after feature is complete and reviewed. Final step in the dev workflow.

---

## Prerequisites

**Load prior artifacts:**
```
Required: projects/[project-name]/.dev-workflow/implementation-plan.md
Required: projects/[project-name]/.dev-workflow/review-report.md
Optional: projects/[project-name]/.dev-workflow/peer-review-analysis.md
```

All code should be reviewed and ready for merge.

---

## Purpose

Documentation is for future AI sessions, not just humans.

When you start a new session, you rely on:
- Project CLAUDE.md for context
- README for setup/usage
- Inline code comments for implementation details

If these are stale, future sessions waste time rediscovering what you already learned.

---

## Execution Steps

### Step 1: Identify What Changed

**From the implementation plan and phase statuses, catalog:**

1. New files created
2. Existing files significantly modified
3. New patterns introduced
4. APIs added or changed
5. Configuration changes
6. Dependencies added

### Step 2: Assess Documentation Impact

**For each change, determine:**

| Change Type | Documentation Needed |
|-------------|---------------------|
| New feature | README usage section, API docs |
| New pattern | CLAUDE.md or architecture docs |
| New dependency | README setup section |
| API change | API documentation, CLAUDE.md |
| Config change | README or setup docs |
| Internal refactor | Possibly CLAUDE.md if patterns changed |

### Step 3: Generate Updates

**For each documentation file affected:**

1. Read the current version
2. Determine what to add/change
3. Generate the specific update

### Step 4: Apply Updates

Either:
- Apply updates directly (if authorized)
- Output diffs for user to apply

### Step 5: Create Documentation Report

---

## Output Format

```markdown
# Documentation Updates: [Feature/Bug Name]

**Project:** [Project name]
**Date:** [YYYY-MM-DD]
**Changes documented:** [Brief list]

---

## Summary

[1-2 sentences on what documentation was updated and why]

---

## Files Updated

| File | Change Type | Status |
|------|-------------|--------|
| `README.md` | Added usage section | Applied / Pending |
| `CLAUDE.md` | Updated key files list | Applied / Pending |
| `docs/api.md` | Added new endpoint | Applied / Pending |

---

## Changes by File

### README.md

**Section:** [Section name]

**Addition/Change:**
```markdown
[The actual content added or changed]
```

**Reason:** [Why this documentation is needed]

---

### CLAUDE.md (or project-specific)

**Section:** [Section name]

**Addition/Change:**
```markdown
[The actual content added or changed]
```

**Reason:** [Why future sessions need this context]

---

### [Other doc files as needed]

---

## New Patterns to Document

| Pattern | Location | Description |
|---------|----------|-------------|
| [Pattern name] | `path/to/example.ts` | [What it is and when to use] |

**If new patterns warrant documentation:**
```markdown
[Suggested documentation content for each pattern]
```

---

## AI Context Updates (CLAUDE.md)

**New key files:**
- `path/to/new/file.ts` — [What it does]

**Updated constraints:**
- [Any new rules or patterns established]

**New dependencies:**
- [Package name] — [What it's used for]

---

## Verification

- [ ] README accurately describes current setup
- [ ] API docs match current implementation
- [ ] CLAUDE.md reflects current architecture
- [ ] No stale documentation that contradicts new code

---

## Session Context

[Key decisions about what to document and why]
```

---

## Handoff

**Artifact saved:** `projects/[project-name]/.dev-workflow/doc-updates.md`

**Documentation files updated:** [List of files]

**Workflow status:** Complete for this feature/bug

---

## What to Document

### README.md

**Update when:**
- New feature users need to know about
- Setup steps changed
- New environment variables
- New commands or scripts
- Changed prerequisites

**Don't update for:**
- Internal refactors
- Implementation details
- Bug fixes (unless user-facing behavior changes)

### CLAUDE.md (Project Context)

**Update when:**
- New architectural patterns established
- New key files that future sessions should know about
- Constraints or conventions changed
- New dependencies with configuration
- Gotchas or edge cases discovered

**Don't update for:**
- Temporary implementation details
- Obvious patterns
- Things already clear from code

### API Documentation

**Update when:**
- New endpoints added
- Request/response format changed
- Authentication changed
- Error handling changed

**Format:**
```markdown
### [Endpoint Name]

`[METHOD] /path/to/endpoint`

**Description:** [What it does]

**Request:**
```json
{
  "field": "type — description"
}
```

**Response:**
```json
{
  "field": "type — description"
}
```

**Errors:**
- `400`: [When this happens]
- `404`: [When this happens]
```

---

## Documentation Quality Checklist

- [ ] Accurate: Matches current implementation
- [ ] Complete: Covers what users/AI need to know
- [ ] Concise: No unnecessary detail
- [ ] Scannable: Headers, bullets, code blocks
- [ ] Actionable: Clear what to do with the information

---

## Common Documentation Mistakes

**Avoid:**
- Documenting obvious code
- Writing for a reader who has full context
- Including temporary implementation details
- Outdated examples
- Missing setup steps

**Prefer:**
- Documenting WHY not just WHAT
- Writing for future-you with no context
- Stable interfaces and patterns
- Current, tested examples
- Complete setup from scratch

---

## Anti-Patterns

**DON'T:**
- Skip documentation because "the code is clear"
- Document implementation details that will change
- Write documentation once and forget it
- Assume future readers have context
- Let CLAUDE.md become stale

**DO:**
- Document patterns and conventions
- Update docs with every significant change
- Write for someone with zero context
- Include examples that actually work
- Keep CLAUDE.md as the source of truth for AI
