# Enum -> Enumerações 1
"""
Enumerações na programação, são usadas em ocasiões onde temos um determinado número de coisas para escolher.
Enums têm membros e seus valores são constantes.
Enums em python:
  - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
  - podem ser iterados para retornar seus membros canônicos na ordem de definição
enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada diretamente (mesmo assim, Enums não são classes normais em Python).
Você poderá usar seu Enum com type annotations, com isinstance e outras coisas relacionadas com tipo.
Para obter os dados:
membro = Classe(valor), Classe['chave']
chave = Classe.chave.name
valor = Classe.chave.value
"""

import enum

# Forma 1 - Declarando diretamente com enum.Enum
# Vantagem: Declaração mais simples.
# Desvantagem: o Tipo não fica claro para o VSCODE, principalmente dentro de funções.
Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção incorreta')
    print(f'Movendo para {direcao}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)

print(Direcoes.ESQUERDA, Direcoes(1), Direcoes['ESQUERDA'])
print(Direcoes.ESQUERDA.name, Direcoes(1).name, Direcoes['ESQUERDA'].name)
print(Direcoes.ESQUERDA.value, Direcoes(1).value, Direcoes['ESQUERDA'].value)
