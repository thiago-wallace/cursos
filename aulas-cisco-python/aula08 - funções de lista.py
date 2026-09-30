numeros = [3, 5, 12, 2, 15, 6]
amigos = ['Marcos', 'Pedro', 'Adriana', 'Karina', 'Júlia']
amigos2 = ['José', 'Maria']
# estender a lista de amigos, com a lista de números
amigos.extend(amigos2)
print(amigos)
# adicionar item no final da lista
amigos.append('João')
print(amigos)
# adicionar um item na posição de índice 3 da lista
amigos.insert(3, 'João')
print(amigos)
# remover um item pelo valor (Adriana)
amigos.remove('Adriana')
print(amigos)
# remover um item pelo índice 2
amigos.pop(3)
print(amigos)
# verificar qual índice da lista o Pedro está
print(amigos.index('Júlia'))
# verificar quantos 'João' tem na lista
print(amigos.count('João'))
# ordenar lista por ordem alfabética ou numérica
amigos.sort()
print(amigos)
numeros.sort()
print(numeros)
