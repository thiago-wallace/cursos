# Funções decoradoras e decoradores (ou decorators)
'''
Decorar = Adicionar / Remover / Restringir / Alterar.
Funções decoradoras são funções que decoram outras funções (Exemplo: criar_funcao).
Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
'''

def criar_funcao(funcao):
    def argumentos(*args):
        return funcao(*args)
    return argumentos

def potencia(base, expoente):
    return base ** expoente

p = criar_funcao(potencia)

x = p(2, 3)
y = p(2, 5)
z = p(5, 3)

print(x)
print(y)
print(z)


