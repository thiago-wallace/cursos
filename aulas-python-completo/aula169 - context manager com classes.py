# context manager com classes

'''
Context Manager com classes - Criando e Usando gerenciadores de contexto.
Você pode implementar seus próprios protocolos apenas implementando os dunder methods que o Python vai usar.
Isso é chamado de Duck typing. Um conceito relacionado com tipagem dinâmica onde o Python não está interessado no tipo, mas se alguns métodos existem
    no seu objeto para que ele funcione de forma adequada.

Duck Typing:
Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de pato.

Para criar um context manager, os métodos __enter__ e __exit__ devem ser implementados.
O método __exit__ receberá a classe de exceção, a exceção e o traceback. Se ele retornar True, exceção no with será suprimidas.
'''


class Abertura:
    def __init__(self, caminho, modo):
        print('Estou no init')
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Estou no enter')
        self._arquivo = open(self.caminho, self.modo, encoding='UTF-8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Estou no exit')
        self._arquivo.close()
        print(class_exception)
        print(exception_)
        print(traceback_)
        return True


a = Abertura('arquivo.txt', 'w')

with a as arquivo:
    print('Estou no with')
    print(arquivo)
    arquivo.write('L1\n')
    arquivo.write('L2\n')
    arquivo.write('L3\n')
