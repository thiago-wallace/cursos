# dir, help e docstring de uma linha
'''
dir() - Retorna os objetos (variáveis, funções, etc.) que um módulo possui
help() - Mostra uma documentação de um módulo

As DocStrings podem entrar na documentação do módulo, no caso desse exemplo, a DocString no início do módulo.
'''

import aula177b

texto = dir(aula177b)
print(texto)

texto = aula177b.__doc__
print(texto)

help(aula177b)

