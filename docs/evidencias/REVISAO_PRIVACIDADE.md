# Revisão de privacidade das evidências (22/11/2026)

| Artefato | Verificação | Resultado |
|---|---|---|
| `Respostas - ... (COLETA).xlsx` (90 linhas) | Leitura de todas as colunas e abas; busca por e-mail, IP e URL em todas as células; leitura dos metadados internos (`xl/persons/person.xml`, comentários) | 17 colunas: carimbo de data/hora, C0, T1, T2, U1, U2, P1 a P5, PP1 a PP5 e AT1. **Sem nome, e-mail, IP ou conta.** Único texto livre: "Outra" em P4 e P5, sem nomes de pessoas ou empresas. Sem comentários nem autor nos metadados. Colunas removidas da exportação: nenhuma (o formulário nunca coletou identificadores) |
| `docs/evidencias/grupo_trabalho_divulgacao_2026-11-17.png` | Revisão visual | Nome e foto de quem postou já estão cobertos por tarja. Aparecem só o texto da divulgação, o canal genérico ("Geral"), a data (17/11 às 11:06) e contagens de reações, sem nomes de reagentes. O nome visível é o de um integrante do grupo, citado no próprio convite |
| `docs/evidencias/canvas_envio_parte1_2026-11-13.png` | Revisão visual | Apenas título da tarefa, prazo, data/hora do envio e nome do arquivo. Sem dados pessoais |
| `...(PRÉ-TESTE)....csv` (5 respostas) | Leitura das colunas e do texto livre (F3 a F5) | Sem identificadores; texto livre vazio ou "Nenhum/Nenhuma". Não entra na análise (protocolo, Seção 4) |

**Decisão sobre o CSV do pré-teste:** mantido no repositório. Não tem dado pessoal, é citado no protocolo como evidência do pré-teste, e o dashboard já o ignora quando existe a exportação da coleta. Se o grupo preferir removê-lo do repositório público, basta `git rm --cached` e incluir o nome no `.gitignore`, sem efeito sobre as análises.

**Observação:** o repositório é público e o XLSX está nele. Como não há identificadores, isso é compatível com o TCLE, mas as respostas (agregadas, anônimas) ficam acessíveis a qualquer pessoa.

## Avaliação da exposição da base bruta no GitHub (22/11/2026)

**Pergunta:** o XLSX bruto pode continuar em repositório público?

**O que a base contém.** Carimbo de data/hora com milissegundos, vínculo, porte da organização, tempo de uso de IA, frequência de uso, anos de experiência (inteiro), ferramentas, tarefas e 17 colunas no total. Sem nome, e-mail, IP ou conta.

**Risco de reidentificação (medido nos dados):**

| Combinação de perfil (69 válidas) | Pessoas únicas |
|---|---:|
| T2 + P2 + P3 + P1 | **32 de 69** |
| T2 + P2 + P1 | 23 de 69 |
| P2 + P1 | 19 de 69 |

- Quase metade das pessoas é única em 4 variáveis de perfil. Quem conhece a empresa e a pessoa (por exemplo, um colega do mesmo grupo de trabalho onde o convite foi postado) pode reconhecê-la. O protocolo (Seção 6) já admite isso.
- O carimbo com milissegundos permite cruzar com quem lembra de ter respondido em certo horário.
- Os textos livres ("Outra") não têm nomes de pessoas nem de empresas, mas alguns descrevem funções e rotinas específicas (por exemplo, "Trabalho operacional para equipes de software", "Especificação de produto"), o que aumenta a identificabilidade em redes pequenas.
- O TCLE prometeu que o dashboard lê uma cópia sem texto livre; o XLSX público contradiz o espírito dessa promessa, ainda que o dashboard não exiba o texto.
- Mesmo que o arquivo saia do estado atual do repositório, ele **continua no histórico do Git** (commit `d3ba46f`) enquanto o repositório for público.

**Impacto de manter público:** baixo a médio. Não há dado sensível nem identificador direto, mas há risco real de reconhecimento por quem conhece o grupo.

**Recomendação (a decidir pelo grupo; nada foi alterado):**
1. **Tornar o repositório privado** e dar acesso ao professor como colaborador. Mantém o bruto, o hash e as evidências intactos e reduz a exposição a quem já tem o link. É a opção de menor custo e não exige reescrever o histórico.
2. Se o repositório precisar ficar público: remover o XLSX do histórico (`git filter-repo`), manter o hash e mostrar o arquivo só na defesa ou entregar ao professor por canal privado (Canvas). O dashboard funciona com o arquivo na raiz ou enviado pela barra lateral.
3. Em qualquer opção: não incluir mais arquivos com texto livre ou carimbos completos.

Mudar a visibilidade ou reescrever o histórico altera o repositório compartilhado do grupo e deve ser combinado com todos os integrantes.

## Decisão sobre o XLSX bruto público (22/11/2026)

**Decisão registrada: manter o XLSX no repositório público, risco aceito e declarado.** Motivos: (1) o enunciado da Parte 2 exige que o dashboard leia o dado bruto, e o dashboard publicado no Streamlit Community Cloud lê o XLSX deste repositório; removê-lo derrubaria o link público; (2) o formulário não coletou nome, e-mail nem IP; (3) o hash em `SHA256SUMS.txt` só prova integridade se o arquivo estiver acessível.

**Risco que permanece:** o arquivo traz o carimbo de data/hora e as respostas em texto livre de P4 e P5 ("Outra"). A combinação de carimbo, perfil e P1 pode, em redes pequenas, ajudar a identificar alguém (risco citado na Seção 6 do protocolo). Já está declarado em D1 (`dashboard/desvios.md`).

**Para o grupo:** decisão **confirmada pelo grupo em 22/11/2026**. Se preferirem remover o XLSX do Git, será preciso trocar a leitura do dashboard (upload manual ou arquivo privado) e republicar o link.

## Prints de divulgação de 16 e 17/11 (24/11/2026)

Os integrantes enviaram os prints de celular e de computador. Há duas versões de cada um:

- **Para entrega:** `docs/evidencias/divulgacao/` (cópias tarjadas, sem dados pessoais).
- **Originais sem tarja:** `docs/evidencias/originais_sem_tarja/` (**ignorada pelo Git**; não subir no Canvas nem no repositório). Os nomes são os mesmos das cópias tarjadas, com extensão `.jpeg`.

Nas cópias tarjadas, tapei nomes e telefones de terceiros, avatares, nomes de grupos e um primeiro nome citado em mensagem individual.

| Arquivo (em `divulgacao/`) | O que mostra | Tarjas |
|---|---|---|
| `divulgacao_2026-11-16_1841_individual.jpg`, `..._1844_individual.jpg` | Mensagem individual com o link, 16/11 às 18:41 e 18:44 | Primeiro nome do destinatário (1844) |
| `divulgacao_2026-11-16_1309_grupo.jpg`, `..._1327_grupo.jpg`, `..._1834_grupo.jpg` | Envio em três grupos, 16/11 às 13:09, 13:27 e 18:34 | Cabeçalho (nome do grupo e participantes), avatares, nomes e telefones de quem respondeu, trechos de conversa alheia |
| `divulgacao_2026-11-17_1006_a.jpg`, `..._1006_b.jpg`, `divulgacao_2026-11-17_1344.jpg` | Mensagem de divulgação, 17/11 às 10:06 (duas capturas do mesmo envio) e 13:44 | Nenhuma (só o texto enviado; o chat não aparece) |

Resta a conferência visual final antes do envio. Os prints mostram respostas de terceiros ("Respondido", "respondo"); sem nome ou telefone, não identificam ninguém.
