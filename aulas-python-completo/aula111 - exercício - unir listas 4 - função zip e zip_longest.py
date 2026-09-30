# Exercício - Unir listas - Solução 4 - função zip e zip_longest
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

A função zip já faz exatamente o exercício proposto.
A função zip_longest também une duas listas, porém usando como base a lista maior, sendo que os itens que sobrarem, por padrão, são pareados com None. Para
    configurar algum valor no lugar de None, podemos utilizar o argumento nomeado fillvalue.
Tanto a função zip quanto a função zip_longest retornam como um iterável, sendo necessário converter para lista, tupla, ou passar por esse iterável
    em um for.
'''

from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista_a, lista_b):
    tamanho = min(len(lista_a), len(lista_b))
    lista_final = [(lista_a[i], lista_b[i]) for i in range(tamanho)]
    return lista_final

print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue='Sem cidade')))

lista_unida = list(zip(cidades, estados))
for item in lista_unida:
    print(item)
