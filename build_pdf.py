import os, subprocess, sys

src, out = sys.argv[1], sys.argv[2]

# O PDF oficial do protocolo é o entregue no Canvas: protocolo/Protocolo_do_Survey_v5.pdf.
# Este script gera um PDF com outro layout, então não pode sobrescrevê-lo nem substituí-lo.
if "protocolo" in os.path.normpath(out).split(os.sep) or os.path.basename(out).startswith("Protocolo_do_Survey"):
    sys.exit("Recusado: o PDF oficial do protocolo (v5, entregue) não deve ser regenerado por este script.")

import markdown
from pypdf import PdfReader
body = markdown.markdown(open(src, encoding="utf-8").read(), extensions=["tables"])
css = """
@page { size: A4; margin: 1.6cm 1.7cm; }
body { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 9.5pt; line-height: 1.32; color: #111; }
h1 { font-size: 14pt; margin: 0 0 4pt; }
h2 { font-size: 11.5pt; margin: 10pt 0 3pt; border-bottom: 1px solid #999; }
p, ul { margin: 3pt 0; } li { margin: 1pt 0; }
hr { display: none; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0; font-size: 8.5pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #bbb; padding: 2pt 4pt; vertical-align: top; text-align: left; }
th { background: #eee; }
code { font-size: 8.5pt; }
"""
html = f"<!doctype html><html lang='pt-BR'><meta charset='utf-8'><style>{css}</style><body>{body}</body></html>"
tmp = "/tmp/protocolo.html"
open(tmp, "w", encoding="utf-8").write(html)
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={out}", f"file://{tmp}"], check=True, capture_output=True)
print("pages:", len(PdfReader(out).pages))
