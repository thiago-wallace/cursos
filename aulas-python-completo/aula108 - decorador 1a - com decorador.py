# Funções decoradoras e decoradores (ou decorators)
'''
Decorar = Adicionar / Remover / Restringir / Alterar.
Funções decoradoras são funções que decoram outras funções (Exemplo: criar_funcao).
Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
Decoradores são "Syntax Sugar" (Açúcar sintático)
'''

def criar_funcao(funcao):
    def argumentos(*args):
        print('função decoradora')
        return funcao(*args)
    return argumentos

@criar_funcao
def potencia(base, expoente):
    return base ** expoente

x = potencia(2, 3)
y = potencia(2, 5)
z = potencia(5, 3)

print(x)
print(y)
print(z)


