"""Dashboard do survey: assistentes de IA e produtividade percebida.

Executar a partir da raiz do projeto:
    .venv/bin/streamlit run dashboard/app.py

O dashboard lê a exportação CSV ou XLSX bruta do Google Formulários. A fonte
é, em ordem: arquivo enviado na barra lateral; variável de ambiente
SURVEY_DATA (SURVEY_CSV também é aceita por compatibilidade); exportação
"Respostas*.xlsx" ou "Respostas*.csv" da raiz do projeto (a coleta tem
preferência sobre o pré-teste).
"""
from __future__ import annotations

import io
import json
import os
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import analise as a

RAIZ = Path(__file__).resolve().parent.parent
PASTA = Path(__file__).resolve().parent

st.set_page_config(page_title="Survey IA e produtividade percebida", layout="wide")

CORES_LIKERT = {1: "#b2182b", 2: "#ef8a62", 3: "#bdbdbd", 4: "#67a9cf", 5: "#2166ac"}


# --------------------------------------------------------------------------
# Fonte de dados
# --------------------------------------------------------------------------
def localizar_dados() -> tuple[Path | None, list[Path]]:
    env = os.environ.get("SURVEY_DATA") or os.environ.get("SURVEY_CSV")
    if env:
        p = Path(env).expanduser().resolve()
        return (p if p.is_file() else None), []
    candidatos = sorted([*RAIZ.glob("Respostas*.csv"), *RAIZ.glob("Respostas*.xlsx")])
    coleta = [c for c in candidatos if "PRÉ-TESTE" not in unicodedata.normalize("NFC", c.name).upper()]
    return (coleta or candidatos or [None])[0], candidatos


@st.cache_data(show_spinner="Lendo e preparando os dados...")
def carregar(conteudo: bytes, nome: str, codificacao_txt: str) -> tuple[a.DadosPreparados, list[str]]:
    codificacao = json.loads(codificacao_txt) if codificacao_txt else {}
    bruto = a.ler_arquivo(io.BytesIO(conteudo), nome)
    return a.preparar(bruto, codificacao), list(map(str, bruto.columns))


@st.cache_data(show_spinner="Calculando testes...")
def confirmatorios(v: pd.DataFrame) -> list[a.Resultado]:
    return a.testes_confirmatorios(v)


@st.cache_data(show_spinner=False)
def alfa_cache(v: pd.DataFrame) -> dict:
    return a.cronbach(v, ["PP1", "PP2", "PP3", "PP4", "PP5r"])


st.sidebar.title("Fonte de dados")
enviado = st.sidebar.file_uploader("Exportação do Google Formulários", type=["csv", "xlsx"])
if enviado is not None:
    conteudo, nome_fonte = enviado.getvalue(), enviado.name
else:
    caminho, _ = localizar_dados()
    if caminho is None:
        st.error("Nenhuma exportação encontrada. Envie um CSV/XLSX na barra lateral ou defina SURVEY_DATA.")
        st.stop()
    conteudo, nome_fonte = caminho.read_bytes(), caminho.name
st.sidebar.caption("Arquivo lido (sem alteração):")
st.sidebar.text(nome_fonte)

cod_path = PASTA / "codificacao_outra.json"
cod_txt = cod_path.read_text(encoding="utf-8") if cod_path.is_file() else ""
try:
    dados, _cabecalho = carregar(conteudo, nome_fonte, cod_txt)
except (ValueError, UnicodeDecodeError, pd.errors.ParserError, ImportError) as exc:
    st.error(f"Não foi possível ler a exportação: {exc}")
    st.stop()

# Pré-teste: nome do arquivo ou colunas de feedback (F1 a F5) que só existem nele
eh_preteste = ("PRÉ-TESTE" in unicodedata.normalize("NFC", nome_fonte).upper()
               or any(str(c).startswith("F1.") for c in _cabecalho))
todas, validas = dados.todas, dados.validas

# --------------------------------------------------------------------------
# Filtros por segmento
# --------------------------------------------------------------------------
st.sidebar.title("Filtros por segmento")
st.sidebar.caption("Valem para perfil, Likert, confiabilidade e análises exploratórias. "
                   "A resposta confirmatória de cada RQ usa sempre a amostra completa.")


def multiselect(rotulo: str, serie: pd.Series) -> list:
    opcoes = [c for c in serie.cat.categories if (serie == c).any()]
    return st.sidebar.multiselect(rotulo, opcoes, placeholder="Todos")


f_faixa = multiselect("Tempo de experiência (P1, anos)", validas["faixa_P1"])
f_t2 = multiselect("Vínculo (T2)", validas["T2"])
f_p2 = multiselect("Porte da organização (P2)", validas["P2"])
f_p3 = multiselect("Tempo de uso de IA (P3)", validas["P3"])
f_u1 = multiselect("Frequência de uso (U1)", validas["U1_rotulo"])
f_p4 = st.sidebar.multiselect("Usa a ferramenta (P4)", dados.categorias_p4, placeholder="Todas")

mask = pd.Series(True, index=validas.index)
for col, sel in [("faixa_P1", f_faixa), ("T2", f_t2), ("P2", f_p2), ("P3", f_p3), ("U1_rotulo", f_u1)]:
    if sel:
        mask &= validas[col].isin(sel)
if f_p4:
    mask &= validas[[f"P4::{c}" for c in f_p4]].any(axis=1)
filtrada = validas[mask]
filtro_ativo = bool(f_faixa or f_t2 or f_p2 or f_p3 or f_u1 or f_p4)
st.sidebar.metric("Respostas válidas no filtro", f"{len(filtrada)} de {len(validas)}")


def segmento_ok() -> bool:
    """Seção 6: com filtro ativo, segmentos com menos de 5 pessoas não são exibidos."""
    if filtro_ativo and len(filtrada) < a.MIN_SEGMENTO:
        st.warning(f"O filtro atual tem {len(filtrada)} pessoa(s). Segmentos com menos de "
                   f"{a.MIN_SEGMENTO} pessoas não são exibidos (Seção 6 do protocolo, anonimização).")
        return False
    if len(filtrada) == 0:
        st.info("Nenhuma resposta válida.")
        return False
    return True


# --------------------------------------------------------------------------
# Cabeçalho
# --------------------------------------------------------------------------
st.title("Assistentes de IA e produtividade percebida")
st.caption("Survey com desenvolvedores no Brasil · Medição e Experimentação em Engenharia de Software (PUC Minas)")
if eh_preteste:
    st.warning("Os dados carregados são do **pré-teste** (06 e 07/11/2026). Pelo protocolo, eles não entram "
               "na análise. Os números abaixo só demonstram o funcionamento do dashboard. Depois da coleta "
               "(11 a 20/11/2026), coloque a exportação da coleta na raiz do projeto ou envie-a na barra lateral.")
if filtro_ativo:
    st.info(f"Filtro ativo: {len(filtrada)} de {len(validas)} respostas válidas.")

abas = st.tabs(["Perfil da amostra", "Itens Likert", "Questões de pesquisa", "Confiabilidade",
                "Segmentos e exploratórias", "Metodologia e desvios"])


def grafico_barras(serie: pd.Series, titulo: str, ordem: list | None = None, pct_base: int | None = None):
    cont = serie.value_counts()
    if ordem is not None:
        cont = cont.reindex(ordem, fill_value=0)
    base = pct_base or int(cont.sum()) or 1
    df = pd.DataFrame({"categoria": cont.index.astype(str), "n": cont.values})
    df["%"] = (df["n"] / base * 100).round(1)
    fig = px.bar(df, x="n", y="categoria", orientation="h", text=df.apply(lambda r: f"{r.n} ({r['%']:.0f}%)", axis=1),
                 title=titulo)
    fig.update_layout(yaxis={"categoryorder": "array", "categoryarray": df["categoria"].tolist()[::-1], "title": None},
                      xaxis_title="respostas", height=90 + 32 * len(df), margin={"l": 10, "r": 10, "t": 40, "b": 10})
    fig.update_traces(textposition="outside", cliponaxis=False)
    return fig


def tabela_multipla(v: pd.DataFrame, prefixo: str, categorias: list[str]) -> pd.DataFrame:
    linhas = [{"Opção": c, "n": int(v[f"{prefixo}::{c}"].sum())} for c in categorias]
    df = pd.DataFrame(linhas)
    df["% dos respondentes"] = (df["n"] / max(len(v), 1) * 100).round(1)
    return df


# --------------------------------------------------------------------------
# 1. Perfil da amostra
# --------------------------------------------------------------------------
with abas[0]:
    st.header("Funil de respostas")
    st.caption("Calculado sobre todas as respostas recebidas, sem filtro. Regras de encerramento e descarte da Seção 3.")
    n_rec = len(todas)
    n_inel = int((todas["status"] == "Inelegível").sum())
    n_desc = int((todas["status"] == "Descartada").sum())
    n_val = int((todas["status"] == "Válida").sum())
    c = st.columns(5)
    c[0].metric("Recebidas", n_rec)
    c[1].metric("Inelegíveis (formulário encerrado)", n_inel)
    c[2].metric("Descartadas", n_desc)
    c[3].metric("Válidas", n_val, delta=f"{n_val - a.N_META} em relação à meta de {a.N_META}", delta_color="normal")
    c[4].metric("Linha reta (só sinalizadas)", int(validas["linha_reta"].sum()))

    esq, dir_ = st.columns([1, 1])
    with esq:
        fig = go.Figure(go.Funnel(y=["Recebidas", "Elegíveis", "Válidas"], x=[n_rec, n_rec - n_inel, n_val],
                                  textinfo="value+percent initial"))
        fig.update_layout(height=280, margin={"l": 10, "r": 10, "t": 10, "b": 10})
        st.plotly_chart(fig, width="stretch")
    with dir_:
        excl = todas[todas["status"] != "Válida"]
        if excl.empty:
            st.success("Nenhuma resposta inelegível ou descartada.")
        else:
            motivos = (excl.assign(m=excl["motivo"].str.split("; ")).explode("m")
                       .assign(m=lambda d: d["m"].str.replace(r" \(marcou .*\)$", "", regex=True)
                               .str.replace(r"em branco: .*$", "em branco", regex=True))
                       .groupby(["status", "m"]).size().reset_index(name="n")
                       .rename(columns={"status": "Situação", "m": "Motivo"}))
            st.subheader("Motivos")
            st.dataframe(motivos, hide_index=True, width="stretch")
    if not excl.empty:
        with st.expander(f"Motivo de cada resposta excluída ({len(excl)})", expanded=True):
            st.dataframe(excl[["id", "carimbo", "status", "motivo"]].rename(
                columns={"id": "Nº da linha", "carimbo": "Data e hora", "status": "Situação", "motivo": "Motivo"}),
                hide_index=True, width="stretch")
    n_fora = int(todas["fora_janela"].sum())
    if n_fora:
        st.warning(f"{n_fora} resposta(s) com data e hora fora da janela de coleta (11 a 20/11/2026). "
                   "Foram sinalizadas, não descartadas (ver Metodologia e desvios).")

    st.header("Perfil das respostas válidas" + (" (filtro ativo)" if filtro_ativo else ""))
    if segmento_ok():
        v = filtrada
        g1, g2 = st.columns(2)
        g1.plotly_chart(grafico_barras(v["T2"], "Vínculo (T2)", [o for o in a.OPCOES_T2]), width="stretch")
        g2.plotly_chart(grafico_barras(v["P2"], "Porte da organização (P2)", a.OPCOES_P2), width="stretch")
        g1.plotly_chart(grafico_barras(v["faixa_P1"], "Tempo de experiência (faixas de P1, anos)", a.ORDEM_FAIXAS),
                        width="stretch")
        g2.plotly_chart(grafico_barras(v["P3"], "Tempo de uso de IA (P3)", a.OPCOES_P3), width="stretch")
        g1.plotly_chart(grafico_barras(v["U1_rotulo"], "Frequência de uso nos últimos 3 meses (U1)",
                                       list(a.U1_ROTULOS.values())[1:]), width="stretch")
        g2.plotly_chart(grafico_barras(v["U2"].astype("Int64").astype(str),
                                       "Dias de uso nos últimos 5 dias úteis (U2)", [str(i) for i in range(6)]),
                        width="stretch")
        g1.subheader("Ferramentas (P4)")
        g1.dataframe(tabela_multipla(v, "P4", dados.categorias_p4), hide_index=True, width="stretch")
        g2.subheader("Tarefas (P5)")
        g2.dataframe(tabela_multipla(v, "P5", dados.categorias_p5), hide_index=True, width="stretch")
        st.caption("P4 e P5 são de múltipla escolha: o percentual é sobre respondentes e não soma 100%.")

        st.subheader("Resumo por escala (Seção 5)")
        linhas = []
        for item, nome in [("P1", "P1 anos de experiência"), ("U2", "U2 dias de uso")]:
            linhas.append({"Item": nome, "Escala": "Razão", **a.resumo_razao(v[item])})
        for item, nome in [("U1", "U1 frequência"), ("P2_ord", "P2 porte (1 = até 10 … 5 = mais de 1000)"),
                           ("PP_med", "PP_med")]:
            linhas.append({"Item": nome, "Escala": "Ordinal (sem média)", **a.resumo_ordinal(v[item])})
        st.dataframe(pd.DataFrame(linhas), hide_index=True, width="stretch",
                     column_config={k: st.column_config.NumberColumn(format="%.2f")
                                    for k in ["Mediana", "Q1", "Q3", "Média", "DP", "Mín", "Máx"]})
        st.caption("Em P2, 'Não se aplica (trabalho autônomo)' é tratado como ausente no porte ordinal.")

# --------------------------------------------------------------------------
# 2. Itens Likert
# --------------------------------------------------------------------------
with abas[1]:
    st.header("Produtividade percebida: itens Likert")
    if segmento_ok():
        v = filtrada
        recodificar = st.toggle("Mostrar PP5 recodificado (6 − x), no mesmo sentido dos outros itens", value=False)
        itens = ["PP1", "PP2", "PP3", "PP4", "PP5"]
        linhas = []
        for item in itens:
            col = v["PP5r"] if (item == "PP5" and recodificar) else v[item]
            dist = col.value_counts(normalize=True).reindex(range(1, 6), fill_value=0) * 100
            rot = a.PP_TEXTO[item] + (" [recodificado]" if item == "PP5" and recodificar else "")
            linhas.append((rot, dist, int(col.notna().sum())))
        fig = go.Figure()
        ordem_y = [r for r, _, _ in linhas][::-1]
        # Neutro dividido ao meio dos dois lados do zero
        for nivel, lado, mostra in [(3, -1, True), (2, -1, True), (1, -1, True), (3, 1, False), (4, 1, True), (5, 1, True)]:
            valores = [d[nivel] / (2 if nivel == 3 else 1) * lado for _, d, _ in linhas]
            texto = [f"{d[nivel]:.0f}%" if (nivel != 3 or lado == 1) and d[nivel] >= 4 else "" for _, d, _ in linhas]
            fig.add_bar(y=[r for r, _, _ in linhas], x=valores, orientation="h", name=f"{nivel} - {a.LIKERT[nivel]}",
                        marker_color=CORES_LIKERT[nivel], showlegend=mostra, legendrank=nivel, text=texto,
                        textposition="inside", insidetextanchor="middle",
                        customdata=[d[nivel] for _, d, _ in linhas],
                        hovertemplate="%{y}<br>" + a.LIKERT[nivel] + ": %{customdata:.1f}%<extra></extra>")
        fig.update_layout(barmode="relative", height=420, legend={"orientation": "h", "y": -0.15, "traceorder": "normal"},
                          xaxis={"title": "% das respostas (discordância à esquerda, concordância à direita)",
                                 "range": [-100, 100], "tickvals": [-100, -50, 0, 50, 100],
                                 "ticktext": ["100%", "50%", "0", "50%", "100%"]},
                          yaxis={"categoryorder": "array", "categoryarray": ordem_y},
                          margin={"l": 10, "r": 10, "t": 20, "b": 10})
        fig.add_vline(x=0, line_color="black", line_width=1)
        st.plotly_chart(fig, width="stretch")
        st.caption(f"n = {len(v)}. O neutro (3) aparece dividido ao meio dos dois lados do zero. "
                   "PP5 é invertido: no original, concordar significa trabalho mais cansativo, ou seja, menor produtividade percebida.")

        resumo = []
        for item in ["PP1", "PP2", "PP3", "PP4", "PP5", "PP5r", "PP_med"]:
            s = v[item]
            resumo.append({"Item": item, **a.resumo_ordinal(s),
                           "% concorda (4–5)": round((s >= 4).mean() * 100, 1),
                           "% neutro (3)": round((s == 3).mean() * 100, 1),
                           "% discorda (1–2)": round((s <= 2).mean() * 100, 1)})
        st.dataframe(pd.DataFrame(resumo), hide_index=True, width="stretch")
        st.plotly_chart(grafico_barras(v["PP_med"].map(lambda x: f"{x} - {a.LIKERT[x]}"),
                                       "Distribuição de PP_med (mediana dos 5 itens, PP5 recodificado)",
                                       [f"{i} - {a.LIKERT[i]}" for i in range(1, 6)]), width="stretch")

# --------------------------------------------------------------------------
# 3. Questões de pesquisa
# --------------------------------------------------------------------------
HIPOTESES = {
    "RQ1": ("H0: P(PP_med > 3) = P(PP_med < 3).", "H1: as probabilidades são diferentes."),
    "RQ2": ("H0: ρ de Spearman entre U1 e PP_med = 0.", "H1: ρ ≠ 0."),
    "RQ3": ("H0: ρ de Spearman entre P1 e PP_med = 0.", "H1: ρ ≠ 0."),
}


def interpretacao(r: a.Resultado) -> str:
    if pd.isna(r.p):
        return "Teste não calculável com estes dados."
    if r.rq == "RQ1":
        if r.rejeita:
            sentido = "acima" if r.efeito > 0.5 else "abaixo"
            return (f"Rejeitamos H0 após a correção de Holm. Entre quem não ficou no neutro, {a.pct(r.efeito)} "
                    f"ficou acima do neutro: a produtividade **percebida** tende a ficar {sentido} do ponto neutro nesta amostra.")
        return "Não rejeitamos H0 após a correção de Holm: os dados não mostram diferença em relação ao neutro (o que não prova igualdade)."
    alvo = "a frequência de uso" if r.rq == "RQ2" else "o tempo de experiência"
    if r.rejeita:
        sentido = "positiva" if r.efeito > 0 else "negativa"
        return (f"Rejeitamos H0 após a correção de Holm. Há associação {sentido} de tamanho {r.leitura_efeito} "
                f"entre {alvo} e a produtividade **percebida**. É associação, não efeito causal.")
    return (f"Não rejeitamos H0 após a correção de Holm. O ρ observado tem tamanho {r.leitura_efeito}; "
            f"com n = {r.n}, só |ρ| a partir de cerca de 0,39 seria detectado com 80% de poder.")


def tabela_resultados(res: list[a.Resultado]) -> pd.DataFrame:
    return pd.DataFrame([{
        "RQ": r.rq, "Teste": r.teste, "n": r.n,
        "Estatística": f"{r.estatistica_nome} = {a.fmt(r.estatistica, 3 if 'ρ' in r.estatistica_nome else 0)}",
        "p bruto": a.fmt_p(r.p), "p (Holm)": a.fmt_p(r.p_holm),
        "Decisão (α = 0,05)": "–" if pd.isna(r.p) else ("Rejeita H0" if r.rejeita else "Não rejeita H0"),
        "Tamanho de efeito": f"{r.efeito_nome} = {a.fmt(r.efeito)}" + (f" ({r.leitura_efeito})" if r.leitura_efeito else ""),
        "IC 95%": f"[{a.fmt(r.ic[0])}; {a.fmt(r.ic[1])}] ({r.ic_metodo})",
        "Margem de erro": r.margem_texto,
    } for r in res])


with abas[2]:
    st.header("Resposta às questões de pesquisa")
    st.caption("Testes bicaudais, α = 0,05, família de 3 testes com correção de Holm (Seção 5). "
               "Calculados sobre a amostra completa de respostas válidas, sem filtro.")
    if len(validas) == 0:
        st.info("Nenhuma resposta válida.")
    else:
        res = confirmatorios(validas)
        st.dataframe(tabela_resultados(res), hide_index=True, width="stretch")
        for r in res:
            with st.container(border=True):
                st.subheader(f"{r.rq}. {r.pergunta}")
                h0, h1 = HIPOTESES[r.rq]
                st.markdown(f"{h0} {h1}  \n**Teste:** {r.teste}.")
                m = st.columns(5)
                m[0].metric("n" + (" efetivo" if r.rq == "RQ1" else ""), r.n)
                m[1].metric("p bruto", a.fmt_p(r.p))
                m[2].metric("p ajustado (Holm)", a.fmt_p(r.p_holm))
                m[3].metric("Efeito", a.fmt(r.efeito), help=r.efeito_nome)
                m[4].metric("IC 95% do efeito", f"[{a.fmt(r.ic[0], 2)}; {a.fmt(r.ic[1], 2)}]", help=r.ic_metodo)
                st.markdown(f"**Margem de erro:** {r.margem_texto}.  \n**Leitura:** {interpretacao(r)}")
                for nota in r.notas:
                    st.caption(nota)
                if r.rq == "RQ1":
                    fig = grafico_barras(validas["classe_PP"], "PP_med em relação ao neutro", a.CLASSES_PP)
                else:
                    x = "U1" if r.rq == "RQ2" else "P1"
                    tab = validas.groupby([x, "PP_med"]).size().reset_index(name="n")
                    fig = px.scatter(tab, x=x, y="PP_med", size="n", text="n",
                                     title=f"{x} × PP_med (tamanho do ponto = número de respostas)")
                    fig.update_traces(textposition="middle center", marker={"sizemin": 10, "opacity": 0.6})
                    fig.update_layout(yaxis={"range": [0.5, 5.5], "dtick": 1}, height=350)
                    if x == "U1":
                        fig.update_layout(xaxis={"range": [1.5, 5.5], "tickvals": [2, 3, 4, 5],
                                                 "ticktext": [a.U1_ROTULOS[i] for i in range(2, 6)]})
                st.plotly_chart(fig, width="stretch")

        if filtro_ativo:
            st.header("Os mesmos testes no segmento filtrado (exploratório)")
            st.caption("Fora da família confirmatória. Não serve para concluir; mostra só como os números mudam no segmento.")
            if segmento_ok():
                st.dataframe(tabela_resultados(confirmatorios(filtrada)), hide_index=True, width="stretch")

# --------------------------------------------------------------------------
# 4. Confiabilidade
# --------------------------------------------------------------------------
with abas[3]:
    st.header("Confiabilidade do construto Produtividade percebida")
    st.caption("Único construto com mais de um item: PP1 a PP5, com PP5 recodificado (6 − x). "
               "Os itens são ordinais, então o alfa é uma aproximação.")
    if segmento_ok():
        c = alfa_cache(filtrada)
        m = st.columns(4)
        m[0].metric("Alfa de Cronbach", a.fmt(c["alfa"]))
        m[1].metric("IC 95% (bootstrap)", f"[{a.fmt(c['ic'][0], 2)}; {a.fmt(c['ic'][1], 2)}]")
        m[2].metric("k (itens)", c["k"])
        m[3].metric("n", c["n"])
        if c["motivo"]:
            st.warning(f"Alfa não calculável: {c['motivo']}.")
        elif np.isfinite(c["alfa"]):
            nivel = ("abaixo de 0,6, fraca" if c["alfa"] < 0.6 else "entre 0,6 e 0,7, questionável" if c["alfa"] < 0.7
                     else "entre 0,7 e 0,9, aceitável a boa" if c["alfa"] < 0.9 else "acima de 0,9, alta (possível redundância)")
            st.markdown(f"Consistência interna {nivel}, pela referência usual (Nunnally).")
        if not c["itens"].empty:
            st.dataframe(c["itens"], hide_index=True, width="stretch",
                         column_config={k: st.column_config.NumberColumn(format="%.3f")
                                        for k in ["Correlação item-total corrigida", "Alfa se o item for removido"]})
        corr = filtrada[["PP1", "PP2", "PP3", "PP4", "PP5r"]].corr(method="spearman")
        fig = px.imshow(corr, text_auto=".2f", zmin=-1, zmax=1, color_continuous_scale="RdBu",
                        title="Correlação de Spearman entre os itens (PP5 recodificado)")
        fig.update_layout(height=420)
        st.plotly_chart(fig, width="stretch")
        st.caption("U1 e U2 não formam construto (Seção 3), por isso não têm alfa.")
        # Protocolo v5, Seção 3
        st.subheader("Checagens previstas no protocolo (Seção 3)")
        if len(filtrada) >= 3:
            mi = a.media_itens_vs_ppmed(filtrada)
            st.markdown(f"**Exploratório:** média dos cinco itens (PP5 recodificado) = {a.fmt(mi['media'], 2)} "
                        f"(DP {a.fmt(mi['dp'], 2)}); Spearman com PP_med: ρ = {a.fmt(mi['rho'])}, p = {a.fmt_p(mi['p'])}, n = {mi['n']}. "
                        "O alfa é indício indireto: PP_med é a mediana, não o escore somado.")
            if np.isfinite(c["alfa"]) and c["alfa"] < 0.70:
                st.warning(f"α = {a.fmt(c['alfa'])} está abaixo de 0,70, a decisão prévia do protocolo. A limitação é declarada e "
                           "as subescalas de rapidez e qualidade são analisadas à parte, como sensibilidade. "
                           "PP5 **não** foi excluído: permanece em PP_med em todas as análises confirmatórias (retirá-lo seria um desvio).")
                st.dataframe(a.sensibilidade_subescalas(filtrada), hide_index=True, width="stretch",
                             column_config={"p bruto": st.column_config.NumberColumn(format="%.4f")})
                st.caption("Escore da subescala = média dos dois itens. Exploratório, sem correção para múltiplas comparações.")
            if not c["itens"].empty:
                r5 = c["itens"].set_index("Item").loc["PP5r"]
                st.caption(f"Só descritivo: correlação item-total corrigida de PP5 = {a.fmt(r5['Correlação item-total corrigida'])}; "
                           f"alfa sem PP5 = {a.fmt(r5['Alfa se o item for removido'])}.")

# --------------------------------------------------------------------------
# 5. Segmentos e exploratórias
# --------------------------------------------------------------------------
SEGMENTOS = {
    "Tempo de experiência (faixas de P1)": "faixa_agrupada",
    "Vínculo (T2)": "T2",
    "Porte da organização (P2)": "P2",
    "Tempo de uso de IA (P3)": "P3",
    "Frequência de uso (U1)": "U1_rotulo",
}

with abas[4]:
    st.header("Análises exploratórias")
    st.caption("Fora da família confirmatória, sem correção para múltiplas comparações e nunca usadas para concluir (Seção 5). "
               "Grupos com menos de 5 pessoas não entram nas comparações.")
    if segmento_ok():
        v = filtrada.copy()
        mapa_faixas = a.agrupar_faixas(v["faixa_P1"].value_counts())
        v["faixa_agrupada"] = v["faixa_P1"].astype(str).map(mapa_faixas)
        ordem_agr = list(dict.fromkeys(mapa_faixas[f] for f in a.ORDEM_FAIXAS))
        v["faixa_agrupada"] = pd.Categorical(v["faixa_agrupada"], categories=ordem_agr, ordered=True)

        st.subheader("Comparação de PP_med entre segmentos")
        rotulo = st.selectbox("Segmento", list(SEGMENTOS))
        col = SEGMENTOS[rotulo]
        cmp_ = a.comparar_grupos(v, col)
        tam = cmp_["tamanhos"]
        resumo = (v.groupby(col, observed=True)["PP_med"]
                  .agg(n="size", Mediana="median", Q1=lambda s: s.quantile(0.25), Q3=lambda s: s.quantile(0.75))
                  .reset_index().rename(columns={col: "Grupo"}))
        resumo = resumo[resumo["n"] >= a.MIN_SEGMENTO]
        if cmp_["excluidos"]:
            st.caption(f"{len(cmp_['excluidos'])} grupo(s) com menos de {a.MIN_SEGMENTO} pessoas omitido(s).")
        if col == "faixa_agrupada" and any(k != val for k, val in mapa_faixas.items()):
            st.caption("Faixas com menos de 5 pessoas foram agrupadas com a vizinha: "
                       + "; ".join(sorted({f"{k} → {val}" for k, val in mapa_faixas.items() if k != val})))
        if not resumo.empty:
            st.dataframe(resumo, hide_index=True, width="stretch")
            dist = (v[v[col].isin(resumo["Grupo"])].groupby([col, "PP_med"], observed=True).size()
                    .reset_index(name="n"))
            dist["%"] = dist["n"] / dist.groupby(col, observed=True)["n"].transform("sum") * 100
            dist["PP_med"] = dist["PP_med"].map(lambda x: f"{x} - {a.LIKERT[x]}")
            fig = px.bar(dist, y=dist[col].astype(str), x="%", color="PP_med", orientation="h",
                         category_orders={"PP_med": [f"{i} - {a.LIKERT[i]}" for i in range(1, 6)]},
                         color_discrete_map={f"{i} - {a.LIKERT[i]}": CORES_LIKERT[i] for i in range(1, 6)},
                         title=f"Distribuição de PP_med por {rotulo}")
            fig.update_layout(yaxis_title=None, height=150 + 40 * len(resumo), barmode="stack")
            st.plotly_chart(fig, width="stretch")
        if cmp_["teste"]:
            st.markdown(f"**{cmp_['teste']}:** estatística = {a.fmt(cmp_['estatistica'], 2)}, p = {a.fmt_p(cmp_['p'])}, "
                        f"{cmp_['efeito_nome']} = {a.fmt(cmp_['efeito'])} "
                        f"(IC 95% bootstrap [{a.fmt(cmp_['ic'][0], 2)}; {a.fmt(cmp_['ic'][1], 2)}]), n = {cmp_['n']}.")
        else:
            st.info(f"Teste não aplicado: {cmp_['motivo']}.")
        if col in ("T2",):
            q = a.qui_quadrado(v, col)
            if q.get("motivo"):
                st.caption(f"χ² não aplicado: {q['motivo']}.")
            else:
                st.markdown(f"**{q['metodo']} (segmento × classe de PP_med):** p = {a.fmt_p(q['p'])}, "
                            f"V de Cramér = {a.fmt(q['v'])} (IC 95% bootstrap [{a.fmt(q['ic'][0], 2)}; {a.fmt(q['ic'][1], 2)}]).")
                if q["esperado_baixo"]:
                    st.caption("Há frequências esperadas abaixo de 5, então, como no protocolo, vale o teste exato "
                               "(Fisher; Freeman-Halton por Monte Carlo em tabelas maiores que 2×2) no lugar do χ².")

        st.divider()
        e1, e2 = st.columns(2)
        with e1:
            st.subheader("Kruskal-Wallis entre faixas de experiência")
            kw = a.comparar_grupos(v, "faixa_agrupada")
            if kw["teste"]:
                st.markdown(f"{kw['teste']} = {a.fmt(kw['estatistica'], 2)}, p = {a.fmt_p(kw['p'])}, "
                            f"{kw['efeito_nome']} = {a.fmt(kw['efeito'])} "
                            f"(IC 95% bootstrap [{a.fmt(kw['ic'][0], 2)}; {a.fmt(kw['ic'][1], 2)}]), n = {kw['n']}.")
            else:
                st.info(f"Não aplicado: {kw['motivo']}.")
        with e2:
            st.subheader("Robustez da RQ2: U2 (dias de uso) × PP_med")
            s = a.spearman_completo(v["U2"], v["PP_med"])
            if s["motivo"]:
                st.info(f"Não calculável: {s['motivo']}.")
            else:
                st.markdown(f"ρ = {a.fmt(s['rho'])} ({a.leitura_cohen(s['rho'])}), p (t) = {a.fmt_p(s['p_t'])}, "
                            f"p (permutação) = {a.fmt_p(s['p_perm'])}, IC 95% [{a.fmt(s['ic'][0], 2)}; {a.fmt(s['ic'][1], 2)}], n = {s['n']}.")

        st.subheader("Sensibilidade: sem respostas em linha reta")
        sem_lr = v[~v["linha_reta"]]
        st.caption(f"{int(v['linha_reta'].sum())} resposta(s) com os cinco itens PP iguais removida(s) nesta análise.")
        if v["linha_reta"].any() and len(sem_lr) >= a.MIN_SEGMENTO:
            comp = pd.concat([tabela_resultados(confirmatorios(v)).assign(Conjunto="Com linha reta"),
                              tabela_resultados(confirmatorios(sem_lr)).assign(Conjunto="Sem linha reta")])
            st.dataframe(comp[["Conjunto", "RQ", "n", "Estatística", "p bruto", "p (Holm)", "Tamanho de efeito", "IC 95%"]],
                         hide_index=True, width="stretch")
        elif not v["linha_reta"].any():
            st.info("Nenhuma resposta em linha reta: a sensibilidade coincide com a análise principal.")

# --------------------------------------------------------------------------
# 6. Metodologia e desvios
# --------------------------------------------------------------------------
with abas[5]:
    st.header("Metodologia")
    st.markdown("""
- **Desenho:** survey transversal, amostra não probabilística (conveniência com bola de neve), desenvolvedores no Brasil que usaram assistente de IA nos últimos 3 meses. Coleta via Google Formulários, prevista para 11 a 20/11/2026 e realizada de 13 a 19/11/2026 (desvio D3).
- **Encerramento (inelegíveis):** C0 = não, T1 = não ou U1 = 1. **Descarte:** AT1 diferente de "Discordo" ou item obrigatório em branco. Linha reta (cinco itens PP iguais) só é sinalizada e testada em sensibilidade.
- **Variável de resposta:** PP_med, mediana de PP1 a PP5 com PP5 recodificado (6 − x). Ordinal: sem média, teste t ou Pearson.
- **RQ1:** teste do sinal exato contra o neutro 3, sem empates; efeito = proporção de PP_med ≥ 4 entre os não empatados com IC de Clopper-Pearson; margem de erro pela fórmula do enunciado sobre a proporção de PP_med ≥ 4 entre todos os usuários válidos.
- **RQ2 e RQ3:** Spearman (U1 × PP_med e P1 × PP_med) com postos médios; p pela aproximação t, e o p por permutação (10.000) prevalece se os dois divergirem na decisão; IC de ρ por bootstrap percentil (10.000). Leitura de ρ por Cohen (0,1 / 0,3 / 0,5).
- **Família confirmatória:** 3 testes bicaudais, α = 0,05, correção de Holm.
- **Margem de erro:** e = 1,96 × √(p(1 − p)/n), referência de precisão (a amostra não é probabilística).
- **Protocolo de referência:** `Protocolo_do_Survey_v5.pdf`, enviado no Canvas (versão final entregue).
- **Ética:** sem dados identificáveis; texto livre não é carregado; segmentos com menos de 5 pessoas não são exibidos.
""")
    st.header("Checagens automáticas sobre os dados carregados")
    res_full = confirmatorios(validas) if len(validas) else []
    empates = int((validas["PP_med"] == 3).sum())
    mapa_tot = a.agrupar_faixas(validas["faixa_P1"].value_counts()) if len(validas) else {}
    agrupadas = sorted({f"{k} → {val}" for k, val in mapa_tot.items() if k != val})
    outras = int(validas.get(f"P4::{a.OUTRA}", pd.Series(dtype=bool)).sum()
                 + validas.get(f"P5::{a.OUTRA}", pd.Series(dtype=bool)).sum())
    checks = [
        ("Fonte dos dados", "Exportação da coleta", "Pré-teste (não entra na análise)" if eh_preteste else "Coleta",
         "Desvio" if eh_preteste else "OK"),
        ("Respostas válidas", f"≥ {a.N_META}", str(len(validas)), "OK" if len(validas) >= a.N_META else "Abaixo da meta"),
        ("Empates em PP_med = 3 (RQ1)", "cerca de 20%",
         f"{empates} ({a.pct(empates / len(validas)) if len(validas) else '–'})", "Informativo"),
        ("Faixas de P1 agrupadas (< 5 pessoas)", "agrupar com a vizinha", "; ".join(agrupadas) or "nenhuma", "Conforme o protocolo"),
        ("Respostas fora de 11 a 20/11/2026", "0", str(int(todas["fora_janela"].sum())),
         "OK" if not todas["fora_janela"].any() else "Sinalizadas"),
        ("Marcações 'Outra' sem codificação (P4 + P5)", "0 após a codificação", str(outras),
         "OK" if outras == 0 else "Pendente (D2)"),
        ("Colunas esperadas ausentes no CSV", "nenhuma", ", ".join(dados.colunas_ausentes) or "nenhuma",
         "OK" if not dados.colunas_ausentes else "Verificar"),
    ]
    st.dataframe(pd.DataFrame(checks, columns=["Checagem", "Previsto no protocolo", "Observado", "Situação"]),
                 hide_index=True, width="stretch")
    if len(validas) < a.N_META:
        st.caption(f"Com n = {len(validas)}, a margem de erro geral (p = 0,5) é ± "
                   f"{a.pp(a.margem_erro(0.5, len(validas)))}, contra ± 13,9 p.p. previstos para n = 50.")

    desvios = PASTA / "desvios.md"
    if desvios.is_file():
        st.markdown(desvios.read_text(encoding="utf-8"))
