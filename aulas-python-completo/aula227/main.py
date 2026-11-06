# Selenium - Automatizando tarefas no navegador
# Abrir a URL do Wikipedia em português, digitar no campo de pesquisa e pressionar Enter
# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

RAIZ_MAIN = Path(__file__).parent
CHROMEDRIVER = RAIZ_MAIN / 'drivers' / 'chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_service = Service(executable_path=str(CHROMEDRIVER))
chrome_browser = webdriver.Chrome(
    service=chrome_service, options=chrome_options)

chrome_browser.get('https://pt.wikipedia.org')

busca_input = WebDriverWait(chrome_browser, 30).until(
    expected_conditions.presence_of_element_located((By.NAME, 'search')))

busca_input.send_keys('Python')
busca_input.send_keys(Keys.ENTER)

sleep(15)
