# Pacote de entrega (Canvas) e verificação final

**Formato do envio:** a Fonte (seção 13, item 1) deixa em aberto o que subir. Sugestão: um PDF com (1) link do dashboard e do repositório, (2) prints das 6 páginas, (3) evidências sem dados pessoais (print do Canvas de 13/11 e do convite de 17/11), (4) tabela de consistência e desvios D1 a D8. **Confirmar com o professor** se também quer o repositório.

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
- [ ] Prints/evidências de divulgação de 13 e 16/11 (pendência de evidência, declarada em D8).
- [x] Painel do Google Formulários aberto pelo dono em 22/11: **90 respostas**, igual ao export. Formulário **fechado** para novas respostas em 22/11 (a coleta terminou em 19/11 17:50; o fechamento formal veio depois).
- [x] (histórico) Abrir o painel do Google Formulários com a conta do **dono** (a ferramenta já está confirmada; falta só testar o acesso ao painel e à aba de respostas). Conferir também se o formulário está **fechado** para novas respostas, para que o painel não mostre mais que as 90 do export.
- [ ] PDF offline com prints das 6 páginas.
- [ ] Definir responsáveis em `docs/defesa.md` e ensaiar com cronômetro.
- [x] Decisão de manter o XLSX público confirmada em 22/11 (`docs/evidencias/REVISAO_PRIVACIDADE.md`).
