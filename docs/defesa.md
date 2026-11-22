# Defesa ao vivo: roteiro, arguição e cenários

Apoio para C5 (2,0 pts). Todos os números abaixo foram recalculados em 22/11/2026 (ver `dashboard/conferencia_rqs.py` e `conferencia_alfa.py`). **Responsáveis em `[CONFIRMAR]`: o grupo decide quem apresenta cada bloco.** A divisão sugerida é só ponto de partida. Qualquer integrante pode ser arguido sobre qualquer bloco.

## 1. Antes de começar (checklist)

- [ ] Dashboard aberto em https://survey-ia-medicao-es.streamlit.app/ **e** local (`streamlit run dashboard/app.py`) como reserva.
- [ ] Painel do Google Formulários aberto com a conta do dono, logada e testada (nunca exibir e-mails de respondentes). Ferramenta confirmada: **Google Formulários** (link em `docs/ENTREGA.md`). O painel deve mostrar 90 respostas.
- [ ] Export bruto, `SHA256SUMS.txt`, print do Canvas (13/11 9:17) e print do convite (17/11) à mão.
- [ ] Plano B offline: PDF com prints das 6 páginas, caso a internet caia.
- [ ] Ensaio com cronômetro, duas vezes.

## 2. Roteiro de 10 minutos

| Tempo | Conteúdo | Responsável (sugestão) |
|---|---|---|
| 0:00–1:00 | Tema, objetivo GQM e as 3 RQs, uma frase cada | `[CONFIRMAR]` Pessoa 1 |
| 1:00–2:30 | Perfil: 90 recebidas, 21 descartadas (11 T1, 10 AT1), 69 válidas; mínimo de 50 atendido; linha do tempo | Pessoa 2 |
| 2:30–4:00 | Evidências: painel do Forms, export com carimbos, hash, print do Canvas, print do convite. **Declarar a lacuna D8 antes de ser perguntado** | Pessoa 3 |
| 4:00–5:30 | Likert divergente e α = 0,675 (< 0,70, declarado) | Pessoa 4 |
| 5:30–8:00 | RQ1, RQ2, RQ3 com teste, p, efeito e margem; **filtro por segmento ao vivo** | Pessoa 5 |
| 8:00–9:00 | Desvios D1 a D8, limitações, ameaças | Pessoa 1 |
| 9:00–10:00 | Síntese e abertura para mudança de cenário | Pessoa 2 |

## 3. Números que todos devem saber de cabeça

| Item | Valor |
|---|---|
| Recebidas / válidas / descartadas | 90 / 69 / 21 (11 inelegíveis por T1 + 10 por AT1) |
| Janela real | 13/11 20:46 a 19/11 17:50 (protocolo enviado 13/11 9:17) |
| Respostas por dia | 13/11: 1 · 16/11: 21 · **17/11: 65** · 18/11: 2 · 19/11: 1 |
| Margem de erro | ±11,8 p.p. (pior caso, n = 69); planejado ±13,9 com n = 50 |
| RQ1 | 55 acima do neutro, 1 abaixo, 13 empates (n efetivo 56). Sinal exato, p ≈ 1,6·10⁻¹⁵ (Holm 4,7·10⁻¹⁵). 79,7% de PP_med ≥ 4 |
| RQ2 | Spearman U1 × PP_med: ρ = 0,367, p = 0,0019 (Holm 0,0038). Efeito médio |
| RQ3 | Spearman P1 × PP_med: ρ = 0,058, p = 0,637. **Inconclusivo**, não "sem efeito" |
| α de Cronbach | 0,6746 com PP5 recodificado (6 − x). 0,3936 se **não** recodificar. 0,6966 sem PP5 |

## 4. Respostas-chave da arguição (Fonte 9.3)

1. **Por que Likert é ordinal?** A distância entre "Concordo" e "Concordo totalmente" não é garantida igual. Por isso testes não paramétricos (sinal, Spearman) e mediana por pessoa (PP_med), não média.
2. **O que a margem de ±11,8 p.p. permite?** Dizer que a proporção da amostra tem essa precisão **se** a amostra fosse probabilística. Não é: é conveniência com bola de neve. Vale como referência, não como garantia de representatividade. Duas proporções que diferem menos que a margem não permitem afirmar diferença.
3. **Por que descartar 10 por AT1?** A pergunta de atenção pedia "Discordo". A regra foi fixada no protocolo **antes** da coleta. Mudar depois de ver os dados seria manipulação (R-07). Se perguntarem sobre quem marcou "Discordo totalmente" (9 dos 10, segundo a auditoria anterior), a resposta é a mesma: critério objetivo, pré-registrado.
4. **Por que α = 0,675 e o que fazer?** Abaixo do 0,70 pré-declarado. O construto mistura rapidez, qualidade e esforço, e PP5 (invertido) tem a menor correlação item-total. O dashboard mostra α sem cada item e subescalas. Sem PP5, α = 0,697. A análise usa a mediana, então o α é indício indireto.
5. **p-valor?** Probabilidade de resultado tão extremo quanto o observado **se H0 fosse verdadeira**. Não é a probabilidade de H0 ser verdadeira nem o tamanho do efeito.
6. **Por que efeito junto do p?** p pequeno com n grande pode vir de efeito trivial; efeito grande com n pequeno pode ter p alto. RQ2: efeito médio e IC largo (0,15 a 0,55). RQ3: efeito desprezível com IC que não exclui efeito pequeno.
7. **Por que Holm?** São três testes confirmatórios. Holm controla o erro de falso positivo da família e é mais potente que Bonferroni. Segmentos filtrados no dashboard são exploratórios e **não** ajustados.
8. **De onde vieram as respostas?** Evidência datada só do grupo de trabalho (17/11, 11:06). 22 respostas (13 e 16/11) não têm registro de canal. Declarado em D8. O carimbo do export prova **quando**, não **de onde**. Não inventar origem.
9. **O convite mencionou produtividade.** Sim (D7). Risco de autosseleção e desejabilidade social. Mitigação: conclusões só sobre produtividade **percebida** nesta amostra.
10. **O que não se pode concluir?** Nada sobre desenvolvedores do Brasil (amostra de conveniência, 78% em empresas com mais de 200 pessoas, 61% com 0 a 2 anos de experiência). Nada causal (survey transversal). Nada sobre produtividade real.
11. **O que fariam diferente?** Guardar print de cada convite na hora, usar mais de um canal, ter segundo codificador para "Outra", dividir a coleta em mais dias.
12. **LGPD?** TCLE (C0), sem identificadores no formulário, texto livre descartado na leitura do dashboard (D1). Ponto fraco: o XLSX está num repositório público (decisão do grupo pendente).

## 5. Mudança de cenário (Fonte 9.2): estrutura e respostas rápidas

Estrutura: **(1)** entendo a mudança, **(2)** o que do protocolo ela afeta, **(3)** o que muda no planejamento, **(4)** o que muda na análise, **(5)** que ameaça surge ou some.

| Cenário | Resposta curta com os nossos números |
|---|---|
| Só uma empresa | Carta de anuência; mínimo cai para 30; generalização ainda mais restrita; pode usar correção de população finita se N for confiável; surge risco de hierarquia e desejabilidade social. |
| n pela metade (≈ 35) | Margem sobe de ±11,8 para ≈ ±16,6 p.p.; RQ2 perde potência (com n ≈ 70 só |ρ| ≥ 0,33 é detectado com 80% de poder); mais resultados inconclusivos. Abaixo de 50 viola R-01. |
| Comparar 4 grupos (ex.: porte) | Kruskal-Wallis com ε² e Dunn com Holm; vários grupos teriam n < 5 (ex.: autônomos = 4), então agregar categorias e declarar. |
| Escala contínua em vez de Likert | Checar normalidade; t de Welch ou Mann-Whitney; efeito d de Cohen; α deixa de ser a medida natural. |
| Amostragem probabilística | Margem passa a ter leitura inferencial; exige quadro amostral; reduz autosseleção e viés de rede. |
| Muita não resposta | Taxa de resposta hoje **não é calculável** (origem não registrada). Registrar convidados por canal, reforçar lembretes, comparar respondentes com a população conhecida. |
| Medir em dois momentos | Dado pareado: Wilcoxon; deixa de ser transversal; atrito e efeito de teste. |
| Remover/inverter item do construto | Recalcular α; já mostramos α sem PP5 (0,697) e subescalas. |
| Pergunta causal | Survey não prova causa. RQ2 pode ter causalidade reversa. Propor quase-experimento (ex.: antes e depois da adoção) ou experimento. |
| Foco em subgrupo pequeno (ex.: seniores, 7 pessoas) | Margem enorme (n = 7: ≈ ±37 p.p.); oversampling; resultado só exploratório. |
