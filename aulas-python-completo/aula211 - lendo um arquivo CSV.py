# lendo um arquivo CSV
'''
csv.reader e csv.DictReader
csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
'''

from pathlib import Path
import csv

ARQUIVO_CSV = Path(__file__).parent / 'aula210b - exemplo 1.csv'

# Ler o CSV em formato de lista
with open(ARQUIVO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
print()

# Ler o CSV em formato de dicionário
with open(ARQUIVO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha)
