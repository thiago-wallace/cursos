# arquivos zip - criar arquivos de exemplo

from pathlib import Path


def criar_arquivos(quantidade: int, diretorio: Path) -> None:
    for i in range(quantidade):
        dir_arquivo = diretorio / f'arquivo-{i}.txt'
        with open(dir_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(f'arquivo-{i}')


caminho_pasta = Path(__file__).parent / 'aula220_arquivos'
caminho_pasta.mkdir(exist_ok=True)
criar_arquivos(10, caminho_pasta)
caminho_subpasta = caminho_pasta / 'subpasta'
caminho_subpasta.mkdir(exist_ok=True)
criar_arquivos(4, caminho_subpasta)
