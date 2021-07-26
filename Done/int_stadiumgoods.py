import json
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
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir={}".format(r'C:\Users\3mora\AppData\Local\Google\Chrome\User Data'))
        # chrome_options.add_argument('--profile-directory=Profile 4')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    def start(self, urls):
        num = 2
        for url in urls:
            self.driver.get(url)
            sleep(6)
            input('- ')
            data = self.driver.execute_script("return document.querySelector('#root + script').text")

            json_data = json.loads(data.replace('window.__PRELOADED_STATE__ = ', ''))
            key = [key for key in json_data['entities']['products'].keys()][0]
            img = set(img['sources']['2048'] for img in json_data['entities']['products'][key]['images'])
            desk = json_data['entities']['products'][key]['description']
            sku = json_data['entities']['products'][key]['sku']
            brand = self.driver.find_element_by_css_selector('div.product-brand').text
            product_name = self.driver.find_element_by_css_selector('h1.product-name').text

            # try:
            #     self.driver.find_element_by_css_selector('p > button.e1q51ql11').click()
            # except:
            #     pass
            # dsk = self.driver.find_element_by_css_selector('[data-test="productDescriptionContainer"]').text.replace('READ MORE', '').text.replace('READ LESS', '')
            self.driver.find_element_by_css_selector('[data-test="pdp-dropdown-button"]').click()
            sleep(1)
            for size in self.driver.find_elements_by_css_selector('.product-shop.css-gluvp2.em3pm8o3 > label'):
                try:
                    if 'UK' in size.find_element_by_css_selector('div.css-1962bhi.euap27q7').text:
                        continue
                except:
                    pass

                name = re.findall(r'\d{1,3}.\d{1,3}|\d{1,3}', size.find_element_by_css_selector('span.euap27q4').text)[0]
                print(name)
                if float(name) > 13:
                    continue
                # price = size.find_element_by_css_selector('input').get_attribute('data-price')
                price = size.find_element_by_css_selector('div > span').text
                self.sheet.cell(num, 1).value = product_name
                self.sheet.cell(num, 2).value = brand
                self.sheet.cell(num, 3).value = sku
                self.sheet.cell(num, 4).value = name
                self.sheet.cell(num, 5).value = price
                self.sheet.cell(num, 6).value = desk
                c = 7
                for i in img:
                    self.sheet.cell(num, c).value = i
                    c += 1
                num += 1

        self.book.save('test.xlsx')


sheet = load_workbook('file.xlsx').active
urls = [sheet.cell(i, 1).value for i in range(1, sheet.max_row+1) if sheet.cell(i, 1).value]
self = CollectPosts()
self.start(urls)