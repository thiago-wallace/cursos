# Gerador de senha com secrets
# Gerar uma senha de 12 caracteres, contendo letras maiúsculas ou minúsculas, números e caracteres especiais.

from secrets import SystemRandom
from string import ascii_letters, digits, punctuation

# SOLUÇÃO 1
# inicializando a classe SystemRandom do módulo secrets
r = SystemRandom()
# atribuíndo as letras maiúsculas e minúsculas, números e caracteres especiais em uma variável só
caracteres = ascii_letters + digits + punctuation
# gerando senha aleatóriamente com 12 caracteres (retornando em lista)
senha_lista = r.choices(caracteres, k=12)
# juntando a lista em uma str só
senha = ''.join(senha_lista)
# exibindo a senha
print(senha)

# SOLUÇÃO 2
# efetuando o mesmo processo acima em apenas uma linha
print(''.join(SystemRandom().choices(ascii_letters + digits + punctuation, k=12)))
