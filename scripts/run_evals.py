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

files = sorted(Path('.').glob('ventura.*.md'))
failures = []

if len(files) != 10:
    failures.append(f"expected 10 agent files, found {len(files)}")

for path in files:
    text = path.read_text(encoding='utf-8')
    if len(text) < 1200:
        failures.append(f"{path}: prompt unexpectedly short")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            failures.append(f"{path}: missing {section}")
    if "## Autonomia" in text and "humano" not in text.lower():
        failures.append(f"{path}: autonomy section lacks human escalation language")

if failures:
    print("AGENT EVALS: FAIL")
    for failure in failures:
        print(f"- {failure}")
    raise SystemExit(1)

print(f"AGENT EVALS: PASS ({len(files)} agents; contract/schema baseline)")
