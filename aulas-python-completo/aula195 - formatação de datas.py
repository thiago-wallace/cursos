# formatação de datas
'''
Formatando datas do datetime
datetime.strftime('DATA', 'FORMATO')
https://docs.python.org/3/library/datetime.html
'''

from datetime import datetime

data_1 = datetime(2026, 10, 13, 1, 28, 25)
data_2 = datetime.strptime('13/10/2026 01:28:25', '%d/%m/%Y %H:%M:%S')

print(data_1 == data_2)
print(data_1)
print(data_1.strftime('%d/%m/%Y'))
print(data_1.strftime('%d/%m/%y'))
print(data_1.strftime('%d/%m/%Y - %H:%M:%S'))

hora_str = data_1.strftime('%H')
hora_int = data_1.hour

dia_str = data_1.strftime('%d')
dia_int = data_1.day

print(hora_str, type(hora_str))
print(hora_int, type(hora_int))

print(dia_str, type(dia_str))
print(dia_int, type(dia_int))
