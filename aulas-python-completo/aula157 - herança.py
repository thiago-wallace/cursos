# herança
'''
Herança simples - Relações entre classes

Herança vs Composição:
Associação - usa;
Agregação - tem;
Composição - É dono de;
Herança - É um;

Classe principal (Pessoa)
  -> super class, base class, parent class
Classes filhas (Cliente)
  -> sub class, child class, derived class
'''


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibir_classe(self):
        nome = self.nome
        sobrenome = self.sobrenome
        # Utilizado para visualizar o nome da classe atual
        classe = self.__class__.__name__
        print(nome, sobrenome, '-', classe, '-', self.texto)

    texto = 'atributo da pessoa'


# Definindo a classe Pessoa como super class (entre parênteses), e a classe Cliente como sub class.
class Cliente(Pessoa):
    texto = 'atributo do cliente'


class Aluno(Pessoa):
    ...


cliente = Cliente('João', 'Pessoa')
aluno = Aluno('Maria', 'Helena')

cliente.exibir_classe()
aluno.exibir_classe()
