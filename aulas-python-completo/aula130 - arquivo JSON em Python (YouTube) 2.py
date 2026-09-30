# arquivo JSON em Python
# baseado no vídeo do youtube
'''
Arquivo JSON é util para guardar valores de variáveis em um arquivo, com uma estrutura organizada. Semelhante ao XML.
https://www.youtube.com/watch?v=XmCrArtfjaQ
'''

import os
import json

pessoas = []

# Pega o diretório em que este arquivo py está
BASE_DIR = os.path.dirname(__file__)
# Junta o diretório salvo anteriormente com o nome do arquivo final
JSON_FILE = os.path.join(BASE_DIR, 'arquivo.json')

print(__file__)
print(BASE_DIR)
print(JSON_FILE)

with open(JSON_FILE, 'r') as file:
    # Carrega a lista do arquivo json
    pessoas = json.load(file)
    print(*pessoas, sep='\n')
    # Converte a lista em json e retorna como string
    texto_string = json.dumps(pessoas, indent=2)
    print(texto_string)
    # Converte a string em json
    texto_json = json.loads(texto_string)
    print(texto_json)
