# arquivos zip - descompactar arquivo zip
'''
ZipFile.extractall(a)
a - diretório para extrair o arquivo zip
'''

import os
from pathlib import Path
from zipfile import ZipFile

caminho_pasta = Path(__file__).parent / 'aula220_arquivos'
caminho_compactado = Path(caminho_pasta).parent / 'aula220_compactado.zip'
caminho_descompactado = Path(
    caminho_compactado).parent / caminho_compactado.stem

# Descompacta o arquivo zip
with ZipFile(caminho_compactado, 'r') as zip:
    zip.extractall(caminho_descompactado)

# Mostrar diretório descompactado
for root, pastas, arquivos in os.walk(caminho_descompactado):
    print(root)
    for p in pastas:
        print('\tPasta:', p)
    for a in arquivos:
        print('\tArquivo:', a)
