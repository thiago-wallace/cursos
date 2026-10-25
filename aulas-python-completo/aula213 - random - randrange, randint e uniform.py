# random - randrange, randint e uniform
'''
random tem geradores de números pseudoaleatórios
Obs.: números pseudoaleatórios significa que os números
parecem ser aleatórios, mas na verdade não são. Portanto,
este módulo não deve ser usado para segurança ou uso criptográfico.
O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
a saída pode ser previsível.
doc: https://docs.python.org/pt-br/3/library/random.html
'''

import random

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
# Ex: Gerar número entre 10 e 20, de 2 em 2 (Sem incluir o 20) - [10, 12, 14, 16, 18]
r_range = random.randrange(10, 20, 2)
print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
# Ex: Gerar número entre 10 e 20 (Incluíndo o 20)
r_int = random.randint(10, 20)
print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
# Ex: Gerar número decimal entre 10 e 20
r_uniform = random.uniform(10, 20)
print(r_uniform)
