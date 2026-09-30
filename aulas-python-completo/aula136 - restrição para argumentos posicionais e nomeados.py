# restrição para argumentos posicionais e nomeados
'''
Positional-Only Parameters (/) e Keyword-Only Arguments (*)

*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)

🟢 Positional-only Parameters (/) - Tudo antes da barra deve ser ❗️APENAS❗️ posicional.
🟢 Keyword-Only Arguments (*) - Tudo depois do asterisco deve ser ❗️APENAS❗️ nomeado.

PEP 570 – Python Positional-Only Parameters
https://peps.python.org/pep-0570/

PEP 3102 – Keyword-Only Arguments
https://peps.python.org/pep-3102/
'''


def somar(a, /, b):
    soma = a + b
    return soma


def multiplicar(a, *, b):
    produto = a * b
    return produto


soma = somar(2, b=3)
print(soma)

multiplicacao = multiplicar(2, b=3)
print(multiplicacao)
