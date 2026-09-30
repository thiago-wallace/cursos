# property e setter
'''
setter - um método para atribuir o valor de um atributo.

Obs: Por convenção, atributos que começar com um ou dois underlines não devem ser usados fora da classe.
'''


class Caneta:
    def __init__(self, cor):
        self._cor = cor  # atribuíndo valor pera a variável direto

    @property
    def cor(self):
        print('getter', self._cor)
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('setter', valor)
        self._cor = valor


caneta = Caneta('Azul')
caneta.cor = "Amarelo"
print(caneta.cor)
