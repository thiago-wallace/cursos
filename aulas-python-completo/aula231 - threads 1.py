# threads 1
# Executando processamentos em paralelo
# https://docs.python.org/pt-br/3.15/library/threading.html

from time import sleep
from threading import Thread

# Criando uma classe que herda da classe Thread


class MinhaThread(Thread):
    def __init__(self, texto: str, tempo: int) -> None:
        self.texto = texto
        self.tempo = tempo
        # executando o __init__ da classe pai
        super().__init__()

    # método que será executado no run() e no start(), sobrescrevendo o método run() da classe pai
    def run(self):
        for i in range(self.tempo):
            print(f'{self.texto} - Volta {i}')
            sleep(1)


thread1 = MinhaThread('Thread A', 20)
thread2 = MinhaThread('Thread B', 20)
thread3 = MinhaThread('Thread C', 20)

thread1.start()
thread2.start()
thread3.start()

for i in range(20):
    print('Thread Main - Volta', i)
    sleep(1)
