# locale para internacionalização
'''
locale para internacionalização (tradução)
https://docs.python.org/3/library/locale.html
https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

Coletar e configurar automaticamente o locale do sistema, deixando uma string vazia no parâmetro: locale.setlocale(locale.LC_ALL, '')

Comando do terminal para verificar lista de locale no Linux e MAC: locale -a 
Comando equivalente do terminal para verificar lista de locale no Windows: Get-WinSystemLocale

Converter ponto flutuante de ponto para vírgula, exemplo: locale.format_string('%f', 1234.56, grouping=True)
Formatos de saída:
%f - float
%.3f - float com 3 casas decimais
%i - int
'''

import locale
import calendar

# Coletar locale padrão do sistema
print(locale.getlocale())
# Coletar e configurar o locale padrão do sistema
locale.setlocale(locale.LC_ALL, '')
# Configurar o locale específico do português Brasil, com UTF-8
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
# Mostrar calendário
print(calendar.calendar(2026))
# Converter um número para str, utilizando vírgula no lugar do ponto para casas decimais (Padrão do Brasil)
x = 1234.567
s = locale.format_string('%.2f', x, grouping=True)
print(s)
