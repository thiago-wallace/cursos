# Exercício - Unir listas - Solução 2
'''
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
'''

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

def parametros_do_decorador(nome=None):
    def decorador(funcao):
        def inner(*args, **kwargs):
            return funcao(*args, **kwargs)
        return inner
    return decorador

@parametros_do_decorador()
def zipper(lista_a, lista_b):
    tamanho = len(lista_a) if len(lista_a) <= len(lista_b) else len(lista_b)
    lista_final = [(lista_a[i], lista_b[i]) for i in range(tamanho)]
    return lista_final

print(zipper(cidades, estados))
print(zipper(estados, cidades))

