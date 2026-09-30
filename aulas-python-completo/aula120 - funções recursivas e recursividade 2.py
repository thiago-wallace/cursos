# Funções recursivas e recursividade 2
'''
- funções que podem se chamar de volta
- úteis p/ dividir problemas grandes em partes menores

Toda função recursiva deve ter:
- Um problema que possa ser dividido em partes menores
- Um caso recursivo que resolve o pequeno problema
- Um caso base que para a recursão
- Exemplo: fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
https://brasilescola.uol.com.br/matematica/fatorial.htm
'''

# usando for

def fatorial_for(x):
    resultado = 1
    for i in range(x, 1, -1):
        resultado *= i
    return resultado

print(fatorial_for(5))

# usando função recursiva

def fatorial_rec(x):
    if x <= 1:
        return x
    return x * fatorial_rec(x - 1)

print(fatorial_rec(5))
