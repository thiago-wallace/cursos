# exercício - somando duas listas 2

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40]

soma = [x + y for x, y in zip(x, y)]
print(soma)
