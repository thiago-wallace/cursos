# threads
# Executando processamentos em paralelo

from time import sleep
from threading import Thread


class MinhaThread(Thread):
    def __init__(self, texto: str, tempo: int) -> None:
        self.texto = texto
        self.tempo = tempo
        super().__init__()

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
