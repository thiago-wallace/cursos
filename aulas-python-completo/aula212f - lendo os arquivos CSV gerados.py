# lendo os arquivos CSV gerados
'''
csv.reader e csv.DictReader
csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
'''

from pathlib import Path
import csv

BASE_ARQUIVOS = Path(__file__).parent
ARQUIVOS_CSV = (
    BASE_ARQUIVOS / 'aula212b.csv',
    BASE_ARQUIVOS / 'aula212c.csv',
    BASE_ARQUIVOS / 'aula212d.csv',
    BASE_ARQUIVOS / 'aula212e.csv',
)

tabelas = []

for arquivo_csv in ARQUIVOS_CSV:
    with open(arquivo_csv, 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        tabelas.append(list(leitor))

validado = True

for i in range(len(tabelas) - 1):
    for j in range(i+1, len(tabelas)):
        if tabelas[i] != tabelas[j]:
            validado = False
            break
    if not validado:
        break

print(*tabelas, sep='\n')
print(f'{validado=}')
