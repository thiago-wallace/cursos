# threads 3
# Executando processamentos em paralelo
# https://docs.python.org/pt-br/3.15/library/threading.html

from threading import Thread
from time import sleep


def caminhos(nome, voltas, tempo):
    for i in range(voltas):
        print(f'{nome} - Volta {i}')
        sleep(tempo)


t = Thread(target=caminhos, args=('Caminho A', 6, 10))
t.start()

# enquanto a thread t estiver rodando, a thread principal rodará este while, sem "congelar" o app
while t.is_alive():
    print('Thread em andamento...')
    sleep(3)
print('Thread finalizada!')
