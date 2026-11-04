# raspagem de sites da internet 2
# raspando partes específicas do site
'''
Coletar apenas o texto do trecho "Top 3 jobs"(Fundo branco):
- Clicar com o botão direito no "Top 3 jobs", ir em inspecionar.
- Aparecerá a tag com o trecho desejado no HTML
- Clicar com o botão direito na tag desejada, ir em Copiar > CSS Selector
- Colar conteúdo no argumento do método select_one
- Obs: select_one para um elemento, select para vários elementos
'''

import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8000/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

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
        # mostrando o mesmo conteúdo, porém corrigindo os caracteres especiais para UTF-8
        for p in article.select('p'):
            print(p.text.encode('latin1').decode('utf-8'))
