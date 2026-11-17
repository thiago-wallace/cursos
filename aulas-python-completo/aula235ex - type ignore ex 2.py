# type: ignore

'''
O comentário "# type: ignore" é utilizado para fazer o vscode ignorar erros de tipagem (quando o typeCheckingMode do vscode está ligado).

Ao colocar o comentário no final de uma linha, o vscode vai ignorar qualquer erro de tipagem naquela linha.

Ao colocar o comentário na primeira linha do arquivo .py, o vscode vai ignorar qualquer erro de tipagem em todo o código do arquivo.

Exemplo: a variável x vai receber o valor 0, porém estará tipada como bool.
'''

x: str = 0
print(x)
