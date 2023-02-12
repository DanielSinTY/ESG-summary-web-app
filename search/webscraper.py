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

def install_chromedriver(version):
    os_type = platform.system().lower()
    chromedriver_path = f"chromedriver_{os_type}64"
    if not os.path.exists(chromedriver_path):
        chromedriver_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_{os_type}64.zip"
        subprocess.run(["wget", chromedriver_url])
        subprocess.run(["unzip", f"chromedriver_{os_type}64.zip"])
        subprocess.run(["rm", f"chromedriver_{os_type}64.zip"])
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
        self.browser = webdriver.Chrome(executable_path=f"./chromedriver_{platform.system().lower()}64",options=options)

    def get(self,url):
        self.browser.get(url)
    
    def getFirstEntry(self):
        search=self.browser.find_element(By.XPATH,'//div[@class="Z26q7c UK95Uc"]/descendant::span')
        return search.text

    def destroy(self):
        self.browser.quit()


