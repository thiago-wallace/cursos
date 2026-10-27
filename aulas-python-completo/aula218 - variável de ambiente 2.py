# variável de ambiente do sistema operacional 2
'''
Variáveis de ambiente com Python

Para variáveis de ambiente:
Windows PS: $env:VARIAVEL="VALOR" | dir env:
Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL

Para obter o valor das variáveis de ambiente
os.getenv ou os.environ['VARIAVEL']

Para configurar variáveis de ambiente
os.environ['VARIAVEL'] = 'valor'
Ou usando python-dotenv e o arquivo .env

pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

https://pypi.org/project/python-dotenv/
OBS.: sempre lembre-se de criar um .env-example
'''

import os
from dotenv import load_dotenv

load_dotenv()

# exibir todas as variáveis ambiente (Tanto do SO quanto do arquivo .env)
print(os.environ)
print()
# exibir a variável ambiente BD_SENHA, configurada no arquivo .env (Retorna None se não existir)
print(os.getenv('BD_SENHA'))
# exibir a variável ambiente BD_SENHA, configurada no arquivo .env (Lança um erro se não existir)
print(os.environ['BD_SENHA'])

# configurar uma variável ambiente (Sem o arquivo .env)
os.environ['BD_SOBRENOME'] = 'Silva'
# exibindo a variável configurada
print(os.environ['BD_SOBRENOME'])
print(os.getenv('BD_SOBRENOME'))
