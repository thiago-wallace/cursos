# exercício - lista de tarefas com desfazer e refazer

tarefas = []
desfeitas = []

print()
while True:
    print('Comandos: listar, desfazer, refazer, sair')
    entrada = input('Digite uma tafera ou comando: ')
    print()
    if entrada == 'desfazer':
        if not tarefas:
            print('Nada a desfazer\n')
        else:
            desfeitas.append(tarefas.pop())
    elif entrada == 'refazer':
        if not desfeitas:
            print('Nada a refazer\n')
        else:
            tarefas.append(desfeitas.pop())
    elif entrada == 'sair':
        break
    elif entrada != 'listar':
        if entrada.strip():
            tarefas.append(entrada)
        else:
            print('Você não digitou nada\n')
    print('TAREFAS:')
    for item in tarefas:
        print(item)
    print()
