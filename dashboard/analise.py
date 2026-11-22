"""Preparação dos dados e estatística do survey (Seções 3 e 5 do protocolo).

Este módulo não depende do Streamlit, para poder ser conferido isoladamente.
Todas as regras de elegibilidade, descarte e os testes seguem o protocolo da
Parte 1. Qualquer decisão que o protocolo não fixou está marcada com
"DECISÃO OPERACIONAL" e aparece na página de metodologia do dashboard.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

# --------------------------------------------------------------------------
# Parâmetros fixados no protocolo
# --------------------------------------------------------------------------
ALPHA = 0.05
Z95 = 1.96
N_META = 50
MIN_SEGMENTO = 5  # Seção 6: não exibir segmentos com menos de 5 pessoas
JANELA_COLETA = (pd.Timestamp("2026-11-11 00:00:00"), pd.Timestamp("2026-11-20 23:59:59"))
# Envio real do protocolo no Canvas (docs/evidencias/canvas_envio_parte1_2026-11-13.png), regra R-08
PROTOCOLO_ENVIO = pd.Timestamp("2026-11-13 09:17:00")

# DECISÃO OPERACIONAL: o protocolo cita permutação e bootstrap sem fixar
# número de reamostragens nem semente. Fixamos para o resultado ser reprodutível.
SEMENTE = 20261109
N_PERMUTACOES = 10_000
N_BOOTSTRAP = 10_000  # protocolo v5, Seção 5

PP_ITENS = ["PP1", "PP2", "PP3", "PP4", "PP5"]
PP_TEXTO = {
    "PP1": "PP1. Concluo minhas tarefas mais rápido",
    "PP2": "PP2. Entrego mais tarefas no mesmo período",
    "PP3": "PP3. A qualidade do código que entrego é melhor",
    "PP4": "PP4. Preciso refazer menos o código depois de entregue",
    "PP5": "PP5 (invertido). O trabalho fica mais cansativo ou trabalhoso",
}
LIKERT = {
    1: "Discordo totalmente",
    2: "Discordo",
    3: "Nem concordo nem discordo",
    4: "Concordo",
    5: "Concordo totalmente",
}
U1_ROTULOS = {
    1: "1 - Nunca",
    2: "2 - Uma ou poucas vezes no período",
    3: "3 - Algumas vezes por mês",
    4: "4 - Algumas vezes por semana",
    5: "5 - Todos ou quase todos os dias",
}
# Opções exatamente como aparecem no Google Formulários
OPCOES_T2 = ["Emprego", "Estágio", "Trabalho autônomo", "Outro"]
OPCOES_P2 = [
    "Até 10 pessoas",
    "11 a 50 pessoas",
    "51 a 200 pessoas",
    "201 a 1000 pessoas",
    "Mais de 1000 pessoas",
    "Não se aplica (trabalho autônomo)",
]
OPCOES_P3 = ["Menos de 3 meses", "De 3 a menos de 6 meses", "De 6 a menos de 12 meses", "12 meses ou mais"]  # rótulos do formulário v5
OPCOES_P4 = ["ChatGPT", "GitHub Copilot", "Claude", "Gemini", "Cursor"]
OPCOES_P5 = [
    "Escrever código",
    "Completar código",
    "Explicar código",
    "Revisar código",
    "Escrever testes",
    "Depurar código",
    "Planejar ou projetar código",  # incluída após o pré-teste (Seção 4)
]
OUTRA = "Outra (não codificada)"

FAIXAS_P1 = [(0, 2), (3, 5), (6, 10), (11, None)]
CLASSES_PP = ["Abaixo do neutro (1–2)", "Neutro (3)", "Acima do neutro (4–5)"]

# Cabeçalhos do CSV do Google Formulários -> código do item.
# Colunas que não casam (F1 a F5 do pré-teste, texto livre) são descartadas
# na leitura: o dashboard nunca carrega texto livre (Seção 6).
PADROES_COLUNAS = {
    "carimbo": r"^Carimbo de data",
    "C0": r"^C0\.",
    "T1": r"^T1\.",
    "T2": r"^T2\.",
    "U1": r"^U1\.",
    "U2": r"^U2\.",
    "P1": r"^P1\.",
    "P2": r"^P2\.",
    "P3": r"^P3\.",
    "P4": r"^P4\.",
    "P5": r"^P5\.",
    "PP1": r"\[PP1\.",
    "PP2": r"\[PP2\.",
    "PP3": r"\[PP3\.",
    "PP4": r"\[PP4\.",
    "PP5": r"\[PP5\.",
    "AT1": r"\[AT1\.",
}
OBRIGATORIOS = ["T2", "U1", "U2", "P1", "P2", "P3", "P4", "P5", *PP_ITENS, "AT1"]


# --------------------------------------------------------------------------
# Leitura e preparação
# --------------------------------------------------------------------------
def ler_arquivo(origem, nome: str = "dados.csv") -> pd.DataFrame:
    """Lê a exportação bruta CSV ou XLSX sem alterar o arquivo.

    No XLSX do Google Formulários, usa a primeira planilha não vazia. Isso
    ignora abas auxiliares vazias sem depender do nome traduzido da aba.
    """
    sufixo = Path(nome).suffix.lower()
    if sufixo == ".csv":
        return pd.read_csv(origem, dtype=str, keep_default_na=False, encoding="utf-8")
    if sufixo == ".xlsx":
        planilhas = pd.read_excel(origem, sheet_name=None, dtype=str, keep_default_na=False)
        for df in planilhas.values():
            if len(df.columns) and len(df):
                return df
        raise ValueError("A planilha XLSX não contém uma aba com respostas.")
    raise ValueError("Formato não aceito. Use a exportação CSV ou XLSX do Google Formulários.")


def ler_csv(origem) -> pd.DataFrame:
    """Compatibilidade com chamadas existentes que fornecem CSV."""
    return ler_arquivo(origem, "dados.csv")


def localizar_colunas(colunas) -> dict[str, str]:
    mapa: dict[str, str] = {}
    for col in colunas:
        nome = str(col).strip()
        for chave, padrao in PADROES_COLUNAS.items():
            if chave not in mapa and re.search(padrao, nome):
                mapa[chave] = col
                break
    return mapa


def _primeiro_digito(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s.str.extract(r"^\s*(\d)", expand=False), errors="coerce")


def _faixa_p1(anos: float) -> str | None:
    if pd.isna(anos):
        return None
    for lo, hi in FAIXAS_P1:
        if anos >= lo and (hi is None or anos <= hi):
            return rotulo_faixa(lo, hi)
    return None


def rotulo_faixa(lo: int, hi: int | None) -> str:
    return f"{lo} ou mais" if hi is None else f"{lo} a {hi}"


ORDEM_FAIXAS = [rotulo_faixa(lo, hi) for lo, hi in FAIXAS_P1]


def _multipla(valor: str, opcoes: list[str], codificacao: dict[str, str]) -> set[str]:
    """Separa uma resposta de múltipla escolha. Texto fora da lista vai para
    a categoria definida no livro de códigos ou, se não houver, para OUTRA."""
    marcadas: set[str] = set()
    if not valor:
        return marcadas
    for parte in valor.split(","):
        parte = parte.strip()
        if not parte:
            continue
        if parte in opcoes:
            marcadas.add(parte)
        else:
            marcadas.add(codificacao.get(parte.casefold(), OUTRA))
    return marcadas


@dataclass
class DadosPreparados:
    todas: pd.DataFrame          # uma linha por resposta recebida, com status e motivo
    validas: pd.DataFrame        # só as válidas, com variáveis derivadas
    colunas_ausentes: list[str]
    categorias_p4: list[str]
    categorias_p5: list[str]


def preparar(bruto: pd.DataFrame, codificacao: dict | None = None) -> DadosPreparados:
    codificacao = codificacao or {}
    cod_p4 = {k.casefold(): v for k, v in codificacao.get("P4", {}).items()}
    cod_p5 = {k.casefold(): v for k, v in codificacao.get("P5", {}).items()}

    mapa = localizar_colunas(bruto.columns)
    ausentes = [k for k in PADROES_COLUNAS if k not in mapa]
    criticas = {"C0", "T1", "U1", *PP_ITENS, "AT1", "P1"}
    if criticas & set(ausentes):
        raise ValueError(
            "O CSV não tem as colunas esperadas do formulário: "
            + ", ".join(sorted(criticas & set(ausentes)))
        )

    d = pd.DataFrame(index=bruto.index)
    for chave in PADROES_COLUNAS:
        d[chave] = bruto[mapa[chave]].astype(str).str.strip() if chave in mapa else ""

    out = pd.DataFrame({"id": np.arange(1, len(d) + 1)}, index=d.index)
    # CSVs trazem normalmente dd/mm/aaaa; XLSX lido como texto pode trazer ISO.
    # O modo mixed aceita ambos sem alterar o valor bruto no arquivo.
    out["carimbo"] = pd.to_datetime(d["carimbo"], format="mixed", dayfirst=True, errors="coerce")
    for item in ["U1", *PP_ITENS, "AT1"]:
        out[item] = _primeiro_digito(d[item])
    out["U2"] = pd.to_numeric(d["U2"].where(d["U2"].str.fullmatch(r"\d+"), None), errors="coerce")
    p1_ok = d["P1"].str.fullmatch(r"\d+")
    out["P1"] = pd.to_numeric(d["P1"].where(p1_ok, None), errors="coerce")
    for item in ["T2", "P2", "P3"]:
        out[item] = d[item].replace("", None)

    status, motivos = [], []
    ultima_assinatura = None
    for i in d.index:
        r = d.loc[i]
        m: list[str] = []
        # Encerramento do formulário (inelegíveis), Seção 3
        if not r["C0"].startswith("Sim"):
            m.append("C0: não consentiu ou tem menos de 18 anos")
        elif r["T1"] != "Sim":
            m.append("T1: não trabalha hoje com desenvolvimento no Brasil")
        elif r["T2"].casefold().startswith("outro"):
            m.append('T2 = "outro": vínculo fora de emprego, estágio ou autônomo')
        elif out.at[i, "U1"] == 1:
            m.append("U1 = 1: não usou assistente de IA nos últimos 3 meses")
        if m:
            status.append("Inelegível")
            motivos.append("; ".join(m))
            continue
        # Descarte (regras definidas antes da coleta), Seção 3
        brancos = [k for k in OBRIGATORIOS if r[k] == ""]
        if brancos:
            m.append("Item obrigatório em branco: " + ", ".join(brancos))
        if r["P1"] != "" and not p1_ok[i]:
            # DECISÃO OPERACIONAL: P1 é resposta curta; valor não inteiro é tratado como inválido
            m.append("P1 não é um número inteiro de anos")
        at1 = out.at[i, "AT1"]
        if r["AT1"] != "" and at1 != 2:
            marcado = LIKERT.get(int(at1), r["AT1"]) if pd.notna(at1) else r["AT1"]
            m.append(f"AT1 diferente de 'Discordo' (marcou '{marcado}')")
        # Protocolo v5, Seção 3: respostas idênticas em todos os itens e enviadas em sequência
        itens_chave = ["T2", "U1", "U2", "P1", "P2", "P3", "P4", "P5", *PP_ITENS, "AT1"]
        assinatura = tuple(r[k] for k in itens_chave)
        if ultima_assinatura is not None and assinatura == ultima_assinatura:
            m.append("Resposta repetida em sequência (idêntica à anterior)")
        ultima_assinatura = assinatura
        if m:
            status.append("Descartada")
            motivos.append("; ".join(m))
        else:
            status.append("Válida")
            motivos.append("")
    out["status"] = status
    out["motivo"] = motivos
    out["fora_janela"] = out["carimbo"].notna() & (
        (out["carimbo"] < JANELA_COLETA[0]) | (out["carimbo"] > JANELA_COLETA[1])
    )

    # Variáveis derivadas (só para válidas)
    v = out[out["status"] == "Válida"].copy()
    v["PP5r"] = 6 - v["PP5"]
    itens_r = ["PP1", "PP2", "PP3", "PP4", "PP5r"]
    v["PP_med"] = v[itens_r].median(axis=1).astype(int)
    v["classe_PP"] = pd.cut(v["PP_med"], bins=[0, 2, 3, 5], labels=CLASSES_PP)
    v["linha_reta"] = v[PP_ITENS].nunique(axis=1) == 1  # cinco itens PP iguais (antes de recodificar)
    v["faixa_P1"] = pd.Categorical(v["P1"].map(_faixa_p1), categories=ORDEM_FAIXAS, ordered=True)
    v["U1_rotulo"] = pd.Categorical(
        v["U1"].map(U1_ROTULOS), categories=list(U1_ROTULOS.values()), ordered=True
    )
    v["T2"] = pd.Categorical(v["T2"], categories=OPCOES_T2)
    v["P2"] = pd.Categorical(v["P2"], categories=OPCOES_P2, ordered=True)
    v["P3"] = pd.Categorical(v["P3"], categories=OPCOES_P3, ordered=True)
    # Porte como ordinal: "Não se aplica" é tratado como ausente (Seção 3)
    v["P2_ord"] = v["P2"].map({o: i + 1 for i, o in enumerate(OPCOES_P2[:-1])}).astype(float)

    p4 = d.loc[v.index, "P4"].map(lambda x: _multipla(x, OPCOES_P4, cod_p4))
    p5 = d.loc[v.index, "P5"].map(lambda x: _multipla(x, OPCOES_P5, cod_p5))
    cat_p4 = _ordenar_categorias(p4, OPCOES_P4)
    cat_p5 = _ordenar_categorias(p5, OPCOES_P5)
    for c in cat_p4:
        v[f"P4::{c}"] = p4.map(lambda s, c=c: c in s)
    for c in cat_p5:
        v[f"P5::{c}"] = p5.map(lambda s, c=c: c in s)

    return DadosPreparados(out, v, ausentes, cat_p4, cat_p5)


def _ordenar_categorias(series: pd.Series, opcoes: list[str]) -> list[str]:
    todas = set().union(*series.tolist()) if len(series) else set()
    extras = sorted(c for c in todas if c not in opcoes and c != OUTRA)
    return [*opcoes, *extras, *([OUTRA] if OUTRA in todas else [])]


# --------------------------------------------------------------------------
# Estatística descritiva
# --------------------------------------------------------------------------
def resumo_ordinal(s: pd.Series) -> dict:
    s = pd.to_numeric(s, errors="coerce").dropna()
    if s.empty:
        return {"n": 0, "Mediana": np.nan, "Q1": np.nan, "Q3": np.nan}
    return {"n": len(s), "Mediana": s.median(), "Q1": s.quantile(0.25), "Q3": s.quantile(0.75)}


def resumo_razao(s: pd.Series) -> dict:
    s = pd.to_numeric(s, errors="coerce").dropna()
    base = resumo_ordinal(s)
    base.update(
        {
            "Média": s.mean() if len(s) else np.nan,
            "DP": s.std(ddof=1) if len(s) > 1 else np.nan,
            "Mín": s.min() if len(s) else np.nan,
            "Máx": s.max() if len(s) else np.nan,
        }
    )
    return base


def margem_erro(p: float, n: int) -> float:
    """Fórmula do enunciado: e = 1,96 × √(p(1 − p)/n)."""
    if n <= 0 or pd.isna(p):
        return np.nan
    return Z95 * np.sqrt(p * (1 - p) / n)


# --------------------------------------------------------------------------
# Testes confirmatórios
# --------------------------------------------------------------------------
@dataclass
class Resultado:
    rq: str
    pergunta: str
    teste: str
    n: int
    estatistica_nome: str
    estatistica: float
    p: float
    efeito_nome: str
    efeito: float
    ic: tuple[float, float]
    ic_metodo: str
    margem: float
    margem_texto: str
    leitura_efeito: str = ""
    p_holm: float = np.nan
    rejeita: bool = False
    notas: list[str] = field(default_factory=list)


def teste_rq1(v: pd.DataFrame) -> Resultado:
    pm = v["PP_med"]
    acima, abaixo, empates = int((pm >= 4).sum()), int((pm <= 2).sum()), int((pm == 3).sum())
    n_eff = acima + abaixo
    notas = [
        f"n válido = {len(v)}; empates em PP_med = 3 fora do teste: {empates}; n efetivo = {n_eff}.",
        f"Proporção com PP_med ≥ 4 entre todos os válidos: {_pct(acima / len(v)) if len(v) else '–'}; "
        f"com PP_med ≤ 2: {_pct(abaixo / len(v)) if len(v) else '–'}.",
    ]
    if n_eff == 0:
        return Resultado("RQ1", "PP_med difere do neutro (3)?", "Teste do sinal exato (binomial, p = 0,5)",
                         0, "k (acima do neutro)", np.nan, np.nan, "Proporção ≥ 4 (sem empates)", np.nan,
                         (np.nan, np.nan), "Clopper-Pearson 95%", np.nan, "", notas=notas + ["Sem casos fora do neutro."])
    res = stats.binomtest(acima, n_eff, 0.5, alternative="two-sided")
    ic = res.proportion_ci(confidence_level=0.95, method="exact")
    prop = acima / n_eff
    # Protocolo v5, Seção 2: a margem da RQ1 é a da proporção de PP_med ≥ 4 entre TODOS os usuários válidos.
    prop_todos = acima / len(v)
    margem = margem_erro(prop_todos, len(v))
    pior = margem_erro(0.5, len(v))
    texto = (f"± {_pp(margem)} (proporção de PP_med ≥ 4 entre todos os usuários válidos: {_pct(prop_todos)}, "
             f"n = {len(v)}); pior caso p = 0,5: ± {_pp(pior)}")
    notas.append("Para a proporção entre os não empatados o intervalo relatado é o de Clopper-Pearson "
                 "(a fórmula do enunciado não vale perto de 0% ou 100%).")
    return Resultado("RQ1", "A produtividade percebida difere do ponto neutro da escala?",
                     "Teste do sinal exato (binomial, p = 0,5 sob H0), bicaudal",
                     n_eff, "k (acima do neutro)", float(acima), float(res.pvalue),
                     "Proporção de PP_med ≥ 4 entre não empatados", prop,
                     (float(ic.low), float(ic.high)), "Clopper-Pearson 95%", margem, texto, notas=notas)


def _rank_pearson_linhas(rx: np.ndarray, ry: np.ndarray) -> np.ndarray:
    """Correlação de Pearson linha a linha entre matrizes de postos (B × n)."""
    rx = rx - rx.mean(axis=1, keepdims=True)
    ry = ry - ry.mean(axis=1, keepdims=True)
    num = (rx * ry).sum(axis=1)
    den = np.sqrt((rx**2).sum(axis=1) * (ry**2).sum(axis=1))
    with np.errstate(invalid="ignore", divide="ignore"):
        return num / den


def spearman_completo(x, y, semente: int = SEMENTE) -> dict:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    ok = ~(np.isnan(x) | np.isnan(y))
    x, y = x[ok], y[ok]
    n = len(x)
    vazio = {"n": n, "rho": np.nan, "p_t": np.nan, "p_perm": np.nan, "ic": (np.nan, np.nan), "motivo": ""}
    if n < 3:
        return vazio | {"motivo": "menos de 3 observações"}
    if np.unique(x).size < 2 or np.unique(y).size < 2:
        return vazio | {"motivo": "uma das variáveis é constante no conjunto filtrado"}
    rho, p_t = stats.spearmanr(x, y)  # postos médios nos empates; p pela aproximação t
    rng = np.random.default_rng(semente)
    rx, ry = stats.rankdata(x), stats.rankdata(y)
    perm = rng.permuted(np.tile(ry, (N_PERMUTACOES, 1)), axis=1)
    r_perm = _rank_pearson_linhas(np.tile(rx, (N_PERMUTACOES, 1)), perm)
    p_perm = (np.sum(np.abs(r_perm) >= abs(rho) - 1e-12) + 1) / (N_PERMUTACOES + 1)
    idx = rng.integers(0, n, size=(N_BOOTSTRAP, n))
    bx = stats.rankdata(x[idx], axis=1)
    by = stats.rankdata(y[idx], axis=1)
    r_boot = _rank_pearson_linhas(bx, by)
    r_boot = r_boot[~np.isnan(r_boot)]
    ic = (float(np.percentile(r_boot, 2.5)), float(np.percentile(r_boot, 97.5))) if r_boot.size else (np.nan, np.nan)
    return {"n": n, "rho": float(rho), "p_t": float(p_t), "p_perm": float(p_perm), "ic": ic, "motivo": ""}


def leitura_cohen(rho: float) -> str:
    if pd.isna(rho):
        return "não calculável"
    a = abs(rho)
    if a < 0.1:
        return "desprezível"
    if a < 0.3:
        return "pequeno"
    if a < 0.5:
        return "médio"
    return "grande"


def _teste_spearman(rq: str, pergunta: str, v: pd.DataFrame, col_x: str, nome_x: str) -> Resultado:
    s = spearman_completo(v[col_x], v["PP_med"])
    notas = [f"Valor p por permutação ({milhar(N_PERMUTACOES)} permutações, semente {SEMENTE}): "
             f"{fmt_p(s['p_perm'])}."]
    if s["motivo"]:
        notas.append(f"Não calculável: {s['motivo']}.")
    margem = margem_erro(0.5, s["n"])
    p_conf = s["p_t"]
    if pd.notna(s["p_perm"]) and pd.notna(p_conf) and ((p_conf < ALPHA) != (s["p_perm"] < ALPHA)):
        # Protocolo v5, Seção 5: a permutação prevalece sobre a aproximação t se os dois divergirem
        p_conf = s["p_perm"]
        notas.append("A aproximação t e a permutação divergem na decisão: vale o p por permutação (protocolo v5).")
    return Resultado(rq, pergunta, f"Correlação de Spearman ({nome_x} × PP_med), postos médios, bicaudal",
                     s["n"], "ρ de Spearman", s["rho"], p_conf, "ρ de Spearman", s["rho"], s["ic"],
                     f"bootstrap percentil 95% ({milhar(N_BOOTSTRAP)} reamostras)",
                     margem, f"± {_pp(margem)} (margem geral da amostra, p = 0,5, n = {s['n']})",
                     leitura_cohen(s["rho"]), notas=notas)


def teste_rq2(v: pd.DataFrame) -> Resultado:
    return _teste_spearman("RQ2", "A frequência de uso (U1) está associada à produtividade percebida?", v, "U1", "U1")


def teste_rq3(v: pd.DataFrame) -> Resultado:
    return _teste_spearman("RQ3", "O tempo de experiência (P1) está associado à produtividade percebida?", v, "P1", "P1")


def holm(resultados: list[Resultado], alpha: float = ALPHA) -> list[Resultado]:
    """Correção de Holm na família de 3 testes. p não calculável conta como 1."""
    m = len(resultados)
    ps = np.array([1.0 if pd.isna(r.p) else r.p for r in resultados])
    ordem = np.argsort(ps)
    ajust = np.empty(m)
    acumulado = 0.0
    parou = False
    for posicao, i in enumerate(ordem):
        acumulado = max(acumulado, min(1.0, (m - posicao) * ps[i]))
        ajust[i] = acumulado
        if not parou and ps[i] <= alpha / (m - posicao):
            resultados[i].rejeita = True
        else:
            parou = True
            resultados[i].rejeita = False
    for r, pa in zip(resultados, ajust):
        r.p_holm = np.nan if pd.isna(r.p) else float(pa)
    return resultados


def testes_confirmatorios(v: pd.DataFrame) -> list[Resultado]:
    return holm([teste_rq1(v), teste_rq2(v), teste_rq3(v)])


# --------------------------------------------------------------------------
# Confiabilidade
# --------------------------------------------------------------------------
def _alfa(m: np.ndarray) -> float:
    k = m.shape[-1]
    var_itens = m.var(axis=-2, ddof=1).sum(axis=-1)
    var_total = m.sum(axis=-1).var(axis=-1, ddof=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return k / (k - 1) * (1 - var_itens / var_total)


def cronbach(v: pd.DataFrame, itens: list[str], semente: int = SEMENTE) -> dict:
    m = v[itens].to_numpy(dtype=float)
    n, k = m.shape
    if n < 3:
        return {"n": n, "k": k, "alfa": np.nan, "ic": (np.nan, np.nan), "itens": pd.DataFrame(),
                "motivo": "menos de 3 respostas válidas"}
    alfa = float(_alfa(m))
    rng = np.random.default_rng(semente)
    boot = _alfa(m[rng.integers(0, n, size=(N_BOOTSTRAP, n))])
    boot = boot[np.isfinite(boot)]
    ic = (float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))) if boot.size else (np.nan, np.nan)
    linhas = []
    for j, item in enumerate(itens):
        resto = np.delete(m, j, axis=1)
        total_resto = resto.sum(axis=1)
        if np.std(m[:, j]) > 0 and np.std(total_resto) > 0:
            r_it = float(np.corrcoef(m[:, j], total_resto)[0, 1])
        else:
            r_it = np.nan
        linhas.append({"Item": item, "Correlação item-total corrigida": r_it,
                       "Alfa se o item for removido": float(_alfa(resto))})
    motivo = "" if np.isfinite(alfa) else "variância total zero (todos responderam igual)"
    return {"n": n, "k": k, "alfa": alfa, "ic": ic, "itens": pd.DataFrame(linhas), "motivo": motivo}


# --------------------------------------------------------------------------
# Análises exploratórias (fora da família, sem correção)
# --------------------------------------------------------------------------
def agrupar_faixas(contagens: pd.Series) -> dict[str, str]:
    """Agrupa faixas de P1 com menos de 5 pessoas com a vizinha (Seção 1, RQ3)."""
    grupos = [[(lo, hi)] for lo, hi in FAIXAS_P1]
    cont = [int(contagens.get(rotulo_faixa(lo, hi), 0)) for lo, hi in FAIXAS_P1]
    # remove faixas vazias nas pontas não altera o agrupamento; vazias no meio são absorvidas
    while len(grupos) > 1 and min(cont) < MIN_SEGMENTO:
        i = int(np.argmin(cont))
        if i == 0:
            j = 1
        elif i == len(grupos) - 1:
            j = i - 1
        else:
            j = i - 1 if cont[i - 1] <= cont[i + 1] else i + 1
        a, b = sorted((i, j))
        grupos[a] = grupos[a] + grupos[b]
        cont[a] = cont[a] + cont[b]
        del grupos[b], cont[b]
    mapa = {}
    for g in grupos:
        rot = rotulo_faixa(g[0][0], g[-1][1])
        for lo, hi in g:
            mapa[rotulo_faixa(lo, hi)] = rot
    return mapa


def _pct_ic(valores) -> tuple[float, float]:
    v = np.asarray(valores, dtype=float)
    v = v[np.isfinite(v)]
    return (float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))) if v.size else (np.nan, np.nan)


def _ic_cliff(y: np.ndarray, grupo_a: np.ndarray, semente: int = SEMENTE) -> tuple[float, float]:
    """IC bootstrap percentil do δ de Cliff (A vs B), vetorizado."""
    idx = np.random.default_rng(semente).integers(0, len(y), size=(N_BOOTSTRAP, len(y)))
    yy, ga = y[idx], grupo_a[idx]
    r = stats.rankdata(yy, axis=1)
    n1 = ga.sum(axis=1)
    n2 = yy.shape[1] - n1
    with np.errstate(invalid="ignore", divide="ignore"):
        u = (r * ga).sum(axis=1) - n1 * (n1 + 1) / 2
        delta = 2 * u / (n1 * n2) - 1
    return _pct_ic(delta)


def _ic_eps2(y: np.ndarray, cod: np.ndarray, k: int, semente: int = SEMENTE) -> tuple[float, float]:
    """IC bootstrap percentil de ε² = H/(n − 1) (H com correção de empates), vetorizado."""
    idx = np.random.default_rng(semente).integers(0, len(y), size=(N_BOOTSTRAP, len(y)))
    yy, gg = y[idx], cod[idx]
    n = yy.shape[1]
    r = stats.rankdata(yy, axis=1)
    soma = np.zeros(len(yy))
    vazio = np.zeros(len(yy), dtype=bool)
    for j in range(k):
        m = gg == j
        nj = m.sum(axis=1)
        vazio |= nj == 0
        soma += np.where(nj > 0, (r * m).sum(axis=1) ** 2 / np.maximum(nj, 1), 0)
    h = 12 / (n * (n + 1)) * soma - 3 * (n + 1)
    t = sum((yy == val).sum(axis=1) ** 3 - (yy == val).sum(axis=1) for val in np.unique(y))
    with np.errstate(invalid="ignore", divide="ignore"):
        eps = (h / (1 - t / (n**3 - n))) / (n - 1)
    eps[vazio] = np.nan
    return _pct_ic(eps)


def comparar_grupos(v: pd.DataFrame, col_grupo: str, col_y: str = "PP_med") -> dict:
    """Mann-Whitney com δ de Cliff (2 grupos) ou Kruskal-Wallis com ε² (3+), só com grupos de ≥ 5 pessoas.

    Protocolo v5, Seção 5: efeitos exploratórios com IC de 95% por bootstrap percentil."""
    dados = v[[col_grupo, col_y]].dropna()
    tamanhos = dados.groupby(col_grupo, observed=True).size()
    usados = tamanhos[tamanhos >= MIN_SEGMENTO].index.tolist()
    excluidos = tamanhos[tamanhos < MIN_SEGMENTO].index.tolist()
    dados = dados[dados[col_grupo].isin(usados)]
    grupos = [dados.loc[dados[col_grupo] == g, col_y].to_numpy(dtype=float) for g in usados]
    base = {"usados": usados, "excluidos": excluidos, "tamanhos": tamanhos}
    if len(grupos) < 2:
        return base | {"teste": None, "motivo": "menos de 2 grupos com 5 ou mais pessoas"}
    n = sum(len(g) for g in grupos)
    y = dados[col_y].to_numpy(dtype=float)
    try:
        if len(grupos) == 2:
            u, p = stats.mannwhitneyu(grupos[0], grupos[1], alternative="two-sided")
            delta = 2 * u / (len(grupos[0]) * len(grupos[1])) - 1  # = δ de Cliff (A vs B)
            ic = _ic_cliff(y, (dados[col_grupo] == usados[0]).to_numpy())
            return base | {"teste": "Mann-Whitney U", "estatistica": float(u), "p": float(p),
                           "efeito_nome": f"δ de Cliff ({usados[0]} vs {usados[1]})",
                           "efeito": float(delta), "ic": ic, "n": n, "motivo": ""}
        h, p = stats.kruskal(*grupos)
        cod = dados[col_grupo].map({g: i for i, g in enumerate(usados)}).to_numpy()
        return base | {"teste": "Kruskal-Wallis H", "estatistica": float(h), "p": float(p),
                       "efeito_nome": "ε² = H / (n − 1)", "efeito": float(h / (n - 1)),
                       "ic": _ic_eps2(y, cod, len(usados)), "n": n, "motivo": ""}
    except ValueError as exc:  # todos os valores iguais
        return base | {"teste": None, "motivo": f"teste não calculável ({exc})"}


def _v_cramer(tab: np.ndarray) -> float:
    n = tab.sum()
    esp = np.outer(tab.sum(axis=1), tab.sum(axis=0)) / n
    with np.errstate(invalid="ignore", divide="ignore"):
        chi2 = np.nansum(np.where(esp > 0, (tab - esp) ** 2 / esp, 0))
    return float(np.sqrt(chi2 / (n * (min(tab.shape) - 1))))


def qui_quadrado(v: pd.DataFrame, col_grupo: str, semente: int = SEMENTE) -> dict:
    """χ² quando todas as frequências esperadas são ≥ 5; senão Fisher (Freeman-Halton em tabelas > 2×2).

    Protocolo v5, Seção 5. DECISÃO OPERACIONAL: o teste exato de tabelas maiores que 2×2 é calculado por
    Monte Carlo (10.000 permutações dos rótulos), pois o SciPy só traz o exato 2×2. Efeito: V de Cramér com IC bootstrap."""
    dados = v[[col_grupo, "classe_PP"]].dropna()
    tamanhos = dados.groupby(col_grupo, observed=True).size()
    usados = tamanhos[tamanhos >= MIN_SEGMENTO].index.tolist()
    dados = dados[dados[col_grupo].isin(usados)]
    tab = pd.crosstab(dados[col_grupo], dados["classe_PP"])
    tab = tab.loc[:, tab.sum() > 0]
    if tab.shape[0] < 2 or tab.shape[1] < 2:
        return {"tabela": tab, "motivo": "tabela com menos de 2 linhas ou colunas"}
    chi2, p_chi, gl, esperado = stats.chi2_contingency(tab)
    arr = tab.to_numpy().astype(float)
    n = arr.sum()
    v_obs = float(np.sqrt(chi2 / (n * (min(tab.shape) - 1))))
    exato = bool((esperado < 5).any())
    if not exato:
        p, metodo = float(p_chi), "χ² de independência"
    elif tab.shape == (2, 2):
        p, metodo = float(stats.fisher_exact(arr)[1]), "teste exato de Fisher (2×2)"
    else:
        rng = np.random.default_rng(semente)
        x = pd.Categorical(dados[col_grupo]).codes
        z = pd.Categorical(dados["classe_PP"]).codes
        kx, kz = tab.shape[0], len(np.unique(z))
        zc = np.unique(z)
        remap = {c: i for i, c in enumerate(zc)}
        z = np.array([remap[c] for c in z])
        from scipy.special import gammaln

        def logp(zz):
            t = np.bincount(x * kz + zz, minlength=kx * kz)
            return -gammaln(t + 1).sum()
        lp0 = logp(z)
        cont = sum(logp(rng.permutation(z)) <= lp0 + 1e-9 for _ in range(N_PERMUTACOES))
        p, metodo = float((cont + 1) / (N_PERMUTACOES + 1)), "teste exato de Fisher-Freeman-Halton (Monte Carlo)"
    # IC bootstrap do V de Cramér
    rng = np.random.default_rng(semente)
    x = pd.Categorical(dados[col_grupo]).codes
    zc = pd.Categorical(dados["classe_PP"]).codes
    kx = tab.shape[0]
    kz = int(zc.max()) + 1
    vs = []
    for _ in range(N_BOOTSTRAP):
        ii = rng.integers(0, len(x), len(x))
        t = np.bincount(x[ii] * kz + zc[ii], minlength=kx * kz).reshape(kx, kz).astype(float)
        t = t[t.sum(axis=1) > 0][:, t.sum(axis=0) > 0]
        if t.shape[0] >= 2 and t.shape[1] >= 2:
            vs.append(_v_cramer(t))
    return {"tabela": tab, "chi2": float(chi2), "p": p, "gl": int(gl), "v": v_obs, "ic": _pct_ic(vs),
            "metodo": metodo, "esperado_baixo": exato, "motivo": ""}


def sensibilidade_subescalas(v: pd.DataFrame) -> pd.DataFrame:
    """Protocolo v5, Seção 3: com α < 0,70, as subescalas de rapidez (PP1, PP2) e qualidade (PP3, PP4)
    são analisadas à parte, como sensibilidade (escore = média dos dois itens; PP5 não é excluído da análise principal)."""
    sub = {"Rapidez (PP1, PP2)": ["PP1", "PP2"], "Qualidade (PP3, PP4)": ["PP3", "PP4"]}
    linhas = []
    for nome, itens in sub.items():
        esc = v[itens].mean(axis=1)
        acima, abaixo = int((esc > 3).sum()), int((esc < 3).sum())
        n_eff = acima + abaixo
        if n_eff:
            p1 = float(stats.binomtest(acima, n_eff, 0.5).pvalue)
            linhas.append({"Subescala": nome, "RQ": "RQ1 (sinal vs. 3)", "n": n_eff,
                           "Estatística": f"k = {acima}", "p bruto": p1,
                           "Efeito": f"{acima / n_eff:.3f} acima do neutro"})
        for rq, col in [("RQ2 (U1)", "U1"), ("RQ3 (P1)", "P1")]:
            r, p = stats.spearmanr(v[col], esc)
            linhas.append({"Subescala": nome, "RQ": rq, "n": int(v[[col]].notna().sum().iloc[0]),
                           "Estatística": f"ρ = {r:.3f}", "p bruto": float(p), "Efeito": f"ρ = {r:.3f} ({leitura_cohen(r)})"})
    return pd.DataFrame(linhas)


def media_itens_vs_ppmed(v: pd.DataFrame) -> dict:
    """Protocolo v5, Seção 3: checagem exploratória, média dos cinco itens (PP5 recodificado) e Spearman com PP_med."""
    media = v[["PP1", "PP2", "PP3", "PP4", "PP5r"]].mean(axis=1)
    r, p = stats.spearmanr(media, v["PP_med"])
    return {"media": float(media.mean()), "dp": float(media.std(ddof=1)), "rho": float(r), "p": float(p), "n": len(v)}


# --------------------------------------------------------------------------
# Formatação (pt-BR)
# --------------------------------------------------------------------------
def fmt(x, casas: int = 3) -> str:
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "–"
    return f"{x:.{casas}f}".replace(".", ",")


def fmt_p(p) -> str:
    if p is None or pd.isna(p):
        return "–"
    return "< 0,001" if p < 0.001 else fmt(p, 3)


def _pct(x: float) -> str:
    return "–" if pd.isna(x) else f"{x * 100:.1f}%".replace(".", ",")


def _pp(x: float) -> str:
    return "–" if pd.isna(x) else f"{x * 100:.1f}".replace(".", ",") + " p.p."


def milhar(n: int) -> str:
    return f"{n:,}".replace(",", ".")


pct = _pct
pp = _pp
