# sobreposição de classe - super 2
'''
classe super() - classe utilizada para chamar um método da super classe.

Exemplo: dentro da classe 'C', ao utilizar o 'super().metodo()' sem argumentos, ele vai automaticamente chamar no pai da classe
    'C' (ou seja, a classe 'B') o método 'metodo', na instância self.
Nesse caso, daria o mesmo resultado digitar 'super().metodo()' ou 'super(C, self).metodo()'
Outro exemplo: dentro da classe 'C', ao utilizar o 'super(B, self).metodo()', ele vai automaticamente chamar no pai da classe
    'B' (ou seja, a classe 'A') o método 'metodo', na instância self. E assim por diante.

função mro() - Method Resolution Order - função que retorna a ordem de super classes, semelhante ao que mostra em parte da função help()
'''


class A:
    atributo_a = 'Valor A'

    def metodo(self):
        return 'Método A'


class B(A):
    atributo_b = 'Valor B'

    def metodo(self):
        return 'Método B'


class C(B):
    atributo_c = 'Valor C'

    def metodo(self):
        print(super().metodo())
        print(super(C, self).metodo())
        print(super(B, self).metodo())
        return 'Método C'


c = C()

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print(c.metodo())
print()
print(C.mro())
print(B.mro())
print(A.mro())
