# dunder methods - operadores
'''
__lt__(self,other) - self < other
__le__(self,other) - self <= other
__gt__(self,other) - self > other
__ge__(self,other) - self >= other
__eq__(self,other) - self == other
__ne__(self,other) - self != other
__add__(self,other) - self + other
__sub__(self,other) - self - other
__mul__(self,other) - self * other
__truediv__(self,other) - self / other
__neg__(self) - -self
__str__(self) - str
__repr__(self) - str
'''


class Cordenadas:
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        nome_classe = self.__class__.__name__
        return f'{nome_classe}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Cordenadas(x, y)

    def __gt__(self, other):
        self.total = self.x + self.y
        other.total = other.x + other.y
        return self.total > other.total


c1 = Cordenadas(1, 2)
c2 = Cordenadas(6, 8)
c3 = c1+c2
print(repr(c3))

if c1 > c2:
    print(f'{c1} é maior do que {c2}')
else:
    print(f'{c1} não é maior do que {c2}')

if c2 > c1:
    print(f'{c2} é maior do que {c1}')
else:
    print(f'{c2} não é maior do que {c1}')
