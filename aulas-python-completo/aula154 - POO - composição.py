# POO - composição
'''
Relações entre classes: associação, agregação e composição
Composição é uma especialização da agregação.
Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.
'''


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self._endereco = []

    def inserir_endereco(self, rua, numero):
        self._endereco.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self._endereco:
            print(f'{endereco.rua}, {endereco.numero}')


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente = Cliente('João Pessoa')
cliente.inserir_endereco('Rua Dois', 22)
cliente.inserir_endereco('Av. Principal', 157)
cliente.listar_enderecos()
