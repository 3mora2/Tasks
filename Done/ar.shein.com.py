import json
import os
import subprocess
from time import sleep
from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import re


class CollectPosts(object):
    def __init__(self):
        self.book = Workbook()
        self.sheet = self.book.active
        # chrome_options = Options()
        # self.user_data = os.path.expanduser("~") + r'\AppData\Local\Google\Chrome\User Data'
        # chrome_options.add_argument("--user-data-dir={}".format(self.user_data))
        # chrome_options.add_argument('--profile-directory=Profile 4')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())#), chrome_options=chrome_options)

    def start(self, urls):
        num = 2
        for url in urls:
            self.driver.get(url)
            sleep(6)
            input('- ')
            data = self.driver.execute_script("return document.querySelector('.c-header.j-c-header1 + script').text")

            d = data.replace('window.goodsDetailv2SsrData = ', '').split('\n    //')[0]
            json_data = json.loads(d[d.find('productIntroData') + 18:d.find('abt:')].strip()[:-1])

            img = []
            img.append(json_data['goods_imgs']['main_image']['origin_image'])
            for i in json_data['goods_imgs']['detail_image']:
                img.append(i['origin_image'])

            l = []
            for i in json_data['detail']['productDetails']:
                l.append((i['attr_name'], i['attr_name_en'], i['attr_value'], i['attr_value_en']))

        self.book.save('test.xlsx')


self = CollectPosts()

'''
https://ar.shein.com/Twist-Bishop-Sleeve-Split-Thigh-Dress-p-3072531-cat-1727.html?scici=navbar_WomenHomePage_%18X%0C%5B%5D%5C%1BY%5BL%0C%1A%5C%0CE55A%7C~0
'''