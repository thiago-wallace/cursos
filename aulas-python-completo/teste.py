from threading import Thread
from time import sleep


def caminho_a():
    for i in range(10):
        print(f'Caminho A - {i}')
        sleep(1)


def caminho_b(voltas):
    for i in range(voltas):
        print(f'Caminho B - {i}')
        sleep(1)


def caminhos(nome, voltas):
    for i in range(voltas):
        print(f'{nome} - {i}')
        sleep(1)


t1 = Thread(target=caminho_a)
t2 = Thread(target=caminho_b, args=(10,))
t3 = Thread(target=caminhos, args=('Caminho C', 10))
t4 = Thread(target=caminhos, args=('Caminho D', 10))

t1.start()
t2.start()
t3.start()
t4.start()

for i in range(10):
    print(f'Caminho Principal - {i}')
    sleep(1)
