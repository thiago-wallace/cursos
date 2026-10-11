# datetime - criando data e hora
'''
datetime(ano, mês, dia)
datetime(ano, mês, dia, horas, minutos, segundos)
datetime.strptime('DATA', 'FORMATO')
https://docs.python.org/3/library/datetime.html
'''

from datetime import datetime

data = datetime(2026, 2, 5)
print(data)

data_e_hora = datetime(2026, 2, 5, 15, 30, 45)
print(data_e_hora)

data_str = '05/02/2026 15:30:35'
data_format = '%d/%m/%Y %H:%M:%S'
data_e_hora = datetime.strptime(data_str, data_format)
print(data_e_hora)
