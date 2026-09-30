# leitura e escrita de arquivos
'''
Métodos úteis:
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)
'''

caminho_arquivo = 'teste.txt'
with open(caminho_arquivo, 'w+') as arquivo:
    # Usando write
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    # Usando writelines - requer um iterável (lista, tupla, etc.)
    arquivo.writelines(['linha 3\n', 'linha 4\n'])
    # Movendo o cursor para o início do arquivos, antes da leitura
    arquivo.seek(0, 0)
    # Usando read - retorna string
    texto = arquivo.read()
    print(texto)
    # Usando readline - retorna uma linha por vez (semelhante ao next)
    arquivo.seek(0, 0)
    # strip() utilizado para remover espaços e quebras de linha de uma string
    texto = arquivo.readline().strip()
    print(texto)
    texto = arquivo.readline().strip()
    print(texto)
    # Usando readlines - retorna uma lista
    arquivo.seek(0, 0)
    texto = arquivo.readlines()
    print(texto)
