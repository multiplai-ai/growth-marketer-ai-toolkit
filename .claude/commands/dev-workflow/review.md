# Review Command

Comprehensive self-review of completed work before peer review.

---

## Usage

```
/review
```

Run after all implementation phases are complete, before `/peer-review`.

---

## Prerequisites

**Load prior artifacts:**
```
Required: projects/[project-name]/.dev-workflow/implementation-plan.md
Required: projects/[project-name]/.dev-workflow/phase-*-status.md (at least one)
```

All phases should be marked complete in the plan.

---

## Execution Steps

### Step 1: Load Context

1. Read `implementation-plan.md` to understand what was built
2. Read all `phase-N-status.md` files to understand what changed
3. Confirm all phases are marked complete
4. If phases remain incomplete, redirect to `/execute` first

### Step 2: Review Changed Files

**For each file modified across all phases:**

1. Read the current state of the file
2. Review against the plan requirements
3. Check for common issues (see checklist below)

### Step 3: Systematic Review

**Check for each category:**

**Correctness:**
- Does the code do what the plan specified?
- Are edge cases handled?
- Is error handling appropriate?

**Quality:**
- Does it follow existing patterns?
- Is the code readable and maintainable?
- Are there unnecessary complications?

**Safety:**
- Any security vulnerabilities?
- Any potential for data loss?
- Any breaking changes to existing functionality?

**Completeness:**
- All plan requirements met?
- Tests added/updated as needed?
- No TODO comments left unaddressed?

### Step 4: Categorize Findings

**Severity levels:**

- **Critical:** Must fix before merge. Security issues, broken functionality, data loss risk.
- **Important:** Should fix. Code quality issues, missing error handling, incomplete implementation.
- **Minor:** Nice to fix. Style issues, optimization opportunities, minor improvements.

### Step 5: Generate Review Report

---

## Output Format

```markdown
# Self-Review: [Feature/Bug Name]

**Project:** [Project name]
**Date:** [YYYY-MM-DD]
**Phases reviewed:** [1, 2, 3, ...]

---

## Summary

[1-2 sentences on overall quality and readiness]

---

## Files Reviewed

| File | Lines Changed | Review Status |
|------|---------------|---------------|
| `path/to/file.ts` | ~X | Clean / Has Issues |

---

## Issues Found

### Critical (must fix before merge)

| # | Issue | Location | Suggested Fix |
|---|-------|----------|---------------|
| 1 | [Issue description] | `file.ts:42` | [How to fix] |

*If none: "No critical issues found."*

### Important (should fix)

| # | Issue | Location | Suggested Fix |
|---|-------|----------|---------------|
| 1 | [Issue description] | `file.ts:55` | [How to fix] |

*If none: "No important issues found."*

### Minor (nice to fix)

| # | Issue | Location | Suggested Fix |
|---|-------|----------|---------------|
| 1 | [Issue description] | `file.ts:78` | [How to fix] |

*If none: "No minor issues found."*

---

## Requirements Checklist

- [ ] All plan requirements implemented
- [ ] Tests pass
- [ ] No regressions in existing functionality
- [ ] Code follows project patterns
- [ ] Error handling is appropriate
- [ ] No security vulnerabilities
- [ ] No hardcoded secrets or credentials
- [ ] No console.logs or debug code left in

---

## Test Coverage

| Test Type | Status | Notes |
|-----------|--------|-------|
| Unit tests | Pass/Fail/None | [Notes] |
| Integration tests | Pass/Fail/None | [Notes] |
| Manual testing | Done/Not done | [Notes] |

---

## Potential Risks

[Things that might cause issues in production or for future development]

- [Risk 1]: [Why it's a risk]
- [Risk 2]: [Why it's a risk]

*If none: "No significant risks identified."*

---

## Verdict

**[ ] PASS** — Ready for peer review
**[ ] NEEDS FIXES** — Address critical/important issues first

### If needs fixes:
Priority order for fixes:
1. [Most important fix]
2. [Second most important]
3. ...

---

## Session Context

[Key observations, patterns noticed, areas of uncertainty]
```

---

## Handoff

**Artifact saved:** `projects/[project-name]/.dev-workflow/review-report.md`

**Next step:**
- If PASS: `/peer-review` (get external review)
- If NEEDS FIXES: Address issues, then re-run `/review`

---

## Review Checklist Details

### Correctness

- [ ] Code matches plan specifications
- [ ] Edge cases handled (null, empty, boundary conditions)
- [ ] Error conditions handled gracefully
- [ ] Async operations handled correctly
- [ ] State management is consistent

### Security

- [ ] No hardcoded credentials or secrets
- [ ] User input is validated/sanitized
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] Authentication/authorization checks in place
- [ ] Sensitive data handled appropriately

### Performance

- [ ] No obvious N+1 queries
- [ ] No unnecessary re-renders (React)
- [ ] Large data sets handled efficiently
- [ ] No blocking operations in hot paths

### Maintainability

- [ ] Code is readable without excessive comments
- [ ] Follows existing patterns in codebase
- [ ] No code duplication
- [ ] Functions/components appropriately sized
- [ ] Naming is clear and consistent

### Testing

- [ ] Critical paths have test coverage
- [ ] Edge cases tested
- [ ] Error conditions tested
- [ ] Tests are meaningful (not just coverage farming)

---

## Self-Review Mindset

**Be hard on your own code.**

- Assume there are bugs — look for them
- Question every decision — is this the best approach?
- Think like an attacker — where could this break?
- Think like future-you — will this be maintainable?

The goal is to find issues before peer review does. A clean peer review is the sign of good self-review.

---

## Anti-Patterns

**DON'T:**
- Rubber-stamp your own work
- Skip the checklist
- Ignore "minor" issues (they accumulate)
- Review without reading the actual code
- Mark PASS when you have doubts

**DO:**
- Actually read every changed file
- Run through the full checklist
- Be honest about issues found
- Prioritize fixes clearly
- Note areas of uncertainty
