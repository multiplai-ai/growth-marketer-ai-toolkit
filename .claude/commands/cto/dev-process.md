---
name: dev-process
description: Development lifecycle orchestrator — maps stages to superpowers. Start here for any dev work.
---

# Dev Process — Lifecycle Orchestrator

You are the entry point for all development work. Your job is to determine what stage of development the user is at and invoke the right superpower.

## The Development Lifecycle

```
┌─────────────┐     ┌──────────┐     ┌─────────────┐
│ 1. Understand│ ──▶ │ 2. Plan  │ ──▶ │ 3. Implement│
└─────────────┘     └──────────┘     └─────────────┘
                                            │
                                            ▼
┌─────────────┐     ┌──────────┐     ┌─────────────┐
│  6. Ship    │ ◀── │ 5. Review│ ◀── │  4. Debug   │
└─────────────┘     └──────────┘     └─────────────┘
```

## Stage Detection & Routing

Analyze the user's request and current context to determine the stage:

### Stage 1: Understand (Creative / Research)
**Signals:** "build", "create", "add feature", "new", "I want to...", or any creative work
**Action:** Invoke `superpowers:brainstorming`
**Why:** Prevents jumping to code before understanding the problem space

### Stage 2: Plan (Design / Architecture)
**Signals:** "implement", brainstorming just completed, spec exists, requirements are clear
**Action:** Invoke `superpowers:writing-plans`
**Why:** Creates bite-sized implementation plan with exact file paths and test design

### Stage 3: Implement (Build / Execute)
**Signals:** Plan exists, ready to code, "execute the plan", "let's build"
**Action:** Choose based on context:
- **Multiple independent tasks?** → Invoke `superpowers:subagent-driven-development`
- **Sequential plan execution?** → Invoke `superpowers:executing-plans`
- **Writing code?** → Invoke `superpowers:test-driven-development` (TDD for each unit)

### Stage 4: Debug (Fix / Investigate)
**Signals:** "bug", "broken", "failing", "error", "not working", test failures
**Action:** Invoke `superpowers:systematic-debugging`
**Why:** Prevents guess-and-check. Forces hypothesis → evidence → fix cycle.

### Stage 5: Review (Validate / QA)
**Signals:** Implementation complete, "I'm done", "ready to review", tests passing
**Action:** Invoke `superpowers:verification-before-completion` first, then `superpowers:requesting-code-review`
**Why:** Verification catches things you missed. Code review catches things verification missed.

### Stage 6: Ship (Integrate / Merge)
**Signals:** Review approved, "ready to merge", "ship it", all checks pass
**Action:** Invoke `superpowers:finishing-a-development-branch`
**Why:** Handles the merge strategy decision (squash, rebase, merge commit)

## How to Use This Skill

1. **Read the user's request**
2. **Identify the stage** using signals above
3. **Announce:** "This is a Stage N ([name]) task. Invoking [superpower]."
4. **Invoke the superpower** using the Skill tool
5. **Follow the superpower's instructions exactly**

If the stage is ambiguous, ask: "Are we starting fresh (understand), or do you already have a plan (implement)?"

## Quick Reference

| Stage | Superpower | One-liner |
|-------|-----------|-----------|
| Understand | `brainstorming` | Define the problem before solving it |
| Plan | `writing-plans` | Design the solution before building it |
| Implement | `executing-plans` / `subagent-driven-development` / `test-driven-development` | Build it right |
| Debug | `systematic-debugging` | Find the root cause, not the symptom |
| Review | `verification-before-completion` → `requesting-code-review` | Prove it works |
| Ship | `finishing-a-development-branch` | Integrate cleanly |
