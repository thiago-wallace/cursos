# exercício - carregar uma classe do JSON
# com importação de módulo e uso do:
# if __name__ == '__main__'

from aula144e import nome_arquivo, Pessoa
import json

dados = []
try:
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    print(f'Arquivo {nome_arquivo} não encontrado')

pessoas = []
for dado in dados:
    pessoas.append(Pessoa(**dado))

for pessoa in pessoas:
    print(pessoa.__dict__)
