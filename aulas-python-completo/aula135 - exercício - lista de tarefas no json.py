# exercício - lista de tarefas no json

import sys
import json


def listar(lista):
    print('TAREFAS:')
    for item in lista:
        print(item)


def desfazer_refazer(lista_a_retirar, lista_a_receber):
    if not lista_a_retirar:
        print('Nada a fazer\n')
    else:
        lista_a_receber.append(lista_a_retirar.pop())
        salvar(tarefas, nome_arquivo)
    listar(tarefas)


def adicionar(tarefa, lista):
    if tarefa.strip():
        lista.append(tarefa)
        salvar(tarefas, nome_arquivo)
    else:
        print('Você não digitou nada\n')
    listar(lista)


def carregar(arquivo):
    try:
        with open(arquivo, 'r') as file:
            lista = json.load(file)
    except FileNotFoundError:
        lista = []
    return lista


def salvar(lista, arquivo):
    with open(arquivo, 'w') as file:
        json.dump(lista, file, indent=2, ensure_ascii=False)


nome_arquivo = 'lista.json'
tarefas = carregar(nome_arquivo)
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
