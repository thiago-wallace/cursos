# gerando arquivo requirements.txt
'''
Arquivo utilizado para salvar as versões dos pacotes instalados no ambiente virtual pelo pip.
O arquivo pode ter qualquer nome, porém por padrão, se usa o nome 'requirements.txt'.
Com esse arquivo salvo, a venv pode ser apagada, e depois se precisar recriar uma nova venv com os mesmo pacotes nas mesmas versões, basta instalar usando
    esse arquivo.

Gerar arquivo
    pip freeze > requirements.txt

Reinstalar pacotes usando o arquivo
    pip install -r requirements.txt

'''
