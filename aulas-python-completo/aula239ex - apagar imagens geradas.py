from pathlib import Path

PASTA_IMAGENS = Path(__file__).parent / 'aula239'
IMAGEM_NOVA_2 = PASTA_IMAGENS / 'nova 2.jpg'
IMAGEM_NOVA_3 = PASTA_IMAGENS / 'nova 3.jpg'
IMAGEM_NOVA_4 = PASTA_IMAGENS / 'nova 4.jpg'

IMAGEM_NOVA_2.unlink(missing_ok=True)
IMAGEM_NOVA_3.unlink(missing_ok=True)
IMAGEM_NOVA_4.unlink(missing_ok=True)
