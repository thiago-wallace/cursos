# Exercício sistema bancário - solução 1

from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: Conta):
        super().__init__(nome, idade)
        self.conta = conta

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta: Conta):
        self._conta = conta


class Conta(ABC):
    def __init__(self, agencia: int, numero: int):
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0.0

    def depositar(self, valor_depositar: float):
        self.saldo += valor_depositar
        print(f'Depósito de {valor_depositar} efetuado com sucesso')

    @abstractmethod
    def sacar(self, valor_sacar: float, banco: Banco,
              cliente: str, agencia: int, conta: int): ...


class ContaCorrente(Conta):
    def sacar(self, valor_sacar: float, banco: Banco, cliente: str, agencia: int, conta: int):
        if not banco.autenticacao(cliente, agencia, conta):
            print('Falha na autenticação')
            return
        if valor_sacar <= self.saldo + 1000.00:
            self.saldo -= valor_sacar
            print(f'Saque de {valor_sacar} efetuado com sucesso')
            return
        print('Valor insuficiente')


class ContaPoupanca(Conta):
    def sacar(self, valor_sacar: float, banco: Banco, cliente: str, agencia: int, conta: int):
        if not banco.autenticacao(cliente, agencia, conta):
            print('Falha na autenticação')
            return
        if valor_sacar <= self.saldo:
            self.saldo -= valor_sacar
            print(f'Saque de {valor_sacar} efetuado com sucesso')
            return
        print('Valor insuficiente')


class Banco:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.conta = self.cliente.conta

    def autenticacao(self, cliente: str, agencia: int, conta: int):
        auth_cliente = cliente == self.cliente.nome
        auth_agencia = agencia == self.conta.agencia
        auth_conta = conta == self.conta.numero
        if auth_cliente and auth_agencia and auth_conta:
            return True
        return False


cc1 = ContaCorrente(1, 1)
p1 = Cliente('Thiago', 26, cc1)
b1 = Banco(p1)

print(b1.cliente.__dict__, b1.conta.__dict__)
cc1.depositar(500)
print(b1.cliente.__dict__, b1.conta.__dict__)
cc1.sacar(1700, b1, 'Thiago', 1, 1)
print(b1.cliente.__dict__, b1.conta.__dict__)
