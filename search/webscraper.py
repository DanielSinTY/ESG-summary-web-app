from selenium import webdriver
# from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# script.py
import os
import sys
import subprocess
import platform
from selenium import webdriver
import wget
import zipfile

def install_chromedriver(version):
    os_type = platform.system().lower()
    system = platform.system()
    if system == 'Windows':
        url = 'https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip'
        filename = 'chromedriver_win32.zip'
    elif system == 'Linux':
        url = 'https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip'
        filename = '/tmp/chromedriver_linux64.zip'

    if not os.path.exists(filename):
        
        wget.download(url, filename)
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall('/tmp')
        os.remove(filename)
        os.environ["PATH"] += os.pathsep + os.getcwd()





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
        version = "87.0.4280.20"
        install_chromedriver(version)

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        if platform.system().lower() == "windows":
            self.browser = webdriver.Chrome(executable_path=f"./chromedriver.exe", options=options)
        else:
            self.browser = webdriver.Chrome(executable_path=f"./chromedriver_{platform.system().lower()}64", options=options)
        # self.browser = webdriver.Chrome(executable_path=f"./chromedriver_{platform.system().lower()}64",options=options)

    def get(self,url):
        self.browser.get(url)
    
    def getFirstEntry(self):
        search=self.browser.find_element(By.XPATH,'//div[@class="Z26q7c UK95Uc"]/descendant::span')
        return search.text

    def destroy(self):
        self.browser.quit()


