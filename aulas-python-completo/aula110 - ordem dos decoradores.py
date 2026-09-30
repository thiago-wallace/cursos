# Ordem dos decoradores
'''
Os decoradores são executados de baixo para cima
'''

def parametros_do_decorador(nome):
    def decorador(funcao):
        print('Decorador:', nome)
        def inner(*args, **kwargs):
            resultado = funcao(*args, **kwargs)
            mensagem = f'{resultado} {nome}'
            return mensagem
        return inner
    return decorador

@parametros_do_decorador('terceiro')
@parametros_do_decorador('segundo')
@parametros_do_decorador('primeiro')
def somar(x, y):
    return x + y

soma1 = somar(10, 20)
soma2 = somar(50, 30)

print(soma1)
print(soma2)

