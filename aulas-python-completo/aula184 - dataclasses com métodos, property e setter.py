# dataclasses com métodos, property e setter

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, nome_completo: str):
        nc = nome_completo.split()
        self.nome = nc[0]
        self.sobrenome = ' '.join(nc[1:])


pessoa = Pessoa('João', 'Pessoa')

print(pessoa)
print(pessoa.nome_completo)
pessoa.nome_completo = 'Maria Ana da Silva'
print(pessoa)
print(pessoa.nome_completo)
