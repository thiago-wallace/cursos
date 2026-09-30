# exercício - classe carro 2

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    def consultar_carro(self):
        return f'Carro: {self.nome}, Motor: {self._motor.nome}, Fabricante: {self._fabricante.nome}'


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

carro1.fabricante = fabricante_volkswagen
carro1.motor = motor_20_gasolina
carro2.fabricante = fabricante_volkswagen
carro2.motor = motor_10_alcool
carro3.fabricante = fabricante_ford
carro3.motor = motor_16_hibrido
carro4.fabricante = fabricante_ford
carro4.motor = motor_10_alcool
carro5.fabricante = fabricante_chevrolet
carro5.motor = motor_20_gasolina
carro6.fabricante = fabricante_renault
carro6.motor = motor_16_hibrido

print(carro1.consultar_carro())
print(carro2.consultar_carro())
print(carro3.consultar_carro())
print(carro4.consultar_carro())
print(carro5.consultar_carro())
print(carro6.consultar_carro())
