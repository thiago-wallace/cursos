# string.Template
'''
string.Template para substituir variáveis em textos
doc: https://docs.python.org/3/library/string.html#template-strings
Métodos:
substitute: substitui mas gera erros se faltar chaves
safe_substitute: substitui sem gerar erros
Você também pode trocar o delimitador e outras coisas criando uma subclasse de template.
'''
# Exemplo de uso, parecido com mala direta do Microsoft Word no Office.

import string
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')

valor = 1_500
data = datetime(2026, 11, 1)

dados = dict(
    nome='João',
    valor=locale.currency(valor, grouping=True),
    data=data.strftime('%d/%m/%Y'),
    empresa='TH LTDA',
    telefone='+55 (11) 1234-5678',
)

with open('aula217b - email.txt', 'r') as arquivo:
    texto = arquivo.read()

email_modelo = string.Template(texto)
print(email_modelo.substitute(dados))
