# usando Python como servidor http
'''
http.server - servindo HTML e CSS via HTTP com comando Python

Dicar no arquivo HTML:
! - Gerar código base
link:css - Gerar link com o arquivo "style.css"

comando python para usar o python como servidor HTTP: 
python -m http.server -d [diretório do arquivo index.html] [opicional: porta lógica para utilizar] 
exemplo: python -m http.server -d aula224_site/ 8000

endereço para acessar a página servida pelo python:
localhost:porta ou 127.0.0.1:porta
exemplo: localhost:8000
'''
