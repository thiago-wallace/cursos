# POO - Encapsulamento (modificadores de acesso: public, protected, private)
'''
Python NÃO TEM modificadores de acesso.
Mas podemos seguir as seguintes convenções:
  (sem underline) = public - pode ser usado em qualquer lugar.
_ (um underline) = protected - só DEVE ser usado dentro da classe ou nas suas subclasses.
__ (dois underlines) = private - "name mangling" (desfiguração de nomes em Python _NomeClasse__nome_attr_ou_method) - só DEVE ser usado na classe em que foi
    declarado.
'''


class Foo:
    def __init__(self):
        self.publico = 'isso é público'
        self._protegido = 'isso é protegido'
        self.__privado = 'isso é privado'

    def metodo_publico(self):
        print(self.publico)
        print(self._protegido)
        print(self.__privado)
        print(self._metodo_protegido())
        print(self.__metodo_privado())
        return 'esse método é público'

    def _metodo_protegido(self):
        return 'esse método é protegido'

    def __metodo_privado(self):
        return 'esse método é privado'


f = Foo()
print(f.metodo_publico())
