# evitando uso de condicionais - guard clause
# com base no código do exercício 133

import os
import sys


def listar(lista):
    print('TAREFAS:')
    for item in lista:
        print(item)


def desfazer_refazer(lista_a_retirar, lista_a_receber):
    if not lista_a_retirar:
        print('Nada a fazer\n')
    else:
        lista_a_receber.append(lista_a_retirar.pop())
    listar(tarefas)


def adicionar(tarefa, lista):
    if tarefa.strip():
        lista.append(tarefa)
    else:
        print('Você não digitou nada\n')
    listar(lista)


tarefas = []
desfeitas = []

print()
while True:
    print('Comandos: listar, desfazer, refazer, sair')
    entrada = input('Digite uma tafera ou comando: ')
    print()
    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer_refazer(tarefas, desfeitas),
        'refazer': lambda: desfazer_refazer(desfeitas, tarefas),
        'sair': lambda: sys.exit()
    }
    comando = comandos.get(entrada)
    comando() if comando is not None else adicionar(entrada, tarefas)
    print()
