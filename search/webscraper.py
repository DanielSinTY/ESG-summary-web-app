from selenium import webdriver
# from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import logging
import time

logger = logging.getLogger(__name__)

# script.py
import os
import sys
import subprocess
import platform
from selenium import webdriver
import wget
import zipfile
from decouple import config

def install_chromedriver():
    logger.debug("Function started")
    os_type = platform.system().lower()
    system = platform.system()
    if system == 'Windows':
        url = 'https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip'
        filename = 'chromedriver_win32.zip'
    else :
        url = 'https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip'
        filename = '/tmp/chromedriver_linux64.zip'

    if not os.path.exists(filename):
        
        wget.download(url, filename)
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall('/tmp')
        os.remove(filename)
        logger.debug(os.listdir('/tmp'))
        os.environ["PATH"] += os.pathsep + '/tmp'
        logger.debug(os.environ["PATH"])





class WebpageScraper():
    def __init__(self):
        # chromedriver_autoinstaller.install() 
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager(path='/tmp').install()))
        # self.browser = webdriver.Chrome(ChromeDriverManager(path=r'/tmp').install(),chrome_options=chrome_options)
        # specify the desired version of ChromeDriver
        
       
        # install_chromedriver()
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # if platform.system().lower() == "windows":
        #     self.browser = webdriver.Chrome(executable_path=f"./chromedriver.exe", options=options)
        # else:
        #     self.browser = webdriver.Chrome(executable_path=f"./chromedriver_{platform.system().lower()}64", options=options)
        # # self.browser = webdriver.Chrome(executable_path=f"./chromedriver_{platform.system().lower()}64",options=options)
        # Set the desired capabilities
        # capabilities = {
        #     "browserName": "chrome",
        #     "version": "87.0",
        #     "platform": "ANY"
        # }
        # # Create a new instance of the Remote WebDriver
        # self.browser = webdriver.Remote(
            
        #     command_executor=f'http://{config("YOUR_USERNAME")}:{config("YOUR_ACCESS_KEY")}@hub.browserstack.com:80/wd/hub',
        #     desired_capabilities=capabilities,
        #     options=chrome_options)
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--remote-debugging-port=9222')
        options.add_argument(f'--remote-debugging-address=0.0.0.0')
        options.add_argument(f'--remote-debugging-port=0')

        self.browser = webdriver.Remote(
            command_executor=f'https://{config("BROWSERLESS_KEY")}@chrome.browserless.io/webdriver',
            desired_capabilities=options.to_capabilities(),
        )

    def get(self,url):
        self.browser.get(url)
    
    def getFirstEntry(self):
        search=self.browser.find_element(By.XPATH,'//div[@class="Z26q7c UK95Uc"]/descendant::span')
        return search.text

    def destroy(self):
        self.browser.quit()

    def scrapeMSCI(self,companyName):
        # company=input("company?")
        # navigate to the MSCI ESG website
        self.browser.get("https://www.msci.com/our-solutions/esg-investing/esg-ratings-climate-search-tool/")
        while not self.browser.find_elements(By.XPATH,"//input[@id='_esgratingsprofile_keywords']"):
            pass
        entrybox=self.browser.find_element(By.XPATH,"//input[@id='_esgratingsprofile_keywords']")
        entrybox.send_keys(companyName)
        time.sleep(3)
        related_companies= self.browser.find_element(By.XPATH,"//ul[@id='ui-id-1']").find_elements(By.CSS_SELECTOR,"li")
        return [i.text for i in related_companies]
        # print(related_companies)
        # for i,com in enumerate(related_companies):
        #     print(f"{i+1}. {com.text}")
        # index=int(input("Please input the number of the company you want to choose"))
        # related_companies[index-1].click()
        # time.sleep(3)
        # element=driver.find_element(By.XPATH,"//div[@id='_esgratingsprofile_esg-rating-history']")

        # svg=element.find_element(By.XPATH,"./div[@class='highcharts-container ']")
        # print(svg.get_attribute('innerHTML'))
        # # entrybox.send_keys(Keys.RETURN)
        # input()


