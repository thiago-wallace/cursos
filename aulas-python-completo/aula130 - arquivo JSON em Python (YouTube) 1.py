# arquivo JSON em Python
# baseado no vídeo do youtube
'''
Arquivo JSON é util para guardar valores de variáveis em um arquivo, com uma estrutura organizada. Semelhante ao XML.
https://www.youtube.com/watch?v=XmCrArtfjaQ
'''

import os
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

# Pega o diretório em que este arquivo py está
BASE_DIR = os.path.dirname(__file__)
# Junta o diretório salvo anteriormente com o nome do arquivo final
SAVE_TO = os.path.join(BASE_DIR, 'arquivo.json')

print(__file__)
print(BASE_DIR)
print(SAVE_TO)

with open(SAVE_TO, 'w') as file:
    # Escreve a lista no arquivo json
    # O argumento indent é útil para deixar o arquivo json mais legível, dando espaçamento de dois caracteres.
    json.dump(pessoas, file, indent=2)
    # Converte a lista em json e retorna como string
    texto = json.dumps(pessoas, indent=2)
    print(texto)
