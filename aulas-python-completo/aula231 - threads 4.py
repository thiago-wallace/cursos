# threads 4
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

# enquanto a thread t estiver rodando, ela se juntará à thread principal, causando "congelamento" do app
t.join()
# como a thread t se juntou a thread principal, a função da thread t continuará sendo executado na thread principal
# ou seja, a partir desse ponto, só será executado quando a função acabar
print('Thread finalizada!')
