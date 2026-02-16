# Peer Review Command

Process feedback from external models (Codex, Gemini, GPT), verifying each finding rather than accepting blindly.

---

## Usage

```
/peer-review
```

Then paste the external model's feedback into the conversation.

---

## Prerequisites

**Load prior artifacts:**
```
Required: projects/[project-name]/.dev-workflow/review-report.md
```

Self-review should pass before requesting peer review.

---

## The Core Principle

**Dev lead verifies. External models catch blind spots but don't dictate.**

AI reviewers can:
- Surface issues you missed
- Question assumptions
- Catch common anti-patterns

But they also:
- Lack full context
- May suggest unnecessary complexity
- Can be wrong about project conventions

Your job: evaluate each finding, don't blindly accept.

---

## Execution Steps

### Step 1: Prepare Review Request

**To get external review, provide:**

1. The changed files (or diffs)
2. Brief context on what was built
3. Specific areas you want reviewed

**Example prompt for external model:**
```
Review this code for:
- Correctness and edge cases
- Security vulnerabilities
- Performance issues
- Code quality and maintainability

Context: [Brief description of what was built]

[Paste code or diffs]
```

### Step 2: Receive Feedback

Paste the external model's feedback into the conversation.

### Step 3: Parse and Evaluate

**For EACH finding in the feedback:**

1. Understand what's being suggested
2. Evaluate against the actual code and context
3. Classify the finding:

| Classification | Meaning | Action |
|----------------|---------|--------|
| **Valid issue** | Real problem that should be fixed | Add to action items |
| **False positive** | Not actually a problem | Explain why and dismiss |
| **Stylistic preference** | Matter of style, not correctness | Note but don't require |
| **Misunderstanding** | Reviewer lacks context | Explain and dismiss |
| **Already addressed** | Issue exists but already handled | Point to existing handling |

### Step 4: Generate Analysis

Create the peer review analysis document.

---

## Output Format

```markdown
# Peer Review Analysis: [Feature/Bug Name]

**Project:** [Project name]
**Date:** [YYYY-MM-DD]
**Reviewer:** [Which model - Codex, Gemini, GPT, etc.]

---

## Summary

**Total findings:** [N]
- Accepted: [N]
- Rejected: [N]
- Noted (stylistic): [N]

**Overall assessment:** [1-2 sentences]

---

## Findings Analysis

### Accepted (Valid Issues)

| # | Finding | Reason Valid | Action Required |
|---|---------|--------------|-----------------|
| 1 | [Finding summary] | [Why it's a real issue] | [What to fix] |
| 2 | [Finding summary] | [Why it's a real issue] | [What to fix] |

*If none: "All findings addressed or rejected with rationale."*

### Rejected (False Positives)

| # | Finding | Reason Rejected |
|---|---------|-----------------|
| 1 | [Finding summary] | [Why it's not actually a problem in our context] |
| 2 | [Finding summary] | [Why the reviewer misunderstood] |

*If none: "No findings rejected."*

### Noted (Stylistic Preferences)

| # | Finding | Decision |
|---|---------|----------|
| 1 | [Finding summary] | Acknowledged but not required — [reason] |

*If none: "No stylistic preferences noted."*

### Already Addressed

| # | Finding | Where Addressed |
|---|---------|-----------------|
| 1 | [Finding summary] | [Point to existing code/handling] |

---

## Action Items

Priority-ordered list of fixes from valid issues:

- [ ] **P1:** [Fix description] — `file.ts:line`
- [ ] **P2:** [Fix description] — `file.ts:line`
- [ ] **P3:** [Fix description] — `file.ts:line`

---

## Meta-Learning

**What does this feedback reveal about blind spots?**

[Reflection on what types of issues were caught, what to check more carefully next time]

Examples:
- "Multiple error handling issues caught — add to self-review checklist"
- "Reviewer caught async race condition — need to be more careful with concurrent operations"

---

## Next Steps

**If action items exist:**
1. Fix issues in priority order
2. Re-run `/review` to verify fixes
3. Consider requesting another peer review for significant fixes

**If no action items:**
1. Proceed to `/document`
2. Code is ready for merge

---

## Session Context

[Discussion of any contentious findings, rationale for rejections]
```

---

## Handoff

**Artifact saved:** `projects/[project-name]/.dev-workflow/peer-review-analysis.md`

**Next step:**
- If action items: Fix issues → `/review`
- If clean: `/document`

---

## Evaluation Framework

### When to Accept a Finding

- The issue is objectively present in the code
- Fixing it would improve correctness, security, or maintainability
- The suggested fix is appropriate (or you have a better one)

### When to Reject a Finding

- The reviewer misunderstood the requirements
- The reviewer lacks context about project conventions
- The "issue" is actually intentional design
- The fix would introduce unnecessary complexity
- The issue is theoretical but won't happen in practice

### When to Note (Stylistic)

- Valid point but matter of preference
- Would require significant refactoring for marginal benefit
- Conflicts with existing codebase style

---

## Common External Reviewer Blind Spots

**Context they lack:**
- Project-specific conventions
- Why certain patterns were chosen
- Full requirements and constraints
- What's intentionally out of scope

**Things they over-flag:**
- Missing error handling for impossible cases
- "Security issues" that are already handled elsewhere
- Performance concerns that don't matter at current scale
- Style preferences presented as issues

**Things they catch well:**
- Logic errors and edge cases
- Common security vulnerabilities
- Async/promise handling mistakes
- Missing null checks

---

## Getting Good External Reviews

**Do:**
- Provide context about what was built
- Share the plan or requirements
- Ask specific questions
- Include related code for context

**Don't:**
- Dump code without context
- Ask for "general review" without focus
- Share entire codebase (signal to noise)
- Expect them to understand project history

---

## Anti-Patterns

**DON'T:**
- Accept all feedback without evaluation
- Reject feedback defensively without genuine consideration
- Implement suggestions you don't understand
- Skip verification of "obvious" findings
- Add complexity just because reviewer suggested it

**DO:**
- Evaluate each finding independently
- Provide clear rationale for rejections
- Learn from patterns in feedback
- Push back when appropriate
- Update self-review checklist based on learnings
