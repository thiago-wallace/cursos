# Decoradores com parâmetros

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(funcao):
        def inner(*args, **kwargs):
            print('Parâmetros da fábrica de decoradores:', a, b, c)
            resultado = funcao(*args, **kwargs)
            return resultado
        return inner
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3)
def somar(x, y):
    return x + y

soma = somar(10, 20)
print(f'{soma=}')
