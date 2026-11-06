# Selenium - Automatizando tarefas no navegador
# Abrir o navegador e acessar URL do Google
# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

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
sleep(5)
