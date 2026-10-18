# módulo os
'''
O módulo os para interação com o sistema
Doc: https://docs.python.org/3/library/os.html
O módulo `os` fornece funcionalidades para interagir com o sistema operacional.
Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
diretório. O método os.system() permite executar comandos do sistema
operacional a partir do seu código Python.

Exemplo de comando para limpar a tela do terminal:
Windows 11 (PowerShell), Linux, Mac = clear
Windows (antigo, cmd) = cls
'''

import os

os.system('clear')
os.system('echo Hello World')
os.system('pwd')

print('a' * 80)
print('a' * 80)
print('a' * 80)
