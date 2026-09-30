# __new__ e __call__ da metaclasse
'''
Em metaclasse, o __new__ retorna a classe, e o __call__ retorna a criação da instância
'''

def meu_repr(self):
    return f'{self.__class__.__name__}({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('Metaclasse New')
        classe = super().__new__(mcs, name, bases, dct)
        classe.__repr__ = meu_repr
        return classe

    def __call__(classe, *args, **kwargs):
        print('Metaclasse Call')
        instancia = super().__call__(*args, **kwargs)
        return instancia


class Pessoa(metaclass=Meta):
    def __new__(classe, *args, **kwargs):
        print('Classe New')
        instancia = super().__new__(classe)
        return instancia

    def __init__(self, nome):
        print('Classe Init')
        self.nome = nome

p = Pessoa('João Pessoa')
print()
print(p.nome)
print(p)
