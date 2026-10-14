# calendar
'''
# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
'''
import calendar
print(calendar.calendar(2026))
print(calendar.month(2026, 10))
print('Dia da semana em int: 13/10/2026:', calendar.weekday(2026, 10, 13))
print('Dias da semana:', list(calendar.day_name))
print('Dia da semana em str: 13/10/2026:',
      calendar.day_name[calendar.weekday(2026, 10, 13)])
print('Calendário em lista: Outubro/2026',
      calendar.monthcalendar(2026, 10), sep='\n')
print('Calendário em lista: Outubro/2026', *
      calendar.monthcalendar(2026, 10), sep='\n')
print('Primeiro dia da semana e o último dia do mês: Outubro/2026:',
      calendar.monthrange(2026, 10))
