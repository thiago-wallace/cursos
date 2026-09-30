"""Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.
"""


def somar(x: int | float, y: int | float) -> int | float:
    """Somar x e y

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float

    """
    return x+y


def multiplicar(x: int | float, y: int | float, z: int | float | None = None) -> int | float:
    """Multiplica x, y e/ou z

    Multiplica x e y. Se z for enviado, multiplica x, y e z.
    """
    if z:
        return x*y*z
    return x*y


variavel1 = multiplicar(2, 3)
variavel2 = multiplicar(2, 3, 5)
