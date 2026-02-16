# Execute Command

Execute a specific phase from the implementation plan. Claude writes the code directly.

---

## Usage

```
/execute [phase-number]
```

**Examples:**
```
/execute 1        # Execute Phase 1
/execute next     # Execute the next incomplete phase
/execute          # Resume from last incomplete phase
```

---

## Prerequisites

**Load prior artifacts:**
```
Required: projects/[project-name]/.dev-workflow/implementation-plan.md
Optional: projects/[project-name]/.dev-workflow/phase-*-status.md (prior phases)
```

If no plan exists, redirect to `/create-plan` first.

---

## Execution Steps

### Step 1: Load Context

1. Read `implementation-plan.md` from the project's `.dev-workflow/` directory
2. Read any existing `phase-N-status.md` files to understand prior progress
3. Determine which phase to execute:
   - If phase specified: use that phase
   - If "next": find first incomplete phase
   - If none specified: resume from last incomplete

### Step 2: Confirm Phase

**Before starting, confirm:**
```
## Executing Phase [N]: [Name]

**Goal:** [Phase goal from plan]
**Files:** [Files to modify]
**Success criteria:** [How to verify]

Ready to proceed? [Confirm or identify blockers]
```

### Step 3: Implementation

**Follow the plan exactly:**

1. Make the code changes specified in the phase
2. Follow existing patterns identified during exploration
3. Run tests if applicable
4. Verify success criteria are met

**During implementation:**
- Stay within phase scope — don't do work from later phases
- If you discover the plan needs adjustment, stop and discuss
- Track any deviations for the status report

### Step 4: Update Plan Status

After completing the phase, update the plan file:
- Mark the phase checkbox as complete: `- [x] **Status:** Complete`
- Keep the plan as the single source of truth

### Step 5: Generate Status Report

Create a status report documenting what was done.

---

## Output Format

```markdown
# Phase [N] Status: [Name]

**Project:** [Project name]
**Date:** [YYYY-MM-DD]
**Status:** Complete / Blocked / Partial

---

## Changes Made

| File | Change | Lines |
|------|--------|-------|
| `path/to/file.ts` | [What changed] | ~X |
| `path/to/file2.ts` | [What changed] | ~X |

---

## Implementation Details

[Brief description of how the changes were implemented]

### Key decisions during implementation:
- [Decision 1]: [Why]
- [Decision 2]: [Why]

---

## Tests

| Test | Status | Notes |
|------|--------|-------|
| [Test name/type] | Pass/Fail/Skipped | [Notes] |

---

## Verification

**Success criteria from plan:**
> [Quote the success criteria]

**Verification result:**
- [ ] Criteria met
- [How it was verified]

---

## Deviations from Plan

| Deviation | Reason | Impact |
|-----------|--------|--------|
| [What differed] | [Why] | [Effect on later phases] |

*If no deviations: "None — implemented as planned"*

---

## Potential Concerns

- [Anything that might cause issues later]
- [Edge cases noticed but not addressed]

---

## Confidence Level

**[High / Medium / Low]**

Rationale: [Why this confidence level]

---

## Next Steps

**Phase complete?** [Yes / No - blocked on X]

**Next action:**
- [ ] Execute Phase [N+1]: `/execute next`
- [ ] Or if all phases complete: `/review`

---

## Session Context

[Key discussion points, problems solved, alternatives tried]
```

---

## Handoff

**Artifact saved:** `projects/[project-name]/.dev-workflow/phase-[N]-status.md`

**Plan updated:** `implementation-plan.md` checkbox marked complete

**Next step:**
- More phases remaining: `/execute next`
- All phases complete: `/review`

---

## Execution Principles

### Stay In Scope

- Only implement what the current phase specifies
- Don't "quickly fix" things in other areas
- Don't refactor adjacent code
- If scope creep is needed, update the plan first

### Follow the Plan

- The plan is the contract
- Deviations require explicit acknowledgment
- If the plan is wrong, discuss before changing

### Report Honestly

- Don't hide problems encountered
- Note concerns even if they seem minor
- Low confidence is useful information

### Test Incrementally

- Verify each phase works before proceeding
- Don't assume — actually test
- Document how you verified

---

## Handling Blockers

**If blocked during execution:**

1. Stop implementation
2. Document what's blocking progress
3. Update status as "Blocked"
4. Ask for input or redirect to investigation

**Common blockers:**
- Missing dependency not in plan
- Discovered complexity requiring re-planning
- External blocker (API, permissions, etc.)
- Ambiguous requirement needing clarification

---

## Anti-Patterns

**DON'T:**
- Execute without reading the plan first
- Skip phases or do them out of order
- Make changes beyond phase scope
- Mark complete without verifying success criteria
- Hide deviations or concerns
- Assume tests pass without running them

**DO:**
- Confirm phase before starting
- Follow plan exactly (or discuss changes)
- Update plan status after completion
- Document everything in status report
- Be honest about confidence level
- Stop at blockers, don't work around silently
