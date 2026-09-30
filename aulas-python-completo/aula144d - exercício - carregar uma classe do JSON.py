# exercício - carregar uma classe do JSON

import json


class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura


dados = []
nome_arquivo = 'pessoas.json'
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
