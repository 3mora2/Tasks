from random import choice
from time import sleep

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from codes import script


class GroupSender(QThread):
    tableWidget_6: QTableWidget
    tableWidget_7: QTableWidget
    driver: WebDriver
    driver_error = Signal()
    error = Signal(object)
    final_message = Signal()
    final = Signal()
    limit_message = Signal()
    Try = False
    pause = False
    stop = False

    def safe_find_element_by(self, by, elem):
        try:
            return self.driver.find_element(by, elem)
        except NoSuchElementException:
            return None

    def run(self):
        state = ''
        sleep(1)
        if self.driver or self.check_live():
            self.Try = True
            try:
                sleep_time_1 = int(self.spinBox.text())
                sleep_time_2 = int(self.spinBox_3.text())
            except:
                sleep_time_2 = 2
                sleep_time_1 = 5
            try:
                sleep_time = choice(range(sleep_time_2, sleep_time_1))
            except:
                sleep_time = 30

            for i in range(self.tableWidget_6.rowCount()):
                if self.limit and self.limit <= i:
                    self.limit_message.emit()
                    break

                while self.pause:
                    if self.stop:
                        break
                    sleep(1)

                if self.stop:
                    break

                number = self.tableWidget_6.item(i, 0).text().strip()

                if number == '':
                    continue
                self.tableWidget_6.item(i, 0).setSelected(True)

                for im in range(self.tableWidget_7.rowCount()):

                    if not self.tableWidget_7.item(im, 2):
                        continue

                    # self.tableWidget_7.item(im, 0).setSelected(True)
                    if self.tableWidget_7.item(im, 2).text().strip() == 'text':
                        text = self.tableWidget_7.item(im, 0).text().strip()
                        state = self.send_text(number, text)

                    elif self.tableWidget_7.item(im, 2).text().strip() == 'img':
                        img = self.tableWidget_7.item(im, 1).text().strip()
                        try:
                            text = self.tableWidget_7.item(im, 0).text().strip()
                        except:
                            text = None
                        state = self.send_img(number, img, text)

                    # self.tableWidget_7.item(im, 0).setSelected(False)

                self.tableWidget_6.setItem(i, 1, QTableWidgetItem(str(state)))
                self.tableWidget_6.item(i, 0).setSelected(False)
                sleep(sleep_time)
            self.final_message.emit()
        else:
            self.driver_error.emit()
        self.Try = False
        self.final.emit()

    def open_name(self, name):

        self.driver.find_element_by_css_selector('#side .copyable-text.selectable-text').send_keys(Keys.CONTROL, 'a',
                                                                                                   Keys.BACKSPACE)
        self.driver.find_element_by_css_selector('#side .copyable-text.selectable-text').clear()
        element = self.driver.find_element_by_css_selector('#side .copyable-text.selectable-text')
        self.driver.execute_script(script, element, name)
        self.driver.find_element_by_css_selector('#side .copyable-text.selectable-text').send_keys(Keys.SPACE)

        sleep(1)
        xpath_1 = f'//div[@role="row"]/div[@data-testid="cell-frame-container"]/div//div[@role="gridcell"]//span[contains(@title, "{name}")]'

        xpath_2 = f'//div[div[@role="row"]] //div/span[contains(@title, "{name}")]'
        try:
            element = WebDriverWait(self.driver, 30).until((ec.presence_of_element_located((By.XPATH, xpath_1))))
            actions = ActionChains(self.driver)
            actions.click(element).perform()
            return True
        except:
            try:
                element = WebDriverWait(self.driver, 20).until((ec.presence_of_element_located((By.XPATH, xpath_2))))
                actions = ActionChains(self.driver)
                actions.click(element).perform()
                return True
            except:
                pass

        return False

    def send_text(self, name, text):
        if self.open_name(name):
            try:
                element = WebDriverWait(self.driver, 5).until(
                    (ec.presence_of_element_located((By.CSS_SELECTOR,
                                                     '#main .copyable-area .copyable-text.selectable-text[contenteditable="true"]'))))
                self.driver.execute_script(script, element, text)

                sleep(2)
                element.send_keys(Keys.ENTER)

                return 'تم الارسال'

            except:
                pass

        return 'لم يتم الارسال'

    def send_img(self, name, img, text):
        if self.open_name(name):
            try:
                WebDriverWait(self.driver, 5).until(
                    (ec.element_to_be_clickable(
                        (By.CSS_SELECTOR, 'div[role="button"][title="إرفاق"]')))).click()
                WebDriverWait(self.driver, 5).until(
                    (ec.presence_of_element_located(
                        (By.CSS_SELECTOR, '[data-testid="attach-image"]+input')))).send_keys(img)
                sleep(1)

                element = WebDriverWait(self.driver, 5).until(
                    (ec.visibility_of_element_located(
                        (By.XPATH, '//div[//*[@data-icon="emoji-input"]]/div/div[@role="textbox"]'))))
                if text:
                    self.driver.execute_script(script, element, text)
                sleep(2)
                element.send_keys(Keys.ENTER)

                return 'تم الارسال'
            except:
                pass

        return 'لم يتم الارسال'

    def Stop(self):
        self.stop = True
