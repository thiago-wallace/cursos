# help
'''
função help - utilizada para obter uma descrição sobre determinado objeto, seja uma classe, função, variável, etc.
'''


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    def inserir_motor(self, motor):
        self._motor = motor

    def inserir_fabricante(self, fabricante):
        self._fabricante = fabricante

    def exibir_carro(self):
        print(
            f'Carro: {self.nome}, Motor: {self._motor.nome}, Fabricante: {self._fabricante.nome}')


help(Carro)
