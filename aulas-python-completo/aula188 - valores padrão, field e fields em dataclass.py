# valores padrão, field e fields em dataclass
"""
Ao atribuir valores padrão aos atribulos, vale a mesma regra que usamos com função e método: os atributos com valor
    padrão devem ficar sempre depois dos atributos sem valor padrão.
Podemos atribuir um valor padrão diretamente (Como no atributo 'idade').
Podemos atribuir um valor padrão utilizando field, com o parâmetro default (Como nos atributos 'sobrenome' e 'tem_cnh').
O field também pode ser utilizado para configurar outros aspectos que normalmente nós configuramos na dataclass, mas
    apenas para aquele atributo. Exemplo, configurar se aquele atributo vai aparecer no init ou no repr (Como no
    atributo 'tem_cnh', ele está configurado para não aparecer no repr).
Na função fields, podemos visualizar todas as configurações do field de uma instância do dataclass.
"""

from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    nome: str
    sobrenome: str = field(default='Silva')
    idade: int = 18
    tem_cnh: bool = field(default=False, repr=False)
    endereco: list[str] = field(default_factory=list)


pessoa = Pessoa('José')
print(pessoa)

pessoa.endereco.append('Av. Principal, 10')
print(pessoa)

print()
print(fields(pessoa))
