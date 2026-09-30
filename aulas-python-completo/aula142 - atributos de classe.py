# atributos de classe
'''
No exemplo abaixo, foi declarada a variável 'ano_atual', essa variável tem escopo na classe.
Ao chamar essa variável no método 'ano_nascimento', podemos chamados como 'self.ano_atual' ou 'Pessoa.ano_atual', porém é recomendável utilizar pelo nome
    da classe dessa forma 'Pessoa.ano_atual', para evitar conflito, ou pegar um valor da variável errada.
'''


class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 34)
p2 = Pessoa('Maria', 26)

print(p1.ano_nascimento())
print(p2.ano_nascimento())
