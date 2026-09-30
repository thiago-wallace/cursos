""" Exemplo de documentação em classe e métodos

Um código como exemplos de documentão em classe e métodos.
"""


class Calculos:
    """ Classe Calculos

    Esta Classe contém três métodos:
    somar, multiplicar e dividir.
    """

    def somar(self, x: int | float, y: int | float) -> int | float:
        """ Método somar

        Este método faz a soma de x e y.

        """
        return x+y

    def multiplicar(self, x: int | float, y: int | float, z: int | float | None = None) -> int | float:
        """ Método multiplicar

        Este método faz a multiplicação de x e y.
        Se o valor z for definido, então é efetuado a multiplicação de x, y e z.
        """
        if z:
            return x*y*z
        return x*y

    def dividir(self, x: int | float, y: int | float) -> float:
        """ Método dividir

        Este método faz a divisão de x por y.

        :raises ZeroDivisionError: Se o y for zero.
        """
        if y == 0:
            raise ZeroDivisionError('Não é possível dividir por zero!')
        return x/y


c = Calculos()
d = c.dividir(15, 3)
