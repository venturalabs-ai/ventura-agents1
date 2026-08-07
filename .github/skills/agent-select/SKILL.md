---
name: agent-select
description: Select the single Ventura Agents business agent whose declared mission best matches a requested outcome. Use when a user needs to choose among the ten agent prompts before execution. Do not use when modifying an agent prompt or coordinating several agents in one workflow.
---

# Agent select

- Map the requested deliverable to the catalog in `README.md`.
- Select one agent when one declared function owns the outcome.
- Prefer the agent's primary delivery domain over keyword similarity.
- State the required user context or data the selected agent will need.
- Do not select an agent for a capability absent from its prompt.
- Escalate to a multi-agent workflow only when ownership genuinely crosses catalog functions.
