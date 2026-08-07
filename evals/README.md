# Ventura Agents — Evaluation Policy

This repository uses two layers of evaluation:

1. **Offline contract evals** — deterministic checks over agent files, required sections, human-escalation language and forbidden unsupported claims. These run on every push/PR.
2. **Semantic/model evals** — task-success, hallucination, tool-use and safety evaluations. These must record dataset version, model/provider, model version, parameters, date and scoring method before results are published.

## Current blocking gate

`python scripts/run_evals.py`

A green contract eval proves repository structure and policy compliance only. It does **not** prove model-level task success or safety.

## Promotion criteria

A future `stable` or `production-grade` claim requires published semantic eval results with fixed cases and regression comparison against the previous release.
