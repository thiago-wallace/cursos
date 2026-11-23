# editar imagem com pillow
'''
Pillow: redimensionando imagens com Python
Essa biblioteca é o Photoshop do Python 😂
https://pypi.org/project/pillow/
https://pillow.readthedocs.io/en/stable/
'''

from PIL import Image
from pathlib import Path

PASTA_IMAGENS = Path(__file__).parent / 'aula239'
IMAGEM_ORIGINAL = PASTA_IMAGENS / 'original.jpg'
IMAGEM_NOVA_2 = PASTA_IMAGENS / 'nova 2.jpg'
IMAGEM_NOVA_3 = PASTA_IMAGENS / 'nova 3.jpg'
IMAGEM_NOVA_4 = PASTA_IMAGENS / 'nova 4.jpg'

# abrindo foto original
foto1 = Image.open(IMAGEM_ORIGINAL)
# coletando o tamanho da foto original
largura, altura = foto1.size
print(f'Original: {largura} x {altura}')
# coletando informações sobre a foto (Como localização, ou o modelo da câmera/celular, caso tenha na foto)
exif = foto1.info['exif']

# configurando o tamanho da foto nova, mantendo a proporção - Forma 1
nova_largura = 1024
nova_altura = round(altura * nova_largura / largura)
print(f'Nova foto 2: {nova_largura} x {nova_altura}')
foto2 = foto1.resize((nova_largura, nova_altura))

# configurando o tamanho da foto nova, mantendo a proporção - Forma 2
nova_largura = round(largura / 4)
nova_altura = round(altura / 4)
print(f'Nova foto 3: {nova_largura} x {nova_altura}')
foto3 = foto1.resize((nova_largura, nova_altura))

# salvando a nova foto
foto2.save(IMAGEM_NOVA_2)
# salvando a nova foto, com as informações coletadas (caso tenha informações)
foto3.save(IMAGEM_NOVA_3, exif=exif)
# salvando a nova foto, otimizando a foto (reduzindo a qualidade e mantendo o tamanho)
foto1.save(IMAGEM_NOVA_4, optimize=True, quality=70)
