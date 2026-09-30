# classes decoradoras 2

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def inner(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return inner


@Multiplicar(10)
def somar(x, y):
    return x + y


s = somar(2, 4)
print(s)
