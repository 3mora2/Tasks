import traceback

import psutil
from PySide2.QtCore import QThread, Signal
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
import chromedriver
import os

scriptDir = os.path.dirname(os.path.realpath(__file__))
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--enable-javascript")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-plugins')
chrome_options.add_argument('--disable-popup-blocking')


def close_chrome_driver():
    try:
        for proc in psutil.process_iter():
            processName = proc.name()
            if 'chromedriver' in processName.lower():
                proc.kill()
    except:
        print(traceback.format_exc())


class OpenDriverYellow(QThread):
    final = Signal()
    error = Signal()
    wait = Signal()
    do_reopen = False
    driver: WebDriver = None

    def run(self):
        if not self.do_reopen:
            result = self.open()
        else:
            result = self.reopen()
        if result:
            self.final.emit()
        else:
            self.error.emit()

    def open(self):
        try:
            close_chrome_driver()
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
            self.driver.get("https://www.yellowpages.com.eg/ar/")
            return True
        except ConnectionResetError:
            print('other driver opend')
        except WebDriverException:
            try:
                self.wait.emit()
                path = chromedriver.install(cwd=scriptDir)
                if 'Traceback' not in path:
                    self.driver = webdriver.Chrome(path, chrome_options=chrome_options)
                    self.driver.get("https://www.yellowpages.com.eg/ar/")
                    return True

            except:
                print(traceback.format_exc())
        except:
            print(traceback.format_exc())

        return False

    def reopen(self):
        try:
            self.driver.quit()
        except:
            pass
        try:
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
            self.driver.get("https://www.yellowpages.com.eg/ar/")
            return True
        except:
            print(traceback.format_exc())
        return False

    def check(self):
        try:
            return self.driver.title
        except:
            return None


