# classes abstratas - Abstract Base Class (abc)
'''
ABCs são usadas como contratos para a definição de novas classes. Elas podem forçar outras classes a criarem métodos concretos. Também podem ter métodos
    concretos por elas mesmas.
@abstractmethods são métodos que não têm corpo.
As regras para classes abstratas com métodos abstratos é que elas NÃO PODEM ser instânciadas diretamente.
Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod).
Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.
É possível criar @property @setter @classmethod @staticmethod e @method como abstratos, para isso use @abstractmethod como decorator mais interno.

Em resumo, requisitos para se criar uma classe abstrata:
- A classe abstrata deve herdar da super classe 'ABC', a classe 'ABC' deverá ser importada do módulo 'abc'.
- O método abstrato deve ser decorado com o @abstractmethod, o 'abstractmethod' deverá ser importada do módulo 'abc'.
Obs: Uma classe só é considerada abstrata se tiver pelo menos um método abstrato.
'''

from pathlib import Path
from abc import ABC, abstractmethod

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log(ABC):
    # Classe abstrata criada com os recursos do Python
    @classmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        with open(LOG_FILE, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{msg} ({self.__class__.__name__})')
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


lp = LogPrintMixin()
lp.log_error('Qualquer erro')
lp.log_success('Deu certo')

lf = LogFileMixin()
lf.log_error('Qualquer erro')
lf.log_success('Deu certo')
