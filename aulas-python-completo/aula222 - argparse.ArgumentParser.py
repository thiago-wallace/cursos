# argparse.ArgumentParser
'''
argparse.ArgumentParser para argumentos mais complexos
Tutoriais:
https://docs.python.org/pt-br/3/howto/argparse.html
https://github.com/luizomf/cursopython2023/commit/e0a5a0365b59bc567170fbebcdee8ce4b30b5c30
https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35609838#overview
'''

from argparse import ArgumentParser

parser = ArgumentParser()

# criar argumento para receber o nome, como argumento obrigatório
parser.add_argument('-n', '--nome', type=str, metavar='string',
                    help='Nome do usuário para identificação', required=True)
# criar argumento para receber um número
parser.add_argument('-m1', '--multi1', type=float, metavar='float',
                    help='Primeiro número para multiplicar')
# criar argumento para receber outro número
parser.add_argument('-m2', '--multi2', type=float, metavar='float',
                    help='Segundo número para multiplicar')
# criar argumento para receber uma lista de números
parser.add_argument('-s', '--somar', type=float, metavar='float',
                    help='Vários números para somar', nargs='+')
# criar argumento para receber se deseja o programa verboso
parser.add_argument('-v', '--verbose',
                    help='Mostra o texto mais verboso', action='store_true')

# coletar os argumentos digitados na execução do programa
arg = parser.parse_args()

print('Verboso:', arg.verbose)
if arg.verbose:
    print(
        f'Bom dia / boa tarde / boa noite {arg.nome}, seja bem vindo à este app.')
else:
    print(f'Olá {arg.nome}')

if arg.multi1 and arg.multi2:
    x: float = arg.multi1
    y: float = arg.multi2
    multiplicacao = x * y
    if arg.verbose:
        print(f'A multiplicação de {x} e {y} é igual a {multiplicacao}')
    else:
        print(f'Multiplicação: {multiplicacao}')

if arg.somar:
    lista_x: list[float] = arg.somar
    soma = sum(lista_x)
    if arg.verbose:
        print(f'A Soma de {lista_x} é igual a {soma}')
    else:
        print(f'Soma: {soma}')
