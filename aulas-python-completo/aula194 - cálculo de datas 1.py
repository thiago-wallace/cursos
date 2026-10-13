# cálculo de datas 1
'''
datetime.timedelta e dateutil.relativedelta (calculando datas)

Docs:
https://dateutil.readthedocs.io/en/stable/relativedelta.html
https://docs.python.org/3/library/datetime.html#timedelta-objects

Obs: Para o dateutil.relativedelta, é necessário baixar as bibliotecas
    'python-dateutil' e 'types-python-dateutil' pelo pip.
'''

from datetime import datetime, timedelta

formato = '%d/%m/%Y - %H:%M:%S'

data_1 = datetime.strptime('23/09/2025 - 14:00:00', formato)
data_2 = datetime.strptime('05/02/2026 - 15:30:00', formato)

print(data_1 > data_2)
print(data_1 < data_2)
print(data_1 == data_2)

delta = data_2 - data_1
print(delta)
print(delta.days, delta.seconds, delta.total_seconds())
tempo = timedelta(days=10, hours=2)
print(data_2 + tempo)
