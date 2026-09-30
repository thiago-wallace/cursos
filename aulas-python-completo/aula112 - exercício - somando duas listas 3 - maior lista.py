# exercício - somando duas listas 3 - maior lista
# Usando como referência dessa vez, a maior lista

from itertools import zip_longest

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40]

# Solução 1

def somar_listas(lista_a, lista_b):
    tamanho_a = len(lista_a)
    tamanho_b = len(lista_b)
    tamanho_min = min(tamanho_a, tamanho_b)
    lista_total = [lista_a[i] + lista_b[i] for i in range(tamanho_min)]
    if tamanho_a < tamanho_b:
        for i in range(tamanho_a, tamanho_b):
            lista_total.append(lista_b[i])
    else:
        for i in range(tamanho_b, tamanho_a):
            lista_total.append(lista_a[i])
    return lista_total

soma = somar_listas(x, y)
print(soma)

# Solução 2

soma = [x + y for x, y in zip_longest(x, y, fillvalue=0)]
print(soma)
