# configurações do decorator dataclass 1
'''
init: configura se a dataclasse vai criar um __init__ automático. True ou False.
    O padrão é True. (Aula185).
frozen: configura se os atributos de uma classe são congelados, caso sim, não é
    possível criar novos atributos, ou alterar o valor dos atributos já 
    definidos na criação da instância da classe. True ou False. O padrão é
    False.
repr: configura se a dataclasse vai criar um __repr__ automático. True ou False.
    O padrão é True.
order: permite ordenar uma lista de instâncias com a função sort.
'''

from dataclasses import dataclass


@dataclass(order=True)
class Pessoa:
    nome: str
    sobrenome: str


pessoas = [
    Pessoa('Maria', 'Helena'),
    Pessoa('João', 'Pessoa'),
    Pessoa('Maria', 'Ana'),
    Pessoa('José', 'Silva'),
]

pessoas.sort()
print(pessoas)
