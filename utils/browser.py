from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import os 

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME


# --headless
def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()    
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    if os.environ.get('SELENIUM_HEADLESS') == '1':
        chrome_options.add_argument('--headless')

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser

if __name__ == '__main__':
    #browser = make_chrome_browser()
    browser = make_chrome_browser('--headless')    # qdo quiser ocultar navegador durante execução
    browser.get('https://www.google.com.br/')
    sleep(5)
    browser.quit()
