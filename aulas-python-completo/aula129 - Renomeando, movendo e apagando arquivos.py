# Renomeando, movendo e apagando arquivos
'''
os.rename - utilizado para renomear ou mover um arquivo
os.remove e os.unlink - utilizados para apagar um arquivo
'''

import os

arquivo = open('teste1.txt', 'x')
arquivo.close()

# Renomeando
os.rename('teste1.txt', 'teste2.txt')

# Movendo
os.rename('teste2.txt', 'pasta1/teste2.txt')

# apagando - tanto o os.remove quanto o os.unlink fazem a mesma função
os.remove('pasta1/teste2.txt')
