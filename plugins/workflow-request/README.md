# MultiplAI Workflow Request for Claude Code

This plugin adds `/workflow-request:build-request` and `/workflow-request:create-ticket`, guided intakes for new workflows, improvements, and issues. Approved requests are submitted to MultiplAI's queue; the public Notion Form remains the fallback when API submission is unavailable.

## Install

In Claude Code, run:

```text
/plugin marketplace add multiplai-ai/growth-marketer-ai-toolkit
/plugin install workflow-request@growth-marketer-toolkit
```

Set the client-specific key provided by MultiplAI in your shell or secrets manager as `MULTIPLAI_WORKFLOW_REQUEST_KEY`, restart Claude Code, then invoke `/workflow-request:build-request`.

Do not commit the key to a repository or paste it into a Claude conversation.
