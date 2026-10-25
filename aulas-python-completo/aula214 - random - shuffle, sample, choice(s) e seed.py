# random - shuffle, sample, choice(s) e seed
'''
random tem geradores de números pseudoaleatórios
Obs.: números pseudoaleatórios significa que os números
parecem ser aleatórios, mas na verdade não são. Portanto,
este módulo não deve ser usado para segurança ou uso criptográfico.
O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
a saída pode ser previsível.
doc: https://docs.python.org/pt-br/3/library/random.html
'''

import random

nomes = ['Luiz', 'Maria', 'Helena', 'Joana']

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes_embaralhados = nomes.copy()
random.shuffle(nomes_embaralhados)
print(nomes_embaralhados)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
# Ex: Escolher 3 nomes na lista aleatoriamente, sem repetir
novos_nomes_sample = random.sample(nomes, 3)
print(novos_nomes_sample)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
# Ex: Escolher 3 nomes na lista aleatoriamente, podendo repetir
novos_nomes_choices = random.choices(nomes, k=3)
print(novos_nomes_choices)

# random.choice(Iterável) -> Escolhe um elemento do iterável
nome = random.choice(nomes)
print(nome)

# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# Altera a semente para gerar números aleatórios a partir desse ponto
# Ex: colocando um número fixo como semente (0), os próximos aleatórios serão sempre os mesmos
random.seed(0)

# Com essa semente, o resultado sempre será: ['Joana', 'Joana', 'Maria']
novos_nomes_choices = random.choices(nomes, k=3)
print(novos_nomes_choices)
