# escopo de classe e do método da classe
'''
Assim como em funções, uma variável declarada em uma classe, ou método, só terá escopo dentro da sua classe ou método.
Exemplo: variável 'saudacao'

Se uma variável tiver self, ela não terá escopo local, pois ela pertencerá à instância da classe.
Exemplo: self.nome
'''


class Animal:
    def __init__(self, nome):
        self.nome = nome
        saudacao = 'Bom dia'
        print(saudacao)

    def comendo(self, alimento):
        return self.nome + ' está comendo ' + alimento

    def executar(self, *args):
        return self.comendo(*args)


leao = Animal('Leão')
print(leao.executar('maça'))
