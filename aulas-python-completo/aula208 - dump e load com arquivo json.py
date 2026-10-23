# dump e load com arquivo json
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
import os
from pprint import pprint

filme = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": [
        "Frodo",
        "Sam",
        "Gandalf",
        "Legolas",
        "Boromir"
    ],
    "budget": None
}
pprint(filme)

# configurando nome do arquivo
# __file__ - Retorna o diretório completo do arquivo atual .py
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), 'aula208.json')

# salvando no arquivo json
with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=4)

# carregando do arquivo json
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados_filme = json.load(arquivo)

pprint(dados_filme)
