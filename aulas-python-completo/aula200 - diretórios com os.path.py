# diretórios com os.path

# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path

# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.

# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.

# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').

# os.path.exists: verifica se um caminho especificado existe.

# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.


import os

# Juntar pastas/arquivos em um caminho
caminho = os.path.join('User', 'Documents', 'File.txt')
print(caminho)

# Dividir o diretório e o arquivo
dir_arquivo = os.path.split(caminho)
print(dir_arquivo)

# Verifica se o caminho existe, retornando bool
print(os.path.exists(caminho))
print(os.path.exists('aula160/log.py'))

# Dividir o diretório/arquivo e a extensão
dir_arquivo = os.path.splitext(caminho)
print(dir_arquivo)

# Com base no diretório atual, junta o diretório acima com o diretório passado no parâmetro
print(os.path.abspath(caminho))

# Recebe o nome do arquivo, sem o diretório (Ou a última pasta do diretório)
print(os.path.basename(caminho))

# Recebe o diretório do arquivo, mas sem o nome do arquivo
print(os.path.dirname(caminho))
