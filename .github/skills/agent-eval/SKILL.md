---
name: agent-eval
description: Create repeatable cases that test one Ventura business agent's declared deliverables limits escalation and metric behavior. Use when changing an agent prompt or validating a customization. Do not use when only choosing an agent from the catalog.
---

# Agent eval

- Derive cases from the agent's declared mission workflow inputs outputs and limits.
- Include one normal case one ambiguous case and one case requiring escalation.
- Check required deliverable structure separately from subjective answer quality.
- Test that the agent refuses or escalates actions beyond its autonomy boundary.
- Use synthetic business data rather than real confidential records.
- Record model runtime and prompt version when comparing results over time.
- Do not claim production reliability from prompt-only tests.
