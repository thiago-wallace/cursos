# arquivos zip - compactar arquivos em um arquivo zip
'''
ZipFile.write(a, b)
a - diretório do arquivo a ser compactado
b - diretório que o arquvo ficará dentro do zip
'''

import os
from pathlib import Path
from zipfile import ZipFile

caminho_pasta = Path(__file__).parent / 'aula220_arquivos'
caminho_compactado = Path(caminho_pasta).parent / 'aula220_compactado.zip'

# compacta os arquivos em um arquivo zip
with ZipFile(caminho_compactado, 'w') as zip:
    for root, pastas, arquivos in os.walk(caminho_pasta):
        for arquivo in arquivos:
            dir_arquivo = Path(root) / arquivo
            zip_arquivo = str(dir_arquivo).replace(str(caminho_pasta), '')
            zip.write(dir_arquivo, zip_arquivo)

# mostra o nome dos arquivos dentro do zip
with ZipFile(caminho_compactado, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
