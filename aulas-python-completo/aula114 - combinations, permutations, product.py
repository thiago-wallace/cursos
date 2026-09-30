# combinations, permutations, product
'''
Combinação - Ordem não importa - iterável + tamanho do grupo
Permutação - Ordem importa - iterável + tamanho do grupo
Produto - Ordem importa e repete valores únicos - vários iteráveis
'''

from itertools import combinations, permutations, product

times_sp_4 = ['São Paulo', 'Santos', 'Palmeiras', 'Corinthians',]
times_rj_4 = ['Flamengo', 'Fluminense', 'Vasco', 'Botafogo']

camiseta = [
    ['azul', 'vermelho', 'amarelo', 'verde'],
    ['P', 'M', 'G', 'GG']
]

com = combinations(times_sp_4, 2)
per = permutations(times_sp_4, 2)
pro = product(times_sp_4, times_rj_4)
camisetas = product(*camiseta)

print(*list(com), sep='\n', end='\n\n')
print(*list(per), sep='\n', end='\n\n')
print(*list(pro), sep='\n', end='\n\n')
print(*list(camisetas), sep='\n', end='\n\n')

