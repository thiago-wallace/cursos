# funções decoradoras com métodos

def meu_planeta(metodo):
    def inner(self, *args, **kwargs):
        planeta = metodo(self, *args, **kwargs)
        print('*', planeta)
        if 'Terra' in planeta:
            planeta = 'Você está em casa'
        return planeta
    return inner


class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def get_planeta(self):
        return f'O planeta é {self.nome}'


terra = Planeta('Terra')
marte = Planeta('Marte')

print('##', terra.get_planeta())
print('##', marte.get_planeta())
