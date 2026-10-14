# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

total_emprestimo = 1_000_000
tempo_emprestimo = relativedelta(years=5)
data_emprestimo = datetime(2022, 12, 20)
data_final = data_emprestimo + tempo_emprestimo
parcelas = []

data = data_emprestimo
while data < data_final:
    parcelas.append(data)
    data += relativedelta(months=1)

total_parcelas = len(parcelas)
valor_parcela = total_emprestimo / total_parcelas
formato_data = '%d/%m/%Y'

print('Data do empréstimo:', data_emprestimo.strftime(formato_data))
print('Data do fim do empréstimo:', data_final.strftime(formato_data))
print(f'\nParcelas: {total_parcelas}x de {valor_parcela:,.2f}')
for data in parcelas:
    print(f'{data.strftime(formato_data)} R$ {valor_parcela:,.2f}')
print(f'\nVocê pegou R$ {total_emprestimo:,.2f} '
      f'para pagar em {tempo_emprestimo.years} anos ({total_parcelas} meses) '
      f'em parcelas de R$ {valor_parcela:,.2f}')
