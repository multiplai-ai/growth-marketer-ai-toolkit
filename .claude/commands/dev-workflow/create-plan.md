# Create Plan Command

Generate a phased markdown implementation plan with status tracking.

---

## Usage

```
/create-plan
```

Run after `/explore` is complete. The plan becomes the contract for implementation.

---

## Prerequisites

**Load prior artifacts:**
```
Required: projects/[project-name]/.dev-workflow/exploration.md
```

If exploration doesn't exist or is incomplete, redirect to `/explore` first.

---

## Execution Steps

### Step 1: Load Context

1. Read `exploration.md` from the project's `.dev-workflow/` directory
2. Confirm the exploration is marked "Ready to Plan: Yes"
3. If not ready, ask user to resolve open questions first

### Step 2: Design Phases

**Break work into logical phases with sequential dependencies:**

- Each phase should be independently testable
- Phases build on each other (phase 2 requires phase 1 complete)
- Keep phases small enough to complete in one session
- Include clear success criteria per phase

**Good phase breakdown:**
- Phase 1: Data layer / models
- Phase 2: API / service layer
- Phase 3: UI components
- Phase 4: Integration / wiring
- Phase 5: Testing / polish

### Step 3: Define Success Criteria

**For each phase, specify:**
- What files will be created/modified
- What behavior should work when complete
- How to verify (manual test, unit test, etc.)

### Step 4: Risk Mitigation

**Include:**
- Rollback strategy (how to undo if things break)
- Test plan (how to verify the whole thing works)
- Dependencies between phases

### Step 5: Generate Plan

Create the implementation plan document.

---

## Output Format

```markdown
# [Feature/Bug Name] - Implementation Plan

**Project:** [Project name]
**Date:** [YYYY-MM-DD]
**Status:** Ready for Execution

---

## Summary

[1-2 sentences describing what this plan accomplishes]

---

## Critical Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| [Decision 1] | [What we chose] | [Why] |
| [Decision 2] | [What we chose] | [Why] |

---

## Phases

### Phase 1: [Name]

- [ ] **Status:** Not started
- **Goal:** [What this achieves]
- **Files:** `file1.ts`, `file2.ts`
- **Changes:**
  - [Specific change 1]
  - [Specific change 2]
- **Success criteria:** [How to verify this phase is complete]
- **Complexity:** Low / Medium / High

### Phase 2: [Name]

- [ ] **Status:** Not started
- **Goal:** [What this achieves]
- **Files:** `file1.ts`, `file2.ts`
- **Changes:**
  - [Specific change 1]
  - [Specific change 2]
- **Success criteria:** [How to verify]
- **Complexity:** Low / Medium / High
- **Depends on:** Phase 1

### Phase 3: [Name]
...

---

## Rollback Plan

**If something breaks:**

1. [Step to revert phase N]
2. [Step to restore previous state]
3. [How to verify rollback succeeded]

**Commit strategy:** [Commit after each phase / commit at end / etc.]

---

## Test Plan

**Unit tests:**
- [ ] [Test case 1]
- [ ] [Test case 2]

**Integration tests:**
- [ ] [Test case 1]

**Manual verification:**
- [ ] [Manual check 1]
- [ ] [Manual check 2]

---

## Open Items

[Any items discovered during planning that need follow-up]

---

## Session Context

[Key decisions made, alternatives considered, constraints applied]
```

---

## Handoff

**Artifact saved:** `projects/[project-name]/.dev-workflow/implementation-plan.md`

**Next step:** Run `/execute` to begin Phase 1

**Key principle:** The plan is the contract. Changes require explicit re-planning.

---

## Planning Principles

### Phase Design

- **Atomic:** Each phase delivers working code
- **Testable:** Clear verification method per phase
- **Sequential:** Later phases depend on earlier ones
- **Sized right:** Completable in one session

### Complexity Estimates

- **Low:** Straightforward change, clear pattern exists
- **Medium:** Some ambiguity, may require exploration
- **High:** Significant complexity, unknown edge cases

### When to Re-Plan

- Requirements change mid-implementation
- Discovery during `/execute` reveals new complexity
- Phase 1 takes significantly longer than expected
- User requests scope change

---

## Anti-Patterns

**DON'T:**
- Create single-phase plans (break it down)
- Skip success criteria (how will you know it works?)
- Ignore rollback (what if it breaks?)
- Plan without completed exploration
- Over-plan (keep phases actionable, not exhaustive)

**DO:**
- Reference exploration findings
- Include all affected files per phase
- Define clear success criteria
- Keep phases independently verifiable
- Document critical decisions with rationale
