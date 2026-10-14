# Precedência matemática

'''
1º Parenteses ()
2º Potência **
3º Multiplicação e Divisão (incluíndo Divisão Inteira e Módulo) * / // %
4º Adição e Subtração
'''

resultado = 1 + 1 * 5
print("1 + 1 * 5 =", resultado)

resultado = (1 + 1) * 5
print("(1 + 1) * 5 =", resultado)

resultado = 1 + 1 ** 5 + 5 * 2
print("1 + 1 ** 5 + 5 * 2 =", resultado)

resultado = (1 + 1) ** (5 + 5) * 2
print("(1 + 1) ** (5 + 5) * 2 =", resultado)

resultado = (1 + 1) ** 5 + 5 * 2
print("(1 + 1) ** 5 + 5 * 2 =", resultado)

resultado = (1 + 1) ** ((5 + 5) * 2)
print("(1 + 1) ** ((5 + 5) * 2) =", resultado)

resultado = 2 ** 20
print("2 ** 20 =", resultado)
