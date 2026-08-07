# Semantic evals

`semantic_cases.jsonl` contém rubricas versionadas. `scripts/score_semantic_outputs.py` **não chama um modelo** e não deve ser usado para alegar qualidade de agente sem saídas realmente geradas no runtime avaliado.

Uso:

```bash
python scripts/score_semantic_outputs.py --outputs reports/model-output.jsonl
```

Cada linha de outputs deve ter `id` e `output`. Um relatório publicável deve registrar modelo/provedor/versão, configuração, data, commit do repositório e arquivo de outputs. Fixtures manuais servem apenas para testar o scorer, nunca para publicar task-success/model-quality.
