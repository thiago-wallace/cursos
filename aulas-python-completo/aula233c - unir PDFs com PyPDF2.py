# unir PDFs com PyPDF2
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
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT = Path(__file__).parent
PASTA_NOVOS_ARQUIVOS = ROOT / 'aula233' / 'novos_arquivos'
PAGINA_1 = PASTA_NOVOS_ARQUIVOS / 'pagina_1.pdf'
PAGINA_2 = PASTA_NOVOS_ARQUIVOS / 'pagina_2.pdf'

# unir arquivos PDF com PdfMerger
merger = PdfMerger()
merger.append(PAGINA_1)
merger.append(PAGINA_2)
paginas_unidas_1 = PASTA_NOVOS_ARQUIVOS / 'paginas_unidas_1.pdf'
with open(paginas_unidas_1, 'wb') as arquivo:
    merger.write(arquivo)

# unir arquivos PDF com PdfReader e PdfWriter
reader: list[PdfReader] = []
reader.append(PdfReader(PAGINA_1))
reader.append(PdfReader(PAGINA_2))

writer = PdfWriter()
for paginas in reader:
    for pagina in paginas.pages:
        writer.add_page(pagina)

paginas_unidas_2 = PASTA_NOVOS_ARQUIVOS / 'paginas_unidas_2.pdf'
with open(paginas_unidas_2, 'wb') as arquivo:
    writer.write(arquivo)
