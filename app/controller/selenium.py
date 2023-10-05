import time
import selenium
from selenium import webdriver


class Automate:
    def __init__(self):
        self.driver = None
        pass

    def open_broser(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        time.sleep(500)

