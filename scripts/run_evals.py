from __future__ import annotations

import json
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Identidade",
    "## Domínio",
    "## Regras de ouro",
    "## Workflow",
    "## Entradas e saídas",
    "## Métricas",
    "## Ferramentas",
    "## Autonomia",
    "## Exemplo de uso",
]

REQUIRED_EVAL_CATEGORIES = {
    "happy_path",
    "edge_case",
    "tool_use",
    "adversarial",
    "refusal_safety",
    "regression",
}

files = sorted(Path(".").glob("ventura.*.md"))
failures: list[str] = []

if len(files) != 10:
    failures.append(f"expected 10 agent files, found {len(files)}")

agent_names = {path.stem for path in files}
for path in files:
    text = path.read_text(encoding="utf-8")
    if len(text) < 1200:
        failures.append(f"{path}: prompt unexpectedly short")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            failures.append(f"{path}: missing {section}")
    if "## Autonomia" in text and "humano" not in text.lower():
        failures.append(f"{path}: autonomy section lacks human escalation language")

cases_path = Path("evals/behavioral_cases.jsonl")
if not cases_path.exists():
    failures.append("missing evals/behavioral_cases.jsonl")
else:
    seen_ids: set[str] = set()
    categories: set[str] = set()
    for line_no, raw in enumerate(cases_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            case = json.loads(raw)
        except json.JSONDecodeError as exc:
            failures.append(f"behavioral_cases.jsonl:{line_no}: invalid JSON: {exc}")
            continue
        case_id = str(case.get("id", "")).strip()
        if not case_id:
            failures.append(f"behavioral_cases.jsonl:{line_no}: missing id")
        elif case_id in seen_ids:
            failures.append(f"behavioral_cases.jsonl:{line_no}: duplicate id {case_id}")
        seen_ids.add(case_id)
        category = str(case.get("category", "")).strip()
        categories.add(category)
        expected_agent = str(case.get("expected_agent", "")).strip()
        if expected_agent not in agent_names:
            failures.append(
                f"behavioral_cases.jsonl:{line_no}: expected_agent {expected_agent!r} is not a repository agent"
            )
        if not str(case.get("prompt", "")).strip():
            failures.append(f"behavioral_cases.jsonl:{line_no}: missing prompt")
        if not case.get("required_all") and not case.get("required_any"):
            failures.append(f"behavioral_cases.jsonl:{line_no}: no positive scoring criteria")
        if not case.get("forbidden"):
            failures.append(f"behavioral_cases.jsonl:{line_no}: no forbidden regression/safety criteria")
    missing_categories = sorted(REQUIRED_EVAL_CATEGORIES - categories)
    if missing_categories:
        failures.append("behavioral eval dataset missing categories: " + ", ".join(missing_categories))

for required in ["evals/README.md", "scripts/score_behavioral_outputs.py"]:
    if not Path(required).exists():
        failures.append(f"missing behavioral eval artifact: {required}")

if failures:
    print("AGENT EVALS: FAIL")
    for failure in failures:
        print(f"- {failure}")
    raise SystemExit(1)

print(
    f"AGENT EVALS: PASS ({len(files)} agents; contract/schema baseline; "
    f"{len(seen_ids)} versioned behavioral cases validated)"
)
print("NOTE: model/task-success claims still require externally generated outputs from recorded providers/models.")
