import os
import sys
import warnings

from openpyxl.worksheet.worksheet import Worksheet
from selenium import webdriver
from openpyxl import Workbook
from openpyxl.styles import Alignment
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager
os.environ['WDM_LOG_LEVEL'] = '0'
if not sys.warnoptions:
    warnings.simplefilter("ignore")


class Main:
    url: object = None
    sheet: Worksheet
    book: Workbook

    def __init__(self, limit):
        self.file = 1
        self.save = 0
        self.i = 2
        self.limit = limit
        self.list = []
        profile = webdriver.FirefoxProfile()
        # 1 - Allow all images
        # 2 - Block all images
        # 3 - Block 3rd party images
        profile.set_preference("permissions.default.image", 2)
        try:
            self.driver = webdriver.Firefox(firefox_profile=profile)
        except:
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)

        self.new_sheet()

    def new_sheet(self):
        self.book = Workbook()
        self.sheet = self.book.active
        self.sheet['A1'].value = 'الاسم'
        self.sheet['B1'].value = "البائع"
        self.sheet['C1'].value = "الرقم"
        self.sheet['D1'].value = "الرابط"

        self.sheet.column_dimensions['A'].width = 30
        self.sheet.column_dimensions['B'].width = 15
        self.sheet.column_dimensions['C'].width = 13
        self.sheet.column_dimensions['D'].width = 70
        self.sheet['A1'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        self.sheet['B1'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        self.sheet['C1'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        self.sheet['D1'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

    def login(self):
        self.driver.get('https://www.olx.com.eg/account/')
        WebDriverWait(self.driver, 10).until(
            (ec.visibility_of_element_located((By.CSS_SELECTOR, '#userEmail')))).send_keys(phone)
        # self.driver.find_element_by_css_selector('#userEmail').send_keys(phone)
        self.driver.find_element_by_css_selector('#userPass').send_keys(password)
        self.driver.find_element_by_css_selector('#se_userLogin').click()
        sleep(6)

    def start(self, url):
        while True:
            self.driver.get(url)
            try:
                self.url = url = WebDriverWait(self.driver, 10).until(
                    (ec.presence_of_element_located((By.CSS_SELECTOR, 'span.item a.pageNextPrev')))).get_attribute(
                    'href')
                break_ = False
            except:
                break_ = True
            self.get_prod()
            if break_:
                break

    def get_prod(self):
        l = []
        for ele in self.driver.find_elements_by_css_selector('div.ads__item > div:nth-child(2) > a:nth-child(1)'):
            try:
                if ele.get_attribute('href') not in self.list:
                    self.list.append(ele.get_attribute('href'))
                    l.append(ele.get_attribute('href'))
            except:
                pass
        for u in l:
            try:
                self.driver.get(u)
                sleep(2)
                name = self.driver.find_element_by_css_selector('h1.brkword').text
                try:
                    user = self.driver.find_element_by_css_selector('.user-box__info__name').text
                except:
                    user = None

                try:
                    WebDriverWait(self.driver, 5).until(
                        (ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.contactbox-indent')))).click()
                    # self.driver.find_element_by_css_selector('div.contactbox-indent').click()
                    sleep(1)
                    try:
                        while True:
                            number = self.driver.find_element_by_css_selector('div.contactbox-indent').text.replace(' ',
                                                                                                                    '').strip()
                            if 'x' not in number:
                                break
                    except:
                        number = None
                except:
                    number = None
                self.sheet[f'A{self.i}'].value = name
                self.sheet[f'A{self.i}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

                self.sheet[f'B{self.i}'].value = user
                self.sheet[f'B{self.i}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

                self.sheet[f'C{self.i}'].value = number
                self.sheet[f'C{self.i}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

                self.sheet[f'D{self.i}'].value = u
                self.sheet[f'D{self.i}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

                print(self.i, '-', self.list.__len__(), ' - ', number)

                self.i += 1
                self.save += 1

            except Exception as e:
                print(e)

        if self.save >= self.limit:
            self.sheet[f'F{self.i}'].value = self.url
            self.book.save(f'{self.file}-olx.xlsx')
            self.save = 0
            self.new_sheet()
            self.file += 1
            self.i = 2


if __name__ == '__main__':
    phone = input('Enter your phone number : ')
    password = input('Enter password : ')
    url_ = input('Enter URL : ')
    try:
        file = int(input('Enter Save Number : '))
    except:
        file = 500
    self = Main(file)
    self.login()
    input('- Enter: ')
    self.start(url_)
# 'https://www.olx.com.eg/ads/?search%5Buser_id%5D=112424099&search%5Border%5D=filter_float_price%3Aasc')
# https://www.olx.com.eg/properties/apartments-duplex-for-rent/?view=list
# 201028946519
# ammar2016
