---
name: tool-boundary
description: Define tool permissions confirmation points and least-privilege boundaries for a Ventura business agent connected to external systems. Use when an agent gains email CRM ERP database code or financial tools. Do not use when the agent is prompt-only with no external action capability.
---

# Tool boundary

- List each external tool and the exact read or write actions the agent needs.
- Default to read-only access until a write action is required.
- Require explicit confirmation for destructive financial legal personnel or irreversible operations unless a stronger approved policy exists.
- Keep authentication authorization and validation in the tool layer rather than the prompt.
- Log material external actions with enough context for audit.
- Remove permissions not exercised by the agent's declared workflow.
