# raspagem de sites da internet 4
# mais sobre problemas com caracteres especiais (utf-8)
'''
Adicionando "encoding" no BeautifulSoup 4 para evitar problemas com caracteres

Uma coisa comum de ocorrer quando trabalhamos com o bs4.BeautifulSoup. é problemas com caracteres. Isso ocorre devido a uma falha na detecção do encoding.

Eu explico mais sobre codificação de caracteres no artigo abaixo:

https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

Caso queira mudar a codificação de caracteres, envie os bytes diretamente para o BeautifulSoup e passe o valor da codificação de caracteres no atributo "from_encoding". Exemplo (para utf-8):

    BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

Perceba que troquei "response.text" para "response.content" para obter os bytes ao invés da string.

'''
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8000/'
response = requests.get(url)
# obtendo retorno em bytes com 'content', ao invés de str com 'text'
bytes_html = response.content
# alterando a codifitação de caracteres, de bytes para utf-8, utilizando 'from_encoding'
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

top_jobs_1 = parsed_html.select_one(
    "#intro > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > h2:nth-child(1)")

# mostrar o texto desta tag, com e sem a tag
print(top_jobs_1)
if top_jobs_1 is not None:
    print(top_jobs_1.text)

    # mostrar todo o artigo do pai desse elemento, com a tag
    article = top_jobs_1.parent
    print(article)
    # mostrar todo o artigo do pai desse elemento em lista, sem a tag
    if article is not None:
        # no método select, foi colocado 'p' no parâmetro, para filtrar todas as tags 'p'
        for p in article.select('p'):
            print(p.text)


'''
Assumindo que a codificação de caracteres da página é utf-8.

Você pode detectar isso no HTML pela tag meta charset dentro da <head>:

    <meta charset="UTF-8">
'''
