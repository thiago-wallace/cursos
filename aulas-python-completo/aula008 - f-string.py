# f-string / cálculo de IMC

nome = 'Joao Pessoa'
altura = 1.80
peso = 95
imc = peso / altura ** 2

# :.2f indica que o valor até duas casas decimais
print(f"{nome} tem {altura:.2f} de altura")
print(f"pesa {peso} quilos,")
print(f"e seu IMC é {imc:.3f}")
