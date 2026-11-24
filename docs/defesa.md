# Defesa ao vivo: roteiro, arguição e cenários

Apoio para C5 (2,0 pts). Os números abaixo foram recalculados em 22/11/2026 (`dashboard/conferencia_rqs.py` e `conferencia_alfa.py`). A divisão dos blocos é só de quem fala primeiro: **qualquer integrante pode ser arguido sobre qualquer bloco e sobre as 20 perguntas da seção 4.**

## 1. Antes de começar (checklist)

- [ ] Dashboard aberto em https://survey-ia-medicao-es.streamlit.app/ **e** local (`streamlit run dashboard/app.py`) como reserva.
- [ ] Painel do Google Formulários aberto com a conta do dono, logada e testada (nunca exibir e-mails de respondentes). Deve mostrar 90 respostas e o formulário fechado.
- [ ] Export bruto, `SHA256SUMS.txt`, print do Canvas (13/11 9:17) e prints de divulgação (16 e 17/11, `docs/evidencias/divulgacao/`) à mão.
- [ ] Plano B offline: PDF com prints das 6 abas, caso a internet caia.
- [ ] Dois ensaios com cronômetro (registrar na seção 6).

## 2. Roteiro de 8 minutos

| Tempo | Conteúdo | Quem fala |
|---|---|---|
| 0:00–2:00 | Tema, objetivo GQM em uma frase e as 3 RQs; aba "Perfil da amostra": 90 recebidas, 11 inelegíveis (T1), 10 descartadas (AT1), 69 válidas, mínimo de 50 atendido | **Marcos** |
| 2:00–3:15 | Evidências: painel do Forms (90 respostas), export com carimbos, hash, print do Canvas, prints de divulgação de 16 e 17/11. **Declarar a lacuna D8 antes de ser perguntado** | **Brenda** |
| 3:15–4:30 | Aba "Itens Likert" (divergente, PP5 recodificado) e aba "Confiabilidade" (α = 0,675, abaixo de 0,70, declarado) | **Bernardo** |
| 4:30–6:30 | RQ1, RQ2, RQ3: teste, p, efeito, margem, conclusão. **Filtro por segmento ao vivo** (ex.: tempo de experiência) | **Gabriel** |
| 6:30–8:00 | Desvios D1 a D8, limitações e ameaças; síntese em 3 frases e abertura para a mudança de cenário | **Gabriela** |

Os 8 minutos deixam folga dentro dos 10 da Fonte. Se o professor pedir para estender, o excedente vai para a demonstração do filtro e para a mudança de cenário.

**Falas de apoio**
- **Marcos:** "Estudamos a produtividade **percebida** de desenvolvedores no Brasil que usam assistentes de IA. RQ1: ela difere do ponto neutro? RQ2: associa-se à frequência de uso? RQ3: associa-se ao tempo de experiência? É autorrelato, transversal, e vale só para esta amostra."
- **Gabriela, síntese:** "RQ1 foi clara: a percepção fica acima do neutro. RQ2 mostrou associação média com a frequência de uso. RQ3 foi inconclusiva. Limites: amostra de conveniência, α abaixo de 0,70 e evidência de canal incompleta, tudo declarado."
- **Todos:** nunca dizer "a IA aumenta a produtividade". Dizer "a produtividade **percebida** é maior nesta amostra".

## 3. Números que todos devem saber de cabeça

| Item | Valor |
|---|---|
| Recebidas / válidas / descartadas | 90 / 69 / 21 (11 inelegíveis por T1 + 10 por AT1) |
| Janela real | 13/11 20:46 a 19/11 17:50 (protocolo enviado 13/11 9:17) |
| Respostas por dia | 13/11: 1 · 16/11: 21 · **17/11: 65** · 18/11: 2 · 19/11: 1 |
| Margem de erro | ±11,8 p.p. (pior caso, n = 69); planejado ±13,9 com n = 50 |
| RQ1 | 55 acima do neutro, 1 abaixo, 13 empates (n efetivo 56). Sinal exato, p ≈ 1,6·10⁻¹⁵ (Holm 4,7·10⁻¹⁵). 79,7% com PP_med ≥ 4 |
| RQ2 | Spearman U1 × PP_med: ρ = 0,367, p = 0,0019 (Holm 0,0038). Efeito médio |
| RQ3 | Spearman P1 × PP_med: ρ = 0,058, p = 0,637. **Inconclusivo**, não "sem efeito" |
| α de Cronbach | 0,6746 com PP5 recodificado (6 − x). 0,3936 se **não** recodificar. 0,6966 sem PP5 |
| AT1 | 10 descartes: **9 "Discordo totalmente"** e **1 "Concordo totalmente"** (conferido no XLSX). Os demais 69 marcaram "Discordo" |

## 4. As 20 perguntas da arguição (Fonte 9.3), com resposta

**Planejamento e GQM**

1. **Objetivo GQM e métricas.** Analisar o uso de assistentes de IA generativa no desenvolvimento, com o propósito de caracterizar, com respeito à produtividade percebida (nível, relação com a frequência de uso e variação com a experiência), do ponto de vista dos desenvolvedores, no contexto de quem trabalha com desenvolvimento no Brasil e usa IA. Métricas: **PP_med** (mediana de PP1 a PP5, com PP5 invertido), proporção com PP_med ≥ 4, **U1** (frequência), **U2** (dias de uso, robustez) e **P1** (anos de experiência).
2. **RQs, itens e métricas.** RQ1 usa PP1 a PP5 → PP_med. RQ2 usa U1 (e U2 como robustez) × PP_med. RQ3 usa P1 × PP_med. Os itens de perfil (P2 a P5) são filtros e covariáveis, sem hipótese própria. A tabela completa está em `docs/codebook.md`.
3. **População e contato.** Desenvolvedores que trabalham hoje com desenvolvimento no Brasil (emprego, estágio ou autônomo) e usaram IA nos últimos 3 meses. O protocolo previa contatos diretos e redes profissionais. Na prática, a divulgação foi em grupos de trabalho dos integrantes (D4), com um print datado (17/11). Não registramos a origem de cada resposta.

**Amostragem e margem de erro**

4. **Amostragem.** Não probabilística, por conveniência com bola de neve, porque não existe quadro amostral dos desenvolvedores do Brasil. Limita a generalização: os resultados descrevem estas 69 pessoas. Há autosseleção e viés de rede (78% em organizações com mais de 200 pessoas, 61% com 0 a 2 anos de experiência).
5. **Margem de erro.** e = 1,96 × √(p(1−p)/n). Com p = 0,5 e n = 69: ±11,8 p.p. Com a proporção observada (79,7%): ±9,5 p.p. Permite dizer que a proporção da amostra tem essa precisão, **se** fosse probabilística; aqui é só referência. Diferenças menores que a margem não sustentam conclusão (R-05).
6. **Por que 50.** É o mínimo do enunciado (R-01) para survey sem carta de anuência. Com 50 a margem seria ±13,9; com 69 foi ±11,8. Com 30 (caso de uma única organização com carta) seria ±17,9. Com n maior, a margem e a potência melhoram; com menor, pioram.

**Dados e qualidade**

7. **Recebidas, descartadas e critérios.** 90 recebidas, 11 inelegíveis e 10 descartadas, 69 válidas. Os critérios (encerrar se T1 = não, T2 = "outro" ou U1 = 1; descartar se AT1 ≠ "Discordo", item obrigatório em branco ou resposta repetida em sequência) foram **definidos pelo grupo no protocolo, entregue em 13/11 às 9:17, antes da primeira resposta** (20:46). Nenhuma regra foi alterada depois de ver os resultados.
8. **Pergunta de atenção (AT1).** Pedia "marque Discordo nesta linha". Serve para detectar leitura descuidada. Falharam 10 de 79 elegíveis (12,7%): 9 marcaram "Discordo totalmente" e 1 "Concordo totalmente". A regra é objetiva e pré-registrada: mudá-la depois de ver os dados seria manipulação (R-07). Risco reconhecido: parte dos 9 pode ter lido o item e escolhido o extremo; está em `limitacoes.md`.
9. **Alfa de Cronbach.** Mede a consistência interna dos itens de um construto. Aqui há um só construto multi-item (PP1 a PP5): **α = 0,675** [0,55; 0,77], abaixo do 0,70 definido antes da coleta. Isso é "questionável": o construto mistura rapidez, qualidade e esforço, e PP5 (invertido) tem a menor correlação item-total (0,28). Sem PP5, α = 0,697. A análise usa a mediana, então o α é só indício indireto. Mostramos subescalas e α sem cada item.
10. **Likert como ordinal.** A distância entre "Concordo" e "Concordo totalmente" não é garantidamente igual à entre "Discordo" e "Nem concordo". Por isso: mediana por pessoa (PP_med), teste do sinal e Spearman, e **nunca média ou teste t** em item isolado.

**Estatística**

11. **Por que este teste.** RQ1: o teste do sinal exato compara "acima" com "abaixo" do neutro 3, só pede escala ordinal. RQ2 e RQ3: Spearman, porque as duas variáveis são ordinais ou de razão e a relação esperada é monotônica, sem exigir normalidade. Eram os testes do plano da Parte 1.
12. **O que é o p-valor.** A probabilidade de observar um resultado tão extremo quanto o nosso **se H0 fosse verdadeira**. **Não** é a probabilidade de H0 ser verdadeira, nem mede o tamanho do efeito.
13. **Tamanho de efeito.** Mostra **quanto** (não só se há diferença). Com n grande, p pequeno pode vir de efeito trivial; com n pequeno, efeito grande pode ter p alto. Aqui: RQ1 proporção 0,982 acima entre os não empatados, RQ2 ρ = 0,367 (médio), RQ3 ρ = 0,058 (desprezível), todos com IC.
14. **Múltiplas comparações.** Rodamos 3 testes confirmatórios (uma família), então corrigimos com **Holm**, que controla o falso positivo e é mais potente que Bonferroni. Mostramos p bruto e ajustado. Segmentos filtrados no dashboard são **exploratórios** e não ajustados, e o dashboard avisa.
15. **p < 0,05 com efeito pequeno / p > 0,05 com efeito grande.** O primeiro é estatisticamente detectável, mas pode ser pouco relevante. O segundo é inconclusivo por falta de poder, não prova ausência de efeito. No nosso caso, RQ3 (ρ = 0,058, IC [−0,17; 0,28]) é inconclusiva, e com n ≈ 70 só |ρ| ≥ 0,33 é detectado com 80% de poder.

**Validade e ética**

16. **Ameaças que se manifestaram.** Autosseleção e viés de rede (quem se interessa por IA responde; 72% das respostas em um dia; só usuários respondem PP, o que favorece RQ1). Desejabilidade social, agravada pelo convite que citava "impactos na produtividade" (D7). Não resposta: taxa não calculável. Mitigação: conclusões só sobre produtividade **percebida** nesta amostra, e ameaças declaradas.
17. **Desvios.** D1 a D8 em `dashboard/desvios.md`: leitura do bruto com texto livre removido na leitura (D1), uma só pessoa codificou "Outra" (D2), coleta de 13 a 19/11 em vez de 11 a 20 (D3), canais (D4), convite sem o aviso aos colegas da turma (D5), protocolo enviado em 13/11 e não 10/11 (D6), convite menciona produtividade (D7), evidência de canal incompleta (D8). Cada um tem motivo, impacto e mitigação.
18. **LGPD.** TCLE como primeira página (C0 obrigatório), sem nome, e-mail, CPF, IP nem login, perfil em categorias, dados no Google Formulários e Planilhas (operador). O texto livre é removido na leitura do dashboard. Ponto fraco: o XLSX está num repositório público (carimbo + perfil + P1 podem, em redes pequenas, ajudar a reconhecer alguém); decisão registrada em `docs/evidencias/REVISAO_PRIVACIDADE.md`.
19. **O que não se pode concluir.** Nada sobre todos os desenvolvedores do Brasil (conveniência). Nada causal (transversal: RQ2 pode ter causalidade reversa). Nada sobre produtividade real, só percebida. Nada sobre RQ3: é inconclusiva.
20. **O que faríamos diferente.** Guardar o print de cada convite na hora, usar mais de um canal, ter segundo codificador para "Outra", manter o texto neutro do convite do protocolo e distribuir a coleta em mais dias.

**Se perguntarem de onde vieram as respostas de 13 e 16/11:** temos o carimbo (prova **quando**, não **de onde**) e os prints dos envios de 16/11 (grupos e mensagens individuais de WhatsApp, 13:09, 13:27, 18:34, 18:41 e 18:44) e de 17/11. 12 das 21 respostas de 16/11 chegaram em até ~20 min depois de um envio; a relação é temporal, o formulário não guarda origem. Sem print: a resposta de 13/11 e 9 de 16/11. Declarado em D8. **Não inventar origem.**

## 5. Mudança de cenário (Fonte 9.2): estrutura e respostas rápidas

Estrutura: **(1)** entendo a mudança, **(2)** o que do protocolo ela afeta, **(3)** o que muda no planejamento, **(4)** o que muda na análise, **(5)** que ameaça surge ou some.

| Cenário | Resposta curta com os nossos números |
|---|---|
| Só uma empresa | Carta de anuência; mínimo cai para 30; generalização ainda mais restrita; pode usar correção de população finita se N for confiável; surge risco de hierarquia e desejabilidade social. |
| n pela metade (≈ 35) | Margem sobe de ±11,8 para ≈ ±16,6 p.p.; RQ2 perde potência (com n ≈ 70 só \|ρ\| ≥ 0,33 é detectado com 80% de poder); mais resultados inconclusivos. Abaixo de 50 viola R-01. |
| Comparar 4 grupos (ex.: porte) | Kruskal-Wallis com ε² e Dunn com Holm; vários grupos teriam n < 5 (ex.: autônomos = 4), então agregar categorias e declarar. |
| Escala contínua em vez de Likert | Checar normalidade; t de Welch ou Mann-Whitney; efeito d de Cohen; α deixa de ser a medida natural. |
| Amostragem probabilística | Margem passa a ter leitura inferencial; exige quadro amostral; reduz autosseleção e viés de rede. |
| Muita não resposta | Taxa de resposta hoje **não é calculável** (origem não registrada). Registrar convidados por canal, reforçar lembretes, comparar respondentes com a população conhecida. |
| Medir em dois momentos | Dado pareado: Wilcoxon; deixa de ser transversal; atrito e efeito de teste. |
| Remover/inverter item do construto | Recalcular α; já mostramos α sem PP5 (0,697) e subescalas. |
| Pergunta causal | Survey não prova causa. RQ2 pode ter causalidade reversa. Propor quase-experimento (ex.: antes e depois da adoção) ou experimento. |
| Foco em subgrupo pequeno (ex.: seniores, 7 pessoas) | Margem enorme (n = 7: ≈ ±37 p.p.); oversampling; resultado só exploratório. |

## 6. Registro dos ensaios

| Ensaio | Data | Tempo total | Blocos que estouraram | Ajustes |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

**Rodada de arguição:** cada integrante sorteia 3 perguntas da seção 4 e responde sem olhar. Anotar quem hesitou e repetir.
