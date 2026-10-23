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
    file.write('Outra linha\n')
with arquivo_txt.open('r') as file:
    print(file.read())
# apagar o arquivo
entrada = input('Deseja apagar o arquivo? (s/N): ').lower().startswith('s')
if entrada:
    arquivo_txt.unlink()
