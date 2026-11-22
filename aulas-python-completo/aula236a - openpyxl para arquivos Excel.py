# openpyxl para arquivos Excel 1
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
ARQUIVO_EXCEL = PASTA_EXCEL / 'pastaTeste.xlsx'

PASTA_EXCEL.mkdir(exist_ok=True)

# Configurando a pasta de trabalho (arquivo excel)
pasta = Workbook()

# Selecionando qual a planilha ativa
planilha1: Worksheet = pasta.active  # type: ignore

# Forma 1 - Escrevendo na planilha - Linha 1 Coluna 2 (B1)
planilha1.cell(1, 2, 'Teste1')
# Forma 2 - Escrevendo na planilha - Linha 2 Coluna 2 (B2)
planilha1['b2'] = 'Teste2'

# Salvando o arquivo
pasta.save(ARQUIVO_EXCEL)
