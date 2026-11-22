"""Conferência independente do alfa de Cronbach: só openpyxl e statistics, sem pandas nem analise.py.

Executar na raiz do projeto: python3 dashboard/conferencia_alfa.py
Resultado esperado (coleta oficial, n = 69): 0,3936 sem recodificar PP5; 0,6746 com PP5 recodificado; 0,6966 sem PP5.
O valor correto é 0,6746. O 0,39 aparece quando PP5 (item invertido) não é recodificado."""
import openpyxl, statistics as st, re, glob
f=glob.glob("Respostas*COLETA*.xlsx")[0]
wb=openpyxl.load_workbook(f,read_only=False); ws=[w for w in wb.worksheets if (w.max_row or 0)>1][0]
rows=list(ws.iter_rows(values_only=True)); h=[str(x) for x in rows[0]]
def col(p): return next(i for i,x in enumerate(h) if re.search(p,x))
c={k:col(p) for k,p in dict(C0=r"^C0",T1=r"^T1",U1=r"^U1",PP1=r"\[PP1\.",PP2=r"\[PP2\.",PP3=r"\[PP3\.",PP4=r"\[PP4\.",PP5=r"\[PP5\.",AT1=r"\[AT1\.").items()}
dig=lambda x: int(str(x).strip()[0]) if x not in (None,"") and str(x).strip()[0].isdigit() else None
M=[]; prev=None
for r in rows[1:]:
    if str(r[c["T1"]]).strip()!="Sim": continue
    if dig(r[c["U1"]])==1: continue
    if dig(r[c["AT1"]])!=2: continue
    M.append([dig(r[c[k]]) for k in ["PP1","PP2","PP3","PP4","PP5"]])
print("n válidas (T1 sim, AT1=2):",len(M))
def alpha(M):
    k=len(M[0]); vi=sum(st.variance([r[j] for r in M]) for j in range(k)); vt=st.variance([sum(r) for r in M]); return k/(k-1)*(1-vi/vt)
print("PP5 sem recodificar:",round(alpha(M),4))
R=[r[:4]+[6-r[4]] for r in M]; print("PP5 recodificado (6-x):",round(alpha(R),4))
print("sem PP5:",round(alpha([r[:4] for r in R]),4))
