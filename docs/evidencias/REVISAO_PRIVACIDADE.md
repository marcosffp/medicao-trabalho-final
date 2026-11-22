# Revisão de privacidade das evidências (22/11/2026)

| Artefato | Verificação | Resultado |
|---|---|---|
| `Respostas - ... (COLETA).xlsx` (90 linhas) | Leitura de todas as colunas e abas; busca por e-mail, IP e URL em todas as células; leitura dos metadados internos (`xl/persons/person.xml`, comentários) | 17 colunas: carimbo de data/hora, C0, T1, T2, U1, U2, P1 a P5, PP1 a PP5 e AT1. **Sem nome, e-mail, IP ou conta.** Único texto livre: "Outra" em P4 e P5, sem nomes de pessoas ou empresas. Sem comentários nem autor nos metadados. Colunas removidas da exportação: nenhuma (o formulário nunca coletou identificadores) |
| `docs/evidencias/grupo_trabalho_divulgacao_2026-11-17.png` | Revisão visual | Nome e foto de quem postou já estão cobertos por tarja. Aparecem só o texto da divulgação, o canal genérico ("Geral"), a data (17/11 às 11:06) e contagens de reações, sem nomes de reagentes. O nome visível é o de um integrante do grupo, citado no próprio convite |
| `docs/evidencias/canvas_envio_parte1_2026-11-13.png` | Revisão visual | Apenas título da tarefa, prazo, data/hora do envio e nome do arquivo. Sem dados pessoais |
| `...(PRÉ-TESTE)....csv` (5 respostas) | Leitura das colunas e do texto livre (F3 a F5) | Sem identificadores; texto livre vazio ou "Nenhum/Nenhuma". Não entra na análise (protocolo, Seção 4) |

**Decisão sobre o CSV do pré-teste:** mantido no repositório. Não tem dado pessoal, é citado no protocolo como evidência do pré-teste, e o dashboard já o ignora quando existe a exportação da coleta. Se o grupo preferir removê-lo do repositório público, basta `git rm --cached` e incluir o nome no `.gitignore`, sem efeito sobre as análises.

**Observação:** o repositório é público e o XLSX está nele. Como não há identificadores, isso é compatível com o TCLE, mas as respostas (agregadas, anônimas) ficam acessíveis a qualquer pessoa.
