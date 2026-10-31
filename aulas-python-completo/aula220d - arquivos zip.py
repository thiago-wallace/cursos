# arquivos zip - apagar os arquivos da aula

from pathlib import Path
from shutil import rmtree

caminho_pasta = Path(__file__).parent / 'aula220_arquivos'
caminho_compactado = Path(caminho_pasta).parent / 'aula220_compactado.zip'
caminho_descompactado = Path(
    caminho_compactado).parent / caminho_compactado.stem

print('Quais pastas/arquivos deseja apagar?')
print('(1) Pasta aula220_arquivos')
print('(2) Arquivo zip aula220_compactado.zip')
print('(3) Pasta aula220_compactado')
entrada = input('Digite os números que deseja apagar: ')

if '1' in entrada:
    rmtree(caminho_pasta, ignore_errors=True)
if '2' in entrada:
    caminho_compactado.unlink(missing_ok=True)
if '3' in entrada:
    rmtree(caminho_descompactado, ignore_errors=True)
