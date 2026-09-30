# count (itertools)
'''
Um contador iterável e com iterator.
Na prática, funciona parecido com o range, porém o count não tem fim (infinito).
count pertence ao módulo itertools.
'''

from itertools import count

r = range(16, 100, 8)
c = count(16, 8)

print('\nRange\n')

for i in r:
    print(i)

print('\nCount\n')

for i in c:
    if i >= 100:
        break
    print(i)

