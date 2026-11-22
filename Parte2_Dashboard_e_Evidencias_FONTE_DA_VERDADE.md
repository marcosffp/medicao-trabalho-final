# Parte 2 · Dashboard e Evidências — Fonte da Verdade

**Disciplina:** Medição e Experimentação em Eng. de Software (2º/2026) · **Trabalho Final em Grupo** (3–4 integrantes)
**Valor da Parte 2:** 8 pts (de 10) · **Entrega no Canvas:** upload de arquivo · **Vencimento:** sexta-feira, 12:00 (provavelmente 27/11/2026 — *confirmar a data exata na tarefa do Canvas*)
**Origem deste documento:** enunciado oficial "Trabalho Final – Resultados" (PUC Minas / Canvas, impresso em 22/11/2026). Tudo nas seções 1–5 e 12 é transcrição/reorganização do enunciado. O que está marcado como **[RECOMENDAÇÃO]** é sugestão nossa, não exigência do professor.

> Como usar: este arquivo é o contrato do grupo. Se algum membro tiver dúvida do tipo "isso é obrigatório?", a resposta está aqui. Preencha os campos `[PREENCHER]` e marque os checklists conforme avançam.

---

## 0. Dados do grupo (preencher)

| Campo | Valor |
|---|---|
| Tema escolhido | Uso de assistentes de IA generativa no desenvolvimento de software e produtividade percebida (survey) |
| Integrantes | Bernardo Alvim, Brenda Evers, Gabriel Nogueira, Gabriela, Marcos (grupo de 5, com autorização do professor, conforme o protocolo v5) |
| Repositório GitHub | https://github.com/gnvr29/medicao-trabalho-final |
| Data/hora do commit/envio da Parte 1 (protocolo) | 13/11/2026 às 9:17, envio no Canvas (`docs/evidencias/canvas_envio_parte1_2026-11-13.png`; arquivo enviado: `Protocolo_do_Survey_v5 (1).pdf`) |
| Data/hora da 1ª resposta coletada | 13/11/2026 20:46 (exportação oficial COLETA; **tem de ser POSTERIOR à data acima**). Última resposta: 19/11/2026 17:50 |
| Ferramenta do dashboard | Streamlit (`dashboard/app.py`, lê o XLSX/CSV bruto; estatística em `dashboard/analise.py`) |
| Link do dashboard | `[PREENCHER]` |
| Organização com carta de anuência? (sim/não) | Não (survey em várias fontes; vale o mínimo de 50 válidas e a evidência E-B) |
| Nº de respostas recebidas / válidas / descartadas | 90 / 69 / 21 (11 inelegíveis por T1 = não atua com desenvolvimento no Brasil + 10 descartadas por falha na pergunta de atenção AT1) |

---

## 1. Visão geral da avaliação

| Entrega | Pontos | Conteúdo |
|---|---|---|
| Parte 1 · Planejamento | 2 pts | Protocolo (PDF, até 6 páginas) entregue **antes** de qualquer coleta, com data comprovada |
| **Parte 2 · Dashboard e evidências** | **8 pts** | Dashboard com dados coletados, evidências da coleta e defesa ao vivo |

### Rubrica da Parte 2 (oficial)

| # | Critério | Pontos | % da Parte 2 |
|---|---|---:|---:|
| C1 | Evidências da coleta e consistência dos dados com o protocolo | 2,0 | 25% |
| C2 | Qualidade dos dados: limpeza, descartes justificados e confiabilidade dos construtos | 1,5 | 18,75% |
| C3 | Questões de pesquisa respondidas com testes, tamanhos de efeito e visualizações corretos | 2,0 | 25% |
| C4 | Desvios em relação ao protocolo e limitações (não resposta, vieses) | 0,5 | 6,25% |
| C5 | Defesa ao vivo: mudança de cenário e arguição individual | 2,0 | 25% |
| | **Total** | **8,0** | 100% |

**Leitura estratégica:** 50% da nota (C1 + C5 = 4 pts) depende de evidência e defesa, não de gráfico bonito. O dashboard em si pesa em C2 + C3 (3,5 pts). Desvios/limitações valem pouco (0,5), mas desvio **não declarado** contamina C1.

---

## 2. Requisitos obrigatórios (rastreáveis)

Cada requisito tem um ID. A coluna "Critério" diz em qual linha da rubrica ele pesa.

### 2.1 Dashboard

| ID | Requisito (enunciado) | Critério |
|---|---|---|
| D-00 | A ferramenta é livre, **mas o dashboard deve ler os dados brutos coletados**, não apenas exibir imagens prontas | C1/C2 |
| D-01 | **Perfil da amostra:** nº de respostas recebidas, nº de respostas descartadas e **o motivo de cada descarte** | C2 |
| D-02 | **Itens em escala Likert em gráfico de barras divergentes** | C3 |
| D-03 | **Resposta a cada questão de pesquisa**, com: teste estatístico usado, p-valor, tamanho de efeito e margem de erro | C3 |
| D-04 | **Filtros por segmento** (ex.: tempo de experiência, tipo de empresa) | C3 |
| D-05 | **Confiabilidade** dos construtos medidos por mais de um item (**alfa de Cronbach**) | C2 |
| D-06 | **Página de metodologia e desvios:** o que mudou em relação ao protocolo da Parte 1 e por quê | C4 |

### 2.2 Evidências da coleta (**pelo menos uma** das opções)

| ID | Opção | Observação |
|---|---|---|
| E-A | **Carta de anuência assinada** pela empresa/organização onde o survey foi aplicado, autorizando a aplicação | Habilita o mínimo reduzido de 30 respostas (ver R-02) |
| E-B | **Registros digitais**, que reúnem os três itens: (1) exportação bruta do formulário com **data e hora de cada resposta**; (2) **capturas datadas dos canais de divulgação**; (3) **acesso ao painel do formulário durante a apresentação** | Os três itens compõem a opção B |
| E-X | **Restrição transversal:** nenhuma evidência pode expor dados pessoais dos respondentes | Vale para E-A e E-B |

> **[RECOMENDAÇÃO]** Apresentar A **e** B quando possível. O enunciado exige só uma, mas as duas juntas blindam C1 (2,0 pts) caso uma seja questionada.

### 2.3 Apresentação e defesa

| ID | Requisito | Critério |
|---|---|---|
| P-01 | Demonstração ao vivo do dashboard, **10 minutos por grupo** | C5 |
| P-02 | **Mudança de cenário:** o professor propõe uma alteração no estudo; o grupo explica o que mudaria no **planejamento** ou na **análise** | C5 |
| P-03 | **Arguição individual:** cada integrante responde a uma pergunta sobre o trabalho | C5 |
| P-04 | **Todos devem dominar o estudo inteiro**, não só a parte que apresentaram | C5 |

---

## 3. Regras da coleta (oficiais)

| ID | Regra |
|---|---|
| R-01 | **Mínimo de 50 respostas válidas.** |
| R-02 | **Mínimo de 30 respostas válidas** quando o survey for aplicado em **uma única organização com carta de anuência**. |
| R-03 | **Colegas da turma não contam como amostra**, exceto se a população-alvo for estudantes **e** isso estiver justificado no protocolo. |
| R-04 | Os dados devem corresponder ao protocolo da Parte 1. **Desvios são aceitos desde que declarados e justificados.** |
| R-05 | A **margem de erro** deve ser relatada junto com os resultados, e **as conclusões devem respeitar esse limite**. |
| R-06 | Seguir as orientações da instituição sobre pesquisas com pessoas. |
| R-07 | **Integridade:** indícios de respostas fabricadas ou dados manipulados são tratados conforme as normas acadêmicas da instituição. |
| R-08 | Dados coletados devem ser posteriores à entrega comprovada da Parte 1 (a data do protocolo precisa ser anterior à primeira resposta). |

**Ponto crítico:** "válidas" = depois da limpeza. Respostas recebidas ≠ respostas válidas. O mínimo vale sobre as **válidas**. Se vocês estão no limite (ex.: 52 recebidas), cada descarte pode derrubar abaixo do mínimo. Planejem folga.

---

## 4. Fonte da verdade dos dados

### 4.1 Princípio

> O dashboard lê **exclusivamente** o arquivo bruto exportado do formulário. Toda limpeza, descarte, recodificação e cálculo acontece por **regra explícita e reproduzível** (script ou fórmulas visíveis), nunca por edição manual silenciosa no arquivo.

### 4.2 Pipeline de dados

```
Formulário (Google Forms / MS Forms / outro)
        │  exportação bruta, com timestamp por resposta
        ▼
data/raw/respostas_brutas_AAAA-MM-DD.csv     ← IMUTÁVEL (nunca editar; guardar hash)
        │  script de limpeza (regras D-xx abaixo)
        ▼
data/processed/respostas_validas.csv         ← usado pelo dashboard
data/processed/respostas_descartadas.csv     ← com coluna "motivo_descarte"
        │
        ▼
Dashboard (lê raw → aplica regras → mostra; ou lê processed + log)
```

**[RECOMENDAÇÃO]** Gerar o SHA-256 do CSV bruto no dia da exportação e registrá-lo no repositório:

```bash
sha256sum data/raw/respostas_brutas_2026-MM-DD.csv > data/raw/SHA256SUMS.txt
```

Isso prova na defesa que o arquivo não foi alterado depois.

### 4.3 Estrutura de pastas sugerida

```
/
├── protocolo/Parte1_Protocolo.pdf          ← com data comprovada (commit)
├── data/
│   ├── raw/                                ← export bruto + SHA256SUMS.txt
│   └── processed/                          ← válidas, descartadas, codebook aplicado
├── docs/
│   ├── codebook.md                         ← item → variável → escala → RQ → métrica
│   ├── regras_de_limpeza.md                ← critérios de descarte numerados
│   ├── log_de_desvios.md                   ← seção 8 deste documento
│   └── evidencias/                         ← capturas datadas, carta (sem dados pessoais)
├── src/                                    ← script de limpeza + estatística
├── dashboard/                              ← arquivo do dashboard / app
└── README.md
```

### 4.4 Regras de descarte (a definir **no protocolo**; aqui, o catálogo de motivos possíveis)

Cada resposta descartada precisa de **um motivo registrado** (D-01). Use códigos fixos para o dashboard agrupar:

| Código | Motivo | Como detectar | Observação |
|---|---|---|---|
| `DSC-01` | Sem consentimento (TCLE) | Campo de aceite ≠ "Concordo" | Obrigatório descartar (ética/LGPD) |
| `DSC-02` | Fora da população-alvo | Pergunta-filtro (ex.: não atua com ES; não é da organização) | Exige que a população esteja definida no protocolo |
| `DSC-03` | Falha na pergunta de atenção | Resposta ≠ instrução da pergunta de atenção | O protocolo **exige** uma pergunta de atenção (Parte 1, seção 3) |
| `DSC-04` | Resposta duplicada | Mesmo identificador/combinação improvável de respostas em curto intervalo | Documentar o critério usado |
| `DSC-05` | Resposta automática/descuidada (straight-lining) | Todos os itens Likert com o mesmo valor **e** tempo de preenchimento implausível | Critério precisa ser objetivo e declarado **antes** de olhar os resultados |
| `DSC-06` | Questionário incompleto | Nulos em itens obrigatórios dos construtos/RQs | Se o formulário já força obrigatoriedade, pode não ocorrer |
| `DSC-07` | Timestamp anterior à entrega do protocolo | `timestamp < data_protocolo` | Viola R-08; investigar antes de descartar |
| `DSC-08` | Respondente da própria turma (se não for população-alvo) | Pergunta de origem | Viola R-03 |
| `DSC-99` | Outro (descrever) | — | Evitar; cada uso exige justificativa por escrito |

**Regra de ouro:** definir os critérios de descarte **sem olhar** para o efeito deles nos resultados. Descartar resposta porque "estraga" a hipótese é manipulação (R-07).

### 4.5 Codebook (modelo — preencher a partir do questionário do protocolo)

| Item | Texto resumido | Variável | Tipo/escala | Construto | RQ | Métrica (GQM) | Codificação |
|---|---|---|---|---|---|---|---|
| Q1 | `[PREENCHER]` | `q01_...` | Nominal / Ordinal / Intervalar / Razão | — | RQ1 | M1 | `[PREENCHER]` |
| Q2 | | | | | | | |
| … | | | | | | | |

> A rastreabilidade **item → RQ → métrica** já foi exigida na Parte 1. O dashboard deve ser coerente com ela. Se um item sumiu ou mudou, vai para o log de desvios (seção 8).

---

## 5. Especificação do dashboard (página a página)

> Estrutura sugerida: 5 a 6 páginas/abas. Nada aqui contradiz o enunciado; a divisão em páginas é **[RECOMENDAÇÃO]**.

### Página 1 — Perfil da amostra  *(D-01)*

**Deve mostrar:**
- Cartões: **Recebidas**, **Válidas**, **Descartadas**, **% descartadas**.
- **Funil**: recebidas → descartadas por motivo → válidas.
- **Tabela de descartes por motivo** (código, descrição, quantidade). O somatório tem que fechar: `recebidas = válidas + Σ descartes`.
- Verificação do mínimo: indicador "válidas ≥ 50" (ou "≥ 30 com anuência") — verde/vermelho.
- Distribuição do perfil dos respondentes (nas variáveis de segmentação: experiência, porte da empresa, função, etc.) em barras.
- **Linha do tempo de respostas** (por dia) — ajuda a provar a janela de coleta e a coerência com o plano de divulgação.

**Checks:**
- [ ] Soma fecha (recebidas = válidas + descartadas).
- [ ] Todo descarte tem motivo.
- [ ] Nenhum dado pessoal visível (nome, e-mail, IP, etc.).
- [ ] Mínimo (R-01 ou R-02) atendido e destacado.

### Página 2 — Itens Likert em barras divergentes  *(D-02)*

**Especificação do gráfico:**
- Barras horizontais **divergentes**, uma linha por item, centradas no ponto neutro.
- Discordância à esquerda, concordância à direita, neutro no centro (ou dividido ao meio entre os lados — escolha uma convenção e declare-a na página).
- Eixo em **% de respondentes** (100% empilhado por item), com o **n** de cada item.
- Ordenar itens por concordância líquida (ou agrupar por construto).
- Escala de cores **divergente e acessível** (dois tons para discordar, cinza para neutro, dois tons para concordar); legenda com os rótulos reais da escala.
- Itens **invertidos** (reverse-coded): indicar e tratar antes de agregar.
- Filtros de segmento (Página 4) devem **atualizar este gráfico**.

**Checks:**
- [ ] Cada item Likert do questionário aparece (ou há justificativa).
- [ ] O n por item aparece (nulos não somem sem aviso).
- [ ] Itens invertidos tratados.
- [ ] Rótulos da escala iguais aos do questionário.

### Página 3 — Questões de pesquisa  *(D-03)*

Uma **seção por RQ** (2 a 4 conforme o protocolo). **Cada seção** precisa conter, **obrigatoriamente**:

| Campo | Conteúdo |
|---|---|
| Pergunta | Texto exato da RQ do protocolo |
| Variáveis e escalas | Quais variáveis, em que escala |
| Teste estatístico | Nome do teste e **por que é coerente com a escala** |
| Estatística do teste | Valor (U, H, χ², ρ, etc.) e graus de liberdade quando aplicável |
| **p-valor** | Bruto **e** ajustado para múltiplas comparações, se houve |
| **Tamanho de efeito** | Medida adequada ao teste + interpretação |
| **Margem de erro** | Da estimativa relevante (ver seção 6.5), com n usado |
| Visualização | Gráfico adequado ao tipo de dado |
| **Conclusão** | Em linguagem simples, **respeitando a margem de erro** (R-05) |
| Ressalvas | Amostra não probabilística, n por grupo, etc. |

**Modelo de card de resposta:**

```
RQ1: <pergunta>
Teste: Mann-Whitney U (ordinal, 2 grupos independentes)
U = ___ · p = ___ (ajustado Holm: ___) · Efeito: rank-biserial r = ___ (pequeno/médio/grande)
n_A = __ · n_B = __ · Margem de erro (p=0,5, 95%): ±__ p.p.
Conclusão: <o que se pode afirmar e o que NÃO se pode>
```

**Checks:**
- [ ] Todas as RQs do protocolo têm resposta (mesmo que "inconclusiva").
- [ ] Teste condiz com a escala (seção 6.1).
- [ ] p-valor **e** tamanho de efeito juntos (nunca só um).
- [ ] Margem de erro presente em cada RQ.
- [ ] Correção para múltiplas comparações aplicada quando há vários testes (seção 6.3).
- [ ] Conclusão **não** extrapola a margem de erro nem a população.

### Página 4 — Filtros por segmento  *(D-04)*

- Filtros **globais** (aplicam a todas as páginas relevantes): ex. tempo de experiência, tipo/porte de empresa, função, uso de determinada prática.
- Mostrar **n do segmento filtrado** o tempo todo.
- **Aviso automático quando n do segmento for pequeno** (ex.: n < 10 → "interpretar com cautela; margem de erro muito ampla"). *[RECOMENDAÇÃO]*
- Os testes e a margem de erro devem **recalcular** com o filtro (ou o dashboard deve deixar claro quais valores são do total e quais do segmento).
- Segmentos definidos **no protocolo**, não escolhidos depois por darem resultado bonito (evita p-hacking).

**Checks:**
- [ ] Pelo menos um filtro por segmento funcional (o enunciado dá como exemplo tempo de experiência ou tipo de empresa).
- [ ] n do filtro visível.
- [ ] Não há segmento com n minúsculo apresentado como conclusão.

### Página 5 — Confiabilidade dos construtos  *(D-05)*

Para **cada construto medido por mais de um item**:

| Construto | Itens | n (casos completos) | Alfa de Cronbach (α) | α se item removido | Interpretação |
|---|---|---:|---:|---|---|
| `[PREENCHER]` | q03, q04, q05 | | | | |

- Mostrar α **e** quantos itens o compõem (α depende do nº de itens).
- Mostrar "α se o item for removido" para identificar item ruim.
- **Referência usual:** α ≥ 0,70 como aceitável em pesquisa exploratória; abaixo disso, declarar a limitação e (se o protocolo previa) analisar itens isoladamente. Não esconder α baixo — explicar.
- Com **2 itens**, α tende a ser instável; reportar também a **correlação entre os itens** (Spearman) como complemento. *[RECOMENDAÇÃO]*
- Itens invertidos recodificados **antes** do cálculo.
- Construtos medidos por **um** item só: declarar que α não se aplica.

**Checks:**
- [ ] Todos os construtos multi-item têm α.
- [ ] Itens invertidos tratados.
- [ ] α baixo explicado, não escondido.

### Página 6 — Metodologia e desvios  *(D-06)*

**Conteúdo:**
1. **Resumo do protocolo**: objetivo GQM, RQs, população, amostragem planejada (n pretendido + margem de erro planejada), instrumento, plano de análise.
2. **Como foi executado de fato**: canais, período real de coleta, nº real, margem de erro real.
3. **Tabela de desvios** (modelo na seção 8): planejado × executado × motivo × impacto.
4. **Ameaças à validade** e como se manifestaram (não resposta, autosseleção, desejabilidade social, etc.).
5. **Limitações** (amostra não probabilística → generalização restrita).
6. **Ética/LGPD**: TCLE, anonimização, armazenamento (cumpriu o que foi prometido?).
7. Link/identificação do protocolo (Parte 1) e a **data comprovada**.

**Checks:**
- [ ] Todo desvio tem justificativa.
- [ ] "Planejado" bate **literalmente** com o PDF da Parte 1.
- [ ] Limitações não são genéricas: falam desta amostra.

---

## 6. Estatística: guia de decisão

> Esta seção é apoio técnico **[RECOMENDAÇÃO]** — o enunciado só pede testes "coerentes com as escalas", tamanho de efeito, correção para múltiplas comparações e margem de erro. Os testes devem ser **os mesmos do plano de análise da Parte 1**; mudou? Vai para o log de desvios.

### 6.1 Qual teste para qual situação

| Pergunta | Variáveis | Teste | Tamanho de efeito |
|---|---|---|---|
| Associação entre duas categóricas | Nominal × nominal | **χ² de independência** (se esperado < 5 em muitas células: **Fisher exato**, 2×2) | **V de Cramér** (ou φ em 2×2) |
| Comparar 2 grupos independentes | Ordinal (Likert) ou não normal × nominal (2 níveis) | **Mann-Whitney U** | **r de ranking biserial** ou **δ de Cliff** |
| Comparar ≥ 3 grupos independentes | Ordinal × nominal (≥3) | **Kruskal-Wallis H** (+ post-hoc **Dunn** com correção) | **ε²** (= H/(n−1)) ou η²_H |
| Associação monotônica | Ordinal × ordinal / ordinal × razão | **Correlação de Spearman (ρ)** | O próprio **ρ** (|ρ|: ~0,1 pequeno, ~0,3 médio, ~0,5 grande) |
| Comparar 2 medidas pareadas | Ordinal pareada | **Wilcoxon (sinais-postos)** | r = Z/√N |
| Proporção de uma categoria | Nominal | **IC de proporção** (Wilson) / margem de erro | — |

Princípios:
- **Likert de item único = ordinal** → testes não paramétricos. Média e desvio de itens Likert isolados são discutíveis; prefira mediana, IQR e distribuição. Para **escores de construto** (soma/média de vários itens) pode-se discutir tratar como intervalar, **desde que o protocolo diga isso** e declare a justificativa.
- O teste deve bater com o **plano da Parte 1**. Trocar de teste depois de ver os dados deve ser declarado como desvio.
- **p-valor sem tamanho de efeito não responde nada**; efeito sem n/IC também não. Reporte os dois.

### 6.2 Interpretação de tamanhos de efeito (referências usuais — declare qual convenção usa)

| Medida | Pequeno | Médio | Grande |
|---|---:|---:|---:|
| V de Cramér (gl=1) | 0,10 | 0,30 | 0,50 |
| r ranking biserial / r | 0,10 | 0,30 | 0,50 |
| δ de Cliff (|δ|) | 0,147 | 0,33 | 0,474 |
| ε² (Kruskal-Wallis) | 0,01 | 0,08 | 0,26 |
| ρ de Spearman (|ρ|) | 0,10 | 0,30 | 0,50 |

> Os limiares variam por autor (Cohen, Romano et al. para δ de Cliff, etc.). **Escolha uma convenção, cite, e use sempre a mesma.** Com amostra pequena, tamanho de efeito pode ser grande sem significância: relate e diga que é inconclusivo, não que "não existe efeito".

### 6.3 Múltiplas comparações

- Se o plano prevê **vários testes** (várias RQs, vários segmentos, várias correlações), controle o erro: **Holm** (recomendado, mais potente que Bonferroni) ou Bonferroni, ou **Benjamini–Hochberg (FDR)** para muitos testes exploratórios.
- Reporte **p bruto e p ajustado**, e diga **qual família de testes** foi considerada.
- Os segmentos de filtro do dashboard são **exploratórios**: se o usuário filtra e testa livremente, o dashboard deve avisar que p-valores por segmento **não estão ajustados** (ou ajustar).

### 6.4 Alfa de Cronbach

```
α = k/(k−1) · (1 − Σσ²_item / σ²_total)
```
`k` = nº de itens do construto; `σ²_item` = variância de cada item; `σ²_total` = variância da soma dos itens.
Calcular só sobre **casos completos** do construto, com itens invertidos já recodificados.

### 6.5 Margem de erro

Fórmula do enunciado (proporção, 95% de confiança):

```
e = 1,96 × √( p(1 − p) / n )
```

Pior caso (p = 0,5):

| n (válidas) | Margem de erro (±p.p.) |
|---:|---:|
| 30 | 17,9 |
| 40 | 15,5 |
| 50 | 13,9 *(o enunciado cita ≈ ±14)* |
| 75 | 11,3 |
| 100 | 9,8 |
| 200 | 6,9 |
| 385 | 5,0 |

Regras de uso:
- A margem se aplica ao **n do recorte**: ao filtrar um segmento com n=12, a margem passa a ≈ ±28 p.p.
- Vale como **referência** para amostras probabilísticas. Para **conveniência/bola de neve**, a fórmula é indicativa — declare isso como limitação (não há garantia de representatividade).
- **Conclusões devem respeitar esse limite (R-05):** se duas proporções diferem em 8 p.p. e a margem é ±14, **não há base para dizer que diferem**. Essa é uma das perguntas mais prováveis na defesa.
- Com **população pequena e conhecida** (ex.: uma única organização), é possível aplicar a **correção de população finita** `√((N−n)/(N−1))`; só use se tiver N confiável e declare no protocolo/metodologia.

### 6.6 Respostas abertas

O plano da Parte 1 deve ter dito como codificar. Apresente no dashboard: esquema de categorias, nº de respostas por categoria e **quem codificou** (ideal: dois codificadores + concordância, ex. κ de Cohen). Se codificou só um, declare como limitação. Nunca exibir trechos que identifiquem o respondente.

---

## 7. Evidências da coleta (como montar)

### 7.1 Opção A — Carta de anuência

- Documento assinado pela organização autorizando a aplicação do survey.
- Deve constar: organização, responsável, objetivo do estudo, autorização, data, assinatura.
- **Cuidado com dados pessoais:** a carta identifica a **organização** e o responsável institucional (isso é esperado), mas **não pode listar respondentes**. Tarje o que não for necessário (ex.: CPF, telefone pessoal).
- Se a organização exigir sigilo do nome, combinar com o professor **antes** de entregar; use a versão tarjada só mediante acordo.
- Consequência: habilita o mínimo de **30 respostas válidas** (R-02) **se** o survey foi aplicado em **uma única organização**.

### 7.2 Opção B — Registros digitais (os 3 itens)

| Item | O que entregar | Como proteger dados pessoais |
|---|---|---|
| (1) Exportação bruta do formulário com data/hora de cada resposta | CSV/XLSX original, **sem edição**, com coluna de carimbo de data/hora | Remover/anonimizar colunas de identificação (nome, e-mail, IP). **Se o formulário nunca coletou identificadores, é o cenário ideal.** Anotar no documento quais colunas foram removidas. |
| (2) Capturas **datadas** dos canais de divulgação | Prints de posts/mensagens/e-mails com data visível (LinkedIn, grupos, Slack/Discord, e-mail, etc.) | Tarjar nomes e fotos de terceiros que reagiram/comentaram; manter data, canal e texto da divulgação |
| (3) Acesso ao painel do formulário **durante a apresentação** | Abrir o painel (Forms/Google Forms) ao vivo na defesa e mostrar o contador de respostas e a aba de respostas | Preparar a tela para **não exibir** e-mail/conta pessoal de respondentes; mostrar só agregados/contagem |

**[RECOMENDAÇÃO] Pacote mínimo antes da defesa:**
- [ ] Export bruto + SHA-256 registrado no repositório.
- [ ] Prints datados de **cada** canal de divulgação, com data do print e período da coleta.
- [ ] Conta com acesso ao painel do formulário **logada e testada** antes de apresentar (e quem tem acesso é o dono do formulário — evitar o "só o fulano acessa e faltou").
- [ ] Evidência do **consistente com o protocolo**: canais usados ⊂ canais previstos, período real vs. planejado.
- [ ] Prova de que a coleta começou **depois** do protocolo (commit com data + 1ª resposta com timestamp posterior).

### 7.3 Consistência exigida (peso de C1 = 2,0 pts)

C1 avalia **evidências + consistência dos dados com o protocolo**. Construam uma tabela de consistência e levem para a defesa:

| Item do protocolo | Planejado | Executado | Consistente? | Se não: ver desvio nº |
|---|---|---|---|---|
| População-alvo | | | | |
| Estratégia de amostragem | | | | |
| n pretendido / margem de erro | | | | |
| Canais de divulgação | | | | |
| Período de coleta | | | | |
| Instrumento (itens/escalas) | | | | |
| Plano de análise (testes) | | | | |
| Ética/LGPD (TCLE, anonimização, armazenamento) | | | | |

---

## 8. Log de desvios (modelo)

Todo desvio é aceito **se declarado e justificado** (R-04). Este log alimenta a Página 6 do dashboard (D-06).

| # | Seção do protocolo | O que estava planejado | O que foi executado | Motivo | Impacto na validade/análise | Mitigação |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |

**Exemplos típicos (só para orientar o raciocínio, não presumir que ocorreram):**
- n obtido menor que o pretendido → margem de erro real maior.
- Canal previsto não rendeu respostas → substituído por outro.
- Item removido/alterado após o pré-teste ou durante a coleta.
- Teste estatístico trocado por violação de pressuposto ou n pequeno em células.
- Período de coleta estendido/encurtado.
- Segmento colapsado por n pequeno (ex.: juntar duas faixas de experiência).

**Regra:** desvio descoberto na defesa **sem** estar declarado é pior do que o desvio em si. Declare cedo.

---

## 9. Defesa ao vivo (C5 = 2,0 pts)

### 9.1 Roteiro de 10 minutos **[RECOMENDAÇÃO]**

| Tempo | Conteúdo | Quem |
|---|---|---|
| 0:00–1:00 | Tema, objetivo GQM, RQs (1 frase cada) | `[PREENCHER]` |
| 1:00–2:30 | Perfil da amostra: recebidas/válidas/descartadas + motivos; mínimo atendido | `[PREENCHER]` |
| 2:30–4:00 | Evidências da coleta: abrir painel do formulário, mostrar export bruto com timestamps, canais, (carta) | `[PREENCHER]` |
| 4:00–5:30 | Likert divergente + confiabilidade (α) | `[PREENCHER]` |
| 5:30–8:00 | Respostas às RQs: teste, p, efeito, margem de erro, conclusão; **demonstrar um filtro por segmento ao vivo** | `[PREENCHER]` |
| 8:00–9:00 | Desvios, limitações, ameaças à validade | `[PREENCHER]` |
| 9:00–10:00 | Síntese + abertura para mudança de cenário | `[PREENCHER]` |

Dicas práticas: dashboard já aberto e logado; plano B offline (prints + PDF) se a internet cair; **ensaiar com cronômetro**; todos devem poder responder sobre qualquer página.

### 9.2 Mudança de cenário (P-02)

O professor propõe uma alteração; vocês dizem o que mudaria no **planejamento** ou na **análise**. Estrutura de resposta que funciona:

> **1) Entendo a mudança → 2) Qual parte do protocolo afeta (RQ, população, amostragem, instrumento, teste, validade) → 3) O que mudaria no planejamento → 4) O que mudaria na análise/teste/efeito/margem de erro → 5) Que ameaça à validade surge ou some.**

**Banco de cenários para ensaiar (e como pensar cada um):**

| Cenário possível | Eixo afetado | Raciocínio esperado |
|---|---|---|
| "E se a população fosse só uma empresa?" | População, amostragem, anuência | Carta de anuência; mínimo cai p/ 30; generalização restringe; possível correção de população finita; ameaça de desejabilidade social/hierarquia |
| "E se o n fosse a metade?" | Margem de erro, potência | Recalcular margem (ex.: de ±14 p.p. com 50 → ±20 com ≈25); testes com menos potência; mais conclusões "inconclusivas" |
| "E se quisessem comparar 4 grupos em vez de 2?" | Teste, múltiplas comparações | Mann-Whitney → Kruskal-Wallis + post-hoc Dunn; correção (Holm); ε² como efeito; n por grupo |
| "E se a escala fosse intervalar/contínua (não Likert)?" | Escala, teste | Checar normalidade/variâncias; t de Welch/ANOVA ou continuar não paramétrico; efeito = d de Cohen / η² |
| "E se a amostragem fosse probabilística?" | Amostragem, validade externa | Margem de erro passa a ter interpretação inferencial direta; menos autosseleção; precisa de lista (quadro amostral) |
| "E se houvesse muita não resposta?" | Validade | Comparar respondentes × população conhecida; reforçar canais; ponderação (se houver dados); declarar viés |
| "E se a variável de interesse fosse medida em dois momentos?" | Delineamento | Dado pareado: Wilcoxon; discutir atrito e efeito de teste; deixa de ser survey transversal |
| "E se um item do construto fosse invertido/removido?" | Confiabilidade | Recalcular α; α se item removido; revalidar o construto |
| "E se a pergunta de pesquisa fosse causal?" | Inferência | Survey transversal não prova causa; só associação; confundidores; propor outro desenho (quase-experimento/experimento) |
| "E se o foco fosse um subgrupo pequeno?" | Margem, potência | Margem do subgrupo muito maior; agregar/oversampling; resultado exploratório |

### 9.3 Arguição individual (P-03/P-04)

Cada integrante recebe **uma pergunta** sobre o trabalho **todo**. Treino: cada pessoa explica, sem olhar, as 10 perguntas abaixo.

**Banco de perguntas (todos devem saber responder):**

*Planejamento e GQM*
1. Qual é o objetivo no template GQM e que métricas derivam dele?
2. Quais eram as RQs e como cada uma se liga a itens e métricas do questionário?
3. Qual a população-alvo e como contataram os respondentes?

*Amostragem e margem de erro*
4. Qual estratégia de amostragem e por que não é probabilística (se não for)? O que isso limita?
5. Qual a margem de erro obtida e o que ela permite/impede concluir? Como calculou?
6. Por que n mínimo era 50 (ou 30)? O que mudaria com n diferente?

*Dados e qualidade*
7. Quantas respostas foram recebidas/descartadas? Quais os critérios de descarte e quem os definiu **antes de ver os resultados**?
8. Para que serve a pergunta de atenção? Quantos falharam?
9. O que é o alfa de Cronbach, qual o valor de cada construto e o que significa um α baixo?
10. Por que itens Likert são tratados como ordinais? Que consequência tem para os testes?

*Estatística*
11. Por que este teste e não outro (escala/pressupostos)?
12. O que é o p-valor — e o que **não** é?
13. O que é o tamanho de efeito e por que reportá-lo junto do p-valor?
14. Para que serve a correção de múltiplas comparações e qual foi aplicada?
15. Se p < 0,05 mas o efeito é pequeno, o que concluir? E se p > 0,05 com efeito grande?

*Validade e ética*
16. Quais ameaças à validade se manifestaram (não resposta, autosseleção, desejabilidade social)? Como mitigaram?
17. Quais foram os desvios do protocolo? Por quê?
18. Como o TCLE/LGPD foi cumprido? Como os dados foram anonimizados e armazenados?
19. O que **não** se pode concluir deste estudo?
20. O que fariam diferente se repetissem?

---

## 10. Critérios de aceitação (Definition of Done)

### 10.1 Obrigatórios (sem isso, perde pontos diretos)

- [ ] **D-00** Dashboard lê o **dado bruto** (ou pipeline reprodutível a partir dele), não imagem pronta.
- [ ] **D-01** Recebidas, descartadas e **motivo de cada descarte**; a soma fecha.
- [ ] **D-02** Likert em **barras divergentes**.
- [ ] **D-03** Cada RQ: **teste + p-valor + tamanho de efeito + margem de erro**.
- [ ] **D-04** **Filtros por segmento**.
- [ ] **D-05** **Alfa de Cronbach** por construto multi-item.
- [ ] **D-06** Página de **metodologia e desvios**.
- [ ] **E-A ou E-B** (preferir ambas), **sem dados pessoais**.
- [ ] **R-01/R-02** Mínimo de respostas **válidas** atingido.
- [ ] **R-03** Nenhum colega da turma como amostra (salvo justificativa no protocolo).
- [ ] **R-08** Protocolo com data comprovada **anterior** à 1ª resposta.
- [ ] **R-05** Conclusões respeitam a margem de erro.
- [ ] Todos os integrantes dominam o estudo inteiro.

### 10.2 Qualidade extra (aumenta a robustez na defesa)

- [ ] SHA-256 do CSV bruto registrado.
- [ ] Script de limpeza versionado e reprodutível.
- [ ] Codebook completo e coerente com o protocolo.
- [ ] Tabela de consistência protocolo × execução (seção 7.3).
- [ ] Aviso de n pequeno nos filtros por segmento.
- [ ] Aviso de p-valores não ajustados em exploração por segmento.
- [ ] Plano B offline para a defesa.
- [ ] Ensaio cronometrado de 10 minutos e rodada da arguição (seção 9.3).

---

## 11. Riscos e armadilhas comuns

| Risco | Por que dói | Como evitar |
|---|---|---|
| Dashboard só com prints/imagens | Viola D-00 (explícito no enunciado) | Conectar ao CSV/planilha bruta |
| "Válidas" abaixo do mínimo após limpeza | Reprova na regra de coleta | Coletar com folga; decidir critérios cedo |
| Descartes sem motivo registrado | Perde D-01 e C2 | Coluna `motivo_descarte` obrigatória |
| Critérios de descarte definidos olhando os resultados | Parece manipulação (R-07) | Fixar regra antes; documentar quando |
| Primeira resposta **antes** do protocolo | Quebra a lógica do pré-registro (R-08) | Conferir `min(timestamp)` vs. data do commit |
| Testes diferentes do plano da Parte 1 sem declarar | Perde C1/C4 | Log de desvios |
| p-valor sem tamanho de efeito (ou o contrário) | Perde C3 | Sempre reportar os dois + margem de erro |
| Concluir além da margem de erro | Viola R-05 | Revisar toda frase conclusiva contra ±e |
| Média/DP em item Likert sem justificar | Incoerência com a escala ordinal | Mediana/distribuição; ou justificar escore de construto |
| Segmento com n minúsculo virando conclusão | Margem enorme; instabilidade | Aviso de n mínimo; agregar categorias (e declarar) |
| Várias comparações sem correção | Falsos positivos | Holm/BH; reportar p ajustado |
| Dados pessoais em prints/export/carta | Viola a regra de evidências + LGPD | Revisão de privacidade antes do envio |
| Só uma pessoa entende o dashboard | Arguição individual (C5) | Todos ensaiam as 20 perguntas |
| Painel do formulário inacessível na defesa | Perde a evidência (3) da opção B | Testar acesso antes; dono presente e logado |
| α calculado sem recodificar itens invertidos | Valor errado | Recodificar antes |
| Mudança de cenário respondida de forma vaga | Perde pontos de C5 | Usar a estrutura de 5 passos (seção 9.2) |

---

## 12. Cronograma reverso **[RECOMENDAÇÃO]**

> Ajustar às datas reais. Hoje é 22/11/2026 (domingo); vencimento no Canvas: sexta, 12:00.

| Quando | Entrega interna |
|---|---|
| Quanto antes | Fechar exportação do formulário; gerar SHA-256; congelar o bruto |
| D-4 | Script de limpeza + tabela de descartes fechando |
| D-3 | Estatística de todas as RQs + α; revisão cruzada dos números |
| D-2 | Dashboard completo (6 páginas) + log de desvios + pacote de evidências sem dados pessoais |
| D-1 | Revisão de privacidade; ensaio cronometrado; rodada de arguição individual |
| Entrega | Upload no Canvas (formato a confirmar — ver 13) |
| Defesa | Plano B offline; dashboard e painel do formulário logados |

---

## 13. Pontos a confirmar com o professor/Canvas

O enunciado deixa estes pontos em aberto; **não assumir**:

1. **O que exatamente subir no Canvas?** A tarefa diz "enviando um upload de arquivo". Sugestão: um **PDF** com link do dashboard (acesso liberado), prints das páginas, evidências sem dados pessoais e o log de desvios — **confirmar** se o professor quer também o arquivo do dashboard/repositório.
2. **Data/hora exata do vencimento** (o PDF diz apenas "sexta-feira por 12:00").
3. **Data da defesa** e ordem dos grupos.
4. Se o dashboard precisa estar **acessível por link público** ou basta demonstração ao vivo.
5. Se a carta de anuência pode ter o nome da organização **tarjado**.
6. Convenção de **tamanho de efeito** esperada (nenhuma é imposta no enunciado).

---

## Anexo A — Trechos de código de apoio (Python)

> **[RECOMENDAÇÃO]** Funções utilitárias para a Página 3 e 5. Requerem `numpy`, `pandas`, `scipy`. Se a ferramenta do dashboard não for Python (Power BI, Looker, Excel), use como **referência de cálculo** para conferir os números.

```python
import numpy as np
import pandas as pd
from scipy import stats

# ---------- Margem de erro (proporção, 95%) ----------
def margem_erro(n, p=0.5, z=1.96):
    return z * np.sqrt(p * (1 - p) / n)          # em fração; *100 para p.p.

# ---------- Alfa de Cronbach (casos completos; itens já recodificados) ----------
def cronbach_alpha(df_itens: pd.DataFrame) -> float:
    d = df_itens.dropna()
    k = d.shape[1]
    if k < 2 or len(d) < 2:
        return np.nan
    var_itens = d.var(axis=0, ddof=1).sum()
    var_total = d.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - var_itens / var_total)

def alpha_sem_item(df_itens: pd.DataFrame) -> pd.Series:
    return pd.Series({c: cronbach_alpha(df_itens.drop(columns=c)) for c in df_itens.columns})

# ---------- Mann-Whitney + tamanho de efeito (rank-biserial) ----------
def mann_whitney(a, b):
    a, b = pd.Series(a).dropna(), pd.Series(b).dropna()
    u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
    r_rb = 2 * u / (len(a) * len(b)) - 1          # rank-biserial (sinal conforme U de 'a')
    return {"U": u, "p": p, "r_rank_biserial": r_rb, "n_a": len(a), "n_b": len(b)}

# ---------- Cliff's delta (a vs b) ----------
def cliffs_delta(a, b):
    a, b = np.asarray(pd.Series(a).dropna()), np.asarray(pd.Series(b).dropna())
    maiores = sum((x > b).sum() for x in a)
    menores = sum((x < b).sum() for x in a)
    return (maiores - menores) / (len(a) * len(b))

# ---------- Kruskal-Wallis + epsilon² ----------
def kruskal(*grupos):
    gs = [pd.Series(g).dropna() for g in grupos]
    h, p = stats.kruskal(*gs)
    n = sum(len(g) for g in gs)
    return {"H": h, "p": p, "epsilon2": h / (n - 1), "n": n, "k": len(gs)}

# ---------- Qui-quadrado + V de Cramér ----------
def qui_quadrado(tabela: pd.DataFrame):
    chi2, p, dof, esperado = stats.chi2_contingency(tabela, correction=False)
    n = tabela.values.sum()
    v = np.sqrt(chi2 / (n * (min(tabela.shape) - 1)))
    return {"chi2": chi2, "p": p, "gl": dof, "V_cramer": v, "n": n,
            "celulas_esperado_lt5": int((esperado < 5).sum())}

# ---------- Spearman ----------
def spearman(x, y):
    d = pd.concat([pd.Series(x), pd.Series(y)], axis=1).dropna()
    rho, p = stats.spearmanr(d.iloc[:, 0], d.iloc[:, 1])
    return {"rho": rho, "p": p, "n": len(d)}

# ---------- Correção para múltiplas comparações (Holm) ----------
def holm(pvals):
    p = np.asarray(pvals, dtype=float)
    m = len(p)
    ordem = np.argsort(p)
    ajust = np.empty(m)
    maximo = 0.0
    for rank, idx in enumerate(ordem):
        val = (m - rank) * p[idx]
        maximo = max(maximo, val)
        ajust[idx] = min(1.0, maximo)
    return ajust

# ---------- Dados para barras divergentes (Likert 1..5) ----------
def dados_divergentes(df_likert: pd.DataFrame, niveis=(1, 2, 3, 4, 5)):
    """Retorna % por nível, por item, e colunas auxiliares para centrar o neutro em 0."""
    pct = df_likert.apply(lambda s: s.value_counts(normalize=True)
                          .reindex(niveis, fill_value=0) * 100).T
    n = df_likert.notna().sum()
    neutro = niveis[len(niveis) // 2]
    esq = pct[[c for c in niveis if c < neutro]].sum(axis=1) + pct[neutro] / 2
    dir_ = pct[[c for c in niveis if c > neutro]].sum(axis=1) + pct[neutro] / 2
    return pct.assign(n=n, discorda_total=esq, concorda_total=dir_)
```

**Avisos de uso do código:**
- Rodar em dados **reais** do projeto e conferir contra uma segunda ferramenta (planilha ou outro pacote) antes de apresentar.
- Mann-Whitney/rank-biserial: o sinal depende de qual grupo é "a". Declare a direção na interpretação.
- Para Kruskal-Wallis com ≥3 grupos significativo, use post-hoc **Dunn** (ex.: pacote `scikit-posthocs`) com correção de Holm.
- Para χ² com muitas células de esperado < 5, use Fisher exato (2×2) ou agregue categorias (e registre o desvio).

---

## Anexo B — Texto-modelo para a Página de Metodologia e Desvios

> Preencher com dados reais. Não presumir nada que não tenha ocorrido.

**Protocolo (Parte 1).** Entregue em `[DATA/HORA]` (`[commit/Canvas]`). Objetivo GQM: `[...]`. Questões de pesquisa: `[RQ1...]`. População-alvo: `[...]`. Amostragem: `[tipo]`; n pretendido `[X]` (margem de erro planejada ±`[Y]` p.p.).

**Execução.** Coleta de `[DATA]` a `[DATA]` via `[canais]`. Recebidas: `[N]`. Descartadas: `[N]` (`[detalhe por motivo]`). Válidas: `[N]`. Margem de erro efetiva (p=0,5, 95%): ±`[Z]` p.p.

**Desvios.** `[tabela da seção 8]`.

**Limitações.** Amostra `[tipo]`: os resultados descrevem esta amostra e não podem ser generalizados para `[população]` sem ressalvas. `[não resposta / autosseleção / desejabilidade social: como se manifestaram]`.

**Ética e LGPD.** TCLE `[como foi coletado]`; anonimização `[como]`; armazenamento `[onde/quem acessa]`; dados brutos `[política de retenção/descarte]`.

---

## Anexo C — Referências do enunciado

- KITCHENHAM, B.; PFLEEGER, S. L. *Personal opinion surveys*. In: SHULL, F.; SINGER, J.; SJØBERG, D. (ed.). *Guide to Advanced Empirical Software Engineering*. London: Springer, 2008.
- WOHLIN, C. et al. *Experimentation in Software Engineering*. Berlin: Springer, 2012.

---

## Anexo D — Rastreabilidade enunciado → este documento

| Trecho do enunciado | Onde está aqui |
|---|---|
| "Dashboard… deve ler os dados brutos" | D-00, seção 4 |
| Perfil da amostra / descartes e motivos | D-01, Página 1, 4.4 |
| Likert em barras divergentes | D-02, Página 2 |
| RQ com teste, p-valor, efeito, margem de erro | D-03, Página 3, seção 6 |
| Filtros por segmento | D-04, Página 4 |
| Alfa de Cronbach | D-05, Página 5, 6.4 |
| Metodologia e desvios | D-06, Página 6, seção 8 |
| Evidências (carta ou registros digitais), sem dados pessoais | E-A, E-B, E-X, seção 7 |
| Demonstração ao vivo, 10 min | P-01, 9.1 |
| Mudança de cenário | P-02, 9.2 |
| Arguição individual / todos dominam o estudo | P-03, P-04, 9.3 |
| Mínimo 50 (ou 30 com anuência) | R-01, R-02 |
| Colegas não contam | R-03 |
| Dados ↔ protocolo; desvios declarados | R-04, seção 8 |
| Margem de erro e conclusões dentro do limite | R-05, 6.5 |
| Respostas fabricadas / dados manipulados | R-07 |
| Rubrica (C1–C5) | Seção 1 |
