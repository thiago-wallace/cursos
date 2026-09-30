# arquivo JSON em Python
# baseado no curso do udemy

import json

pessoas = [
    {
        "Nome": "João",
        "Sobrenome": "Pessoa",
        "Idade": 21,
        "Endereço": {"Rua": "Alameda 1", "Número": 100, "Cidade": "São Paulo", "Estado": "SP"},
        "Ativo": True,
    },
    {
        "Nome": "Maria",
        "Sobrenome": "Helena",
        "Idade": 25,
        "Endereço": {"Rua": "Alameda 2", "Número": 200, "Cidade": "Rio de Janeiro", "Estado": "RJ"},
        "Ativo": True,
    },
    {
        "Nome": "José",
        "Sobrenome": "Da Silva",
        "Idade": 31,
        "Endereço": {"Rua": "Alameda 3", "Número": 300, "Cidade": "São José do Rio Preto", "Estado": "SP"},
        "Ativo": False,
    },
    {
        "Nome": "Ana",
        "Sobrenome": "Maria",
        "Idade": 28,
        "Endereço": {"Rua": "Alameda 4", "Número": 400, "Cidade": "Fortaleza", "Estado": "CE"},
        "Ativo": True,
    },
]

with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoas, arquivo, indent=2)

'''
Por padrão, ele salva o arquivo em codificação de caracteres em ASCII, caso precise manter em UTF-8,
    pode utilizar o argumento nomeado ensure_ascii como False.
'''
with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoas, arquivo, indent=2, ensure_ascii=False)
