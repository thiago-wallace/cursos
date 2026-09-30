# Métodos de classe + factories (fábricas)
'''
Métodos de classe: São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe.

Os métodos vistos até aqui, com "self", são métodos de instância.

Já os métodos de classe, com "cls", recebe o nome da classe, e não tem acesso à instância, por não ter o "self".
'''


class Pessoa:
    # Método da instância
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    # Método da classe, como retorna uma classe criada para uma nova instância, é chamado de fábrica.
    def criar_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    # Método da classe, como retorna uma classe criada para uma nova instância, é chamado de fábrica.
    def criar_anonimo(cls, idade):
        return cls("Anônimo", idade)


p1 = Pessoa('João', 35)
p2 = Pessoa.criar_50_anos('Maria')
p3 = Pessoa.criar_anonimo(16)

print('Nome:', p1.nome, '\t Idade:', p1.idade)
print(f'Nome: {p2.nome} \t Idade: {p2.idade}')
print('Nome: {} \t Idade: {}'.format(p3.nome, p3.idade))
