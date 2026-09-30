# arquivo JSON em Python
# baseado no curso do udemy

import json

pessoas = []

with open('arquivo.json', 'r', encoding='utf-8') as arquivo:
    pessoas = json.load(arquivo)
    print(*pessoas, sep='\n')

'''
Por padrão, ele salva o arquivo em codificação de caracteres em ASCII, caso precise manter em UTF-8,
    pode utilizar o argumento nomeado ensure_ascii como False.
'''
with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoas, arquivo, indent=2, ensure_ascii=False)
