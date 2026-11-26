# Pacote de entrega (Canvas) e verificação final

**Formato do envio:** a Fonte (seção 13, item 1) deixa em aberto o que subir. Sugestão: um PDF com (1) link do dashboard e do repositório, (2) prints das 6 páginas, (3) evidências sem dados pessoais (print do Canvas de 13/11 e prints de divulgação de 16 e 17/11), (4) tabela de consistência e desvios D1 a D8. **Confirmar com o professor** se também quer o repositório.

| Item | Valor |
|---|---|
| Dashboard | https://survey-ia-medicao-es.streamlit.app/ |
| Repositório | https://github.com/marcosffp/medicao-trabalho-final (alimenta o Streamlit) |
| Formulário da coleta (Google Formulários, confirmado pelo grupo em 22/11) | https://docs.google.com/forms/d/e/1FAIpQLSd2wm9FwwFUBmADLLqTiH9ChwPw5o7NAsM57JEJdjPGntZCKA/viewform |
| Hash do bruto (SHA-256) | `2c8745d20ed1dff651fd3d0137c68272ab8ec852af2191e335789f4e04be0683` |

## Verificado em 22/11/2026
- Link público abriu e as 6 abas carregaram (Perfil, Itens Likert, Questões de pesquisa, Confiabilidade, Segmentos, Metodologia). Valores conferidos na tela: 90 recebidas, 11 inelegíveis, 10 descartadas, 69 válidas; RQ1 n efetivo 56, efeito 0,982; RQ3 p = 0,637; α = 0,675, IC [0,55; 0,77]. Em 22/11 o app foi aberto no navegador logado e, sem login, o link responde 200 (Sharing = "public and searchable"). Repositório de origem do app: `marcosffp/medicao-trabalho-final`.
- Hash do XLSX confere. RQ1 a RQ3 e α conferidos por segunda implementação.

## Ainda manual
- [x] Prints de divulgação de 16/11 (3 grupos de WhatsApp e 2 mensagens individuais) e 17/11 (3 mensagens), recebidos dos integrantes em 23 e 24/11, tarjados e salvos em `docs/evidencias/divulgacao/`. D8, D4, `consistencia.md` e `limitacoes.md` atualizados. **Sem evidência até hoje:** convites de 13/11 (1 resposta, 20:46) e 9 respostas de 16/11 fora das janelas dos prints.
- [x] `docs/dashboard_offline.pdf` regerado em 24/11 (22 páginas, tema escuro, com D4 e D8 atualizados), a partir do dashboard local com o XLSX oficial.
- [x] Tarjas dos prints conferidas visualmente em 24/11 (nomes, telefones e avatares cobertos).
- [x] Painel do Google Formulários aberto pelo dono em 22/11: **90 respostas**, igual ao export. Formulário **fechado** para novas respostas em 22/11 (a coleta terminou em 19/11 17:50; o fechamento formal veio depois).
- [x] (histórico) Abrir o painel do Google Formulários com a conta do **dono** (a ferramenta já está confirmada; falta só testar o acesso ao painel e à aba de respostas). Conferir também se o formulário está **fechado** para novas respostas, para que o painel não mostre mais que as 90 do export.
- [x] PDF offline com prints das 7 abas (inclui "Apresentação"): `docs/dashboard_offline.pdf` (gerado em 22/11, regerado em 26/11 a partir do dashboard com o XLSX oficial; sem dados pessoais). Regerar se o código ou os dados mudarem.
- [x] PDF do protocolo conferido contra o `.md` em 22/11: mesmo texto (só quebras de linha e formatação diferem). As datas do PDF (entrega 10/11, abertura 11/11) são as planejadas; a divergência está em D6.
- [ ] Enviar a mensagem ao professor (modelo no fim deste arquivo) e anotar a resposta aqui.
- [x] Responsáveis definidos em `docs/defesa.md` (um bloco contínuo por integrante).
- [ ] Ensaiar com cronômetro (dois ensaios) e registrar na seção 6 de `docs/defesa.md`.
- [x] Decisão de manter o XLSX público confirmada em 22/11 (`docs/evidencias/REVISAO_PRIVACIDADE.md`).

## Mensagem para o professor (item 11 da Fonte, seção 13)

Quem envia é o grupo; o texto abaixo é só um modelo.

> Professor, tudo bem? Sobre a entrega da Parte 2 do trabalho final, queremos confirmar quatro pontos:
> 1. No Canvas, basta um PDF com o link do dashboard, o link do repositório, os prints das 6 abas, as evidências da coleta (sem dados pessoais) e o log de desvios? Ou o senhor também quer o arquivo do dashboard?
> 2. O dashboard precisa estar acessível por link público, ou basta a demonstração ao vivo? Hoje ele está público em https://survey-ia-medicao-es.streamlit.app/.
> 3. Qual é a data e hora exata do vencimento (entendemos sexta-feira, 27/11, às 12:00) e a data e a ordem das defesas?
> 4. Qual convenção de tamanho de efeito o senhor espera? Usamos a de Cohen (1988) para ρ, como declarado no protocolo.
> Obrigado, [grupo]

## Estado do formulário (conferido em 22/11/2026)

- Painel do Google Formulários (versão COLETA): **90 respostas**, igual ao export.
- Aviso do formulário: "Este formulário não está aceitando respostas" (fechado em 22/11; a última resposta é de 19/11 17:50). Está declarado em D3.
