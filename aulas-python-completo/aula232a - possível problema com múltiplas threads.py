# possível problema com múltiplas threads
'''
Uma thread será criada dentro de um laço for, gerando 9 threas simultâneas.
Essas threads vão executar um método, que demorará pelo menos meio segundo para ser finalizado (devido ao sleep colocado).

Problema: ao executar esse código, todas as threas vão passar pelo if antes de os ingressos serem debitados do estoque, dando True,
    porém na hora de debitar, já não vai haver ingressos suficientes, gerando um bug de ingressos negativos.

Curso Aula 329 - https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/36391772#overview


'''

from threading import Thread
from time import sleep


class Ingressos:
    def __init__(self, estoque: int) -> None:
        self.estoque = estoque

    def comprar(self, quantidade: int) -> None:
        if quantidade > self.estoque:
            print('Não possui ingressos suficientes para essa compra. Estoque: {}'.format(
                self.estoque))
            return
        sleep(0.5)
        self.estoque -= quantidade
        print(
            f'Efetuada compra de {quantidade} ingresso(s). Estoque: {self.estoque}')


ingressos = Ingressos(10)

for i in range(1, 10):
    thread = Thread(target=ingressos.comprar, args=(i,))
    thread.start()
