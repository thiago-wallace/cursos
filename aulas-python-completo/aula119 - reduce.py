# reduce
'''
Faz a redução de um iterável em um valor.
Exemplo: Somar o preço dos produtos de uma lista.
Obs: Para somar, sempre colocar como parâmetro inicial um zero.
'''

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Sem o Reduce

total_1 = 0
for produto in produtos:
    total_1 += produto['preco']
print(f'Total: {total_1:.2f}')

# Com o Reduce e uma função

def somar_reduce(total, produto):
    return total + produto['preco']

total_2 = reduce(somar_reduce, produtos, 0)
print(f'Total: {total_2:.2f}')

# Com o Reduce e lambda

total_3 = reduce(lambda total, produto: total + produto['preco'], produtos, 0)
print(f'Total: {total_3:.2f}')
