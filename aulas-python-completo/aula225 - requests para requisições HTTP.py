# requests para requisições HTTP
'''
Mólulo requests
Download do módulo requests e da tipagem deste módulo:
pip install requests types-requests

Porta padrão de sites:
http:// -> 80
https:// -> 443

Tutorial módulo requests com python -> https://youtu.be/Qd8JT0bnJGs
'''

import requests

url = 'http://localhost:8000/'
response = requests.get(url)

# print('código da página: ', response.text)
print('status code:', response.status_code)
print('cabeçarios: ', response.headers)
# Caso a requisição tenha resposta em JSON, poderá ser utilizado:
# response.json()
