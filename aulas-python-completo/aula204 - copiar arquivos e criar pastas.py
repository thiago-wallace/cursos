# copiar arquivos e criar pastas
'''
os + shutil - Copiando arquivos com Python
Vamos copiar arquivos de uma pasta para outra.
Copiar -> shutil.copy
'''

import os
import shutil
from datetime import datetime

# Receber o diretório home do usuário - equivalente ao "echo $HOME" no Linux
home = os.path.expanduser('~')

# Configurar caminhos
caminho_1 = os.path.join(home, 'Documentos', 'Exemplo Python')
caminho_1a = os.path.join(caminho_1, 'a')
caminho_1b = os.path.join(caminho_1, 'b')
caminho_1aa = os.path.join(caminho_1a, 'aa')
caminho_1ab = os.path.join(caminho_1a, 'ab')
caminho_2 = os.path.join('aula204 - documentos', 'Exemplo Python')

# criar a pasta nova. Se o exist_ok estiver False, o código apresenta erro ao tentar criar uma pasta já existente.
os.makedirs(caminho_1, exist_ok=True)
os.makedirs(caminho_1a, exist_ok=True)
os.makedirs(caminho_1b, exist_ok=True)
os.makedirs(caminho_1aa, exist_ok=True)
os.makedirs(caminho_1ab, exist_ok=True)
os.makedirs(caminho_2, exist_ok=True)

# criar arquivos como exemplo
with open(os.path.join(caminho_1, 'ex1.txt'), 'w', encoding='utf-8') as arquivo:
    arquivo.write('teste\n' + str(datetime.now()))
with open(os.path.join(caminho_1a, 'a1.txt'), 'w', encoding='utf-8') as arquivo:
    arquivo.write('teste a\n' + str(datetime.now()))
with open(os.path.join(caminho_1b, 'b1.txt'), 'w', encoding='utf-8') as arquivo:
    arquivo.write('teste b\n' + str(datetime.now()))
with open(os.path.join(caminho_1aa, 'aa1.txt'), 'w', encoding='utf-8') as arquivo:
    arquivo.write('teste aa\n' + str(datetime.now()))
with open(os.path.join(caminho_1ab, 'ab1.txt'), 'w', encoding='utf-8') as arquivo:
    arquivo.write('teste ab\n' + str(datetime.now()))

# copiar arquivos e pastas
for root, pastas, arquivos in os.walk(caminho_1):
    print(root)
    for pasta in pastas:
        print('\tPasta: ' + pasta)
        # criar novas pastas para receber as cópias
        nova_pasta = os.path.join(root.replace(caminho_1, caminho_2), pasta)
        os.makedirs(nova_pasta, exist_ok=True)
    for arquivo in arquivos:
        print('\tArquivo: ' + arquivo)
        dir_arquivo = os.path.join(root, arquivo)
        novo_arquivo = os.path.join(
            root.replace(caminho_1, caminho_2), arquivo)
        # copiar arquivos
        shutil.copy(dir_arquivo, novo_arquivo)
