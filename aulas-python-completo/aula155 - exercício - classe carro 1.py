# exercício - classe carro 1

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


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


carro1 = Carro('Fusca')
carro2 = Carro('Gol')
carro3 = Carro('Focus')
carro4 = Carro('Fiesta')
carro5 = Carro('Ômega')
carro6 = Carro('Clio')

fabricante_volkswagen = Fabricante('Volkswagen')
fabricante_ford = Fabricante('Ford')
fabricante_chevrolet = Fabricante('Chevrolet')
fabricante_renault = Fabricante('Renault')

motor_20_gasolina = Motor('2.0 Gasolina')
motor_16_hibrido = Motor('1.6 Híbrido')
motor_10_alcool = Motor('1.0 Alcool')

carro1.inserir_motor(motor_20_gasolina)
carro1.inserir_fabricante(fabricante_volkswagen)
carro2.inserir_motor(motor_10_alcool)
carro2.inserir_fabricante(fabricante_volkswagen)
carro3.inserir_motor(motor_16_hibrido)
carro3.inserir_fabricante(fabricante_ford)
carro4.inserir_motor(motor_10_alcool)
carro4.inserir_fabricante(fabricante_ford)
carro5.inserir_motor(motor_20_gasolina)
carro5.inserir_fabricante(fabricante_chevrolet)
carro6.inserir_motor(motor_16_hibrido)
carro6.inserir_fabricante(fabricante_renault)

carro1.exibir_carro()
carro2.exibir_carro()
carro3.exibir_carro()
carro4.exibir_carro()
carro5.exibir_carro()
carro6.exibir_carro()
