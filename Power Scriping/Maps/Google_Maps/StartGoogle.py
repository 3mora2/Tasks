import traceback
import typing
from time import sleep
import PySide2
from PySide2.QtCore import QThread, Signal
from selenium.webdriver.common.by import By
from PySide2.QtWidgets import QTableWidgetItem
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StartGoogle(QThread):
    driver: WebDriver
    final = Signal(object)
    error = Signal()
    error_driver = Signal()
    pause = False
    stop = False
    skip = False
    data: dict

    def __init__(self):
        super().__init__()
        self.urls = set()
        self.data = dict()

    def run(self):
        if self.check():
            self.open(self.text)
            if not self.stop:
                self.extract()
        else:
            self.error_driver.emit()

        self.final.emit(self.data)

    def open(self, txt):
        current_n = 0
        current_n_n = 0
        self.driver.get(f'https://www.google.com/maps/search/{txt}')
        print('Program is loading,please wait!')
        sleep(5)
        while True:
            while self.pause:
                if self.stop:
                    break
                if self.skip:
                    break
                sleep(1)

            if self.stop:
                break

            if self.skip:
                break

            num_scroll = 0
            while True:
                try:
                    _ = self.driver.find_element_by_css_selector('.wo1ice-loading').location_once_scrolled_into_view
                    sleep(5)
                    num_scroll += 1

                    if num_scroll > 5:
                        print('- Break Scroll..')
                except Exception as e:
                    # print(e)
                    break

            sleep(3)
            num_pl = len(self.driver.find_elements_by_css_selector('div.section-layout.section-scrollbox div > a'))
            if num_pl == 0:
                break

            old_number = [self.tableWidget.item(i, 0).text() for i in range(self.tableWidget.rowCount())]
            for element in self.driver.find_elements_by_css_selector('div.section-layout.section-scrollbox div>a'):
                self.urls.add(element.get_attribute('href'))
                if element.get_attribute('href') not in old_number:
                    r = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(r)
                    self.tableWidget.setItem(r, 0, QTableWidgetItem(str(element.get_attribute('href'))))

            print(len(self.urls))

            try:
                if self.driver.find_element_by_css_selector(
                        'button[jsaction="pane.paginationSection.nextPage"]').get_attribute('disabled') == 'true':
                    break

                try:
                    self.driver.execute_script('document.querySelector(\'*[aria-label="الصفحة التالية"]\').click()')
                except:
                    self.driver.execute_script(
                        'document.querySelector(\'button[jsaction="pane.paginationSection.nextPage"]\').click()')
                sleep(5)
            except:
                break

            if len(self.urls) != current_n:
                current_n = len(self.urls)
                current_n_n = 0

            else:
                current_n_n += 1
            if current_n_n > 3:
                break

    def extract(self):
        num = 2
        for url in self.urls:
            while self.pause:
                if self.stop:
                    break
                sleep(1)

            if self.stop:
                break
            try:
                self.driver.get(url)
                sleep(4)
                try:
                    main_photo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                        By.CSS_SELECTOR,
                        'button[jsaction="pane.heroHeaderImage.click"] > img'))).get_attribute(
                        'src')
                except:
                    main_photo = None

                try:
                    rat = ''.join(set(rat.get_attribute('aria-label') for rat in
                                      self.driver.find_elements_by_css_selector('ol')
                                      if rat.get_attribute('aria-label') is not None)).replace('stars', '').strip()
                except:
                    try:
                        _ = self.driver.find_element_by_css_selector(
                            '[jsaction="pane.reviewChart.moreReviews"] .gm2-display-2').location_once_scrolled_into_view
                        rat = self.driver.find_element_by_css_selector(
                            '[jsaction="pane.reviewChart.moreReviews"] .gm2-display-2').text
                    except:
                        rat = None
                try:
                    comment = list(set(rat.get_attribute('aria-label') for rat in
                                       self.driver.find_elements_by_css_selector('[jsaction="pane.rating.moreReviews"]')
                                       if rat.get_attribute('aria-label') is not None))[0]
                except:
                    comment = None

                name = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//h1/span[1]'))).text
                try:
                    ty = self.driver.find_element_by_css_selector('[jsaction="pane.rating.category"]').text
                except:
                    ty = None
                try:
                    phone = \
                        self.driver.find_element_by_xpath(
                            "//div/button[contains(@data-item-id, 'phone:')]").get_attribute(
                            'data-item-id').split('tel:')[-1]
                except:
                    phone = None
                try:
                    address = \
                        self.driver.find_element_by_xpath(
                            "//div/button[contains(@data-item-id, 'address')]").get_attribute(
                            'aria-label').split(":")[-1]
                except:
                    address = None
                try:
                    web = \
                        self.driver.find_element_by_xpath(
                            "//div/button[contains(@data-item-id, 'authority')]").get_attribute(
                            'aria-label').split(":")[-1]
                except:
                    web = None
                try:
                    cont = \
                        self.driver.find_element_by_css_selector('[data-item-id="oloc"]').get_attribute(
                            'aria-label').split(
                            ':')[-1]
                except:
                    cont = None
                try:
                    opened = self.driver.find_element_by_xpath("//div[contains(@jsaction, 'pane.openhours')]").text
                except:
                    opened = None
                try:
                    address_num = '@' + ','.join(
                        self.driver.find_element_by_css_selector('link[rel="shortcut icon"]+script').get_attribute(
                            'innerText').split('/@')[1].split(',')[:2])
                except Exception as e:
                    print(e)
                    address_num = None

                if self.open_url:
                    try:
                        if len(self.driver.find_elements_by_xpath(
                                "//div/button[contains(@data-item-id, 'authority')]")):
                            self.driver.execute_script(
                                'document.querySelector("[data-item-id=\'authority\'] [dir=\'ltr\']").click();')
                            sleep(3)
                            if len(self.driver.window_handles) > 1:
                                self.driver.close()
                                self.driver.switch_to.window(self.driver.window_handles[-1])
                                web = self.driver.current_url
                            else:
                                pass
                    except:
                        pass

                self.data[num] = {
                    'name': name,
                    'ty': ty,
                    'web': web,
                    'rat': rat,
                    'comment': comment,
                    'address': address,
                    'cont': cont,
                    'phone': phone,
                    'main_photo': main_photo,
                    'opened': opened,
                    'address_num': address_num,
                    'url': url
                }
                print(num - 1, len(self.urls))

                r = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(r)
                self.tableWidget_2.setItem(r, 0, QTableWidgetItem(str(name)))
                self.tableWidget_2.setItem(r, 1, QTableWidgetItem(str(phone)))

                num += 1
            except Exception as e:
                print(e)

        print('- Done....', end='\r')
