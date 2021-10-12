import traceback
from time import sleep
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QTableWidgetItem, QTableWidget
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait

from codes import script


class AddMembers(QThread):
    tableWidget_12: QTableWidget
    driver: WebDriver
    error = Signal(object)
    final = Signal()
    driver_error = Signal()
    final_message = Signal()
    limit_message = Signal()
    error_group = Signal()
    Try = False
    pause = False
    stop = False
    eer = False
    is_open_add = False

    def open_add(self):
        try:
            try:
                WebDriverWait(self.driver, 2).until((ec.presence_of_element_located(
                    (By.CSS_SELECTOR, '[role="button"]+div[data-testid="cell-frame-container"]')))).click()
            except:
                WebDriverWait(self.driver, 5).until(
                    (ec.presence_of_element_located((By.CSS_SELECTOR, 'div[role="button"]+div[role="button"]')))).click()
                sleep(1)
                WebDriverWait(self.driver, 5).until((ec.presence_of_element_located(
                    (By.CSS_SELECTOR, '[role="button"]+div[data-testid="cell-frame-container"]')))).click()
            self.is_open_add = True
            sleep(1)
        except Exception as e:
            print(e)
            return False

    def run(self):
        self.is_open_add = False
        self.eer = False
        if self.driver or self.check_live():
            self.Try = True

            num = 0
            for i in range(self.tableWidget_12.rowCount()):
                if self.limit and self.limit <= i:
                    self.limit_message.emit()
                    break

                while self.pause:
                    if self.stop:
                        break
                    sleep(1)

                if self.stop:
                    break

                number = self.tableWidget_12.item(i, 0).text().strip()
                if number == '':
                    continue

                if not self.is_open_add:
                    self.open_add()

                if self.is_open_add:
                    state = self.add(number)
                else:
                    self.error_group.emit()
                    self.eer = True
                    break
                num += 1

                self.tableWidget_12.setItem(i, 1, QTableWidgetItem(str(state)))
                if num >= self.number_ber_once:
                    self.save()
                    sleep(1)
                    num = 0

                # self.is_open_add = False
            if self.is_open_add:
                self.save()
            if not self.eer:
                self.final_message.emit()
        else:
            self.driver_error.emit()

        self.Try = False
        self.final.emit()

    def Stop(self):
        self.stop = True

    def add(self, number):
        try:
            sleep(1)
            self.driver.find_element_by_css_selector('[role="dialog"] div[role="textbox"]').send_keys(Keys.CONTROL, 'a',
                                                                                                      Keys.BACKSPACE)
            sleep(1)
            element = self.driver.find_element_by_css_selector('[role="dialog"] div[role="textbox"]')
            self.driver.execute_script(script, element, number)
            self.driver.find_element_by_css_selector('[role="dialog"] div[role="textbox"]').send_keys(Keys.SPACE)

            sleep(1)
            self.driver.find_element_by_css_selector(
                '[role="dialog"] span+div div[data-testid="cell-frame-container"] > div > [role="gridcell"]').click()
            sleep(1)
            return 'تم'
        except Exception as e:
            print(e)
            pass
        return 'فشل'

    def save(self):
        try:
            self.driver.find_element_by_css_selector('[role="dialog"] span+div+span [role="button"]').click()
            sleep(2)
            self.driver.find_element_by_css_selector('[role="dialog"] [role="button"]+[role="button"]').click()
            self.is_open_add = False
        except Exception as e:
            print(e)
            pass


# if __name__ == '__main__':
#     self = OpenDriver()
#     self.start()
