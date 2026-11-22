"""Conferência independente de RQ1, RQ2 e RQ3: só openpyxl e a biblioteca padrão (sem pandas, scipy nem analise.py).

Executar na raiz do projeto: python3 dashboard/conferencia_rqs.py
Resultado esperado (coleta oficial, n = 69), a ser comparado com o dashboard:
  RQ1: 55 acima / 1 abaixo / 13 empates, p ~ 1,6e-15
  RQ2: rho(U1, PP_med) = 0,3674, p ~ 0,0019 (aproximação t)
  RQ3: rho(P1, PP_med) = 0,0578, p ~ 0,637 (aproximação t)
O p da aproximação t pode diferir na 3ª casa do p por permutação do dashboard; a decisão é a mesma."""
import openpyxl, statistics as st, re, glob, math

f = glob.glob("Respostas*COLETA*.xlsx")[0]
wb = openpyxl.load_workbook(f)
ws = [w for w in wb.worksheets if (w.max_row or 0) > 1][0]
rows = list(ws.iter_rows(values_only=True)); h = [str(x) for x in rows[0]]
col = lambda p: next(i for i, x in enumerate(h) if re.search(p, x))
c = {k: col(p) for k, p in dict(C0=r"^C0", T1=r"^T1", T2=r"^T2", U1=r"^U1", P1=r"^P1\.",
     PP1=r"\[PP1\.", PP2=r"\[PP2\.", PP3=r"\[PP3\.", PP4=r"\[PP4\.", PP5=r"\[PP5\.", AT1=r"\[AT1\.").items()}
dig = lambda x: int(str(x).strip()[0]) if x not in (None, "") and str(x).strip()[0].isdigit() else None

V = []  # (U1, P1, PP_med)
for r in rows[1:]:
    if not str(r[c["C0"]]).startswith("Sim") or str(r[c["T1"]]).strip() != "Sim": continue
    if str(r[c["T2"]]).strip().casefold().startswith("outro"): continue
    if dig(r[c["U1"]]) == 1 or dig(r[c["AT1"]]) != 2: continue
    raw = r[c["P1"]]
    if isinstance(raw, (int, float)) and float(raw).is_integer(): p1 = str(int(raw))
    else: p1 = str(raw).strip()
    if not p1.isdigit(): continue
    pp = [dig(r[c[k]]) for k in ["PP1", "PP2", "PP3", "PP4", "PP5"]]
    pp[4] = 6 - pp[4]
    V.append((dig(r[c["U1"]]), int(p1), st.median(pp)))
n = len(V); print("n válidas:", n)

# RQ1: sinal exato bicaudal
pm = [x[2] for x in V]
k = sum(1 for x in pm if x >= 4); b = sum(1 for x in pm if x <= 2); e = n - k - b; m = k + b
p1 = min(1.0, 2 * sum(math.comb(m, i) for i in range(0, min(k, m - k) + 1)) / 2 ** m)
print(f"RQ1: acima={k} abaixo={b} empates={e} n_eff={m} p={p1:.3g} prop>=4 (todos)={k/n:.4f}")

def ranks(x):
    o = sorted(range(len(x)), key=lambda i: x[i]); r = [0.0] * len(x); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and x[o[j + 1]] == x[o[i]]: j += 1
        for t in range(i, j + 1): r[o[t]] = (i + j) / 2 + 1
        i = j + 1
    return r

def pearson(a, b):
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(
        sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))

def p_t(t, df, passos=200000):  # p bicaudal por integração numérica da densidade t
    cst = math.gamma((df + 1) / 2) / (math.sqrt(df * math.pi) * math.gamma(df / 2))
    a, h_ = abs(t), 0.0
    L = 60.0; dx = (L - a) / passos
    s = sum(cst * (1 + (a + (i + .5) * dx) ** 2 / df) ** (-(df + 1) / 2) for i in range(passos)) * dx
    return 2 * s

def spearman(x, y):
    rho = pearson(ranks(x), ranks(y)); t = rho * math.sqrt((len(x) - 2) / (1 - rho ** 2))
    return rho, p_t(t, len(x) - 2)

for nome, idx in (("RQ2 U1", 0), ("RQ3 P1", 1)):
    rho, p = spearman([x[idx] for x in V], pm)
    print(f"{nome} x PP_med: rho={rho:.4f} p(t)={p:.4g}")
