# criando arquivos e context manager
'''
Usamos a função open para abrir um arquivo em Python (ele pode ou não existir).

Modos:
r (leitura), w (escrita), x (para criação), a (escreve ao final), b (binário), t (modo texto), + (leitura e escrita)

Context manager - with (abre e fecha) - o arquivo é aberto no início do with, e é fechado automaticamente no final do with.
'''

caminho_arquivo_1 = 'teste1.txt'
arquivo1 = open(caminho_arquivo_1, 'w')
print('Arquivo 1 aberto')
arquivo1.close()

# Utilizando o Context manager - with

caminho_arquivo_2 = 'teste2.txt'
with open(caminho_arquivo_2, 'w') as arquivo2:
    print('Arquivo 2 aberto')
