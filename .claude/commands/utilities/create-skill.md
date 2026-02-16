# Create Skill Command

Invoke the skill-creator plugin to build a new Claude Code skill.

---

## Execution

Immediately invoke the skill-creator plugin:

```
Skill: document-skills:skill-creator
```

Then follow the skill-creator's 6-step process, using the supplementary guidance below.

---

## Skill Categories

Before starting, identify which category your skill fits:

| Category | Use When | Examples |
|----------|----------|----------|
| **Document & Asset Creation** | Creating consistent, high-quality output | docx, pptx, pdf, frontend-design |
| **Workflow Automation** | Multi-step processes needing consistent methodology | sprint-planning, code-review, onboarding |
| **MCP Enhancement** | Adding workflow guidance on top of MCP tool access | notion-project-setup, linear-sprint |

**MCP + Skills ("kitchen analogy"):**
- MCP = the professional kitchen (tools, ingredients, equipment)
- Skills = the recipes (step-by-step instructions on how to create value)

---

## Workflow Patterns

Choose the pattern that fits your skill:

**1. Sequential Orchestration** — Multi-step processes in specific order
```
Step 1: Create account → Step 2: Setup payment → Step 3: Create subscription
```

**2. Multi-MCP Coordination** — Workflows spanning multiple services
```
Phase 1: Export from Figma → Phase 2: Upload to Drive → Phase 3: Create Linear tasks
```

**3. Iterative Refinement** — Output improves with iteration
```
Draft → Validate → Refine → Re-validate → Finalize
```

**4. Context-Aware Selection** — Same outcome, different tools based on context
```
Large files → cloud storage | Collaborative docs → Notion | Code → GitHub
```

**5. Domain-Specific Intelligence** — Specialized knowledge beyond tool access
```
Check compliance rules → Process if passed → Log audit trail
```

---

## Testing Framework

Before packaging, create test cases:

### Triggering Tests
```
Should trigger:
- "Help me [exact phrase users would say]"
- "[Paraphrased version of request]"

Should NOT trigger:
- "[Unrelated request that sounds similar]"
- "[Request handled by different skill]"
```

### Functional Tests
- [ ] Valid outputs generated
- [ ] Scripts execute without errors
- [ ] Edge cases handled
- [ ] Error messages are helpful

### Performance Comparison
Document before/after:
- Messages needed to complete task
- Token consumption
- Failed attempts requiring retry

---

## Troubleshooting

### Skill Won't Upload
| Error | Cause | Fix |
|-------|-------|-----|
| "Could not find SKILL.md" | Wrong filename | Must be exactly `SKILL.md` (case-sensitive) |
| "Invalid frontmatter" | YAML formatting | Check `---` delimiters, closed quotes |
| "Invalid skill name" | Spaces or capitals | Use `kebab-case` only |

### Skill Doesn't Trigger
- Description too vague → Add specific trigger phrases
- Missing file types → Mention `.docx`, `.pdf`, etc. if relevant
- Debug: Ask Claude "When would you use the [skill-name] skill?"

### Skill Triggers Too Often
- Add negative triggers: "Do NOT use for [specific case]"
- Be more specific about scope
- Clarify relationship to other skills

### Instructions Not Followed
- Too verbose → Use bullets and numbered lists
- Critical steps buried → Move to top with `## Important` header
- Ambiguous → Replace "validate properly" with explicit checklist

---

## YAML Reference

**Required:**
```yaml
name: skill-name-in-kebab-case
description: What it does. Use when [specific triggers].
```

**Optional (for distribution):**
```yaml
license: MIT
compatibility: Requires Python 3.9+, network access
metadata:
  author: Your Name
  version: 1.0.0
  mcp-server: server-name
```

---

## Output Location

New skills for this repo go in: `.claude/commands/<skill-name>.md`

For distributable plugin skills, use the skill-creator's packaging workflow.
