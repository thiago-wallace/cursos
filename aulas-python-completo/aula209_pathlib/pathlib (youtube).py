# pathlib (youtube)
# Link YouTube: https://www.youtube.com/watch?v=T17BTNKBeJY

from pathlib import Path

# cria uma variável do tipo Path com o diretório do projeto atual do vscode
caminho_projeto = Path()
print('1 -', caminho_projeto)
# mostra o caminho absoluto, ou seja, o caminho desde a raiz até este diretório
print('2 -', caminho_projeto.absolute())
# cria uma variável do tipo Path com o diretório do arquivo atual (Arquivo .py), incluindo o arquivo
caminho_arquivo = Path(__file__)
print('3 -', caminho_arquivo)
# mostra um nível acima, ou seja, mostra o diretório do arquivo atual (Arquivo .py), mas sem incluir o arquivo
print('4 -', caminho_arquivo.parent)
# mostra dois níveis acima, ou seja, o diretório pai do diretório atual
print('5 -', caminho_arquivo.parent.parent)
# mostra três níveis acima
print('6 -', caminho_arquivo.parent.parent.parent)
# criar uma pasta no diretório
ideias = caminho_arquivo.parent / 'ideias'
print('7 -', ideias)
# mostrar um arquivo dentro dessa pasta
print('8 -', ideias / 'arquivo.txt')
# verificar a home do usuário
print('9 -', Path.home())
# acessar a pasta Desktop na home do usuário
print('10 -', Path.home() / 'Desktop')
# salvar um arquivo
arquivo_txt = Path(__file__).parent / 'arquivo.txt'
arquivo_txt.touch()
print('11 -', arquivo_txt)
# escrever no arquivo e ler esse arquivo - forma 1
arquivo_txt.write_text('Olá mundo')
print(arquivo_txt.read_text())
# escrever no arquivo e ler esse arquivo - forma 2
with arquivo_txt.open('w', encoding='utf-8') as file:
    file.write('Uma linha\n')
    file.write('Outra linha')
with arquivo_txt.open('r') as file:
    print(file.read())
# apagar o arquivo
entrada = input('Deseja apagar o arquivo? (s/N): ').lower().startswith('s')
if entrada:
    arquivo_txt.unlink()

# criar e salvar uma pasta
pasta = Path(__file__).parent / 'Informações e módulos'
pasta.mkdir(exist_ok=True)
print('12 -', pasta)
# criar e salvar uma subpasta
subpasta = pasta / 'Módulo'
subpasta.mkdir(exist_ok=True)
print('13 -', subpasta)
# salvar um arquivo dentro da subpasta
arquivo_subpasta = subpasta / 'arquivo do arquivo.txt'
arquivo_subpasta.touch()
print('14 -', arquivo_subpasta)
arquivo_subpasta.write_text('Hey')
print(arquivo_subpasta.read_text())

# criar uma nova pasta e salvar 10 arquivos dentro
caminho_pasta_file = pasta / 'Files'
print('15 -', caminho_pasta_file)
caminho_pasta_file.mkdir(exist_ok=True)
for i in range(10):
    f = caminho_pasta_file / f'File {i+1}'
    f.touch()
    f.write_text(f'Arquivo Teste {i+1}')


# apagar pasta recursivamente (sem utilizar shutil)
def apagar_pasta(root: Path) -> None:
    # glob - lista arquivos e pastas de um diretório, filtrando de acordo com o parâmetro.
    # Ex1: glob('*') - lista todos os arquivos e pastas.
    # Ex2: glob('**') - lista todos os arquivos e pastas de forma recursiva.
    # Ex3: rglob('*') - lista todos os arquivos e pastas de forma recursiva também.
    # Ex4: glob('*.txt') - lista os arquivos com formato txt.
    # Ex5: rglob('*.py') - lista os arquivos com formato py de forma recursiva.
    teste = root.glob('*')
    for item in teste:
        if item.is_dir():
            apagar_pasta(item)
        else:
            item.unlink()
    root.rmdir()


entrada = input(
    'Deseja apagar a pasta e seu conteúdo? (s/N): ').lower().startswith('s')
if entrada:
    apagar_pasta(pasta)
