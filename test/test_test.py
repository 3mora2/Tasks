import os
import subprocess
from time import sleep
from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


class CollectPosts(object):
    def __init__(self):
        self.drivers = set()
        self.user_data = r'C:\selenium\AutomationProfile'

    def create_profile(self):
        for i in range(9):
            try:
                pros = subprocess.Popen(
                    '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
                    rf' --user-data-dir="{self.user_data}" --profile-directory="Profile {i}"'
                    ' --remote-debugging-port=9222')
            except:
                pros = subprocess.Popen(
                    '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
                    rf' --user-data-dir="{self.user_data}" --profile-directory="Profile {i}"'
                    '  --remote-debugging-port=9222')
            sleep(5)
            pros.kill()

    def open_driver(self):
        for i in range(9):
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            # chrome_options.add_argument(
            #     'user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; '
            #     'CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
            # chrome_options.add_argument('--disable-plugins')
            # chrome_options.add_argument('--disable-popup-blocking')
            chrome_options.add_argument(fr"--user-data-dir={self.user_data}\Profile {i}")
            # chrome_options.add_argument(f'--profile-directory=Profile {i}')
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
            self.drivers.add(driver)

    def test(self, url):
        for driver in self.drivers:
            try:
                driver.get(url)
                print('-')
            except Exception as e:
                print(e)


if __name__ == '__main__':
    self = CollectPosts()
    while True:
        choose = input('- Enter 1 for create profile \n- Enter 2 To Open : '
                       '\n- Enter 3 to Test : ')
        if choose == '1':
            self.create_profile()
        if choose == '2':
            self.open_driver()
        if choose == '3':
            ur = input('- Enter url : ')
            self.test(ur)
        if choose == 'q':
            try:
                for driver in self.drivers:
                    driver.quit()
            except:
                pass