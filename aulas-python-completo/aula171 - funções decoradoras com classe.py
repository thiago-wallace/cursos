# funções decoradoras com classe

def meu_repr(cls):
    def repr_(self):
        classe = self.__class__.__name__
        parametro = self.nome
        return f'{classe}({parametro!r})'
    cls.__repr__ = repr_
    return cls


@meu_repr
class Pais:
    def __init__(self, nome):
        self.nome = nome


@meu_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Pais('Brasil')
italia = Pais('Itália')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(italia)

print(terra)
print(marte)
