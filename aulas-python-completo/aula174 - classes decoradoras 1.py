# classes decoradoras 1

class Multiplicar:
    def __init__(self, func):
        self._func = func
        self.multiplicador = 10

    def __call__(self, *args, **kwargs):
        resultado = self._func(*args, **kwargs)
        return self.multiplicador * resultado


@Multiplicar
def somar(x, y):
    return x + y


s = somar(2, 4)
print(s)
