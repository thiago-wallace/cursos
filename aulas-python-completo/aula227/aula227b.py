# Selenium - Automatizando tarefas no navegador
# Abrir a URL do Google, digitar no campo de pesquisa e pressionar Enter
# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

from pathlib import Path
from time import sleep
# usado para chamar o navegador e para configurar as opções/argumentos da chamada do navegador
from selenium import webdriver
# usado para indicar qual serviço vai utilizar o chromedriver
from selenium.webdriver.chrome.service import Service
# usado para selecionar um elemento da página aberta
from selenium.webdriver.common.by import By
# usado para fazer o selenium esperar o elemento carregar na página
from selenium.webdriver.support.wait import WebDriverWait
# usado para configurar uma condição de espera ao selenium
from selenium.webdriver.support import expected_conditions
# usado para informar uma tecla para o selenium pressionar na página
from selenium.webdriver.common.keys import Keys

RAIZ_MAIN = Path(__file__).parent
CHROMEDRIVER = RAIZ_MAIN / 'drivers' / 'chromedriver'

# options - Opções/Argumentos para abrir o chrome pelo terminal (Ex: --help, --start-maximized)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
# service - utilizado para indicar qual serviço vai utilizar o chromedriver.
# no parâmetro executable_path, colocar o diretório do arquivo do chromedriver.
chrome_service = Service(executable_path=str(CHROMEDRIVER))
# browser - para chamar o navegador, passando o serviço (chromedriver) e as opções
chrome_browser = webdriver.Chrome(
    service=chrome_service, options=chrome_options)

# abrir o navegador e acessar essa url
chrome_browser.get('https://www.google.com.br')

# Esperar o browser por 30 segundos, até a condição esperada: presença de um elemento localizado, este elemento é o 'name'="q"
'''
WebDriverWait(chrome_browser, 30) - Esperar o browser por 30 segundos,
until(expected_conditions. - até a condição esperada:
presence_of_element_located(( - presença de um elemento localizado,
By.NAME, 'q'))) - este elemento é o 'name'="q"
'''
busca_input = WebDriverWait(chrome_browser, 30).until(
    expected_conditions.presence_of_element_located((By.NAME, 'q')))

# Digitar no campo de busca - input
busca_input.send_keys('Hello World')
# Pressionar enter no campo de busca
busca_input.send_keys(Keys.ENTER)

sleep(5)
