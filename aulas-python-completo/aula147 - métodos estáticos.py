# métodos estáticos
'''
@staticmethod - Métodos estáticos: são métodos que estão dentro da classe, mas não tem acesso ao self nem ao cls.
Em resumo, funcionam exatamente como funções, porém estão dentro da sua classe.
Podem ficar dentro de uma classe, por exemplo, por organização, e devido à estar dentro da classe, podem ser chamadas pela instância ou pela classe direto,
    mas fazem ações exatamente como uma função.
'''


class Matematica:

    @staticmethod
    def somar(x, y):
        return x + y


def somar(x, y):
    return x + y


m = Matematica()
n1 = m.somar(2, 3)  # chamando método estático pela instância
n2 = Matematica.somar(2, 3)  # chamando método estático pela classe
n3 = somar(2, 3)  # chamando função

print(n1)
print(n2)
print(n3)
