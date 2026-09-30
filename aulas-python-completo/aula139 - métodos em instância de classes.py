# métodos em instância de classes

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(self.nome, 'está acelerando...')


fusca = Carro('Fusca')
celta = Carro('Celta')

print(fusca.nome)
print(celta.nome)

fusca.acelerar()
celta.acelerar()
