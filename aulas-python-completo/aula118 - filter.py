# filter
'''
Utilizada para filtrar dados, semelhante ao list comprehension com for.
Exemplo, em uma lista de produtos, filtrando produtos com o valor igual ou acima de 20.
'''

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def print_lista_dicionarios(lista):
    print(*lista, sep='\n', end='\n\n')

# list comprehension com for
produtos_filtrados = [{**produto} for produto in produtos if produto['preco'] >= 20]
print_lista_dicionarios(produtos_filtrados)

# filter
produtos_filtrados = filter(lambda produto: produto['preco'] >= 20, produtos)
print_lista_dicionarios(produtos_filtrados)

