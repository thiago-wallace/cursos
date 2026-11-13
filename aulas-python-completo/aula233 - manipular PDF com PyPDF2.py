# manipular PDF com PyPDF2
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
from PyPDF2 import PdfReader

ROOT = Path(__file__).parent
PASTA_PDFS_ORIGINAIS = ROOT / 'aula233' / 'pdfs_originais'
PASTA_NOVOS_ARQUIVOS = ROOT / 'aula233' / 'novos_arquivos'
BACEN_2023 = PASTA_PDFS_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVOS_ARQUIVOS.mkdir(exist_ok=True)

# Ler o arquivo PDF
reader = PdfReader(BACEN_2023)

print(reader)
