# dumps, loads e tipagem com json
'''
dumps - converter os dados do python em json, retornando o resultado em uma str
loads - converter o json em dados do python, entrando em str
dump - converter os dados do python em json, salvando em um arquivo .json
load - carregando um arquivo .json em dados do python
Ao converter de Python para JSON:
Python        JSON
dict          object
list, tuple   array
str           string
int, float    number
True          true
False         false
None          null
'''

import json
from pprint import pprint
from typing import TypedDict


# Criando a tipagem para um dicionário
class TypeFilme(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: float | None


# criando uma string, contendo um json
# doc-string também pode ser utilizado como uma string de multi-linhas
json_string_1 = """{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": [
        "Frodo",
        "Sam",
        "Gandalf",
        "Legolas",
        "Boromir"
    ],
    "budget": null
}"""

# converter de json para python, e aplicando a tipagem do dicionário
filme: TypeFilme = json.loads(json_string_1)
# exibindo o dicionário, um item por linha
print('PYTHON - DICT')
print(*filme.items(), sep='\n')
print('\nPYTHON - DICT - PPRINT')
# utilizando pprint para exibir o dicionário
pprint(filme)
print('\nJSON - OBJECT')
# converter de python para json, retornando o resultado em uma str
json_string_2 = json.dumps(filme, ensure_ascii=False, indent=4)
print(json_string_2)
