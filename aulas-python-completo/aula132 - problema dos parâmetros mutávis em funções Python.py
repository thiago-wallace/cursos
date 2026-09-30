# Problema dos parâmetros mutávis em funções Python
'''
Quando criar uma função, não passar um tipo de variável mutável (Ex: lista) como argumento padrão, ao invés disso, passar o argumento padrão como None,
    e tratar dentro da função para transformar a variável que está com None em variável mutável.
'''


def adicionar_nome(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


l1 = adicionar_nome('João')
adicionar_nome('Pessoa', l1)
print(l1)

l2 = adicionar_nome('Maria')
adicionar_nome('Helena', l2)
print(l2)
