# criando Exceptions por classe
'''
Para criar uma Exception em Python, você só precisa herdar de alguma exceção da linguagem.
A recomendação da doc é herdar de Exception.
https://docs.python.org/3/library/exceptions.html
Criando exceções (comum colocar Error ao final)
Levantando (raise) / Lançando (throw) exceções
Relançando exceções
Adicionando notas em exceções (3.11.0)
'''


class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def lancando():
    excecao = MeuError('Ocorreu o meu erro')
    excecao.add_note('Nota 1 do MeuError')
    excecao.add_note('Nota 2 do MeuError')
    raise excecao


try:
    lancando()
except MeuError as e:
    print(e)
    print(e.__class__.__name__)
    excecao = OutroError('Ocorreu outro erro')
    excecao.__notes__ = e.__notes__.copy()
    excecao.add_note('Nota 1 do OutroError')
    raise excecao from e
