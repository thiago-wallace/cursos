from log import LogFileMixin, LogPrintMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


class Smartphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()
        if self._ligado:
            self.log_success(f'{self._nome} ligado com sucesso')
        else:
            self.log_error(f'Erro ao ligar {self._nome}')

    def desligar(self):
        super().desligar()
        if not self._ligado:
            self.log_success(f'{self._nome} desligado com sucesso')
        else:
            self.log_error(f'Erro ao desligar {self._nome}')
