# partial - função para criar função
'''
A função 'partial' faz exatamente o que a função 'criar_funcar' faz abaixo. Ele faz parte do módulo functools.
'''

from functools import partial

def criar_funcao(func, *args1):
    def inner(*args2):
        return func(*args1, *args2)
    return inner

def somar(x, y):
    return x+y

x = criar_funcao(somar)
y = partial(somar)

print(x(7, 4))
print(y(7, 4))

