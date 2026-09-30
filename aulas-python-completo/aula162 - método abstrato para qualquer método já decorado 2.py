# método abstrato para qualquer método já decorado 2
'''
abstractmethod para qualquer método já decorado (@property e setter)
É possível criar @property @property.setter @classmethod @staticmethod e métodos normais como abstratos, para isso use @abstractmethod como
    decorator mais interno.

Foo - Bar são palavras usadas como placeholder para palavras que podem mudar na programação.
'''
# Exemplo de método abstrato para o setter

from abc import ABC, abstractmethod


class AbstratoFoo(ABC):
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    @abstractmethod
    def nome(self, nome): ...


class Foo(AbstratoFoo):
    def __init__(self, nome):
        super().__init__(nome)

    @AbstratoFoo.nome.setter
    def nome(self, nome):
        self._nome = nome


foo = Foo('Fighters')
foo.nome = 'U2'
print(foo.nome)
