from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd


def print_percent_done(index, total, bar_len=50):
    percent_done = index / total * 100
    percent_done = round(percent_done, 1)

    done = round(percent_done / (100 / bar_len))
    togo = bar_len - done

    done_str = '█' * int(done)
    togo_str = '░' * int(togo)

    print(f'- ⏳ {total}\\{index} - [{done_str}{togo_str}] ({percent_done} %)', end='\r')


class CollectPosts(object):
    def __init__(self):
        print('- Start')
        self.drivers = set()
        self.user_data = os.path.expanduser("~") + r'\AppData\Local\Google\Chrome\User Data'
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-plugins')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument(f"--user-data-dir={self.user_data}")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://web.mobeasy.com/#/')

    def open_page_audio(self):
        element = self.driver.find_element(By.XPATH,
                                           './/flt-picture[flt-canvas/img[contains(@src,"https://web.mobeasy.com/assets/assets/images/ic_audio.svg")]]/following::flt-clip[1]')
        self.do_action(element)

    def do_action(self, element, text=None):
        actions = ActionChains(self.driver)
        if text:
            actions.send_keys_to_element(element, text).perform()
        else:
            actions.click(element).perform()

    def check_url(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR,
                                             'body > flt-glass-pane > flt-scene-host > flt-scene > flt-transform > flt-offset > flt-offset > flt-clip > flt-clip-interior > flt-clip:nth-child(1) > flt-clip-interior > flt-offset > flt-clip > flt-clip-interior > flt-offset:nth-child(4) > flt-picture > flt-canvas > p'))

    def close_x(self):
        if len(self.driver.find_elements_by_xpath('//flt-transform/flt-picture[2]/flt-canvas/canvas')):
            element = self.driver.find_element_by_xpath('//flt-transform/flt-picture[2]/flt-canvas/canvas')
            self.do_action(element)

    def send_text(self, url, text):
        if self.check_url() == 0:
            self.tern_to_url()
            sleep(1)

        element = self.driver.find_element(By.CSS_SELECTOR,
                                           'body > flt-glass-pane > flt-scene-host > flt-scene > flt-transform > flt-offset > flt-offset > flt-clip > flt-clip-interior > flt-clip:nth-child(1) > flt-clip-interior > flt-offset > flt-clip > flt-clip-interior > flt-offset:nth-child(4) > flt-picture > flt-canvas > p')
        self.do_action(element, url)

        sleep(1)
        try:
            element = self.driver.find_element(By.CSS_SELECTOR,
                                               'body > flt-glass-pane > flt-scene-host > flt-scene > flt-transform > flt-offset > flt-offset > flt-clip > flt-clip-interior > flt-clip:nth-child(1) > flt-clip-interior > flt-offset > flt-clip > flt-clip-interior > flt-offset:nth-child(14) > flt-picture > flt-canvas > p')
            self.do_action(element, text)
        except:
            element = self.driver.find_element(By.CSS_SELECTOR,
                                               'flt-offset > flt-picture > flt-canvas > draw-rect')
            self.do_action(element, 'text')

    def tern_to_url(self):
        try:
            element = self.driver.find_element(By.XPATH, '//p[*[contains(text(),"رابط")]]')
            self.do_action(element)
            return True
        except:
            return False

    def save_change(self):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR,
                                               'flt-clip-interior > flt-transform > flt-clip > flt-clip-interior > flt-picture > flt-canvas p')
            self.do_action(element)
        except:
            element = self.driver.find_element(By.CSS_SELECTOR,
                                               'flt-clip-interior > flt-transform > flt-clip > flt-clip-interior > flt-picture > flt-canvas')
            self.do_action(element)

    def load_file(self, sheet):
        for index, value in enumerate(sheet.values):
            link = value[u]
            title = value[t]
            print_percent_done(index, len(sheet))
            self.close_x()
            sleep(1)
            self.open_page_audio()
            sleep(1)
            r = self.tern_to_url()
            if not r:
                self.open_page_audio()
                self.tern_to_url()
            sleep(1)
            self.send_text(link, title)
            sleep(1)
            self.save_change()
            sleep(1)


if __name__ == '__main__':
    file_name = None
    df = []
    self = CollectPosts()
    while True:
        if input('- Enter: ') == 'q':
            break
        while True:
            try:
                file_name = input('- Enter file name : ')  # 'Book1.xlsx'
                if file_name == 'q':
                    break
                data = pd.read_excel(file_name)
                df = data.dropna(axis='columns', how='all')

                first = input('- 1 >>> if URL first: ')
                if first == '1':
                    u = 0
                    t = 1
                else:
                    u = 1
                    t = 0
                break
            except FileNotFoundError:
                print('- No such file or directory')
            except Exception as e:
                print(e)

        if file_name == 'q':
            break
        self.load_file(df)
