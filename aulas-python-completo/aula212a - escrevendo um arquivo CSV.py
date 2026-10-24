# escrevendo um arquivo CSV

from pathlib import Path
import csv

clientes_dicionarios = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

clientes_listas = [
    ['Nome', 'Endereço'],
    ['Luiz Otávio', 'Av 1, 22'],
    ['João Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
]

# forma 1 - Dicionários com for percorrendo a list[dict]
ARQUIVO_CSV_1 = Path(__file__).parent / 'aula212b.csv'
with open(ARQUIVO_CSV_1, 'w') as arquivo:
    # no DictWriter, colocar o arquivo e o nome das colunas da tabela
    escritor = csv.DictWriter(arquivo, clientes_dicionarios[0].keys())
    # escrecer no arquivo o nome das colunas da tabela
    escritor.writeheader()
    # escrever no arquivo as demais linhas uma por uma
    for linha in clientes_dicionarios:
        escritor.writerow(linha)

# forma 2 - Dicionários com for percorrendo a list[list]
ARQUIVO_CSV_2 = Path(__file__).parent / 'aula212c.csv'
with open(ARQUIVO_CSV_2, 'w') as arquivo:
    # no writer, colocar o arquivo
    escritor = csv.writer(arquivo)
    # escrever no arquivo as linhas da tabela uma por uma
    for linha in clientes_listas:
        escritor.writerow(linha)

# forma 3 - Dicionários com writerows recebendo a list[dict]
ARQUIVO_CSV_3 = Path(__file__).parent / 'aula212d.csv'
with open(ARQUIVO_CSV_3, 'w') as arquivo:
    # no DictWriter, colocar o arquivo e o nome das colunas da tabela
    escritor = csv.DictWriter(arquivo, clientes_dicionarios[0].keys())
    # escrecer no arquivo o nome das colunas da tabela
    escritor.writeheader()
    # escrever no arquivo as demais linhas em um só comando
    escritor.writerows(clientes_dicionarios)

# forma 4 - Listas com writerows recebendo a list[list]
ARQUIVO_CSV_4 = Path(__file__).parent / 'aula212e.csv'
with open(ARQUIVO_CSV_4, 'w') as arquivo:
    # no writer, colocar o arquivo
    escritor = csv.writer(arquivo)
    # escrever no arquivo as linhas da tabela em um só comando
    escritor.writerows(clientes_listas)
