# threads 3
# Executando processamentos em paralelo
# https://docs.python.org/pt-br/3.15/library/threading.html

from threading import Thread
from time import sleep


def caminhos(nome, voltas):
    for i in range(voltas):
        print(f'{nome} - Volta {i}')
        sleep(1)


t = Thread(target=caminhos, args=('Caminho A', 10))
t.start()

caminhos('Caminho Principal', 10)
