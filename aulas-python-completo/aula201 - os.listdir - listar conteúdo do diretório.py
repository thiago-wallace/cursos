# os.listdir - listar conteúdo do diretório

'''
os.listdir - retorna uma lista com o nome dos arquivos e pastas daquele diretório.
Obs: Ele não possui recursão (Não acessa sub pastas).

os.path.isdir - verifica se um caminho é um diretório (pasta), retornando bool.
'''

import os

caminho = os.path.join('/home', 'Thiago', 'Documentos')
print(os.listdir(caminho))
for item in os.listdir(caminho):
    caminho2 = os.path.join(caminho, item)
    if not os.path.isdir(caminho2):
        continue
    print(item)
    for item2 in os.listdir(caminho2):
        print(f'\t{item2}')
