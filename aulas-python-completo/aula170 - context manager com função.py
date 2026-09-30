# context manager com função

from contextlib import contextmanager


@contextmanager
def abertura(caminho, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho, modo, encoding='UTF-8')
        yield arquivo
    except Exception as e:
        print('Ocorreu o erro:')
        print(e.__class__.__name__)
        print(e)
    finally:
        print('Fechando arquivo')
        arquivo.close()


a = abertura('arquivo.txt', 'w')

with a as arquivo:
    print(arquivo)
    arquivo.write('L1\n')
    arquivo.write('L2\n')
    arquivo.write('L3\n')
    arquivo.write('L4\n')
    arquivo.write('L5\n', 'aaaa')
