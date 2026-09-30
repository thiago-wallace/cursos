# Método especial __call__
'''
Callable é algo que pode ser executado com parênteses (como uma função por exemplo)
Em classes normais, __call__ faz a instância de uma classe ser "callable"
Com esse métodos __call__, podemos executar a instância como se fosse um método
'''


class Ligacao:
    def __init__(self, telefone):
        self.telefone = telefone

    def __call__(self, nome):
        msg = f'{nome} está ligando no telefone {self.telefone}'
        print(msg)
        return msg


ligacao = Ligacao('5555-5555')
print(ligacao('João Pessoa'))
