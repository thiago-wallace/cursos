# copiar, apagar e mover arquivos e pastas 3 - apagar
'''
os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
Vamos copiar arquivos de uma pasta para outra.
Copiar -> shutil.copy
Copiar Árvore recursivamente -> shutil.copytree
Apagar Árvore recursivamente -> shutil.rmtree
Apagar arquivos -> os.unlink
Renomear/Mover -> shutil.move ou os.rename
'''

import os
import shutil

# Receber o diretório home do usuário - equivalente ao "echo $HOME" no Linux
home = os.path.expanduser('~')

# Configurar caminhos
caminho_1 = os.path.join(home, 'Documentos', 'Exemplo Python')
caminho_2 = os.path.join('aula204 - documentos')
caminho_3 = os.path.join('aula205 - documentos')

# Perguntar qual caminho deverá ser excluído
print('Quais diretórios deseja excluir?')
print('1 - /home/Thiago/Documentos/Exemplo Python')
print('2 - aula204 - documentos')
print('3 - aula205 - documentos')
entrada = input('> ')

# Excluir caminhos selecionados, verificando antes, se o caminho realmente existe
if '1' in entrada:
    if os.path.exists(caminho_1):
        shutil.rmtree(caminho_1)
        print('Diretório 1 excluído')
    else:
        print('Diretório 1 não encontrado')
if '2' in entrada:
    if os.path.exists(caminho_2):
        shutil.rmtree(caminho_2)
        print('Diretório 2 excluído')
    else:
        print('Diretório 2 não encontrado')
if '3' in entrada:
    if os.path.exists(caminho_3):
        shutil.rmtree(caminho_3)
        print('Diretório 3 excluído')
    else:
        print('Diretório 3 não encontrado')
