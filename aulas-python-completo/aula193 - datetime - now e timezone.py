# datetime - now, timezone e timestamp
'''
datetime(ano, mês, dia)
datetime(ano, mês, dia, horas, minutos, segundos)
datetime.strptime('DATA', 'FORMATO')
datetime.now()
https://pt.wikipedia.org/wiki/Era_Unix
datetime.fromtimestamp(Unix Timestamp)
https://docs.python.org/3/library/datetime.html
Para timezones
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
Instalando o pytz
pip install pytz types-pytz
'''

from datetime import datetime
from pytz import timezone

data_e_hora = datetime.now()
print('Data e hora agora:', data_e_hora)

data_e_hora = datetime.now(timezone('America/Sao_Paulo'))
print('Fuso horário São Paulo:', data_e_hora)

data_e_hora = datetime.now(timezone('America/Los_Angeles'))
print('Fuso horário Los Angeles:', data_e_hora)

data_e_hora = datetime.now(timezone('Asia/Tokyo'))
print('Fuso horário Tokyo:', data_e_hora)

data_e_hora = datetime(2026, 2, 5, 15, 30, 45,
                       tzinfo=timezone('America/Sao_Paulo'))
print('Gerada data e hora no fuso horário de São Paulo:', data_e_hora)

data_e_hora = datetime.now()
data_unix = data_e_hora.timestamp()
print('Data no formato Unix:', data_unix)
nova_data = datetime.fromtimestamp(data_unix)
print('Data no formato padrão:', nova_data)
