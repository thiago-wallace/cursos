# namedtuples 2
"""
namedtuples - tuplas imutáveis com nomes para valores.
Usamos namedtuples para criar classes de objetos que são apenas um
agrupamento de atributos, como classes normais sem métodos, ou registros de
bases de dados, etc.
As namedtuples são imutáveis assim como as tuplas.
https://docs.python.org/3/library/collections.html#collections.namedtuple
https://docs.python.org/3/library/typing.html#typing.NamedTuple
https://brasilescola.uol.com.br/curiosidades/baralho.htm
"""
# Forma 2 - Declarando como classe

from typing import NamedTuple


class Carta(NamedTuple):
    valor: str
    naipe: str


as_espada = Carta('As', 'Espada')

print(as_espada)
print(as_espada.valor)
print(as_espada.naipe)
print(as_espada[0])
print(as_espada[1])
for item in as_espada:
    print(item)
print(as_espada._asdict())
