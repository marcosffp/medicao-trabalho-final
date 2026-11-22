# Regras de limpeza

Todas as regras foram fixadas na Seção 3 do protocolo v5, **antes da coleta**, e são aplicadas pelo código (`preparar()` em `dashboard/analise.py`). Nenhum arquivo bruto é editado: a limpeza acontece em memória a cada carga do dashboard. Para cada resposta fica registrado um `status` e um `motivo`.

A ordem de avaliação é a da tabela. A primeira regra de encerramento que se aplica define o motivo da inelegibilidade.

## 1. Encerramento do formulário (resposta "Inelegível")

O formulário se encerra para essas pessoas, então elas entram no funil como inelegíveis e **não contam** como descartadas.

| # | Regra | Código no dashboard | Ocorrências |
|---|---|---|---:|
| E1 | C0 diferente de "Sim" (não consentiu ou tem menos de 18 anos) | `C0: não consentiu…` | 0 |
| E2 | T1 = "Não" (não trabalha com desenvolvimento no Brasil) | `T1: não trabalha hoje…` | **11** |
| E3 | T2 = "Outro" | `T2 = "outro"…` | 0 |
| E4 | U1 = 1 (não usou IA nos últimos 3 meses) | `U1 = 1…` | 0 |

## 2. Descarte (resposta "Descartada")

Cada resposta descartada recebe um motivo. Os motivos podem se acumular na mesma resposta.

| # | Regra | Motivo registrado | Ocorrências |
|---|---|---|---:|
| D1 | AT1 diferente de "Discordo" (nível 2) | `AT1 diferente de 'Discordo' (marcou …)` | **10** (9 marcaram "Discordo totalmente", 1 "Concordo totalmente") |
| D2 | Item obrigatório em branco (T2, U1, U2, P1 a P5, PP1 a PP5, AT1) | `Item obrigatório em branco: …` | 0 |
| D3 | P1 não inteiro (decisão operacional: P1 é resposta curta) | `P1 não é um número inteiro de anos` | 0 |
| D4 | Resposta idêntica à anterior em todos os itens (enviada em sequência) | `Resposta repetida em sequência…` | 0 |

## 3. Só sinalizado, não descartado

| Situação | Tratamento |
|---|---|
| Linha reta (cinco itens PP originais iguais) | Marcada em `linha_reta` (1 caso); entra na análise principal e é testada em sensibilidade |
| Carimbo fora de 11 a 20/11/2026 | Marcado em `fora_janela` (0 casos); o protocolo não previa descarte |
| Carimbo anterior ao envio do protocolo (13/11, 9:17) | Alerta de violação de R-08 na página 1 (0 casos). Nesse caso, investigar antes de decidir |

## 4. Resultado e equação do funil

`90 recebidas = 11 inelegíveis + 10 descartadas + 69 válidas`

Verificações feitas: nenhuma data ilegível, nenhuma resposta duplicada (nem consecutiva nem espaçada) entre as elegíveis.

## 5. Princípios

- As regras não olham para o resultado das análises. Mudar uma regra depois de ver os dados seria desvio e precisaria ser declarado em `dashboard/desvios.md`.
- A regra D1 é estrita de propósito: AT1 só passa com "Discordo". Isso descarta quem marcou "Discordo totalmente", que pode ter lido a instrução. A regra foi fixada antes da coleta e mantida.
- Itens da matriz PP não têm "não sei": não há imputação, e itens em branco levam ao descarte.
- Texto livre ("Outra" em P4 e P5) não é carregado como texto: é trocado pela categoria de `codificacao_outra.json` ao ler o arquivo.
