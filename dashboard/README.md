# Dashboard do survey

Streamlit que lê a exportação CSV bruta do Google Formulários e recalcula tudo a cada carga: funil e motivos de descarte, Likert em barras divergentes, RQ1 a RQ3 (teste, p bruto e Holm, efeito com IC, margem de erro), alfa de Cronbach, filtros por segmento e a página de metodologia e desvios.

## Como rodar

Na raiz do projeto:

```sh
python3 -m venv .venv
.venv/bin/pip install -r dashboard/requirements.txt
.venv/bin/streamlit run dashboard/app.py
```

**Acesso:** o dashboard não tem link público. Ele roda localmente com os comandos acima e é demonstrado ao vivo na defesa.

## Fonte dos dados (nesta ordem)

1. Arquivo CSV ou XLSX enviado na barra lateral do dashboard.
2. Variável de ambiente `SURVEY_DATA` com o caminho da exportação (`SURVEY_CSV` também funciona por compatibilidade).
3. Arquivo `Respostas*.xlsx` ou `Respostas*.csv` na raiz do projeto. A exportação da coleta tem preferência sobre a do pré-teste. Se só houver o pré-teste, o dashboard mostra um aviso.

O dashboard já encontra automaticamente o arquivo oficial `Respostas - Uso de assistentes de IA no desenvolvimento de software (COLETA).xlsx`. No XLSX, ele usa a primeira aba não vazia, atualmente `Respostas ao formulário 1`, e ignora a aba vazia `Página1`.

O arquivo nunca é alterado. Colunas de texto livre não são carregadas.

## Arquivos

- `app.py`: interface.
- `analise.py`: regras de elegibilidade e descarte e toda a estatística (sem Streamlit).
- `consistencia.md`: tabela protocolo × execução, exibida na última página, antes dos desvios.
- `desvios.md`: tabela de desvios em relação ao protocolo da Parte 1, exibida na última página. Atualizar depois da coleta.
- `codificacao_outra.json`: resultado da codificação das respostas "Outra" de P4 e P5.
