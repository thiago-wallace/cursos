# copiar arquivos e criar pastas

import os
import shutil

# Receber o diretório home do usuário - equivalente ao "echo $HOME" no Linux
home = os.path.expanduser('~')
documentos = os.path.join(home, 'Documentos')
caminho_1 = os.path.join(documentos, 'Exemplo Python')
# criar a pasta nova. Se o exist_ok estiver False, o código apresenta erro ao tentar criar uma pasta já existente.
os.makedirs(caminho_1, exist_ok=True)
os.makedirs(os.path.join(caminho_1, 'a'), exist_ok=True)
os.makedirs(os.path.join(caminho_1, 'b'), exist_ok=True)
os.makedirs(os.path.join(caminho_1, 'a', 'aa'), exist_ok=True)
os.makedirs(os.path.join(caminho_1, 'a', 'ab'), exist_ok=True)
