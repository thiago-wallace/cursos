from pathlib import Path
from shutil import rmtree

PASTA_EXCEL = Path(__file__).parent / 'aula236'

if PASTA_EXCEL.exists():
    rmtree(PASTA_EXCEL)
