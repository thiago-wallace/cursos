# ler e editar arquivo excel

from pathlib import Path
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet

PASTA_EXCEL = Path(__file__).parent / 'aula236'
ARQUIVO_EXCEL = PASTA_EXCEL / 'Estudantes4.xlsx'

# Carregando arquivo excel
pasta = load_workbook(ARQUIVO_EXCEL)

planilha: Worksheet = pasta.active  # type: ignore

# exibir planilha na tela
for linha in planilha.iter_rows():
    for celula in linha:
        print(celula.value, end='\t')
    print()

# salvar planiha em uma lista de lista
estudantes: list[list] = []
for i, linha in enumerate(planilha.iter_rows()):
    estudantes.append([])
    for celula in linha:
        estudantes[i].append(celula.value)
print(*estudantes, sep='\n')

# alterar dado da planilha - forma 1 - exemplo: idade da Maria
planilha['B3'] = 14

# alterar dado da planilha - forma 2 - exemplo: idade do Luiz
planilha.cell(4, 2, 16)

# alterar dado da planilha - forma 3 - exemplo: idade do Alberto (Sem a localização da célula)
for linha in planilha.iter_rows():
    for celula in linha:
        if celula.value == 'Alberto':
            planilha.cell(celula.row, 2, 17)

# salvar alterações
pasta.save(ARQUIVO_EXCEL)
