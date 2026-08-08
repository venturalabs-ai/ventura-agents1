#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{line_no}: invalid JSON: {exc}") from exc
    return rows


def score_case(case: dict, result: dict) -> tuple[bool, list[str]]:
    failures: list[str] = []
    selected = str(result.get("selected_agent", "")).strip().lower()
    expected = str(case.get("expected_agent", "")).strip().lower()
    output = str(result.get("output", ""))
    text = output.lower()

    if selected != expected:
        failures.append(f"wrong agent: expected {expected}, got {selected or '<missing>'}")

    required_all = [str(item).lower() for item in case.get("required_all", [])]
    required_any = [str(item).lower() for item in case.get("required_any", [])]
    forbidden = [str(item).lower() for item in case.get("forbidden", [])]

    missing_all = [item for item in required_all if item not in text]
    if missing_all:
        failures.append("missing required concepts: " + ", ".join(missing_all))
    if required_any and not any(item in text for item in required_any):
        failures.append("missing any-of concepts: " + ", ".join(required_any))
    present_forbidden = [item for item in forbidden if item in text]
    if present_forbidden:
        failures.append("forbidden claims present: " + ", ".join(present_forbidden))

    return not failures, failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Score externally generated Ventura Agents outputs.")
    parser.add_argument("--cases", type=Path, default=Path("evals/behavioral_cases.jsonl"))
    parser.add_argument("--outputs", type=Path, required=True)
    args = parser.parse_args()

    cases = {row["id"]: row for row in load_jsonl(args.cases)}
    outputs = {row["id"]: row for row in load_jsonl(args.outputs)}
    missing = sorted(set(cases) - set(outputs))
    if missing:
        print("BEHAVIORAL EVALS: FAIL")
        print("missing outputs: " + ", ".join(missing))
        return 2

    failures: list[str] = []
    categories: dict[str, list[bool]] = {}
    for case_id, case in cases.items():
        ok, reasons = score_case(case, outputs[case_id])
        category = str(case.get("category", "uncategorized"))
        categories.setdefault(category, []).append(ok)
        print(f"{case_id}: {'PASS' if ok else 'FAIL'}")
        failures.extend(f"{case_id}: {reason}" for reason in reasons)

    passed = len(cases) - len({failure.split(':', 1)[0] for failure in failures})
    task_success = passed / max(len(cases), 1)
    print(f"task_success={task_success:.3f}")
    for category, values in sorted(categories.items()):
        print(f"category.{category}={sum(values) / len(values):.3f}")

    if failures:
        print("BEHAVIORAL EVALS: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"BEHAVIORAL EVALS: PASS ({len(cases)} externally supplied outputs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
