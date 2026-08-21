# Intake and submission schema

Collect requester name, requester email, client/company, title, request type, system, workflow/product, feature/area, why now, impact estimate, success mode, observable acceptance criteria, tools/data/access, QA owner and destination, priority, and any Loom, transcript, or supporting links.

For a **New Workflow**, also capture the current process step-by-step, desired future state, smallest useful MVP, four weekly increments, and follow-on iterations.

For an **Improvement / Feature**, capture the existing release or feature area, current versus desired behavior, what must remain unchanged, affected inputs/outputs/integrations, QA route, and release dependencies.

For an **Issue / Bug**, capture expected versus actual behavior, reproduction steps, frequency, first observed time, affected users or records, severity, evidence, workaround, correction, and regression checks.

Use `TBD — owner: [name]` for unresolved facts. Never put passwords, private keys, tokens, or unrestricted credentials in the brief.

## Canonical brief

```markdown
# [Ticket title]

**Request type:**
**System → Workflow / Product → Feature / Area:**
**Requester / client:**
**Priority / severity / target:**
**Evidence:**

## 1. What are we building or correcting?
## 2. Why and estimated impact
## 3. Success and acceptance
## 4. Current process or reproduction
## 5. Desired future state
## 6. MVP or smallest safe correction
## 7. Build plan
## 8. Data, tool, access, and QA requirements
## 9. Follow-on iterations or regression coverage
## Open items
```

## JSON payload

All fields are strings. Optional URLs may be omitted or empty.

```json
{
  "ticket": "Observable outcome or problem",
  "requestType": "New Workflow | Improvement / Feature | Issue / Bug",
  "requester": "Name",
  "requesterEmail": "name@example.com",
  "client": "Company",
  "system": "Parent system",
  "workflow": "Workflow or product",
  "feature": "Feature or area",
  "priority": "Urgent | High | Normal | Low",
  "severity": "Blocking | Major | Minor | Not Applicable",
  "impact": "Baseline, target, formula, and assumptions",
  "successMode": "Goal | Loop | Output",
  "acceptanceCriteria": "Observable pass/fail checks",
  "currentProcess": "Steps, tools, data sources, and destinations",
  "buildRequirements": "Access, data, QA owner, environment, and destinations",
  "completedBrief": "The complete rendered Markdown brief",
  "loomUrl": "https://...",
  "transcriptUrl": "https://..."
}
```
