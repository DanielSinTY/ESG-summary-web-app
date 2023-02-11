from selenium import webdriver
# from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import chromedriver_autoinstaller


class WebpageScraper():
    def __init__(self):
        # chromedriver_autoinstaller.install() 
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager(path='/tmp').install()))
        # self.browser = webdriver.Chrome(ChromeDriverManager(path=r'/tmp').install(),chrome_options=chrome_options)

    def get(self,url):
        self.browser.get(url)
    
    def getFirstEntry(self):
        search=self.browser.find_element(By.XPATH,'//div[@class="Z26q7c UK95Uc"]/descendant::span')
        return search.text

    def destroy(self):
        self.browser.quit()


