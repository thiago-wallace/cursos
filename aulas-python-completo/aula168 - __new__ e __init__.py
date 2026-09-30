# __new__ e __init__
'''
__new__ e __init__ em classes Python
__new__ é o método responsável por criar e retornar o novo objeto. Por isso, new recebe cls.
__new__ DEVE retornar o novo objeto

__init__ é o método responsável por inicializar a instância. Por isso, init recebe self.
__init__ NÃO DEVE retornar nada (None)

object é a super classe de uma classe
'''


class Pessoa:
    def __new__(cls, nome):
        print('Estou no new - antes de criar a instância')
        instancia = super().__new__(cls)
        print('Estou no new - depois de criar a instância')
        return instancia

    def __init__(self, nome):
        print('Estou no init')
        self.nome = nome

    def __repr__(self):
        return f'{self.__class__.__name__}()'


p = Pessoa('João Pessoa')
print(p)
print(p.nome)
