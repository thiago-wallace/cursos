# Exercício sistema bancário - solução 2

import contas
import pessoas
import banco

c1 = pessoas.Cliente('João Pessoa', 26)
cc1 = contas.ContaCorrente(111, 222, 0, 100)
c1.conta = cc1
c2 = pessoas.Cliente('Maria Helena', 33)
cp1 = contas.ContaPoupanca(111, 223, 0)
c2.conta = cp1
b1 = banco.Banco()
b1.clientes.extend([c1, c2])
b1.contas.extend([cc1, cp1])
b1.agencias.extend([cc1.agencia, cp1.agencia])
print(c1)
print(c1.conta)
print(c2)
print(c2.conta)
print(b1)

if b1.autenticar(c1, cc1):
    cc1.depositar(10)
    c1.conta.depositar(10)
    print(c1.conta)
