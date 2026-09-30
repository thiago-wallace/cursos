# Abstração

from pathlib import Path
import os

LOG_FILE = Path(__file__).parent / 'log.txt'
LOG_FILE_2 = os.path.join(os.path.dirname(__file__), 'log.txt')


class Log:
    # Classe abstrata criada "manualmente"
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

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


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer erro')
    lp.log_success('Deu certo')

    lf = LogFileMixin()
    lf.log_error('Qualquer erro')
    lf.log_success('Deu certo')

    print(LOG_FILE)
    print(LOG_FILE_2)
