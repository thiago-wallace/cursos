# Tipos de variáveis no JSON
'''
bool
number - qualquer dado numérico, tanto número inteiro (int) quanto número com ponto flutuante (float)
string - str
array [] - equivalente à lista (list) do Python. Engloba também tupla (tuple). 
objeto {} - equivalente ao dicionário (dict) do Python
null - equivalente ao None do Python

Obs: Ao passar uma tupla para o json, ele ficará salvo como um array, e ao carregar o json no python, esse array ficará como lista, mesmo que antes ele
    era uma tupla.

Obs: Ao passar um None para o json, ele vai salvar como null, e vice-versa.
'''
