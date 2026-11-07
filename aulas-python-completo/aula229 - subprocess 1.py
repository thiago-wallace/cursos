# subprocess 1
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

comando = ['ping', '8.8.8.8', '-c', '4']

# Executar comando sem capturar a saída
retorno = subprocess.run(comando)
print()
print(retorno)
print(retorno.args)
print(retorno.stdout)
print(retorno.stderr)
print(retorno.returncode)
print()

# Capturando a saída do comando e decodificando de bytes para o padrão (utf-8 no Linux) - Forma 1
retorno = subprocess.run(comando, capture_output=True)
print()
print(retorno.stdout.decode())
print()

# Capturando a saída do comando e decodificando de bytes para o padrão (utf-8 no Linux) - Forma 2
retorno = subprocess.run(comando, capture_output=True, text=True)
print()
print(retorno.stdout)
print()

# Capturando a saída do comando e decodificando de bytes explicitamente para o utf-8 - Forma 3
retorno = subprocess.run(comando, capture_output=True,
                         text=True, encoding='utf-8')
print()
print(retorno.stdout)
print()
