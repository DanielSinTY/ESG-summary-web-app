from selenium import webdriver
# from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument("--headless")

class WebpageScraper():
    def __init__(self):
        self.browser = webdriver.Chrome(ChromeDriverManager(path = r".\\Drivers").install(),chrome_options=chrome_options)

    def get(self,url):
        self.browser.get(url)
    
    def getFirstEntry(self):
        search=self.browser.find_element(By.XPATH,'//div[@class="Z26q7c UK95Uc"]/descendant::span')
        return search.text

    def destroy(self):
        self.browser.quit()


