# Protocolo do Survey: assistentes de IA e produtividade percebida

**Disciplina:** Medição e Experimentação em Engenharia de Software (PUC Minas) · **Integrantes:** Bernardo Alvim, Brenda Evers, Gabriel Nogueira, Gabriela, Marcos (grupo de 5, com autorização do professor)
**Data de entrega:** 10/11/2026 · **Coleta:** 11/11 a 20/11/2026

---

## 1. Objetivo e questões de pesquisa

**Objetivo (GQM, template de cinco campos, Aula 2; Basili et al., 1994).** Analisar o **uso de assistentes de IA generativa em atividades de desenvolvimento de software**, com o propósito de **caracterizar**, com respeito à **produtividade percebida (seu nível, sua relação com a frequência de uso e sua variação segundo o tempo de experiência)**, do ponto de vista dos **desenvolvedores**, no contexto de **pessoas que trabalham atualmente com desenvolvimento de software no Brasil, em emprego, estágio ou trabalho autônomo, e que usam assistentes de IA generativa**.

**Escopo.** O estudo mede percepção por autorrelato, não produtividade objetiva. As conclusões tratam de produtividade percebida e de associação, nunca de causalidade. Quem não usa assistentes de IA não entra: o formulário é encerrado para essas pessoas, e o mínimo de respostas válidas do enunciado é contado só entre usuários.

**Definições operacionais.**
- **Assistente de IA generativa:** ferramenta de IA generativa usada no trabalho de desenvolvimento para escrever, completar, explicar, revisar, testar ou depurar código. Autocomplete tradicional, linters e busca em documentação não contam.
- **Usuário:** desenvolvedor que usou assistente de IA no trabalho ao menos uma vez nos últimos 3 meses (U1 nos níveis 2 a 5; o nível 1 é "nunca usou").
- **Produtividade percebida (PP):** autoavaliação sobre rapidez, qualidade e esforço ao usar assistentes de IA, medida por cinco itens Likert de 5 pontos (PP1 a PP5, com o item de esforço invertido e recodificado) e resumida pela mediana dos itens (PP_med). Os itens são obrigatórios, então PP_med é sempre um inteiro de 1 a 5, e 3 é o ponto neutro.
- **Tempo de experiência:** anos completos de atuação profissional em desenvolvimento.
- **Frequência de uso:** frequência de uso de assistentes de IA nos últimos 3 meses, em escala ordinal de 5 níveis.

**RQ1. A produtividade percebida dos usuários de assistentes de IA generativa difere do ponto neutro da escala?**
- **Entidade e atributo:** Recurso, atributo externo *Produtividade*, medido por percepção.
- **Métricas:** PP_med (itens PP1 a PP5, ordinal, derivada); proporção de usuários com PP_med ≥ 4, o mesmo que acima do neutro (derivada, calculada sobre todos os usuários e usada na margem de erro); proporção com PP_med ≤ 2 (derivada, relatada de forma descritiva).
- **Hipóteses (teste do sinal, bicaudal):** H0: a probabilidade de PP_med ficar acima do neutro é igual à de ficar abaixo. H1: as probabilidades são diferentes. Usuários com PP_med = 3 ficam fora do teste, e o n efetivo e o número de empates são relatados.

**RQ2. A frequência de uso de assistentes de IA generativa está associada à produtividade percebida dos desenvolvedores?**
- **Entidades e atributos:** Processo, a prática de uso de assistentes de IA, atributo *Frequência de uso*, por autorrelato (proxy do uso real); Recurso, atributo externo *Produtividade*, por percepção.
- **Métricas:** U1, frequência nos últimos 3 meses (ordinal, níveis 2 a 5 entre usuários); PP_med; U2, dias de uso nos últimos 5 dias úteis, contagem de 0 a 5 (razão), só para robustez.
- **Hipóteses:** H0: a correlação de Spearman entre frequência de uso e produtividade percebida é zero na população. H1: é diferente de zero.
- **Observação:** é associação, não efeito. O desenho é transversal, e quem percebe mais ganho pode passar a usar mais.

**RQ3. A produtividade percebida está associada ao tempo de experiência do desenvolvedor?**
- **Entidades e atributos:** Recurso, atributo interno *Nível de experiência*; Recurso, atributo externo *Produtividade*, por percepção.
- **Métricas:** P1, anos completos de atuação (razão); PP_med; faixas de P1 (0 a 2, 3 a 5, 6 a 10, 11 ou mais; ordinal, derivada), usadas só na análise exploratória, e faixas com menos de 5 pessoas são agrupadas com a vizinha.
- **Hipóteses (confirmatórias):** H0: a correlação de Spearman entre anos de experiência e produtividade percebida é zero na população. H1: é diferente de zero.

**Observações.** As hipóteses e os testes (Seção 5) são fixados antes da coleta e só mudam como desvio declarado. O sentido é bicaudal porque as questões não indicam direção. Mede-se percepção e não produtividade objetiva (linhas de código, pull requests por pessoa-mês) porque essas métricas ficam distorcidas quando parte do código é gerada por IA. Porte da organização, tempo de uso de IA, ferramentas e tarefas são itens de perfil, usados como covariáveis e filtros de segmento das RQ2 e RQ3 (leitura descritiva, sem hipótese própria).

---

## 2. População e amostragem

**População-alvo.** Desenvolvedores que trabalham atualmente com desenvolvimento no Brasil (emprego, estágio ou trabalho autônomo) e que usaram assistente de IA generativa nos últimos 3 meses.
- **Entram:** 18 anos ou mais, com atuação atual em desenvolvimento no Brasil, que usaram assistente de IA no período e consentiram.
- **Não entram:** quem não atua em desenvolvimento (incluindo estudantes sem estágio ou trabalho na área, e quem informa vínculo "outro" em T2), quem não usou IA no período, quem não consentiu ou tem menos de 18 anos e os **colegas da turma**. O enunciado só aceita colegas quando a população-alvo é de estudantes, o que não é o caso. A divulgação não usa canais da turma, e o convite informa que colegas da disciplina não devem responder. Como o formulário não tem item que identifique colegas, essa exclusão não é verificável e fica registrada como limitação.

**Origem dos contatos.** Cerca de 30 contatos diretos (5 integrantes, 6 a 7 cada) e divulgação aberta em redes profissionais e comunidades de desenvolvedores, de onde vem a maior parte do volume (canais na Seção 8).

**Estratégia de amostragem.** Não probabilística, por **conveniência com bola de neve** (divulgação aberta e pedido de repasse a colegas de trabalho; Kitchenham e Pfleeger, 2008). Não existe quadro amostral de todos os desenvolvedores do Brasil. Há risco de autosseleção e de viés de rede, então a margem de erro é só referência de precisão e as conclusões ficam limitadas à amostra.

**Tamanho pretendido e margem de erro.** Pretendem-se **50 respostas válidas** de usuários (mínimo do enunciado; a carta de anuência não será usada, pois o survey não é em uma única organização). A divisão de cerca de 10 por integrante é só uma referência de divulgação: o link é único e a origem das respostas não é registrada, então só o total é contado. O descarte esperado de cerca de 15% é uma estimativa do grupo, sem base empírica (o pré-teste não teve descartes), e por isso buscam-se ao menos 60 respostas de elegíveis. A coleta vai de 11/11 a 20/11/2026 (10 dias corridos e 7 dias úteis, pois 20/11 é feriado nacional). Se em 20/11 houver menos de 50 válidas, a coleta é prorrogada pelo mínimo necessário e a prorrogação é declarada como desvio na Parte 2. Todas as válidas entram na análise.

Pela fórmula do enunciado, `e = 1,96 × √( p(1 − p) / n )`, com p = 0,5 (pior caso):

| Situação | n | Margem (± p.p.) |
|---|---|---|
| Pretendido (margem relatada com a RQ1, sobre todos os usuários válidos) | 50 | 13,9 |
| Só referência: proporção entre os não empatados no teste do sinal da RQ1, se 20% empatarem em PP_med = 3 | 40 | 15,5 |
| Subgrupo, por exemplo uma faixa de experiência | 20 | 21,9 |

Na RQ1 a margem relatada é a da proporção observada de PP_med ≥ 4 entre todos os usuários válidos (n = 50 na meta; ±13,9 p.p. no pior caso, recalculada com o n e a proporção observados na Parte 2). A linha de n = 40 mostra apenas a precisão esperada da proporção entre os não empatados, que é a base do teste do sinal. Para essa proporção o intervalo relatado é o de Clopper-Pearson (Seção 5), e não a fórmula acima. Para as RQ2 e RQ3, relatam-se a margem geral da amostra e o intervalo de confiança de ρ. Com n = 50, o Spearman detecta com 80% de poder |ρ| a partir de cerca de 0,39 sem correção e de cerca de 0,44 no primeiro passo de Holm (aproximação de Fisher; empates e a faixa restrita de U1 reduzem um pouco o poder).

---

## 3. Questionário com rastreabilidade

**Fluxo.** Termo de consentimento → texto com a definição de assistente de IA (incluindo o que não conta) → triagem (T1, T2, U1) → uso (U2) → perfil (P1 a P5) → produtividade percebida (PP1 a PP5 com a pergunta de atenção AT1 na mesma matriz). Cerca de 5 minutos.

**Encerramento e descarte (definidos antes da coleta).** O formulário **encerra** se C0 = não, T1 = não, T2 = "outro" ou U1 = nível 1, e essas pessoas entram no funil como inelegíveis. A resposta é **descartada**, com o motivo registrado, se AT1 for diferente de "Discordo" (nível 2), se algum item obrigatório ficar em branco ou se houver respostas repetidas (idênticas em todos os itens e enviadas em sequência). Cinco itens PP iguais (linha reta) não descartam: são sinalizados e testados em sensibilidade.

**Construto.** Só a produtividade percebida usa mais de um item (cinco: rapidez PP1 e PP2, qualidade PP3 e PP4, esforço PP5). A confiabilidade é medida pelo alfa de Cronbach, com PP5 recodificado (6 − x) e lembrando que os itens são ordinais. O alfa mede a consistência interna dos cinco itens e pressupõe um escore somado ou médio, enquanto PP_med é a mediana, outra estatística resumo, com mais empates. Por isso o alfa é um indício indireto de que os itens medem o mesmo construto e não é a confiabilidade de PP_med. Como checagem exploratória, relatam-se a média dos cinco itens e sua correlação de Spearman com PP_med. Decisão prévia: alfa ≥ 0,70 é aceitável. Abaixo disso, a limitação é declarada e as subescalas de rapidez (PP1, PP2) e qualidade (PP3, PP4) são analisadas à parte como sensibilidade. PP5 não é excluído automaticamente por causa do alfa: ele permanece em PP_med em todas as análises confirmatórias, e relatam-se, só de forma descritiva, a correlação item-total corrigida de PP5 e o alfa sem ele. Retirar PP5 seria um desvio, declarado e justificado na Parte 2. U1 e U2 não formam construto: U1 é a métrica da RQ2 e U2 é checagem de robustez.

| RQ | Métricas | Itens |
|---|---|---|
| RQ1 | PP_med; proporção ≥ 4; proporção ≤ 2 | PP1 a PP5 |
| RQ2 | U1; PP_med; U2 (robustez) | U1, U2, PP1 a PP5 |
| RQ3 | P1; PP_med; faixas de P1 (exploratória) | P1, PP1 a PP5 |

Escala dos itens PP e de AT1: Likert de 5 pontos (1 = Discordo totalmente, 2 = Discordo, 3 = Nem concordo nem discordo, 4 = Concordo, 5 = Concordo totalmente), ordinal.

| ID | Item | RQ | Métrica | Escala |
|---|---|---|---|---|
| C0 | Tenho 18 anos ou mais, li o termo e aceito participar (sim/não) | RQ1 a 3 (elegibilidade) | Elegibilidade | Nominal |
| T1 | Hoje trabalha com desenvolvimento de software no Brasil? (sim/não) | RQ1 a 3 (elegibilidade) | Elegibilidade | Nominal |
| T2 | Vínculo: emprego, estágio, autônomo ou outro ("outro" encerra o formulário) | RQ2 e 3 (filtro e elegibilidade) | Perfil | Nominal |
| U1 | Nos últimos 3 meses, com que frequência usou assistentes de IA no trabalho de desenvolvimento? 1 Nunca; 2 Uma ou poucas vezes no período; 3 Algumas vezes por mês; 4 Algumas vezes por semana; 5 Todos ou quase todos os dias | RQ2 | Frequência de uso | Ordinal |
| U2 | Em quantos dos últimos 5 dias úteis usou assistentes de IA? (0 a 5) | RQ2 (robustez) | Dias de uso | Razão (contagem) |
| P1 | Anos completos de atuação profissional em desenvolvimento (inteiro; 0 = menos de 1 ano) | RQ3 | Anos de experiência | Razão |
| P2 | Porte da organização: até 10, 11 a 50, 51 a 200, 201 a 1000, mais de 1000 pessoas, ou "não se aplica (autônomo)" (tratado como ausente no porte) | RQ2 e 3 (filtro) | Porte | Ordinal |
| P3 | Há quanto tempo usa assistentes de IA no trabalho? Menos de 3 meses; de 3 a menos de 6 meses; de 6 a menos de 12 meses; 12 meses ou mais | RQ2 e 3 (covariável) | Tempo de uso de IA | Ordinal |
| P4 | Quais assistentes usa? (múltipla escolha, com "Outra") | RQ2 e 3 (filtro) | Ferramentas | Nominal |
| P5 | Em quais tarefas usa? Escrever, completar, explicar, revisar, testar, depurar ou planejar/projetar código (múltipla escolha, com "Outra") | RQ2 e 3 (filtro) | Tarefas | Nominal |
| PP1 | Com assistentes de IA, concluo minhas tarefas de desenvolvimento mais rápido | RQ1, 2, 3 | PP_med (rapidez) | Ordinal |
| PP2 | Com assistentes de IA, consigo entregar mais tarefas no mesmo período | RQ1, 2, 3 | PP_med (rapidez) | Ordinal |
| PP3 | Com assistentes de IA, a qualidade do código que entrego é melhor | RQ1, 2, 3 | PP_med (qualidade) | Ordinal |
| PP4 | Com assistentes de IA, preciso refazer menos o meu código depois de entregue | RQ1, 2, 3 | PP_med (qualidade) | Ordinal |
| PP5 (invertido) | Usar assistentes de IA torna meu trabalho de desenvolvimento **mais cansativo ou trabalhoso** (recodificado 6 − x) | RQ1, 2, 3 | PP_med (esforço) | Ordinal |
| AT1 | Pergunta de atenção na matriz PP: "Para mostrar que está lendo com atenção, marque 'Discordo' nesta linha" | RQ1 a 3 (qualidade) | Conformidade | Nominal |

Itens de triagem, perfil e controle (C0, T1, T2, P2 a P5, AT1) ligam-se às RQs como elegibilidade, filtro de segmento, covariável ou controle de qualidade. Não há perguntas abertas obrigatórias, e as respostas "Outra" são codificadas na Seção 5.

---

## 4. Pré-teste

**Método.** O formulário final foi aplicado a desenvolvedores que usam IA, com meta de 3 a 5 pessoas de perfis diferentes (por exemplo estagiário, júnior e sênior), que não deveriam participar da coleta (condição não verificável, ver a tabela abaixo). Mediram-se o tempo de resposta e, em conversa curta, a clareza dos itens PP, o entendimento da definição de assistente de IA, as opções de U1, o encerramento da triagem e a pergunta de atenção. O pré-teste usou uma cópia idêntica do formulário, com planilha própria e uma página extra de feedback, então suas respostas não se misturam com as da coleta.

**Instrumento do pré-teste.** Google Formulários (versão PRÉ-TESTE): https://docs.google.com/forms/d/e/1FAIpQLSfvfqzhbticuoK79xMvUB6wbzkhEcYWZj-Dq9JeX2it9uDXFA/viewform

**Resultado.** Aplicado em 06 e 07/11/2026. Foram 5 respostas: 1 pessoa respondeu T1 = não e o formulário encerrou como previsto, e 4 eram elegíveis. O tempo autorrelatado (F1) foi de 3, 5, 5 e 3 minutos, com média de 4 minutos, compatível com os "cerca de 5 minutos" do termo. Os 4 elegíveis acharam a definição de assistente de IA clara (F2), não apontaram item difícil nem opção faltando no feedback aberto, acertaram a pergunta de atenção (AT1) e nenhum respondeu em linha reta.

| Item ou aspecto | Problema observado | Mudança feita |
|---|---|---|
| P5 (tarefas) | Um respondente escreveu "Planejar código" em "Outra", tarefa que não estava na lista | Inclusão da opção "Planejar ou projetar código" |
| P4 (ferramentas) | Um respondente citou em "Outra" uma ferramenta fora da lista | Mantido o "Outra", codificado conforme a Seção 5 |
| PP5 (invertido) | Um respondente concordou com rapidez (PP1 = 4, PP2 = 5) e concordou totalmente que a IA deixa o trabalho mais cansativo (PP5 = 5). Pode ser leitura errada do item invertido | Destaque em negrito de "mais cansativo ou trabalhoso" no enunciado de PP5. O item continua invertido, por controlar aquiescência |
| Triagem, AT1, tempo, definição de IA | Funcionaram como previsto | Nenhuma |
| Perfil dos participantes | Os 4 elegíveis eram estagiários, e não houve perfis júnior e sênior como planejado | Limitação declarada: o pré-teste não verificou a compreensão por profissionais mais experientes |
| Participação na coleta | O formulário não identifica respondentes, então não é possível verificar que as pessoas do pré-teste não responderam também à coleta | Limitação declarada; sem mudança no formulário |

As mudanças da tabela foram aplicadas ao formulário de coleta antes da sua abertura. As respostas do pré-teste não entram na análise, e o alfa de Cronbach não foi calculado com n = 4. Os ajustes posteriores ao pré-teste (regra de T2 = "outro", faixas de P3, rótulos da escala Likert e texto do termo, Seções 3 e 6) serão aplicados ao formulário de coleta antes da abertura em 11/11 e não foram testados com respondentes.

---

## 5. Plano de análise

**Preparação.** A exportação bruta (com data e hora) fica intacta e a análise usa uma cópia. Aplicam-se as regras da Seção 3, registrando o motivo de cada exclusão (funil: recebidas, inelegíveis, descartadas, válidas). Recodifica-se PP5, calculam-se PP_med e as faixas de P1. Os itens PP são obrigatórios, então não há imputação.

**Estatística descritiva, por escala.**

| Escala | Itens | Resumo |
|---|---|---|
| Nominal | C0, T1, T2, P4, P5, AT1 | Frequência e percentual, moda. Em P4 e P5, percentual de respondentes por opção |
| Ordinal | U1, P2, P3, PP1 a PP5, PP_med | Distribuição, mediana e quartis, com Likert em barras divergentes. **Sem média** |
| Razão | P1, U2 | Mediana, quartis, média, desvio padrão, mínimo e máximo |
| Construto PP | PP1 a PP5 | Alfa de Cronbach (com k e n), após recodificar PP5 |

**Testes confirmatórios (bicaudais, α = 0,05).** As variáveis de resposta são ordinais, então valem mediana e Spearman. Média, teste t e Pearson não valem nessa escala.

| RQ | Variáveis | Teste | Efeito e margem |
|---|---|---|---|
| RQ1 | PP_med contra o neutro 3 | Teste do sinal exato (binomial, p = 0,5 sob H0), sem os empates | Proporção de PP_med ≥ 4 entre os não empatados, com IC de 95% de Clopper-Pearson. Margem de erro pela fórmula do enunciado, sobre a proporção de ≥ 4 entre todos os usuários. Relatam-se também as proporções de ≥ 4 e de ≤ 2 entre todos |
| RQ2 | U1 × PP_med | Spearman, com postos médios nos empates. Valor p por permutação (10.000 permutações), que prevalece sobre a aproximação t se os dois divergirem | ρ, com IC de 95% por bootstrap percentil (10.000 reamostragens, semente fixa) |
| RQ3 | P1 × PP_med | Spearman, como na RQ2 | ρ, com IC de 95% por bootstrap |

**Tamanho de efeito.** Relatado junto ao valor p. A leitura de ρ é declarada antes dos dados (convenção de Cohen, 1988): abaixo de 0,1 desprezível, 0,1 a 0,3 pequeno, 0,3 a 0,5 médio, a partir de 0,5 grande. Com n próximo de 50, um ρ moderado com p alto indica pouco poder, e o texto diz "não rejeitamos H0", nunca "aceitamos H0".

**Múltiplas comparações.** A família confirmatória tem 3 testes, com correção de Holm (menor p contra α/3, o seguinte contra α/2, o último contra α, parando na primeira não rejeição). Relatam-se o p bruto e o ajustado. Os ICs de 95% dos efeitos confirmatórios (proporção e ρ) não são ajustados por Holm: a decisão usa o p ajustado, e uma divergência entre IC e p ajustado é relatada, sem ser resolvida em favor de um dos dois.

**Exploratórias (fora da família, sem correção, nunca usadas para concluir).** Kruskal-Wallis da PP_med entre as faixas de experiência (efeito ε²); Spearman entre U2 e PP_med; média dos itens PP e sua correlação com PP_med; sensibilidade sem respostas em linha reta; comparações entre segmentos do dashboard, sem comparar segmentos com menos de 5 pessoas: Mann-Whitney para 2 grupos (efeito: δ de Cliff), Kruskal-Wallis para 3 ou mais (efeito: ε²) e, em variáveis nominais, χ² quando todas as frequências esperadas forem ≥ 5 e, nos demais casos, teste exato de Fisher (Freeman-Halton em tabelas maiores que 2 × 2), com efeito V de Cramér. Os efeitos exploratórios trazem IC de 95% por bootstrap percentil (10.000 reamostragens, semente fixa).

**Respostas abertas (opção "Outra" de P4 e P5).** Duas pessoas leem de forma independente e agrupam em categorias, reclassificando em opções existentes quando couber e criando categorias nominais para o resto. Divergências são resolvidas em conversa. Relatam-se só frequências.

**Relato (Wohlin et al., 2012).** Para cada RQ: teste, estatística, valor p (bruto e ajustado), efeito com intervalo, margem de erro, n e interpretação em termos de produtividade **percebida** e associação.

---

## 6. Ética e LGPD

- **Termo de consentimento.** É a primeira página, e o aceite (C0) é obrigatório antes de qualquer pergunta. Informa objetivo (atividade acadêmica), participação voluntária, duração de cerca de 5 minutos, exigência de 18 anos ou mais, dados coletados (respostas, data e hora), quem acessa (integrantes do grupo e professor), que as respostas são processadas pelo Google Formulários e Planilhas (que pode armazenar dados fora do Brasil) e contato do grupo. Informa também que, sem identificação, não é possível retirar a resposta depois do envio, mas quem desistir pode fechar o formulário antes de enviar, sem consequência.
- **Base legal.** Consentimento do titular (LGPD, Lei 13.709/2018, art. 7º, I), dado no aceite de C0. Não se coletam dados sensíveis nem de menores.
- **Não identificação.** Não se coletam nome, e-mail, CPF, telefone, IP nem nome da empresa, e o formulário não exige login, então os dados são tratados como não identificados. O grupo não afirma anonimato absoluto: a data e hora de envio e a combinação de respostas de perfil podem, em redes pequenas, permitir que alguém que conheça o respondente o reconheça. Por isso o perfil é coletado em categorias, exceto P1 (anos de atuação, número inteiro). Em "Outra", pede-se para não citar nomes, e identificadores que aparecerem são removidos antes da análise. Dashboard e apresentação não exibem segmentos com menos de 5 pessoas.
- **Armazenamento.** Os dados ficam no Google Formulários e Planilhas, serviço do Google que atua como operador. A exportação bruta fica em pasta de acesso restrito aos integrantes (e ao professor, se solicitado), com cópia de segurança em uma segunda pasta, de outro integrante. O dashboard lê uma cópia sem texto livre, e nenhuma evidência expõe dados pessoais. Os dados são mantidos até o fim da avaliação da disciplina e depois apagados. O grupo segue a LGPD e as orientações da instituição sobre pesquisas com pessoas.

---

## 7. Ameaças à validade

| Ameaça | Como aparece | Mitigação |
|---|---|---|
| Não resposta | Quem não responde pode ter menos interesse em IA ou tempo, e a divulgação aberta não permite taxa de resposta | Formulário curto, lembretes, relato do funil (taxa de resposta não calculável, link único), limitação declarada |
| Autosseleção e viés de rede | Quem tem opinião forte sobre IA tende a responder, e a bola de neve traz respondentes parecidos | Convite neutro (sem citar ganho de produtividade), vários canais e pontos de partida, relato do perfil, conclusões restritas à amostra |
| Desejabilidade social | Parecer moderno ou produtivo ao usar IA | Participação sem identificação (sem login nem e-mail), linguagem neutra e convite que não cita ganho. Mitigação parcial: PP1 a PP4 têm o mesmo sentido positivo e só PP5 é invertido, e os itens PP medem percepção de resultado, não prática. A limitação é declarada |
| Respostas descuidadas ou automáticas | Marcação sem ler | AT1 com regra de descarte prévia, item invertido PP5 (mitigação parcial da aquiescência), linhas retas em sensibilidade |
| Respostas repetidas e nova tentativa | Sem login, a mesma pessoa pode responder mais de uma vez ou refazer a triagem com outras respostas | Descarte de respostas idênticas em sequência, limitação declarada |
| Seleção por uso e faixa restrita | Só usuários respondem a PP, o que tende a favorecer resultados positivos na RQ1, e U1 de 2 a 5 reduz a variação na RQ2 | Conclusões restritas a usuários, intervalo de confiança de ρ relatado |
| Percepção diferente da realidade | O caso METR (2025; Aula 2): desenvolvedores se percebiam mais rápidos e mediram mais lentos. Toda medida é um proxy (Goodhart) | Conclui-se só sobre produtividade percebida, sem afirmar ganho real |
| Causalidade reversa e confundidores | Estudo transversal: quem percebe ganho pode usar mais, e tempo de uso, porte e ferramentas podem confundir | Linguagem de associação, confundidores medidos e usados só na leitura descritiva |
| Medição | Mediana de 5 itens perde informação e gera empates. "IA" pode ser entendida de formas diferentes. Frequências dependem de memória | Itens cobrindo rapidez, qualidade e esforço, alfa (indício indireto, Seção 3), pré-teste, definição de IA exibida antes da triagem, janelas curtas e U2 como checagem de U1 |
| Validade estatística | Com n = 50, só ρ a partir de cerca de 0,39 (0,44 no primeiro passo de Holm) é detectado com 80% de poder. Empates reduzem o n do teste do sinal. Há 3 testes | Relato do poder e do n efetivo, correção de Holm, subgrupos pequenos só descritivos |
| Validade externa | Amostra não probabilística, só no Brasil, coletada em 7 dias úteis, com ferramentas que mudam rápido | Sem generalização, margem de erro como referência |

---

## 8. Plano de divulgação

**Período.** De quarta-feira, 11/11/2026, a sexta-feira, 20/11/2026 (7 dias úteis; 20/11 é feriado nacional). A divulgação só começa depois do envio do protocolo, feito em 10/11/2026 na plataforma da disciplina, e o formulário fecha ao fim de 20/11. A meta do grupo é de 50 respostas válidas, e cada integrante divulga nas próprias redes. Se faltarem respostas em 20/11, vale a prorrogação descrita na Seção 2.

**Instrumento e registro dos dados.** O questionário é um Google Formulários (versão COLETA), sem login e sem coleta de e-mail: https://docs.google.com/forms/d/e/1FAIpQLSd2wm9FwwFUBmADLLqTiH9ChwPw5o7NAsM57JEJdjPGntZCKA/viewform. O formulário foi construído e conferido antes da coleta e permanece **fechado para respostas** até o envio deste protocolo, para que nenhuma resposta anteceda a data de entrega. Cada resposta é gravada automaticamente em uma planilha própria, com data e hora de envio (carimbo gerado pelo Google). Ao fim da coleta, a planilha é exportada em CSV, sem alteração, como dado bruto e evidência de data. O pré-teste usou formulário e planilha separados, e seus dados não entram na análise. Todos os integrantes divulgam o mesmo link, e a origem de cada resposta não é registrada, para evitar a identificação dos respondentes.

**Canais.** Convite individual aos contatos diretos de cada integrante; publicação de cada integrante no LinkedIn com pedido de compartilhamento; grupos de WhatsApp, Telegram e Discord e fóruns de desenvolvedores, respeitando as regras de cada grupo; pedido de repasse a colegas de trabalho. Não se usam canais da turma.

**Convite.** Texto neutro: tema (uso de assistentes de IA no trabalho de desenvolvimento), tempo (cerca de 5 minutos), participação sem identificação e quem pode responder (colegas da disciplina não participam). Não cita ganho de produtividade nem resultados esperados.

| Data | Ação |
|---|---|
| Qua, 11/11 | Abertura do formulário. Convites individuais, publicações no LinkedIn e envio nas comunidades |
| Qui, 12/11 e sex, 13/11 | Lembrete aos contatos diretos e pedido de repasse |
| Seg, 16/11 | Segundo reforço nas comunidades |
| Ter, 17/11 | Conferência do total de respostas válidas. Se estiver abaixo de 50, novo reforço em todos os canais em 18/11 e 19/11 |
| Qui, 19/11 | Último lembrete (véspera do feriado) |
| Sex, 20/11 (feriado nacional) | Fechamento do formulário e exportação bruta com data e hora, feitos remotamente por um integrante |

**Evidências.** Capturas datadas das publicações e dos envios (contatos ocultados, sem dados pessoais), a exportação bruta com data e hora de cada resposta e o acesso ao painel do formulário na apresentação.

**Referências.** BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric approach. In: Encyclopedia of Software Engineering. New York: Wiley, 1994. COHEN, J. Statistical Power Analysis for the Behavioral Sciences. 2. ed. Hillsdale: Lawrence Erlbaum, 1988. KITCHENHAM, B.; PFLEEGER, S. L. Personal opinion surveys. In: SHULL, F.; SINGER, J.; SJØBERG, D. (ed.). Guide to Advanced Empirical Software Engineering. London: Springer, 2008. METR. Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity. arXiv:2507.09089, jul. 2025. WOHLIN, C. et al. Experimentation in Software Engineering. Berlin: Springer, 2012.
