# Dev Workflow: How We Build Features Together

A structured process for feature development and bug fixes using Claude Code.

---

## The Big Idea

**Think before you build. Plan before you code. Review before you ship.**

We use a 7-step workflow that forces us to slow down at the right moments. Claude acts as a "dev lead" — it plans, implements, and reviews. You guide it, verify its work, and make the final calls.

---

## Roles

| Role | Who | Responsibilities |
|------|-----|------------------|
| **Product Manager** | [Your PM] | Define requirements, answer clarifying questions, approve plans, final sign-off |
| **Engineer** | You | Run the workflow, guide Claude, verify implementations, catch issues, make technical decisions |

---

## The Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  PM provides requirement → Engineer runs workflow with Claude   │
└─────────────────────────────────────────────────────────────────┘

     /explore        →    /create-plan    →    /execute
   (understand)          (break it down)       (build it)
        │                      │                   │
        ▼                      ▼                   ▼
   "What exactly       "Here's the plan     "Phase 1 done,
    are we building?"   in 3 phases"         moving to Phase 2"
        │                      │                   │
        └──────────────────────┴───────────────────┘
                               │
                               ▼
     /review          →    /peer-review    →    /document
   (self-check)           (external check)      (update docs)
        │                      │                   │
        ▼                      ▼                   ▼
   "Found 2 issues,     "Codex flagged X,    "README updated,
    fixing now"          but it's a false     ready to merge"
                         positive because..."
```

**Side workflow (anytime):**
```
/create-issue → Quick capture bug/feature idea → Back to work
```

---

## Step-by-Step

### 1. `/explore` — Understand First

**What happens:** Claude asks clarifying questions, reads the codebase, identifies risks.

**Your job:**
- Answer Claude's questions (or loop in your PM if it's a product question)
- Verify Claude understands the requirement correctly
- Add context Claude might be missing

**Output:** `exploration.md` — summary of what we're building and what's affected

**Move on when:** Claude says "Ready to Plan: Yes" and you agree

---

### 2. `/create-plan` — Break It Down

**What happens:** Claude creates a phased implementation plan with checkboxes.

**Your job:**
- Review the plan for feasibility
- Push back if phases are too big or dependencies are wrong
- Confirm the plan makes sense before execution

**Output:** `implementation-plan.md` — phased plan with success criteria

**Move on when:** You approve the plan

---

### 3. `/execute` — Build It

**What happens:** Claude implements code, one phase at a time.

**Your job:**
- Monitor what Claude is writing
- Catch mistakes early (don't wait until review)
- Verify each phase actually works before moving on
- Flag if Claude deviates from the plan

**Output:** `phase-N-status.md` — what changed, what was tested

**Move on when:** All phases complete and verified

---

### 4. `/review` — Self-Check

**What happens:** Claude reviews its own work against a checklist.

**Your job:**
- Verify Claude's self-assessment is honest
- Check anything marked "Low confidence"
- Add issues Claude missed

**Output:** `review-report.md` — issues found, categorized by severity

**Move on when:** All critical/important issues fixed, verdict is PASS

---

### 5. `/peer-review` — External Check

**What happens:** You get a different AI (Codex, Gemini, GPT) to review. Claude then evaluates that feedback.

**Your job:**
- Get external review (paste code into another model)
- Paste feedback back to Claude
- Verify Claude's assessment of each finding (it might reject valid issues or accept bad suggestions)

**Output:** `peer-review-analysis.md` — accepted vs rejected findings with rationale

**Move on when:** All valid issues addressed

---

### 6. `/document` — Update Docs

**What happens:** Claude updates README, CLAUDE.md, API docs as needed.

**Your job:**
- Verify documentation is accurate
- Add anything Claude missed
- Confirm future sessions will have the context they need

**Output:** `doc-updates.md` — what was documented and why

**Done!**

---

### Anytime: `/create-issue` — Quick Capture

**What happens:** You notice a bug or idea mid-flow. Capture it fast, don't lose momentum.

**Your job:**
- Give a brief description
- Answer 2-3 quick questions (type, priority)
- Get back to work

**Output:** Issue in your tracking system (or formatted text to paste)

---

## Where Things Get Saved

```
projects/[project-name]/
├── .dev-workflow/
│   ├── exploration.md          ← from /explore
│   ├── implementation-plan.md  ← from /create-plan
│   ├── phase-1-status.md       ← from /execute
│   ├── phase-2-status.md
│   ├── review-report.md        ← from /review
│   ├── peer-review-analysis.md ← from /peer-review
│   └── doc-updates.md          ← from /document
└── CLAUDE.md                   ← project context
```

These artifacts persist across sessions. If we stop mid-feature, the next session picks up where we left off.

---

## Your Key Responsibilities

1. **Guide, don't dictate** — Claude proposes, you approve or redirect
2. **Verify, don't trust blindly** — Check Claude's work at each step
3. **Push back** — If a plan looks wrong or Claude is making bad decisions, say so
4. **Own the technical decisions** — Claude suggests, you decide
5. **Keep momentum** — Don't over-analyze, but don't skip steps either

---

## When to Loop In Your PM

- Requirements are unclear or conflicting
- Scope needs to change
- Tradeoffs need product input (speed vs quality, feature A vs B)
- Something is blocked on a product decision

---

## Quick Reference

| Skill | When to Use | Key Question |
|-------|-------------|--------------|
| `/explore` | Starting any new work | "Do we fully understand what we're building?" |
| `/create-plan` | After exploration | "Is this plan realistic and complete?" |
| `/execute` | After plan approved | "Is Claude following the plan?" |
| `/review` | After all phases done | "Did Claude catch its own mistakes?" |
| `/peer-review` | After self-review passes | "What did we miss?" |
| `/document` | Before merge | "Will future sessions have context?" |
| `/create-issue` | Anytime | "Capture now, solve later" |
