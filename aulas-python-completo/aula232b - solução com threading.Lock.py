# solução com threading.Lock
'''
Uma thread será criada dentro de um laço for, gerando 9 threas simultâneas.
Essas threads vão executar um método, que demorará pelo menos meio segundo para ser finalizado (devido ao sleep colocado).

Problema: ao executar esse código, todas as threas vão passar pelo if antes de os ingressos serem debitados do estoque, dando True,
    porém na hora de debitar, já não vai haver ingressos suficientes, gerando um bug de ingressos negativos.

Curso Aula 329 - https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/36391772#overview

Solução: Utilizando a classe Lock, após instancia-lo, é possível bloquear o início do método quando uma thread passa, para as demais
    threads ficarem esperando naquele ponto, até a primeira thread passar pelo ponto de desbloqueio e terminar a execução, e então,
    a próxima thread passar. Assim, só uma thread por vez poderá passar entre os pontos de bloqueio e desbloqueio. Como um quarto em
    que só uma pessoa de cada vez pode entrar e sair, e só depois que a primeira saiu, a próxima poderá entrar, formando uma fila. 
'''

from threading import Thread, Lock
from time import sleep


class Ingressos:
    def __init__(self, estoque: int) -> None:
        self.estoque = estoque
        # instanciando a classe Lock
        self.lock = Lock()

    def comprar(self, quantidade: int) -> None:
        # bloqueando o método, a partir desse ponto, só uma thread pode passar por vez, e as demais vão esperar aqui, formando uma fila.
        self.lock.acquire()
        if quantidade > self.estoque:
            print('Não possui ingressos suficientes para essa compra. Estoque: {}'.format(
                self.estoque))
            # desbloqueando o método, a partir desse ponto, a próxima thread na fila poderá passar pelo ponto de bloqueio acima.
            self.lock.release()
            return
        sleep(0.5)
        self.estoque -= quantidade
        print(
            f'Efetuada compra de {quantidade} ingresso(s). Estoque: {self.estoque}')
        # desbloqueando o método, a partir desse ponto, a próxima thread na fila poderá passar pelo ponto de bloqueio acima.
        self.lock.release()


ingressos = Ingressos(10)

for i in range(1, 10):
    thread = Thread(target=ingressos.comprar, args=(i,))
    thread.start()
