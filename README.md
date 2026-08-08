# Ventura Agents

[![License](https://img.shields.io/github/license/venturalabs-ai/ventura-agents)](LICENSE)
[![Stars](https://img.shields.io/github/stars/venturalabs-ai/ventura-agents)](https://github.com/venturalabs-ai/ventura-agents/stargazers)
[![Forks](https://img.shields.io/github/forks/venturalabs-ai/ventura-agents)](https://github.com/venturalabs-ai/ventura-agents/forks)

Coleção de **10 agentes de IA especializados em funções de negócio**, estruturados como system prompts reutilizáveis e orientados a entregas, métricas, ferramentas e limites de autonomia.

## Catálogo

| Agente | Função | Entrega principal |
|---|---|---|
| `ventura.vendas` | SDR / Vendas | prospecção, follow-up e pipeline |
| `ventura.marketing` | Marketing | estratégia, conteúdo, SEO e funil |
| `ventura.suporte` | Atendimento | tickets, CSAT e knowledge base |
| `ventura.recrutamento` | RH | triagem e entrevistas estruturadas |
| `ventura.dados` | Dados / BI | SQL, dashboards e relatórios |
| `ventura.engenharia` | Engenharia | code review, arquitetura e refactoring |
| `ventura.financeiro` | Financeiro | fluxo de caixa e conciliação |
| `ventura.projetos` | Projetos | planejamento, riscos e status |
| `ventura.social` | Social media | calendário, copy e análise |
| `ventura.juridico` | Jurídico / Compliance | contratos, LGPD e análise de risco |

## Anatomia de um agente

Cada arquivo descreve:

1. identidade e missão;
2. domínio e limites;
3. regras de operação;
4. workflow;
5. entradas e saídas;
6. métricas;
7. ferramentas e integrações sugeridas;
8. autonomia e escalonamento humano;
9. exemplo de ativação.

## Uso

```text
1. Escolha um agente.
2. Use o arquivo .md como system prompt ou base de configuração.
3. Forneça contexto, objetivo e dados necessários.
4. Conecte somente as ferramentas compatíveis com o ambiente utilizado.
5. Mantenha ações de risco sob confirmação ou política explícita.
```

## Arquitetura de eficiência

O projeto usa o ciclo:

**Explore → Compile → Replay → Regenerate**

A ideia é transformar caminhos validados em regras e skills reutilizáveis, reduzindo redecisões e consumo desnecessário de contexto em tarefas recorrentes.

## Segurança

Prompts não substituem controles técnicos. Agentes conectados a e-mail, banco de dados, CRM, ERP, código ou sistemas financeiros devem operar com autenticação, autorização, logging, least privilege e validação no lado da ferramenta.

## Família Ventura

- [Ventura Agents II](https://github.com/venturalabs-ai/ventura-agents-2)
- [Ventura Pro](https://github.com/venturalabs-ai/ventura-pro)
- [Autor Ventura](https://github.com/venturalabs-ai/autor-ventura)
- [Ventura Art](https://github.com/venturalabs-ai/ventura-art)
- [Ventura.SEG](https://github.com/venturalabs-ai/Ventura.SEG)

## Licença

MIT — consulte [LICENSE](LICENSE).

## Autor

Wemerson Mota de Oliveira — Ventura Labs AI

[GitHub](https://github.com/venturalabs-ai) · [LinkedIn](https://www.linkedin.com/in/wemerson-mota-de-oliveira-81aa8226/)
