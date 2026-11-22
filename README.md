# Assistentes de IA e produtividade percebida: survey e dashboard

Trabalho final de **Medição e Experimentação em Engenharia de Software** (PUC Minas, 2º/2026). Survey com desenvolvedores no Brasil sobre o uso de assistentes de IA generativa e a produtividade percebida, com dashboard que lê a exportação bruta do formulário.

**Integrantes:** Bernardo Alvim, Brenda Evers, Gabriel Nogueira, Gabriela e Marcos.

## Resultado em uma tabela

| Etapa | n |
|---|---:|
| Respostas recebidas | 90 |
| Inelegíveis (T1 = não) | 11 |
| Descartadas (falha na pergunta de atenção AT1) | 10 |
| **Válidas** | **69** |

Coleta de 13 a 19/11/2026 (Google Formulários), margem de erro de ±11,8 p.p. no pior caso. Os resultados das RQs, os testes e os desvios aparecem no dashboard.

## Como executar

Requer Python 3.12 ou superior. Na raiz do projeto:

```sh
python3 -m venv .venv
.venv/bin/pip install -r dashboard/requirements.txt
.venv/bin/streamlit run dashboard/app.py
```

O dashboard abre no navegador e encontra sozinho o arquivo `Respostas - … (COLETA).xlsx` na raiz. Também aceita outro CSV ou XLSX enviado na barra lateral ou a variável `SURVEY_DATA`. Detalhes em `dashboard/README.md`. **Dashboard no ar:** https://survey-ia-medicao-es.streamlit.app/ (Streamlit Community Cloud).

**Só a análise, sem interface:** `dashboard/analise.py` não depende do Streamlit.

```sh
cd dashboard
../.venv/bin/python -c "import analise as a, json; \
f='../Respostas - Uso de assistentes de IA no desenvolvimento de software (COLETA).xlsx'; \
d=a.preparar(a.ler_arquivo(f,f), json.load(open('codificacao_outra.json'))); \
[print(r.rq, r.p, r.p_holm, r.efeito) for r in a.testes_confirmatorios(d.validas)]"
```

**Conferência independente** (só `openpyxl` e biblioteca padrão, sem o código do dashboard): `python3 dashboard/conferencia_alfa.py` (alfa de Cronbach) e `python3 dashboard/conferencia_rqs.py` (RQ1, RQ2 e RQ3) na raiz.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `protocolo/` | Protocolo da Parte 1 (v5, PDF entregue no Canvas e `.md`) |
| `Respostas - … (COLETA).xlsx` | Exportação bruta do formulário, não editada. Hash em `SHA256SUMS.txt` |
| `dashboard/app.py`, `analise.py` | Interface e estatística (regras de elegibilidade, descarte, testes, alfa) |
| `dashboard/desvios.md`, `consistencia.md`, `limitacoes.md` | Desvios, tabela protocolo × execução e limitações, exibidos na página de metodologia |
| `dashboard/codificacao_outra.json` | Codificação das respostas "Outra" de P4 e P5 |
| `docs/codebook.md` | Itens, variáveis, escalas e codificação |
| `docs/regras_de_limpeza.md` | Critérios de encerramento e descarte |
| `docs/evidencias/` | Prints datados (Canvas e divulgação) e revisão de privacidade |
| `docs/ENTREGA.md` | Pacote de entrega e verificação final |
| `docs/defesa.md` | Roteiro de 10 minutos, respostas-chave da arguição e cenários |

## Reprodutibilidade e integridade

- O arquivo bruto nunca é alterado. A limpeza acontece em memória, por regras explícitas (`docs/regras_de_limpeza.md`).
- Conferir o hash: `shasum -a 256 "Respostas - Uso de assistentes de IA no desenvolvimento de software (COLETA).xlsx"` deve coincidir com `SHA256SUMS.txt`.
- Permutações e bootstrap usam a semente 20261109, então os números se repetem.

## Privacidade

O formulário não coletou nome, e-mail nem IP. Veja `docs/evidencias/REVISAO_PRIVACIDADE.md`, inclusive a avaliação sobre a base bruta estar em repositório público.
