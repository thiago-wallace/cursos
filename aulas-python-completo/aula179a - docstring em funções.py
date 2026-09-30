# docstring em funções
"""
Para documentar uma função, podemos fazer de duas maneiras:
- Documentar os tipos de variáveis na assinatura da função;
- Documentar os tipos de variáveis no corpo da docstring, embaixo da descrição.
A descrição da função sempre fica na docstring dentro da função.
"""

import aula179b

texto = dir(aula179b)
print(texto)

texto = aula179b.__doc__
print(texto)

help(aula179b)
