# Funções decoradoras e decoradores
'''
Decorar = Adicionar / Remover / Restringir / Alterar.
Funções decoradoras são funções que decoram outras funções (Exemplo: criar_funcao).
Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
Decoradores são "Syntax Sugar" (Açúcar sintático)
'''

def criar_funcao(funcao): # isso é uma função decoradora
    def argumentos(*args):
        for arg in args:
            is_string(arg)
        resultado = funcao(*args)
        return resultado
    return argumentos

@criar_funcao # isso é um decorador
def inverter_string(texto):
    return texto[::-1]

def is_string(texto):
    if not isinstance(texto, str):
        raise 'Valor não é uma string, necessário apenas valores em string'

invertido = inverter_string
print(invertido('12345'))


