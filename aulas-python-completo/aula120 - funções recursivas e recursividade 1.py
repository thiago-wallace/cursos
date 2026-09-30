# Funções recursivas e recursividade 1
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

def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return inicio
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

