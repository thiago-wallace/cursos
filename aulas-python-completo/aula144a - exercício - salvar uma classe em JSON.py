# exercício - salvar uma classe em JSON

import json


class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura


pessoa1 = Pessoa('João', 'Pessoa', 34, 1.70)
pessoa2 = Pessoa('Maria', 'Helena', 26, 1.67)
pessoa3 = Pessoa('José', 'da Silva', 18, 1.84)
pessoa4 = Pessoa('Ester', 'Souza', 15, 1.56)

dados = []
dados.append(pessoa1.__dict__)
dados.append(pessoa2.__dict__)
dados.append(pessoa3.__dict__)
dados.append(pessoa4.__dict__)

nome_arquivo = 'pessoas.json'
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)
