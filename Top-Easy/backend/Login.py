from time import sleep
from PySide2.QtCore import QThread, Signal
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
# from requests_html import HTMLSession
#
# session = HTMLSession()

import os

from backend import chromedriver

scriptDir = os.path.dirname(os.path.realpath(__file__))


class Login(QThread):
    driver: WebDriver = None
    final = Signal()
    error = Signal()

    def run(self):
        try:
            self.driver = webdriver.Chrome()
        except WebDriverException:
            path = chromedriver.install(cwd=scriptDir)
            self.driver = webdriver.Chrome(path)

        self.driver.get('https://sa.aqar.fm/login')
        try:
            sleep(1)
            self.driver.find_element_by_css_selector('input[name="phone"]').send_keys(self.email)
            sleep(1)
            self.driver.find_element_by_css_selector('input[name="password"]').send_keys(self.password)
            sleep(1)
            self.close()
            self.driver.execute_script("document.querySelector('a.submitBtn').click()")
            sleep(2)
            if '/login' in self.driver.current_url:
                self.error.emit()
            else:
                self.final.emit()
        except:
            self.error.emit()

    def close(self):
        try:
            self.driver.find_element_by_css_selector('.national-closeBtn').click()
            sleep(1)
        except:
            pass

    def check(self):
        try:
            return self.driver.title
        except:
            return None
'''

'''