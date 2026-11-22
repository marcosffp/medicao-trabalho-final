# Auditoria da Parte 2 contra a Fonte da Verdade

**Data:** 22/11/2026 · **Base:** `Parte2_Dashboard_e_Evidencias_FONTE_DA_VERDADE.md` · **Estado auditado:** branch `main`, commit `3aba90e`

**Legenda:** ✅ atendido · ⚠️ atendido com ressalva ou risco · ❌ não atendido · ❓ não verificável por mim

**Como foi feito.** Li o protocolo v5 (`.md`), `dashboard/analise.py`, `dashboard/app.py`, `desvios.md`, `README.md`, `REVISAO_PRIVACIDADE.md` e as duas imagens de evidência. Recalculei o funil e as estatísticas executando `analise.py` sobre o XLSX bruto (pandas 2.3.3 e scipy 1.13.1, em ambiente isolado, não as versões do `requirements.txt`). Conferi o SHA-256 do XLSX. **Não executei o `app.py` (Streamlit)**, então a interface, os gráficos e a página de metodologia na tela não foram testados. **Não abri o PDF do protocolo**, e a comparação "planejado × PDF" usou o `.md`.

**Andamento dos P0 (22/11):** D7 registrado em `dashboard/desvios.md` (A5 resolvido) e D5 ampliado para os convites de 13 e 16/11 (R-03). **Andamento dos itens de alta prioridade (22/11):**
- **Alfa (item 5):** α = **0,6746** (recodificando PP5). O valor 0,3936 é o que sai **sem recodificar PP5**, então a outra auditoria errou ao não aplicar 6 − x. Conferido por duas implementações (`analise.py` e `dashboard/conferencia_alfa.py`, só `openpyxl` + `statistics`), que dão 0,3936 / 0,6746 / 0,6966 (sem PP5).
- **Tabela de consistência (6):** `dashboard/consistencia.md`, exibida na página de metodologia.
- **Gráfico por dia (7):** na página "Perfil da amostra", com a linha do envio do protocolo (13/11, 9:17) e a checagem R-08 (nova linha nas checagens automáticas).
- **Link (8):** declarado "apenas localmente" na Fonte da Verdade e no `dashboard/README.md`.
- **Ambiente limpo (9):** cópia limpa, Python 3.12, `requirements.txt` com versões fixas instalou sem erro. `streamlit run` respondeu `200` e o `AppTest` das 6 páginas rodou sem exceção, também com filtro ativo.
- **Metodologia (10):** `app.py` agora cita repetidas em sequência, T2 = "outro" e P1 não inteiro.
- **Codificação (11):** P4 confere (12 respondentes). **P5 estava errado: 15 respondentes, não 19**, e os fragmentos são 13 (P4) e 27 (P5). `desvios.md` D2 corrigido.

**Andamento dos itens 12 a 18 (22/11):** `docs/codebook.md`, `docs/regras_de_limpeza.md` e `README.md` da raiz criados; n por item nos gráficos; aviso de segmento pequeno (n < 10); `dashboard/limitacoes.md` na página de metodologia; avaliação da base pública em `docs/evidencias/REVISAO_PRIVACIDADE.md` (decisão do grupo pendente).

Seguem pendentes, e dependem do grupo, a recuperação dos prints de 13 e 16/11 (A1, A2) e o teste do painel do Forms (A6).

---

## 1. Resumo executivo

O núcleo está sólido: dados brutos preservados com hash válido, funil que fecha, regras de descarte pré-declaradas, estatística coerente com o plano da Parte 1 e desvios declarados com franqueza. Os riscos estão na **evidência (C1)** e na **defesa (C5)**, que juntas valem 4 dos 8 pontos.

**Pendências bloqueantes ou de alto risco:**

| # | Pendência | Critério | Gravidade |
|---|---|---|---|
| A1 | **Divulgação de 16/11 sem nenhuma evidência.** O único print é de 17/11 às 11:06. Mas 22 das 90 respostas chegaram antes do dia 17 (1 em 13/11 e 21 em 16/11), e outras 12 entraram em 17/11 antes das 11:06. Falta mostrar de onde vieram. | C1 | Alta |
| A2 | **Só 1 canal evidenciado.** Para E-B(2) o grupo tem um print de um canal (Teams, "Geral"). O protocolo previa LinkedIn, WhatsApp, Telegram, Discord e fóruns. | C1 | Alta |
| A3 | **Link do dashboard em `[PREENCHER]`** (Fonte, seção 0). O dashboard só roda localmente. | Entrega | Média |
| A4 | **Sem tabela de consistência protocolo × execução** (Fonte 7.3). Os desvios existem, mas não no formato "planejado × executado × consistente?". | C1 | Média |
| A5 | **Convite divergiu do protocolo e isso não está no log de desvios.** O print diz "impactos na produtividade", enquanto o protocolo (Seção 8) exige convite que "não cita ganho de produtividade". Ver 4.3. | C1/C4 | Média |
| A6 | **Painel do formulário ao vivo** (E-B 3) ainda não testado. É preciso ter a conta do dono logada. | C1/C5 | Média |
| A7 | **Pasta `docs/` incompleta** em relação à Fonte 4.3: faltam `codebook.md`, `regras_de_limpeza.md`, `log_de_desvios.md` e o `README.md` da raiz. | C2 | Baixa/Média |

---

## 2. Requisitos obrigatórios (Fonte, seção 2)

| ID | Requisito | Situação | Evidência / observação |
|---|---|---|---|
| D-00 | Dashboard lê o dado bruto | ✅ | `app.py:39-46` localiza `Respostas*.xlsx/csv` na raiz. `analise.py:109-124` lê o arquivo sem alterá-lo. |
| D-01 | Recebidas, descartadas e motivo de cada descarte | ✅ | `app.py:176-216`: cartões, funil, tabela de motivos e lista linha a linha. Soma: 90 = 69 + 10 + 11. |
| D-02 | Likert em barras divergentes | ⚠️ | `app.py:253-297`: neutro dividido ao meio, cores divergentes, legenda com os rótulos reais, PP5 com alternância de recodificação. **Ressalvas:** (a) itens na ordem PP1…PP5, não por concordância líquida (a Fonte pede "ordenar ou agrupar por construto"; agrupar por PP resolve); (b) o **n por item** só aparece na legenda geral, não por barra (Checks da Página 2). |
| D-03 | Cada RQ com teste, p, efeito e margem de erro | ✅ | `app.py:339-374`. Cada RQ traz teste, estatística, p bruto e Holm, efeito com IC, margem, conclusão e gráfico. |
| D-04 | Filtros por segmento | ⚠️ | Seis filtros globais (`app.py:95-120`) e n do filtro sempre visível. A Fonte recomenda aviso para n < 10, mas o dashboard só **oculta** n < 5, sem aviso intermediário. Com filtro, o gráfico divergente e o perfil atualizam. Os testes confirmatórios **não** recalculam (decisão deliberada, documentada); a versão filtrada aparece como exploratória. Atende a Fonte ("ou deixar claro quais valores são do total"). |
| D-05 | Alfa de Cronbach | ✅ | `app.py:385-429`: α, IC bootstrap, k, n, α sem o item, correlação item-total e matriz de Spearman. Mostra o aviso de α < 0,70 e a sensibilidade por subescalas. |
| D-06 | Página de metodologia e desvios | ✅ | `app.py:527-572` + `desvios.md` (D1 a D6) + checagens automáticas. |
| E-A | Carta de anuência | n/a | Não se aplica: amostra em várias fontes, vale o mínimo de 50 (R-01). |
| E-B(1) | Export bruto com data/hora | ✅ | XLSX com carimbo por resposta; SHA-256 conferido (ver 3). |
| E-B(2) | Capturas datadas dos canais | ❌/⚠️ | Só 1 print (17/11). Ver A1 e A2. |
| E-B(3) | Painel do formulário ao vivo | ❓ | Pendente para a defesa. Ver A6. |
| E-X | Sem dados pessoais | ✅ | `REVISAO_PRIVACIDADE.md` cobre XLSX, 2 prints e CSV do pré-teste. Confirmei visualmente o print de 17/11: nome e foto de quem postou estão tarjados. Aparece o nome "Marcos Alberto", integrante citado no próprio convite. A revisão registra isso. |
| P-01 a P-04 | Demonstração, mudança de cenário, arguição | ❓ | Ainda não há roteiro nem ensaio registrados no repositório. |

---

## 3. Regras da coleta (Fonte, seção 3)

| ID | Regra | Situação | Evidência |
|---|---|---|---|
| R-01 | ≥ 50 válidas | ✅ | **69 válidas.** Folga de 19. |
| R-02 | Mínimo de 30 com anuência | n/a | Sem carta. |
| R-03 | Colegas da turma fora | ⚠️ | Não verificável pelo formulário (o protocolo admite). Mitigação: canal é grupo de trabalho. Mas o convite **não traz a frase** "colegas da disciplina não devem responder", que o protocolo prometia (D5 declara). |
| R-04 | Dados batem com o protocolo, desvios declarados | ⚠️ | Seis desvios declarados. Falta o desvio do convite (A5) e o da coleta de 16/11 sem evidência. |
| R-05 | Margem de erro e conclusões dentro do limite | ✅ | ±11,8 p.p. no pior caso com n = 69 (cálculo próprio: 1,96·√(0,25/69) = 11,80). Dashboard traz também ±9,5 sobre p observado = 79,7%. |
| R-06 | Orientações da instituição | ❓ | Não há registro de consulta a comitê de ética. A Parte 1 alega seguir as orientações. |
| R-07 | Integridade | ✅ | Regras definidas no protocolo antes da coleta. Nenhuma edição manual no bruto. Hash confere. |
| R-08 | Dados posteriores ao protocolo | ✅ | 1ª resposta em **13/11 às 20:46:28**, protocolo enviado em 13/11 às 9:17 (Canvas, ~11 h antes). ⚠️ O dashboard **não testa isso**: `JANELA_COLETA` começa em 11/11 (`analise.py:25`), então uma resposta entre 11/11 e 13/11 9:17 passaria sem alerta. Hoje não ocorre nos dados. |

**Integridade do bruto.**
`shasum -a 256` do XLSX = `2c8745d2…0683`, **idêntico** ao `SHA256SUMS.txt`. ✅

---

## 4. Auditoria dos números (reexecutados por mim)

### 4.1 Funil e limpeza (C2)

| Etapa | n | Confere com a Fonte, seção 0 e `desvios.md`? |
|---|---:|---|
| Recebidas | 90 | ✅ |
| Inelegíveis (T1 = não) | 11 | ✅ |
| Descartadas (AT1 ≠ "Discordo") | 10 | ✅ |
| Válidas | 69 | ✅ |
| Fora da janela 11–20/11 | 0 | ✅ |
| Valores de data não lidos | 0 | ✅ |
| Respostas duplicadas | 0 | ✅ (nem consecutivas nem não consecutivas entre elegíveis) |
| Linha reta (só sinalizada) | 1 | ✅ |

**Ponto de atenção na defesa.** Das 10 descartadas por AT1, **9 marcaram "Discordo totalmente" (1)** e só 1 marcou "Concordo totalmente" (5). Ou seja, 9 aparentam ter **lido** a instrução e marcado a opção "mais forte". A regra estava fixada antes da coleta (`DSC-03`), então descartar é correto e defensável, mas espere a pergunta "por que descartar quem discordou totalmente?". Resposta pronta: a regra foi pré-registrada (Seção 3), e a mudança depois de ver os dados seria manipulação (R-07). Vale ter à mão a sensibilidade: o que muda se essas 9 entrassem? O dashboard **não calcula isso**, e ficaria como análise extra só para a defesa (sem alterar a análise oficial).

### 4.2 Estatística (C3)

| RQ | Teste | n | Estatística | p bruto | p Holm | Efeito | IC 95% | Decisão |
|---|---|---:|---|---:|---:|---|---|---|
| RQ1 | Sinal exato | 56 (13 empates) | k = 55 | 1,6·10⁻¹⁵ | 4,7·10⁻¹⁵ | 0,982 acima do neutro | [0,904; 0,9995] | Rejeita H0 |
| RQ2 | Spearman U1 × PP_med | 69 | ρ = 0,367 | 0,0019 | 0,0038 | médio | [0,146; 0,549] | Rejeita H0 |
| RQ3 | Spearman P1 × PP_med | 69 | ρ = 0,058 | 0,637 | 0,637 | desprezível | [−0,172; 0,282] | Não rejeita |

Por que confio nos números: o cálculo vem do mesmo código do dashboard, os dados são os do bruto, e a margem de erro e a contagem de empates batem com `desvios.md` (±11,8; 13 empates = 18,8%). Eles **não foram conferidos por uma segunda ferramenta**, como o Anexo A da Fonte recomenda ("conferir contra planilha ou outro pacote"). Isso ainda está em aberto.

**Leituras que merecem cuidado na defesa:**

- **RQ1 (ceiling).** 79,7% dos usuários têm PP_med ≥ 4 e só 1,4% ≤ 2. O resultado é muito forte, mas a amostra é de usuários, autosselecionada, em empresas grandes (54 de 69 em organizações com mais de 200 pessoas) e quase só em 17/11. Conclusão segura: *"nesta amostra, a produtividade percebida é majoritariamente acima do neutro"*. Nada sobre os desenvolvedores do Brasil.
- **RQ2 (faixa restrita).** 57 de 69 (83%) estão no nível 5 de U1, e nenhum no nível 1 (excluídos por desenho). O ρ = 0,367 vem de uma variável com 3 níveis efetivos (3, 4, 5), onde os níveis 3 e 4 somam só 12 pessoas. O IC é largo (0,15 a 0,55). Isso é associação, e o protocolo já prevê causalidade reversa.
- **RQ3.** Faixas de P1: 42 / 20 / 4 / 3 (0–2, 3–5, 6–10, 11+). As duas faixas altas têm < 5 pessoas e são agrupadas pelo código. A amostra é de júnior e estagiário (61% com 0 a 2 anos), então **"inconclusivo" é mais honesto que "sem associação"**: o ρ de 0,058 com IC [−0,17; 0,28] não exclui efeito pequeno.
- **Alfa.** α = **0,675** (IC 95% [0,545; 0,768]), abaixo do 0,70 pré-declarado. O dashboard e o protocolo previam isso: a limitação é declarada e a sensibilidade por subescalas é mostrada, sem tirar PP5. O α sem PP5 sobe para 0,697 (só descritivo), e a correlação item-total de PP5 é a menor (0,283). Está tudo dentro do plano.
- **Sensibilidade por subescalas** (`sensibilidade_subescalas`): a subescala de rapidez dá ρ(U1) = 0,210 (pequeno) e a de qualidade ρ(U1) = 0,297, ambos **menores** que o 0,367 de PP_med. Convém ter pronta uma frase sobre isso: a associação da RQ2 existe nas duas subescalas, mas é mais fraca do que no PP_med.

### 4.3 Consistência com o protocolo (C1, C4)

Tabela da Fonte 7.3, preenchida com o que verifiquei. **Esta tabela deveria ir para o repositório e para a defesa (A4).**

| Item do protocolo | Planejado (protocolo v5) | Executado | Consistente? | Desvio |
|---|---|---|---|---|
| População-alvo | Devs no Brasil que usaram IA nos últimos 3 meses | Filtro por T1/T2/U1 aplicado como previsto | ✅ | — |
| Estratégia | Conveniência com bola de neve, link único | Divulgação em grupo de trabalho, link único | ⚠️ | D4 |
| n pretendido / margem | 50 válidas, ±13,9 p.p. | 69 válidas, ±11,8 p.p. | ✅ (melhor) | D3 |
| Canais | Convites, LinkedIn, WhatsApp, Telegram, Discord, fóruns | Só grupo de trabalho **evidenciado**; origem das 21 respostas de 13 e 16/11 desconhecida | ❌ | D4 (incompleto, ver A1) |
| Período | 11–20/11 | 13–19/11 | ⚠️ | D3, D6 |
| Convite | Neutro, **sem citar ganho de produtividade**, com a frase sobre colegas da turma | Cita "**impactos na produtividade**" e **não** traz a frase | ❌ | D5 cobre só a frase. **O trecho sobre produtividade não está declarado.** |
| Instrumento | Itens C0, T1, T2, U1, U2, P1–P5, PP1–PP5, AT1 | 17 colunas, mesmos itens | ✅ | — |
| Plano de análise | Sinal, Spearman × 2, Holm, permutação, bootstrap, Clopper-Pearson | Implementado como previsto | ✅ | — |
| Descarte | AT1, branco, repetida em sequência | Implementado | ✅ | — |
| Respostas abertas | 2 codificadores | 1 codificador | ⚠️ | D2 |
| Ética / LGPD | TCLE, sem identificação, cópia sem texto livre | Dashboard lê o bruto e descarta texto livre em memória | ⚠️ | D1 |

**Linha do tempo, importante para C1.** Contagem por dia (do bruto): 13/11 = 1 · 16/11 = 21 · 17/11 = 65 · 18/11 = 2 · 19/11 = 1. Ou seja, **72% das respostas são de 17/11**, com pico às 11 h (22 respostas), logo depois do post das 11:06. Mas **22 respostas (13 e 16/11)** e mais algumas de 17/11 (1 às 7 h, 1 às 8 h e 10 entre 10 h e 11 h, parte antes do post) chegaram **antes** do único post evidenciado. O padrão de 16/11 (6 respostas às 13 h, 7 às 18 h e 6 às 19 h) indica outro canal ou contatos diretos. **Hoje nada no repositório explica essas respostas.** Na defesa, o professor pode perguntar "de onde vieram?".

---

## 5. Evidências de privacidade e publicação

- O **repositório é público** (`REVISAO_PRIVACIDADE.md` reconhece) e contém o XLSX com data/hora e as respostas "Outra" em texto livre. Para o próprio protocolo (Seção 6), "o dashboard lê uma cópia sem texto livre" e as respostas abertas "são removidas antes da análise" se identificarem alguém. A revisão afirma que não há nomes. Mantenho ⚠️: o texto livre está **público** no Git, e a combinação carimbo + perfil + P1 (inteiro, máx. 25) pode identificar alguém em redes pequenas, risco que o próprio protocolo cita. Decisão para o grupo: manter público (aceito e declarado) ou mover o XLSX para fora do Git antes da entrega.
- O CSV do pré-teste está versionado (5 respostas, sem identificadores). OK.
- `.gitignore` oculta `guia_operacional*.md` (links de edição). Boa prática.

---

## 6. Estrutura do repositório vs. Fonte 4.3

| Esperado | Existe? | Observação |
|---|---|---|
| `protocolo/Parte1_Protocolo.pdf` | ✅ | Como `Protocolo_do_Survey_v5.pdf` (+ `.md`). |
| `data/raw/` + `SHA256SUMS.txt` | ⚠️ | Bruto e hash estão **na raiz**. Funciona, mas o dashboard depende desse caminho (`Respostas*.xlsx` na raiz). |
| `data/processed/respostas_validas.csv` e `respostas_descartadas.csv` | ❌ | Não gerados. A Fonte aceita "ler raw → aplicar regras → mostrar", então só é necessário se o grupo quiser mostrar os arquivos. |
| `docs/codebook.md` | ❌ | Rastreabilidade item → RQ → métrica existe no protocolo (Seção 3), não como arquivo. |
| `docs/regras_de_limpeza.md` | ❌ | As regras estão em `analise.py` e no protocolo. Códigos `DSC-xx` não são usados (o dashboard mostra o motivo em texto). |
| `docs/log_de_desvios.md` | ⚠️ | Existe como `dashboard/desvios.md`. |
| `docs/evidencias/` | ⚠️ | 2 imagens + revisão de privacidade. Falta o resto dos canais (A1, A2). |
| `src/` | ⚠️ | A lógica está em `dashboard/analise.py`. Aceitável. |
| `README.md` (raiz) | ❌ | Só há `dashboard/README.md`. |

Outros pontos de reprodutibilidade: `requirements.txt` fixa versões exatas (`pandas==3.1.1`, `scipy==1.18.1` etc.); não consegui instalá-las neste ambiente (usei versões mais antigas e `analise.py` funcionou). Teste a instalação limpa na máquina que fará a defesa. `build_pdf.py` aponta para `/tmp/protocolo.html` e para o Chrome do macOS, e recusa sobrescrever o PDF oficial. Isso é bom.

---

## 7. Pontos menores de coerência

1. **Metodologia no `app.py:534`** diz "Descarte: AT1 diferente de Discordo ou item obrigatório em branco", sem a regra de **repetidas em sequência** que o protocolo v5 inclui (e que o código aplica). Atualize o texto.
2. **Checagem "Respostas fora de 11 a 20/11"** (`app.py:557`) deveria também comparar com a **data real do protocolo** (13/11 às 9:17). Ver R-08.
3. **Perfil da amostra:** a Fonte sugere **linha do tempo por dia** (Página 1). O dashboard **não tem** esse gráfico, e ele é justamente o que prova a janela de coleta e o pico de 17/11.
4. **Indicador visual do mínimo** (verde/vermelho): existe só como `delta` do cartão "Válidas" e como linha da tabela de checagens. Aceitável.
5. **`desvios.md`, D3:** "7 dias corridos (13 a 19/11)" ✅ (13, 14, 15, 16, 17, 18, 19). A frase "Todas as respostas ficaram dentro da janela" ✅.
6. **`desvios.md`, D2:** os números de respostas "Outra" (12 em P4, 19 em P5) são **respondentes**; contei **fragmentos** separados por vírgula (14 em P4, 31 em P5). Não bate nem desbate sem reler as respostas, então confira o texto antes da defesa.
7. **Cabeçalho** do README: `dashboard/README.md` diz que o dashboard "recalcula tudo a cada carga". OK.

---

## 8. Plano de ação priorizado (faltam 5 dias para sexta, 27/11, 12:00; confirmar a data no Canvas)

| Prioridade | Ação | Resolve |
|---|---|---|
| **P0** | Levantar de onde vieram as 22 respostas de 13 e 16/11 (e as anteriores a 11:06 de 17/11) e guardar os prints datados desses canais, tarjando terceiros | A1, A2 |
| **P0** | Acrescentar o **D7** em `desvios.md`: convite postado cita "impactos na produtividade" (o protocolo vedava) e a mesma divulgação difere do texto neutro previsto | A5, R-04 |
| **P0** | Testar o acesso ao **painel do Forms** com a conta do dono, logada, antes da defesa | A6 |
| **P1** | Implantar o dashboard (Streamlit Community Cloud ou equivalente) e preencher o link na Fonte (seção 0). Confirmar no Canvas se basta demonstração ao vivo | A3 |
| **P1** | Colocar a **tabela de consistência** (seção 4.3 acima) em `docs/` e no PDF da entrega | A4 |
| **P1** | Adicionar o gráfico de **linha do tempo** da Página 1 e a checagem R-08 contra 13/11 9:17 | C1/C2 |
| **P1** | Conferir RQ1, RQ2, RQ3 e α **em uma segunda ferramenta** (planilha ou R) e registrar | C3 |
| **P2** | Criar `docs/codebook.md`, `docs/regras_de_limpeza.md` (com códigos `DSC-03` e `DSC-02`) e o `README.md` da raiz | A7 |
| **P2** | Decidir: manter o XLSX público ou removê-lo do Git | Privacidade |
| **P2** | Ensaiar 10 min cronometrados e as 20 perguntas (Fonte 9.3), com atenção a: ceiling da RQ1, faixa restrita da RQ2, inconclusivo na RQ3, α < 0,70 e os 9 descartes por "Discordo totalmente" | C5 |

---

## 9. Veredito por critério (estimativa qualitativa, não é nota)

| Critério | Peso | Situação | Principal risco |
|---|---:|---|---|
| C1 Evidências e consistência | 2,0 | ⚠️ Médio | A1, A2, A5: o bruto está ótimo, mas a **evidência de canais** e a consistência do convite têm lacunas |
| C2 Qualidade dos dados | 1,5 | ✅ Bom | Falta `codebook` e `regras_de_limpeza` como documentos; α < 0,70 explicado |
| C3 RQs com testes e efeitos | 2,0 | ✅ Bom | Faltou conferência em segunda ferramenta; ordenar o Likert e mostrar n por item |
| C4 Desvios e limitações | 0,5 | ✅ Bom | Incluir o D7 (convite) |
| C5 Defesa ao vivo | 2,0 | ❓ Não avaliável | Sem roteiro e ensaio registrados; todos precisam dominar o estudo inteiro |
