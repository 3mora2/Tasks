import datetime
import traceback

import psutil
from PySide2.QtCore import QThread, Signal

import os
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import chromedriver
from codes.error import error_Text


def close_chrome_driver():
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            if 'chromedriver' in processName.lower():
                proc.kill()

        except:
            error_Text(traceback.format_exc())


class OpenDriver(QThread):
    driver = None
    final = Signal()
    found = Signal()
    wait = Signal()
    is_used_now = False
    Try: bool = False
    reopen = False

    def run(self):
        self.Try = True
        if self.reopen:
            self.close()

        if not self.driver or not self.check_live():
            try:
                close_chrome_driver()
                chrome_options = Options()
                chrome_options.add_argument("--disable-infobars")
                chrome_options.add_argument("--disable-notifications")
                chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
                chrome_options.add_argument('--disable-blink-features=AutomationControlled')
                chrome_options.add_experimental_option('useAutomationExtension', False)
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--disable-plugins')
                chrome_options.add_argument('--disable-popup-blocking')
                chrome_options.add_argument("--user-data-dir={}".format(r'C:\selenium\AutomationProfile'))
                try:
                    self.driver = webdriver.Chrome(chrome_options=chrome_options)
                except WebDriverException:
                    self.wait.emit()
                    scriptDir = os.path.dirname(os.path.realpath(__file__))
                    path = chromedriver.install(cwd=scriptDir)
                    if 'Traceback' not in path:
                        try:
                            os.popen('attrib +h chromedriver.exe')
                        except:
                            with open('log.log', 'a+', encoding="utf-8") as f:
                                f.write(
                                    f'{datetime.datetime.now()}: {str(traceback.format_exc())}\n')

                        self.driver = webdriver.Chrome(path, chrome_options=chrome_options)

                    else:
                        error_Text(path)
                        raise Exception
                except:
                    error_Text(traceback.format_exc())

                # win32gui.EnumWindows(enumWindowFunc, [])
                self.driver.get('https://web.whatsapp.com/')
                # chrome_options = webdriver.ChromeOptions()
                # chrome_options.add_argument('--no-sandbox')
                # chrome_options.add_argument('--disable-gpu')
                # chrome_options.add_argument("--disable-infobars")
                # chrome_options.add_argument("--disable-notifications")
                # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                # self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
                print('- done')
                self.final.emit()
            except Exception as a:
                print(a)
                error_Text(traceback.format_exc())
        else:
            self.found.emit()
            print('- found')
        self.Try = False

    def check_live(self):
        if not self.driver:
            return False
        try:
            return self.driver.title
        except:
            return False

    def close(self):
        try:
            self.driver.quit()
        except:
            pass
        close_chrome_driver()
        self.driver = None
