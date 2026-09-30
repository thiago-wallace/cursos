# POO - associação
'''
Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.
Essa é a relação mais comum entre objetos e tem subconjuntos como agregação e composição (que veremos depois).
Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.
A associação não especifica como um objeto controla o ciclo de vida de outro objeto.
'''


class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta:
    def __init__(self, ferramenta):
        self.ferramenta = ferramenta

    def escrever(self):
        return f'{self.ferramenta} está sendo usado para escrever'


escritor_joao = Escritor('João Pessoa')
ferramenta_caneta = Ferramenta('Caneta Bic')
escritor_joao.ferramenta = ferramenta_caneta

print(escritor_joao.ferramenta.escrever())
