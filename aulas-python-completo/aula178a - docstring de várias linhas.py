# docstring de várias linhas
"""
docstring de várias linhas pode ser utilizado para documentação.
Segundo a PEP-8, é recomendável por boa prática, a docstring ter no máximo 80
    caracteres, por linha.
Para visualizar o limite de forma fácil, podemos adicionar uma linha editando o
    arquivo settings do VSCODE, adicionando a configuração:
    "editor.rulers": [80], ou "editor.rulers": [80,120],
Segundo também a PEP-8, é recomendável utilizar a docstring sempre com aspas
    duplas.
"""

import aula178b

texto = dir(aula178b)
print(texto)

texto = aula178b.__doc__
print(texto)

help(aula178b)
