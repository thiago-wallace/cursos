# modo de abertura de arquivos e encoding

'''
Modos:
r (leitura)
r+ (leitura com possibilidade de escrita)
w (criação e escrita)
w+ (criação e escrita com possibilidade de leitura)
x (apenas para criação)
a (escreve ao final do arquivo)
a+ (escreve ao final do arquivo com possibilidade de leitura)

Obs:
Modos r e r+ - Só funciona se o arquivo já existir
Modos w e w+ - Se o arquivo não existir, ele cria um novo, porém se o arquivo já existir, ele apaga o conteúdo do arquivo já no início da abertura.
Modos a e a+ - Se o arquivo não existir, ele cria um novo, e se o arquivo já existir, ele escreve apenas a partir do final do arquivo, sem alterar o restante.

Encoding - modo de codificação dos caracteres.
Por padrão, o Linux e o MAC utilizam o UTF-8, enquando o Windows utiliza uma codificação própria, sendo que por padrão, o Python utiliza o UTF-8 (mesmo
    utilizando o Python e o VSCODE no Windows). Com isso, ao escrever um arquivo com caracteres especiais no Windows, esses caracteres podem não serem
    exibidos corretamente.
Para garantir que os caracteres especiais vão aparecer corretamente em todos os sistemas, podemos utilizar o argumento nomeado na função open 'encoding',
    colocando como parâmetro "utf-8" ou "utf8"
'''

caminho_arquivo = 'teste.txt'
with open(caminho_arquivo, 'a+', encoding='utf-8') as arquivo:
    arquivo.write('Atenção 1\nAtenção 2\n')
    arquivo.seek(0, 0)
    print(arquivo.read())
