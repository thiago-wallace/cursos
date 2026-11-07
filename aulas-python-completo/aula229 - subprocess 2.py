# subprocess 2
'''
Usando subprocess para executar e comandos externos
subprocess é um módulo do Python para executar
processos e comandos externos no seu programa.
O método mais simples para atingir o objetivo é usando subprocess.run().
Argumentos principais de subprocess.run():
- stdout, stdin e stderr -> Redirecionam saída, entrada e erros
- capture_output -> captura a saída e erro para uso posterior
- text -> Se True, entradas e saídas serão tratadas como texto
e automaticamente codificadas ou decodificadas com o conjunto
de caracteres padrão da plataforma (geralmente UTF-8).
- shell -> Se True, terá acesso ao shell do sistema. Ao usar
shell (True), recomendo enviar o comando e os argumentos juntos.
- executable -> pode ser usado para especificar o caminho
do executável que iniciará o subprocesso.
Retorno:
stdout, stderr, returncode e args
Importante: a codificação de caracteres do Windows pode ser
diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
mac, use utf_8.
Comando de exemplo:
Windows: ping 127.0.0.1
Linux/Mac: ping 127.0.0.1 -c 4
'''

import subprocess
import sys

# sys.platform para verificar o sistema operacional
# possíveis retornos = linux, linux2, darwin, win32
sistema_operacional = sys.platform
print(sistema_operacional, '\n')

comando = ['ping', '8.8.8.8']
if sistema_operacional == 'win32':
    codificacao = 'cp850'
else:
    codificacao = 'utf-8'
    comando += ['-c', '4']

# Capturando a saída do comando e decodificando de bytes explicitamente para o utf-8 ou cp850
retorno = subprocess.run(comando, capture_output=True,
                         text=True, encoding=codificacao)
print()
print('retorno.args:', retorno.args, sep='\n')
print('retorno.stdout:', retorno.stdout, sep='\n')
print('retorno.stderr:', retorno.stderr, sep='\n')
print('retorno.returncode:', retorno.returncode, sep='\n')
print()
