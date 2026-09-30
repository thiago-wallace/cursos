# property e conceito de getter
'''
@property - um getter no modo Pythônico
getter - um método para obter o valor de um atributo. Exemplo: get_cor()
modo pythônico - modo do Python de fazer coisas

@property é uma propriedade do objeto, ela é um método que se comporta como um atributo, ou seja, ao chamar esse método fora da classe, ele é chamado da
    mesma forma que a gente chamaria um atributo da instância.
Geralmente é usada nas seguintes situações:
- como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
Código cliente - é o código de outra pessoa, que usa seu código.
Exemplo: Se você alterar o nome de uma variável, e outros códigos utilizam o seu código, todo mundo vai precisar alterar também o valor dessa variável nos
    seus códigos clientes. Para evitar isso, utiliza-se o conceito de getter. Em Python, podemos utilizar o getter (comum em outras linguagens, e funciona no 
    Python), ou podemos utilizar o @property (modo Pythônico de se fazer getter)
'''

# exemplo de código utilizando getter
# originalmente, a variável se chamava self.cor, e foi alterada para self.cor_tinta. Para evitar quebrar o código do cliente, utilizamos get_cor()


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    def get_cor(self):
        return self.cor_tinta


caneta = Caneta("Azul")

print(caneta.get_cor())
