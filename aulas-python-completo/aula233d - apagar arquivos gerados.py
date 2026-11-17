# apagar arquivos gerados nas aulas a, b e c

from pathlib import Path
from shutil import rmtree

PASTA_NOVOS_ARQUIVOS = Path(__file__).parent / 'aula233' / 'novos_arquivos'

if PASTA_NOVOS_ARQUIVOS.exists():
    rmtree(PASTA_NOVOS_ARQUIVOS)
