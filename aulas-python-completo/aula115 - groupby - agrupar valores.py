# groupby - agrupar valores
'''
Antes de agrupar, é necessário deixar a lista em ordem
'''

from itertools import groupby

letras = ['a', 'b', 'c', 'a', 'b', 'a']

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordenar_por_nota(lista):
    return lista['nota']

print('\nLetras\n')
letras_ordenadas = sorted(letras)
letras_agrupadas = groupby(letras_ordenadas)
for grupo, itens in letras_agrupadas:
    print(grupo)
    print(list(itens))

print('\nAlunos\n')
alunos_ordenados = sorted(alunos, key=ordenar_por_nota)
alunos_agrupados = groupby(alunos_ordenados, key=ordenar_por_nota)
for grupo, itens in alunos_agrupados:
    print(grupo)
    for item in itens:
        print(item)
