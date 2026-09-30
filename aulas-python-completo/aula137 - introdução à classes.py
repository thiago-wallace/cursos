# introdução à classes
'''
Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que podem ter seus próprios atributos (dados, variáveis) e métodos (ações, funções).
Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de classes. Ou seja, a primeira letra maiúscula de cada palavra, inclusive a primeira palavra/letra.
'''


class Pessoa:
    ...


p1 = Pessoa()
p1.nome = 'João'
p1.sobrenome = 'Pessoa'

p2 = Pessoa()
p2.nome = 'Maria'
p2.sobrenome = 'Helena'

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)
