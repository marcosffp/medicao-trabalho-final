# Codebook

Item do questionário → variável → escala → RQ → métrica → codificação. Fonte: Seção 3 do protocolo v5 e `dashboard/analise.py` (os códigos abaixo são os usados no código). Na exportação do Google Formulários, cada coluna começa pelo código do item (por exemplo, `P1. Quantos anos…`); o código reconhece a coluna por esse prefixo.

## 1. Itens do formulário

| Item | Texto resumido | Escala | RQ | Métrica (GQM) | Codificação no código |
|---|---|---|---|---|---|
| `carimbo` | Carimbo de data/hora gerado pelo Google | Data/hora | Todas (evidência) | – | `datetime`; usado no funil, na janela de coleta e na regra R-08 |
| C0 | Tenho 18 anos ou mais, li o termo e aceito participar | Nominal | RQ1–3 (elegibilidade) | Elegibilidade | Texto começando por "Sim" = consentiu. Outro valor = inelegível |
| T1 | Hoje trabalha com desenvolvimento de software no Brasil? | Nominal | RQ1–3 (elegibilidade) | Elegibilidade | "Sim" = elegível. "Não" = inelegível |
| T2 | Vínculo atual | Nominal | RQ2–3 (filtro) | Perfil | Emprego, Estágio, Trabalho autônomo. "Outro" = inelegível |
| U1 | Frequência de uso de IA nos últimos 3 meses | Ordinal | RQ2 | Frequência de uso | Primeiro dígito do rótulo: 1 Nunca (inelegível), 2 Uma ou poucas vezes no período, 3 Algumas vezes por mês, 4 Algumas vezes por semana, 5 Todos ou quase todos os dias |
| U2 | Dias de uso nos últimos 5 dias úteis | Razão (contagem) | RQ2 (robustez) | Dias de uso | Inteiro de 0 a 5 |
| P1 | Anos completos de atuação em desenvolvimento | Razão | RQ3 | Anos de experiência | Inteiro (0 = menos de 1 ano). Valor não inteiro invalida a resposta (decisão operacional) |
| P2 | Porte da organização | Ordinal | RQ2–3 (filtro) | Porte | Até 10 · 11 a 50 · 51 a 200 · 201 a 1000 · Mais de 1000. "Não se aplica (trabalho autônomo)" fica como ausente no porte ordinal |
| P3 | Tempo de uso de IA no trabalho | Ordinal | RQ2–3 (covariável) | Tempo de uso | Menos de 3 meses · 3 a menos de 6 · 6 a menos de 12 · 12 meses ou mais |
| P4 | Assistentes usados (múltipla escolha + "Outra") | Nominal | RQ2–3 (filtro) | Ferramentas | Uma coluna lógica por opção (`P4::ChatGPT`, `P4::Claude`…). "Outra" recodificada por `dashboard/codificacao_outra.json` |
| P5 | Tarefas em que usa (múltipla escolha + "Outra") | Nominal | RQ2–3 (filtro) | Tarefas | Uma coluna lógica por opção (`P5::Escrever código`…). "Outra" recodificada pelo mesmo arquivo |
| PP1 | Concluo minhas tarefas mais rápido | Ordinal (Likert 5) | RQ1–3 | PP_med (rapidez) | Primeiro dígito: 1 a 5 |
| PP2 | Entrego mais tarefas no mesmo período | Ordinal (Likert 5) | RQ1–3 | PP_med (rapidez) | 1 a 5 |
| PP3 | A qualidade do código que entrego é melhor | Ordinal (Likert 5) | RQ1–3 | PP_med (qualidade) | 1 a 5 |
| PP4 | Preciso refazer menos o código depois de entregue | Ordinal (Likert 5) | RQ1–3 | PP_med (qualidade) | 1 a 5 |
| PP5 | Usar IA torna o trabalho **mais cansativo ou trabalhoso** | Ordinal (Likert 5), **invertido** | RQ1–3 | PP_med (esforço) | 1 a 5 na coluna original; recodificado em `PP5r = 6 − PP5` antes de qualquer cálculo |
| AT1 | Pergunta de atenção: "marque 'Discordo' nesta linha" | Nominal (controle) | Qualidade | Conformidade | Passa se = 2. Qualquer outro valor descarta a resposta |

Escala Likert dos itens PP e AT1: 1 Discordo totalmente · 2 Discordo · 3 Nem concordo nem discordo · 4 Concordo · 5 Concordo totalmente.

## 2. Variáveis derivadas (só nas respostas válidas)

| Variável | Definição | Usada em |
|---|---|---|
| `PP5r` | `6 − PP5` | α de Cronbach, PP_med, escores |
| `PP_med` | Mediana de PP1, PP2, PP3, PP4 e PP5r (inteiro de 1 a 5; 3 = neutro) | RQ1, RQ2, RQ3 |
| `classe_PP` | Abaixo do neutro (1–2) · Neutro (3) · Acima do neutro (4–5) | RQ1, χ²/Fisher |
| `linha_reta` | Cinco itens PP originais iguais. Só sinaliza, não descarta | Sensibilidade |
| `faixa_P1` | 0 a 2 · 3 a 5 · 6 a 10 · 11 ou mais. Faixas com menos de 5 pessoas são agrupadas com a vizinha | Exploratória (Kruskal-Wallis) |
| `P2_ord` | Porte como inteiro de 1 (até 10) a 5 (mais de 1000) | Resumo ordinal |
| `status` | Válida · Inelegível · Descartada | Funil |
| `motivo` | Texto do motivo de encerramento ou descarte | Funil e lista por resposta |
| `fora_janela` | Carimbo fora de 11 a 20/11/2026 (sinaliza, não descarta) | Checagens |

## 3. Métricas por questão de pesquisa

| RQ | Variáveis | Teste | Efeito |
|---|---|---|---|
| RQ1 | `PP_med` contra o neutro 3 | Teste do sinal exato, sem empates (PP_med = 3) | Proporção de PP_med ≥ 4 entre os não empatados, IC de Clopper-Pearson |
| RQ2 | `U1` × `PP_med` | Spearman | ρ, IC bootstrap |
| RQ3 | `P1` × `PP_med` | Spearman | ρ, IC bootstrap |
| Exploratórias | `U2`, `faixa_P1`, T2, P2, P3, U1 | Spearman, Mann-Whitney, Kruskal-Wallis, χ²/Fisher | ρ, δ de Cliff, ε², V de Cramér |

## 4. Codificação das respostas "Outra" (P4 e P5)

Arquivo: `dashboard/codificacao_outra.json` (texto como veio → categoria). Codificação feita por uma única pessoa (desvio D2). Respostas sem mapeamento ficam como "Outra (não codificada)". Cada fragmento separado por vírgula recebe uma categoria; o dashboard não exibe texto livre.
