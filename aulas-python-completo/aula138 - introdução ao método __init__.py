# introdução ao método __init__.py
'''
O __init__ é um iniciador de atributos, ele é uma das primeiras ações executadas em uma classe.
No init, o primeiro parâmetro sempre vai ser self, onde o python automaticamente vai colocar o nome da instância a ser criada (Nesse caso, seria p1 e p2).
Os demais parâmetros, são passados na chamada da classe.
'''


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('João', 'Pessoa')

p2 = Pessoa('Maria', 'Helena')

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)
