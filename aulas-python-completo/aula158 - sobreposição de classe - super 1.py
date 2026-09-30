# sobreposição de classe - super 1

'''
super() - classe utilizada para chamar um método da super classe.

Exemplo: dentro da classe 'MinhaPropriaString', ao utilizar o 'super().upper()' sem argumentos, ele vai automaticamente chamar no pai da classe
    'MinhaPropriaString' (ou seja, a classe 'str') o método 'upper', na instância self.
Nesse caso, daria o mesmo resultado digitar 'super().upper()' ou 'super(MinhaPropriaString, self).upper()'
'''


class MinhaPropriaString(str):
    def upper(self):
        texto = 'ops...\n' + super().upper()
        return texto


nome = MinhaPropriaString('Thiago')

print(nome.lower())
print(nome.upper())
