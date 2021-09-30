import os
import traceback
import uuid
from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import json


class Main:
    URL_IH = 'https://sa.iherb.com/search?kw='
    STOCK_STATUS = (By.CSS_SELECTOR, '#stock-status')

    URL_LOGIN = 'https://login.noon.partners/en/'
    URL_CAT = 'https://catalog.noon.partners/en-sa/noon-catalog'

    MAIL_ELEMENT_SELECTOR = (By.NAME, 'email')
    PASS_ELEMENT_SELECTOR = (By.NAME, 'password')
    BUTTON_LOGIN_ELEMENT_SELECTOR = (By.CSS_SELECTOR, '#formContainer > button')

    SEARCH_INPUT_SELECTOR = (By.CSS_SELECTOR, 'input[type="search"]')
    FIRST_ELEMENT_SELECTOR = (By.CSS_SELECTOR, 'a[href*="/en-sa/noon-catalog/preview/"]')

    DEACTIVE_SCRIPT = 'if (document.querySelector(\'input[id="offerActive"]\').checked == true){document.querySelector(\'input[id="offerActive"]\').click()};'
    ACTIVE_SCRIPT = 'if (document.querySelector(\'input[id="offerActive"]\').checked == false){document.querySelector(\'input[id="offerActive"]\').click()};'

    SAVE_CHANGE_SELECTOR = (By.CSS_SELECTOR, 'div.tabsWrapper ~ div > div.solid')
    SUBMIT_SELECTOR = (By.XPATH,
                       '//div[calss="btnWrapper"]/div[text()="Submit"] | //div[contains(@class,"showAlert")]//div[contains(@class,"solid")][2]')

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver.get('https://sa.iherb.com/')

    def login(self):
        try:
            self.driver.get(self.URL_LOGIN)
            WebDriverWait(self.driver, 5).until(
                (ec.visibility_of_element_located(self.MAIL_ELEMENT_SELECTOR))).send_keys(email)
            WebDriverWait(self.driver, 5).until(
                (ec.visibility_of_element_located(self.PASS_ELEMENT_SELECTOR))).send_keys(password)
            WebDriverWait(self.driver, 5).until(
                (ec.visibility_of_element_located(self.BUTTON_LOGIN_ELEMENT_SELECTOR))).click()
            while True:
                if 'login.noon' not in self.driver.current_url:
                    self.driver.get(self.URL_CAT)
                    break

        except:
            print(traceback.print_exc())
            print('- Login Error')

    def check(self):
        data = test_request()
        self.d = data
        old_data = self.edit_data()
        self.deactivate(data, old_data)
        # out_stock = set()
        # for i in range(2, self.sheet.max_row+1):
        #     code = self.sheet.cell(i, 6).value
        #     if code is not None:
        #         self.driver.get(f'{self.URL_IH}{code}')
        #         sleep(3)
        #         static = WebDriverWait(self.driver, 10).until(
        #             (ec.visibility_of_element_located(self.STOCK_STATUS))).text
        #         if 'متوفر حاليا' in static or 'In Stock' in static:
        #             print(i, code, 'In Stock')
        #             continue
        #         else:
        #             self.sheet.cell(i, 7).value = 'Out Stock'
        #             print(i, code, 'Out Stock')
        #             out_stock.add(code)
        # self.book.save(file)
        # self.deactivate(out_stock)

    def edit_data(self):
        files = [int(f.split('-')[0]) for f in os.listdir() if f.endswith('new.json')]
        files.sort()
        try:
            with open(f'{files[-1]}-new.json',) as fl:
                data_old = json.load(fl)

            return [data_old, files[-1]]

        except Exception as e:
            print(e)
            return [dict(), 0]

    def deactivate(self, stock, old_data):
        action = ''
        nn = old_data[1]
        self.login()
        i = 1
        old_data = old_data[0]
        input('- Enter to .............')
        for code in stock:
            if code in old_data:
                if stock[code] == old_data[code]['now']:
                    old_data[code] = {'static': None, 'now': stock[code]}
                else:
                    if stock[code] == 'InStock':
                        print(code, stock[code],)
                        old_data[code] = {'static': stock[code], 'now': stock[code]}
                        action = self.ACTIVE_SCRIPT
                    elif stock[code] == 'OutStock':
                        old_data[code] = {'static': stock[code], 'now': stock[code]}
                        print(code, stock[code],)
                        action = self.DEACTIVE_SCRIPT
            else:
                if stock[code] == 'InStock':
                    print(code, stock[code], )
                    old_data[code] = {'static': stock[code], 'now': stock[code]}
                    action = self.ACTIVE_SCRIPT
                elif stock[code] == 'OutStock':
                    old_data[code] = {'static': stock[code], 'now': stock[code]}
                    print(code, stock[code], )
                    action = self.DEACTIVE_SCRIPT
            # try:
            #     self.driver.get(self.URL_CAT)
            #     sleep(3)
            #     WebDriverWait(self.driver, 20).until((ec.visibility_of_element_located(self.SEARCH_INPUT_SELECTOR))
            #                                          ).send_keys(code, Keys.ENTER)
            #     sleep(2)
            # except:
            #     print(traceback.print_exc())
            #     continue
            # sleep(1)
            # try:
            #     WebDriverWait(self.driver, 10).until(
            #         ec.visibility_of_element_located(self.FIRST_ELEMENT_SELECTOR)).click()
            #     sleep(4)
            # except:
            #     print('- Not found')
            #     sleep(5)
            #     continue
            #
            # sleep(1)
            # try:
            #     self.driver.execute_script(action)
            # except:
            #     print(traceback.print_exc())
            #
            # try:
            #     WebDriverWait(self.driver, 10).until(
            #         (ec.visibility_of_element_located(self.SAVE_CHANGE_SELECTOR))).click()
            #     sleep(1)
            #     WebDriverWait(self.driver, 10).until((ec.visibility_of_element_located(self.SUBMIT_SELECTOR))).click()
            #     sleep(1)
            # except:
            #     print(traceback.print_exc())
            #     print('Cant Save')

        with open(f'{nn+1}-new.json', 'w') as fl:
            json.dump(old_data, fl)

    # def all_url(self):
    #     new_edit = dict()
    #     cont = 2
    #     in_ = 0
    #     out_ = 0
    #     urls = [element.get_attribute('href') for element in
    #             self.driver.find_elements_by_css_selector('.type-heading a')]
    #     for url in urls:
    #         self.driver.get(url)
    #         sleep(2)
    #         self.number()
    #         next_pag = True
    #         while next_pag:
    #             for ele in self.driver.find_elements_by_css_selector('div.product-inner.product-inner-wide'):
    #                 try:
    #                     code = ele.find_element_by_css_selector('div.absolute-link-wrapper > a').get_attribute(
    #                         'data-part-number')
    #                     if 'InStock' in ele.find_element_by_css_selector('meta+link').get_attribute('href'):
    #                         new_edit[code] = 'InStock'
    #                         in_ += 1
    #                     else:
    #                         out_ += 1
    #                         new_edit[code] = 'OutStock'
    #
    #                     print(f'- {cont} : {code} >>> {new_edit[code]}, IN : {in_}, OUT : {out_}', end='\r')
    #                 except:
    #                     print(traceback.print_exc())
    #                 cont += 1
    #
    #             next_pag = self.next_page()
    #             sleep(1)
    #
    #     return new_edit
    #
    # def get(self, url):
    #     try:
    #         self.driver.get(url)
    #         sleep(4)
    #     except:
    #         print(traceback.print_exc())
    #
    # def next_page(self):
    #     try:
    #         url = self.driver.find_element_by_css_selector('.pagination-next').get_attribute('href')
    #         self.get(url)
    #
    #         return True
    #     except:
    #         return False
    #
    # def number(self):
    #     self.driver.find_element_by_css_selector(
    #         'div.panel-content.border.show-page.text-right > div > div > select').send_keys('48')
    #     sleep(2)


def add_mac():
    try:
        os.remove(str(uuid.getnode()))
    except:
        pass
    try:
        with open(str(uuid.getnode()), 'w+') as file:
            file.write(str(uuid.getnode()))
        os.popen('attrib +h ' + str(uuid.getnode()))
        return True
    except:
        print('delete old file')
        return False


def check_mac():
    try:
        with open(str(uuid.getnode()), 'r') as file:
            text = file.readlines()
        if str(uuid.getnode()) in text:
            return True
        else:
            print('ref')
            return False
    except FileNotFoundError:
        print('ref')
        return False


def test_request():
    new_edit = dict()
    cont = 0
    out_ = 0
    in_ = 0
    s = HTMLSession()
    r = s.get('https://sa.iherb.com/')
    if r.ok:
        urls = ['https://sa.iherb.com' + element.attrs['href'] + '?noi=192' for element in
                r.html.find('.category') if '/c/' in element.attrs['href']]

        for url in urls[-1:]:
            r_ = s.get(url)
            print(url)
            next_pag = True
            while next_pag:
                for ele in r_.html.find('div.product-inner.product-inner-wide'):
                    code = ele.find('div.absolute-link-wrapper > a')[0].attrs['data-part-number']
                    try:
                        static = ele.find('meta+link')[0].attrs['href']
                    except:
                        static = ''
                    if code in new_edit:
                        pass
                    elif 'InStock' in static:
                        new_edit[code] = 'InStock'
                        in_ += 1
                    elif static == '':
                        new_edit[code] = ''
                    else:
                        out_ += 1
                        new_edit[code] = 'OutStock'
                    cont += 1
                print(f'- {cont} , IN : {in_}, OUT : {out_}', end='\r')
                try:
                    url = 'https://sa.iherb.com' + r_.html.find('.pagination-next')[0].attrs['href']
                    r_ = s.get(url)
                    if not r_.ok:
                        sleep(30)
                        r_ = s.get(url)
                except:
                    break

        for elem in new_edit.keys():
            if new_edit[elem] == '':
                r = s.get('https://sa.iherb.com/search?kw=' + elem)
                static = r.html.find('#stock-status')[0].text
                if 'متوفر حاليا' in static or 'In Stock' in static:
                    new_edit[elem] = 'InStock'
                else:
                    new_edit[elem] = 'OutStock'
    else:
        print(r.status_code)

    return new_edit


if __name__ == "__main__":
    email = input('- Enter your email : ')
    password = input('- Enter your password : ')

    app = Main()
    app.check()
