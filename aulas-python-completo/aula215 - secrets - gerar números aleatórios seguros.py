# secrets - gerar números aleatórios seguros

import secrets

# USANDO DIRETAMENTE O SECRETS

# gerar número aleatório entre 0 e 20 (Sem incluir o 20)
numero = secrets.randbelow(20)
print(numero)

# escolhe uma cidade aleatoriamente na lista
cidades = ['São Paulo', 'Rio de Janeiro',
           'Belo Horizonte', 'Porto Alegre', 'Fortaleza']
print(secrets.choice(cidades))

# USANDO SYSTEMRANDOM, COM OS MESMOS MÉTODOS DO MÓDULO RANDOM

r = secrets.SystemRandom()

print('Número entre [10-20):', r.randrange(10, 20, 2))
print('Número entre [10-20]:', r.randint(10, 20))
print('Número decimal entre [10-20)]:', r.uniform(10, 20))
print('Número decimal entre [0-1)]:', r.random())

cidades_embaralhadas = cidades.copy()
r.shuffle(cidades_embaralhadas)
print('Cidades embaralhadas:', cidades_embaralhadas)

print('Uma Cidade escolhida:', r.choice(cidades))
print('Três cidades (Sem repetir):', r.sample(cidades, 3))
print('Três cidades (Podendo repetir):', r.choices(cidades, k=3))
