# __dict__ e função vars - de instância (classe) para dicionário
'''
Tanto o __dict__ quanto o vars são usados para mostrar os atributos de uma instância em dicionário.
Com isso em dicionário, podemos por exemplo, salvar esse dicionário em um arquivo .json.
Posteriormente, podemos carregar esse arquivo .json para dentro da instância da classe. 
'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 34)
p2 = Pessoa('Maria', 26)

# exibindo os atributos e valores da instância em dicionário, via __dict__
print(p1.__dict__)
# exibindo os atributos e valores da instância em dicionário, via vars()
print(vars(p2))

dados = {
    'nome': 'José',
    'idade': 18,
}

# iniciando uma nova instância carregando as chaves e valores do dicionário
# desempacotando com **, entrará na classe como argumento nomeado (nome='José', idade=18)
p3 = Pessoa(**dados)

print(p3.__dict__)
