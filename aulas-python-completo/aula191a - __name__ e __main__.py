# __name__ e __main__
# arquivo A
'''
Utilizando if __name__ == '__main__'
Ao executar este arquivo A, este arquivo passará a ser o __main__.
Ao executar o arquivo B, ele passará a ser o __main__.
Quando colocamos if __name__ == '__main__' no arquivo B, e importamos o B no arquivo A,
    o conteúdo desse if só será executado se o arquivo executado for o arquivo B.
'''

from aula191b import somar

print(somar(10, 20))
