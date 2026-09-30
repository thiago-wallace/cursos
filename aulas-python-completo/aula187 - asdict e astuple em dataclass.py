# asdict e astuple em dataclass
'''
asdict - converte a instância da classe em dicionário
astuple - converte a instância da classe em tupla
'''

from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


pessoa = Pessoa('João', 'Pessoa')

dicionario = asdict(pessoa)
print(dicionario)
print(pessoa.__dict__)

tupla = astuple(pessoa)
print(tupla)
