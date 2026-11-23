# manipular planilha no arquivo excel

from pathlib import Path
from openpyxl import Workbook

PASTA_EXCEL = Path(__file__).parent / 'aula236'
ARQUIVO_EXCEL = PASTA_EXCEL / 'Estudantes4.xlsx'

PASTA_EXCEL.mkdir(exist_ok=True)

estudantes = [
    ['Nome', 'Idade', 'Nota'],
    ['João', 14, 5.5],
    ['Maria', 13, 9.7],
    ['Luiz', 15, 8.8],
    ['Alberto', 16, 10],
]

pasta = Workbook()

# Criar uma planilha dentro do arquivo
pasta.create_sheet('Planilha 3')

# Criar uma planilha e colocar no índice 0 (Colocar em primeiro)
pasta.create_sheet('Planilha 1', 0)

# Selecionar a Planilha 1 na variável
planilha1 = pasta['Planilha 1']
# Selecionar a Planilha 3 na variável
planilha3 = pasta['Planilha 3']
# Selecionar a Planilha Sheet na variável
planilha_padrao = pasta['Sheet']

# Renomear uma planilha
planilha_padrao.title = 'Planilha 2'

# Selecionar a planilha recem nomeada
planilha2 = pasta['Planilha 2']

# Visualizar as planilhas deste arquivo
print(pasta.sheetnames)

# Apagar uma planihla - Forma 1
pasta.remove(pasta['Planilha 3'])

# Apagar uma planihla - Forma 2
pasta.remove(planilha2)

# Preencher a planilha com os dados dos estudantes
for est in estudantes:
    planilha1.append(est)

# Salvar arquivo
pasta.save(ARQUIVO_EXCEL)
