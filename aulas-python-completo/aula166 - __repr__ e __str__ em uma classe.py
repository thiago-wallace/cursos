# __repr__ e __str__ em uma classe
'''
Tanto o __repr__ quanto o __str__ são métodos que devem retornar string, porém o __repr__ é focado para orientar outros desenvolvedores sobre como a sua
    classe deve ser iniciada, e o __str__ é focado apenas em mostrar dados da sua classe de forma simples.
Se ambos os métodos forem criados na classe, então como padrão, o python mostrará o método __str__.
Em resumo, o __repr__ deve retornar informações para outro desenvolvedor sobre a classe, e o __str__ deve apenas retornar uma string sobre a classe.
Em f-string, ao adicionar em um objeto o '!r', ele mostrará o __repr__ desse objeto. Ao adicionar em um objeto o '!s', ele mostrará o __str__
    desse objeto.
repr() - equivalente ao '!r' na f-string.
str() - equivalente ao '!s' na f-string.
'''


class Pontos:
    def __init__(self, x, y, opcao='Opção'):
        self.x = x
        self.y = y
        self.opcao = opcao


class Cordenadas:
    def __init__(self, x, y, opcao='Opção'):
        self.x = x
        self.y = y
        self.opcao = opcao

    def __str__(self):
        return f'({self.x}, {self.y}, {self.opcao})'

    def __repr__(self):
        # Duas formas de coletar apenas o nome da classe
        nome_classe = self.__class__.__name__  # Forma 1
        nome_classe = type(self).__name__  # Forma 2
        # Dentro de um __repr__, é recomendável retornar o repr dos valores.
        return f'{nome_classe}(x={self.x!r}, y={self.y!r}, opcao={self.opcao!r})'


p1 = Pontos(1, 2)
p2 = Pontos(950, 560)
c1 = Cordenadas(1, 2)
c2 = Cordenadas(950, 560)

print(p1)
print(p2)
print(c1)
print(c2)
print(f'{c1!r}')
print(repr(c2))
