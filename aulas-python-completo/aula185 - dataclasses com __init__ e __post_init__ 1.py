# dataclasses com __init__ e __post_init__ 1

"""
__post_init__ - Método que é executado logo após o __init__ da dataclasse.
O __post_init__ é executado somente após o __init__ da dataclasse. Ou seja, se a
    classe tiver um __init__ manual, ou se o parâmetro init na dataclass estiver
    como False, o __post_init__ não é executado.
"""

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        print('post init')


pessoa = Pessoa('João', 'Silva')
print(pessoa)
