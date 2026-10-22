# copiar, apagar e mover arquivos e pastas 1 - copiar
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
caminho_2 = os.path.join('aula204 - documentos', 'Exemplo Python')

# Verificar se a pasta já não existe
if os.path.exists(caminho_1) and not os.path.exists(caminho_2):
    # Copiar pastas recursivamente (com arquivos e subpastas)
    shutil.copytree(caminho_1, caminho_2)
    print('Cópia efetuada')
