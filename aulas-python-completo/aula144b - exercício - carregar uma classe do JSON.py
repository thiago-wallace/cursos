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

pessoa1 = Pessoa(**dados[0])
pessoa2 = Pessoa(**dados[1])
pessoa3 = Pessoa(**dados[2])
pessoa4 = Pessoa(**dados[3])

print(pessoa1.__dict__)
print(pessoa2.__dict__)
print(pessoa3.__dict__)
print(pessoa4.__dict__)
