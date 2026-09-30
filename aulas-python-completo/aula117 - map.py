# map
'''
Utilizada para mapear dados, semelhante ao list comprehension com for.
Exemplo, em uma lista de produtos, aumentar 10% o valor dos produtos.
'''

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_valor_dicionario(dicionario):
    return {**dicionario, 'preco': round(dicionario['preco'] * 1.10, 2)}

def print_lista_dicionarios(lista):
    print(*lista, sep='\n', end='\n\n')

# list comprehension com for
produtos_ajustados = [aumentar_valor_dicionario(produto) for produto in produtos]
print_lista_dicionarios(produtos_ajustados)

# map
produtos_ajustados = map(aumentar_valor_dicionario, produtos)
print_lista_dicionarios(produtos_ajustados)

