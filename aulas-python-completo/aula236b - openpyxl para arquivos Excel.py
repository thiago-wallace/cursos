# openpyxl para arquivos Excel 2
'''
openpyxl para arquivos Excel xlsx, xlsm, xltx e xltm (instalação)
Com essa biblioteca será possível ler e escrever dados em células
específicas, formatar células, inserir gráficos,
criar fórmulas, adicionar imagens e outros elementos gráficos às suas
planilhas. Ela é útil para automatizar tarefas envolvendo planilhas do
Excel, como a criação de relatórios e análise de dados e/ou facilitando a
manipulação de grandes quantidades de informações.
Instalação necessária: pip install openpyxl
Documentação: https://openpyxl.readthedocs.io/en/stable/
'''

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pathlib import Path

PASTA_EXCEL = Path(__file__).parent / 'aula236'
ARQUIVO_EXCEL = PASTA_EXCEL / 'Estudantes2.xlsx'

PASTA_EXCEL.mkdir(exist_ok=True)

estudantes = [
    # Nome, Idade, Nota
    ['João', 14, 5.5],
    ['Maria', 13, 9.7],
    ['Luiz', 15, 8.8],
    ['Alberto', 16, 10],
]

pasta = Workbook()
planilha: Worksheet = pasta.active  # type:ignore

# Primeira linha com os cabeçarios
# append recebe uma lista ou tupla, cada item da lista representa uma coluna na mesma linha
planilha.append(('Nome', 'Idade', 'Nota'))

# Preenchendo as demais linhas
# Cada volta do laço for, representa uma linha na planilha
for est in estudantes:
    planilha.append(est)

pasta.save(ARQUIVO_EXCEL)
