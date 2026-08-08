# Threat Model — ventura-agents

| Surface | Threat | Mitigation |
|---------|--------|------------|
| System prompts | prompt injection quando usados em runtime | orientar uso com Ventura.SEG |
| Evals | dados sensiveis em fixtures | sem PII real |
| Distribuicao | prompts maliciosos em forks | review + CI structure |
