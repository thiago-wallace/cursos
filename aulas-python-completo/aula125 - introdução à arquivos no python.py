# introdução à arquivos no python
'''
Usamos a função open para abrir um arquivo em Python (ele pode ou não existir).

Modos:
r (leitura), w (escrita), x (para criação), a (escreve ao final), b (binário), t (modo texto), + (leitura e escrita)

Context manager - with (abre e fecha)

Métodos úteis:
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)

Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load
'''

# Exemplo caminho de arquivos - Linux, MAC e Windows:
'''
Obs: Como o Windows por padrão usa barra invertida entre diretórios, e o Python já usa a barra invertida para caractere de escape (Exemplo: \n, \"), então
    ao indicar caminho no Windows, deve-se utilizar barra dupla invertida.
'''
exemplo_linux = '/home/thiago/pasta/subpasta/arquivo.txt'
exemplo_mac = '/Users/thiago/pasta/subpasta/arquivo.txt'
exemplo_windows = 'C:\\Users\\thiago\\pasta\\subpasta\\arquivo.txt'
