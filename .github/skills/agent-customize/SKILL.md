---
name: agent-customize
description: Customize one Ventura Agents prompt for a concrete organization while preserving its mission limits metrics and escalation boundaries. Use when adapting an existing agent to a real operating context. Do not use when the requested role is outside the existing catalog or when only selecting an agent.
---

# Agent customize

- Start from the closest existing agent prompt rather than creating a parallel persona.
- Replace generic organization context with approved processes terminology metrics and tools.
- Preserve the agent's declared mission and human-escalation boundaries.
- Add only integrations that exist in the target environment.
- Keep credentials permissions and authorization outside the prompt and enforce them in tools.
- Remove instructions that conflict with target policy or duplicate existing agent rules.
- Record the organization-specific assumptions introduced by the customization.
