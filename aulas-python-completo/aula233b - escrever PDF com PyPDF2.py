# escrever PDF com PyPDF2
'''
PyPDF2 para manipular arquivos PDF (Instalação)
PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
extrair texto e imagens, manipular metadados, e mais.
A documentação contém todas as informações necessárias para usar PyPDF2.
Link: https://pypdf2.readthedocs.io/en/3.0.0/
Ative seu ambiente virtual
pip install pypdf2

PDFs que serão utilizados como exemplo: banco central relatório focus
'''

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

ROOT = Path(__file__).parent
PASTA_PDFS_ORIGINAIS = ROOT / 'aula233' / 'pdfs_originais'
PASTA_NOVOS_ARQUIVOS = ROOT / 'aula233' / 'novos_arquivos'
BACEN_2023 = PASTA_PDFS_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVOS_ARQUIVOS.mkdir(exist_ok=True)

# Ler o arquivo PDF
reader = PdfReader(BACEN_2023)

# Guardar as páginas do PDF em um iterável
paginas = reader.pages

# Salvar apenas a página 1 em um novo arquivo PDF
writer = PdfWriter()
writer.add_page(paginas[0])
pagina1_caminho = PASTA_NOVOS_ARQUIVOS / 'primeira_pagina.pdf'
with open(pagina1_caminho, 'wb') as arquivo:
    writer.write(arquivo)

# Salvar todas as páginas de um PDF em um novo arquivo PDF (equivalente a criar uma cópia)
writer = PdfWriter()
for pagina in paginas:
    writer.add_page(pagina)
paginas_caminho = PASTA_NOVOS_ARQUIVOS / 'todas_paginas.pdf'
with open(paginas_caminho, 'wb') as arquivo:
    writer.write(arquivo)

# Salvar cada página de um PDV em um novo arquivo PDF separado
for i, pagina in enumerate(paginas):
    writer = PdfWriter()
    writer.add_page(pagina)
    pagina_caminho = PASTA_NOVOS_ARQUIVOS / f'pagina_{i+1}.pdf'
    with open(pagina_caminho, 'wb') as arquivo:
        writer.write(arquivo)

# Salvar todas as páginas de um PDF, em um novo arquivo PDV, porém na ordem invertida
writer = PdfWriter()
quantidade_paginas = len(paginas)
for i in range(quantidade_paginas - 1, -1, -1):
    writer.add_page(paginas[i])
invertido_caminho = PASTA_NOVOS_ARQUIVOS / 'paginas_invertidas.pdf'
with open(invertido_caminho, 'wb') as arquivo:
    writer.write(invertido_caminho)
