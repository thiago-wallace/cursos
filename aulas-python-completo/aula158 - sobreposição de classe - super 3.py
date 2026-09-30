# sobreposição de classe - super 3
'''
classe super() - classe utilizada para chamar um método da super classe.

Exemplos de formas para lidar com a sobreposição do método __init__
'''


class A:
    def __init__(self, atributo):
        self.atributo = atributo


class B(A):
    def __init__(self, atributo, outro_atributo):
        super().__init__(atributo)
        self.outro_atributo = outro_atributo


class C(B):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


c = C('valor C1', 'Valor C2')
b = B('Valor B1', 'Valor B2')
a = A('Valor A')
print(c.atributo, c.outro_atributo)
print(b.atributo, b.outro_atributo)
print(a.atributo)
