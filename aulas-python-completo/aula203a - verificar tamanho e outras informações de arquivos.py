# verificar tamanho e outras informações de arquivos

'''
os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
os.path.get e os.stat - podem ser usado para verificar outras informações de arquivos 
'''

import os
from aula203b_formatar_tamanho import formata_tamanho

caminho = os.path.join('/home', 'Thiago', 'Documentos')
for diretorio, pastas, arquivos in os.walk(caminho):
    print(diretorio)
    for pasta in pastas:
        print(f'\tPasta: {pasta}')
    for arquivo in arquivos:
        dir_arquivo = os.path.join(diretorio, arquivo)
        # forma 1 de verificar o tamanho
        tamanho_bytes = os.path.getsize(dir_arquivo)
        # forma 2 de verificar o tamanho
        tamanho_bytes = os.stat(dir_arquivo).st_size
        # formatar tamanho
        tamanho = formata_tamanho(tamanho_bytes)
        print(f'\tArquivo: {arquivo} - Tamanho: {tamanho}')
