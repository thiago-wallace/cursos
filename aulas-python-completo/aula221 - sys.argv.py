# sys.argv
'''
sys.argv
Coletando argumentos da execução
Executando arquivos com argumentos no sistema

Exemplo:
Ao executar o código digitando no terminal "python aula221.py", a execução terá um argumento, retornando ["aula221.py"]
Ao executar o código digitando no terminal "python aula221.py -a -m", a execução terá três argumentos, retornando ["aula221.py", "-a", "-m"]
'''
import sys


argumentos = sys.argv
quantidade = len(argumentos)
if quantidade <= 1:
    print('Execução não teve mais de um argumento')
else:
    print('Execução teve os argumentos extras:', argumentos[1:])
