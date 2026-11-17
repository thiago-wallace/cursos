# ler PDF com PyPDF2
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

# Guardar as páginas do PDF em um iterável
paginas = reader.pages

# Verificar a quantidade de páginas
print('Número de páginas:', len(paginas), end='\n\n')

# Extrair o texto da primeira página
print(paginas[0].extract_text(), end='\n\n')

# Imagens da primeira página - Necessário instalar dependência image: pip install PyPDF2[image]
print(paginas[0].images, end='\n\n')

# Quantidade de imagens na página
print('Número de imagens:', len(paginas[0].images), end='\n\n')

# Guardar a primeira imagem da primeira página
imagem = paginas[0].images[0]

# Salvar a imagem em um arquivo .png
# no open, ao salvar, deverá ser configurado como 'wb' ao invés de 'w', pois o open salvará os dados do arquivo em bytes
imagem_caminho = PASTA_NOVOS_ARQUIVOS / imagem.name
with open(imagem_caminho, 'wb') as arquivo:
    arquivo.write(imagem.data)
