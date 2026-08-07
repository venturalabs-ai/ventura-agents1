# Ventura Agents

![MIT](https://img.shields.io/github/license/chamseddinehiddoud/ventura-agents)
![stars](https://img.shields.io/github/stars/chamseddinehiddoud/ventura-agents)
![forks](https://img.shields.io/github/forks/chamseddinehiddoud/ventura-agents)

Coleção de **10 super agentes de IA de negócio** para o mercado, com a
identidade da família **Ventura.** — cada um especializado em uma função de
alta demanda: vendas, marketing, suporte, recrutamento, dados, engenharia,
financeiro, projetos, social media e jurídico.

Cada agente é um **system prompt completo, plugável**: copie o arquivo, anexe
como system prompt no seu modelo/plataforma (ChatGPT, Claude, Gemini, copilots
empresariais) e adicione as ferramentas/APIs indicadas no bloco "Integrações".

## Catálogo (os 10 mais buscados pelo mercado)

| # | Agente | Função | Entrega principal |
|---|---|---|---|
| 1 | [ventura.vendas](ventura.vendas.md) | SDR / Vendas | prospecção qualificada, sequência de follow-up, pipeline limpo |
| 2 | [ventura.marketing](ventura.marketing.md) | Marketing de conteúdo | estratégia + calendário + copy com SEO e funil |
| 3 | [ventura.suporte](ventura.suporte.md) | Suporte ao cliente | tickets resolvidos, CSAT alto, knowledge base |
| 4 | [ventura.recrutamento](ventura.recrutamento.md) | Recrutamento & RH | triagem, entrevistas estruturadas, time-to-hire reduzido |
| 5 | [ventura.dados](ventura.dados.md) | Análise de dados & BI | dashboards, SQL, relatórios com storytelling |
| 6 | [ventura.engenharia](ventura.engenharia.md) | Engenharia de software | code review, arquitetura, refactoring seguro |
| 7 | [ventura.financeiro](ventura.financeiro.md) | Financeiro & contabilidade | fluxo de caixa, contas a pagar/receber, conciliação |
| 8 | [ventura.projetos](ventura.projetos.md) | Gestão de projetos | planejamento, sprints, riscos, status executivo |
| 9 | [ventura.social](ventura.social.md) | Social media | calendário, copy, engajamento, análise por plataforma |
| 10 | [ventura.juridico](ventura.juridico.md) | Jurídico & compliance | contratos, LGPD, análise de risco e conformidade |

## Anatomia de cada agente

```
1. Identidade        — nome (ventura.<função>), missão, tom de voz
2. Domínio           — escopo de atuação, o que faz / não faz
3. Regras de ouro    — princípios inegociáveis (dados, ética, segurança)
4. Workflow          — pipeline operacional passo a passo
5. Entradas e saídas — o que recebe, o que entrega (contrato)
6. Métricas          — KPIs que o agente persegue
7. Ferramentas       — integrações sugeridas (CRM, ERP, helpdesk...)
8. Autonomia         — o que decide sozinho vs. o que sobe para humano
9. Exemplo de uso    — prompt de ativação pronto
```

## Como usar

```text
1. Escolha o agente no catálogo.
2. Copie o conteúdo do .md como system prompt.
3. Forneça as variáveis obrigatórias (empresa, persona, contexto, acesso).
4. Ative com o "Exemplo de uso" do próprio agente.
5. Conecte as integrações sugeridas para autonomia real.
```

## Família Ventura

| Projeto | Repositório | Foco |
|---|---|---|
| **Ventura Agents** | `ventura-agents` | agentes de negócio multi-função |
| Autor Ventura | `autor-ventura` | super agente escritor (livros) |
| Ventura Art | `ventura-art` | criação de vídeos multi-plataforma |
| Ventura Pro | `ventura-pro` | soluções tecnológicas |

Frase-guia do estúdio: **"Todo agente nasce de uma função; toda função, de
uma entrega; toda entrega, de uma obrigação com o negócio."**

## Arquitetura Token-Efficient & Regenerative

Este sistema foi projetado sob três princípios fundamentais:

1. **Economia de Tokens** — maximizar valor por token gasto  
2. **Loop de Alto Rendimento** — cada ciclo deve justificar o consumo  
3. **Comportamento Regenerativo** — o sistema se reconstrói melhor a cada execução

### Ciclo Principal: Explore → Compile → Replay

| Fase | Descrição | Consumo de Tokens |
|------|-----------|-------------------|
| **Explore** | Modelo forte descobre o melhor caminho | Alto (único) |
| **Compile** | Transforma o caminho em skill determinística | Baixo |
| **Replay** | Executa a skill sem raciocínio completo | Mínimo / Zero |
| **Regenerate** | Quando o domínio muda, regenera a skill | Sob demanda |

### Regras de Engenharia

- **Token Budget** explícito por especialista e por etapa
- **Context Engineering** + **Context Compaction** em todas as passagens
- **Context Firewall** entre sub-agentes (cada um só recebe o necessário)
- **Prefix Caching** com system prompt estável
- **Yield-based Stop Condition** (para quando o valor não justifica mais tokens)
- **Skill Distillation** após caminhos bem-sucedidos

### Resultado esperado

- Redução drástica de tokens em execuções recorrentes
- Qualidade mantida ou superior
- Sistema que se auto-otimiza com o uso
