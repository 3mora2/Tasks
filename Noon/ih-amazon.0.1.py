import os

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import subprocess
import csv
from time import sleep
from requests_html import HTMLSession

s = HTMLSession()


class Main:
    PRODUCT_URL = 'https://sellercentral.amazon.sa/skucentral?mSku={}&ref=myi_skuc'
    IH_URL = 'https://www.iherb.com/search?kw='

    def __init__(self):
        # chrome_options = Options()
        # try:
        #     subprocess.Popen(
        #         '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222')
        # except:
        #     subprocess.Popen(
        #         '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222')
        # chrome_options.add_argument("--disable-infobars")
        # chrome_options.add_argument("--disable-notifications")
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"

        self.driver = webdriver.Chrome(desired_capabilities=caps, executable_path=ChromeDriverManager().install())#, chrome_options=chrome_options)
        self.driver.get('https://sellercentral.amazon.sa/home')
        sleep(3)

    def read_txt(self, file):
        error = []
        _dict = dict()
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            first = True
            n = 0
            for i in csv_reader:
                if first:
                    first = False
                    continue

                n += 1

                try:
                    r = s.get(self.IH_URL + i[0], timeout=1)
                    static = 'Out' in r.html.find('div.product-inner.product-inner-wide meta+link', first=True
                                                  ).attrs['href']
                except:
                    error.append(i)
                    static = None

                if static and float(i[3]) > 0:
                    _dict[i[0]] = 0
                    print(n, i[0], 'Out')
                elif not static and float(i[3]) == 0:
                    _dict[i[0]] = 36
                    print(n, i[0], 'update to 36')
                else:
                    print(n, i[0], static)

            for i in error:
                try:
                    sleep(2)
                    r = s.get(self.IH_URL + i[0])
                    static = 'Out' in r.html.find('div.product-inner.product-inner-wide meta+link', first=True
                                                  ).attrs['href']
                except:
                    static = None

                if static and float(i[3]) > 0:
                    _dict[i[0]] = 0
                    print(i[0], 'Out')
                elif not static and float(i[3]) == 0:
                    _dict[i[0]] = 36
                    print(i[0], 'update to 36')
                else:
                    print(i[0], static)

        return _dict

    def start(self, file):
        _dict = self.read_txt(file)
        for key in _dict:
            self.driver.get(self.PRODUCT_URL.format(key))
            sleep(4)
            try:
                WebDriverWait(self.driver, 10).until(
                    (ec.element_to_be_clickable((By.CSS_SELECTOR, '#INVENTORY_CARD > div ~ div a')))).click()
                sleep(1)
                WebDriverWait(self.driver, 10).until(
                    (ec.visibility_of_element_located((By.CSS_SELECTOR, 'kat-input > input')))).clear()
                sleep(1)
                WebDriverWait(self.driver, 10).until(
                    (ec.visibility_of_element_located((By.CSS_SELECTOR, 'kat-input > input')))).send_keys(str(_dict[key]))
                sleep(1)
                WebDriverWait(self.driver, 10).until(
                    (ec.element_to_be_clickable((By.CSS_SELECTOR, 'kat-popover > kat-popover-anchor > a')))).click()
                sleep(3)
            except:
                print('- Not found')
        self.driver.quit()


if __name__ == '__main__':
    while True:
        try:
            file_name = input('- Enter file name : ')  # 'Book1.xlsx'
            if os.path.isfile(file_name) and file_name.endswith('.txt'):
                break
            print('- No such file or directory')
        except FileNotFoundError:
            print('- No such file or directory')
        except Exception as e:
            print(e)
    app = Main()
    input('- Enter...')
    app.start(file_name)

# Assad098765
# bh2030098765@gmail.com
# pyinstaller --add-data C:/Users/3mora/AppData/Local/Programs/Python/Python39/Lib/site-packages/pyppeteer-0.2.5.dist-info;pyppeteer-0.2.5.dist-info
