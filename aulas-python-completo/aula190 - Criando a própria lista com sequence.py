# Criando a própria lista com sequence
"""
Implementando o protocolo do Iterator em Python
Essa é apenas uma aula para introduzir os protocolos de collections.abc no
Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
estrutura usada nessa aula.
https://docs.python.org/3/library/collections.abc.html
"""

from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._list = {}
        self._index_len = 0
        self._next_index = 0

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        if index >= 0 and index < self._index_len:
            self._list[index] = value
        else:
            raise IndexError('Este indice não existe')

    def __len__(self):
        return self._index_len

    def append(self, value):
        self._list[self._index_len] = value
        self._index_len += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index_len:
            self._next_index = 0
            raise StopIteration
        value = self._list[self._next_index]
        self._next_index += 1
        return value


nomes = MyList()
nomes.append('Maria')
nomes.append('João')
nomes.append('José')
nomes.append('Helena')

nomes[2] = 'Mateus'

print(nomes[1])
print(nomes[3])
print(nomes[0])
print(nomes[2])
print()

for nome in nomes:
    print(nome)
print()

print(*nomes, sep='\n')

print(nomes.__dict__)
