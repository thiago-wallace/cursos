# POO - agregação
'''
Agregação é uma forma mais especializada de associação entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.
Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.
(existem controvérsias sobre as definições de agregação).
'''


class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produtos(self, *produtos):
        self._produtos += produtos

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def total(self):
        total = 0
        for produto in self._produtos:
            total += produto.preco
        print(total)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1 = Produto('Salgadinho', 5.00)
p2 = Produto('Bolacha', 2.50)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
carrinho.total()
