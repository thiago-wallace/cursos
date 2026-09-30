# exercício - salvar uma classe em JSON

import json


class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura


pessoas = []
pessoas.append(Pessoa('João', 'Pessoa', 34, 1.70))
pessoas.append(Pessoa('Maria', 'Helena', 26, 1.67))
pessoas.append(Pessoa('José', 'da Silva', 18, 1.84))
pessoas.append(Pessoa('Ester', 'Souza', 15, 1.56))

dados = []
for pessoa in pessoas:
    dados.append(pessoa.__dict__)

nome_arquivo = 'pessoas.json'
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)
