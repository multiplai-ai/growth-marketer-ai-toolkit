---
name: build-request
description: Guide a requester through a MultiplAI workflow, feature, or bug intake and submit the approved brief to the client queue.
---

# Build Request

Read [references/intake-schema.md](references/intake-schema.md), then guide the requester through only the questions needed for a `New Workflow`, `Improvement / Feature`, or `Issue / Bug` request. Accept a rough description, transcript, or Loom link as starting context. Summarize answers in plain language and do not invent impact, access, current-state facts, reproduction results, or acceptance criteria.

Produce the canonical brief and resolve material gaps. Always show the completed brief before submission. Invocation is not authorization: ask the requester to explicitly confirm submission after reviewing the brief.

After confirmation, create a JSON payload using the field names in the reference, save it to a temporary file outside the current repository, and run:

```text
multiplai-submit-request /absolute/path/to/payload.json
```

The command requires `MULTIPLAI_WORKFLOW_REQUEST_KEY`. Never print, save, request in chat, or embed that value in the payload. If the command or key is unavailable, offer the public Notion Form instead:

`https://app.notion.com/p/its-me-hanna/ed43bf6b074240ca91ab6dc6f5daf432?pvs=106`

If neither route completes, return the brief and clearly state that no ticket was created. The downstream PDF/email is not confirmed until the ticket records `Delivery Status = Sent`.
