import traceback
from time import sleep

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import random

from selenium.webdriver.support.wait import WebDriverWait

from codes import script
from codes.error import error_Text


class SenderNumber(QThread):
    tableWidget_3: QTableWidget
    driver: WebDriver
    error = Signal(object)
    final = Signal()
    driver_error = Signal()
    final_message = Signal()
    limit_message = Signal()
    Try = False
    pause = False
    stop = False
    eer = False

    def safe_find_element_by(self, by, elem):
        try:
            return self.driver.find_element(by, elem)
        except NoSuchElementException:
            return None

    @staticmethod
    def com(phone):
        return '''
        if (!document.querySelector('header > a')){
        header = document.querySelector('header');
        newlink = document.createElement('a');
        header.appendChild(newlink);
        }
        a = document.querySelector('header > a');
        a.setAttribute('href', ''' + f'"https://web.whatsapp.com/send?phone={phone}&text&app_absent=0"' + ''');
        document.querySelector('header > a').click()
        '''

    def run(self):
        state = ''
        sleep(1)
        if self.driver or self.check_live():
            self.Try = True
            try:
                sleep_time_2 = int(self.spinBox_2.text())
                sleep_time_1 = int(self.spinBox_4.text())
            except:
                sleep_time_1 = 2
                sleep_time_2 = 4
            try:
                sleep_time = random.choice(range(sleep_time_1, sleep_time_2))
            except:
                sleep_time = 10

            for i in range(self.tableWidget_3.rowCount()):
                if self.limit and self.limit <= i:
                    self.limit_message.emit()
                    break
                # if self.pause is True:
                while self.pause:
                    if self.stop:
                        break
                    sleep(1)

                if self.stop:
                    break

                number = self.tableWidget_3.item(i, 0).text().strip()

                if number == '':
                    continue
                self.tableWidget_3.item(i, 0).setSelected(True)

                for im in range(self.tableWidget_4.rowCount()):

                    if not self.tableWidget_4.item(im, 2):
                        continue

                    # self.tableWidget_4.item(im, 0).setSelected(True)
                    if self.tableWidget_4.item(im, 2).text().strip() == 'text':
                        text = self.tableWidget_4.item(im, 0).text().strip()
                        state = self.send_text(number, text)

                    elif self.tableWidget_4.item(im, 2).text().strip() == 'img':
                        img = self.tableWidget_4.item(im, 1).text().strip()
                        try:
                            text = self.tableWidget_4.item(im, 0).text().strip()
                        except:
                            text = None
                        state = self.send_img(number, img, text)
                    # self.tableWidget_4.item(im, 0).setSelected(False)

                self.tableWidget_3.setItem(i, 1, QTableWidgetItem(str(state)))
                self.tableWidget_3.item(i, 0).setSelected(False)
                sleep(sleep_time)
            if not self.eer:
                self.final_message.emit()
        else:
            self.driver_error.emit()
        self.Try = False
        self.final.emit()

    def check_number(self):
        sleep(1)
        return False if len(
            self.driver.find_elements_by_css_selector('div[data-animate-modal-body="true"]')) > 0 else True

    def send_text(self, number, text):
        try:
            self.driver.execute_script(self.com(number))
            sleep(2)

        except Exception as e:
            error_Text(traceback.format_exc())
            self.error.emit(e)
            self.eer = True
            self.driver_error.emit()
            self.Stop()
            return 'لم يتم الارسال'

        try:
            element = WebDriverWait(self.driver, 20).until(
                (ec.presence_of_element_located((By.CSS_SELECTOR,
                                                 '#main .copyable-area .copyable-text.selectable-text[contenteditable="true"]'))))
            self.driver.execute_script(script, element, text)
            sleep(2)
            element.send_keys(Keys.ENTER)
            return 'تم الارسال'
        except:
            error_Text(traceback.format_exc())
            return 'لم يتم الارسال'

    def send_img(self, number, img, text):
        try:
            self.driver.execute_script(self.com(number))
        except:
            self.eer = True
            self.driver_error.emit()
            self.Stop()
            error_Text(traceback.format_exc())
            return 'لم يتم الارسال'

        try:

            WebDriverWait(self.driver, 10).until(
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
            sleep(1)
            element.send_keys(Keys.ENTER)

            return 'تم الارسال'

        except:
            error_Text(traceback.format_exc())
            return 'لم يتم الارسال'

    def Stop(self):
        self.stop = True
