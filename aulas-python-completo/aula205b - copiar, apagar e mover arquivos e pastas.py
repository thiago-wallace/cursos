# copiar, apagar e mover arquivos e pastas 2 - mover
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

# Configurar caminhos
caminho_2 = os.path.join('aula204 - documentos')
caminho_3 = os.path.join('aula205 - documentos')

# Verificar se a pasta já não existe
if os.path.exists(caminho_2) and not os.path.exists(caminho_3):
    # Mover pasta recursivamente
    shutil.move(caminho_2, caminho_3)
    print('Alteração efetuada')
