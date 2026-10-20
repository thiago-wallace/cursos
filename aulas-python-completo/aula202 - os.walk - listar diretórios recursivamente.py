# os.walk - listar diretórios recursivamente
'''
os.walk para navegar de caminhos de forma recursiva
os.walk é uma função que permite percorrer uma estrutura de diretórios de
maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
e uma lista dos arquivos do diretório atual (files).
'''

import os

caminho = os.path.join('/home', 'Thiago', 'Documentos')
print(os.walk(caminho))
for c in os.walk(caminho):
    print(c)
print()
for diretorio, pastas, arquivos in os.walk(caminho):
    print(diretorio)
    for pasta in pastas:
        print(f'\tPasta: {pasta}')
    for arquivo in arquivos:
        print(f'\tArquivo: {arquivo}')
