# exercício - somando duas listas 1

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40]

def somar_listas(lista_a, lista_b):
    tamanho = min(len(lista_a), len(lista_b))
    return [lista_a[i] + lista_b[i] for i in range(tamanho)]

soma = somar_listas(x, y)
print(soma)
