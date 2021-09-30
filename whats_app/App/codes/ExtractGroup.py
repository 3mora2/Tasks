import traceback
from time import sleep

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QTableWidgetItem
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from codes.error import error_Text


class ExtractGroup(QThread):
    driver: WebDriver
    error = Signal(object)
    final = Signal()
    driver_error = Signal()
    final_message = Signal()
    not_group = Signal()
    Try = False
    limit_message = Signal()

    def safe_find_element_by(self, by, elem):
        try:
            return self.driver.find_element(by, elem)
        except NoSuchElementException:
            return None

    def run(self):
        self.Try = True
        if self.driver or self.check_live():
            try:
                users = self.safe_find_element_by(By.CSS_SELECTOR, '[role="button"] .selectable-text.copyable-text')
                if users:
                    numbers = users.get_attribute('title').split('،')
                    if numbers.__len__() == 1:
                        sleep(3)
                        users = self.safe_find_element_by(By.CSS_SELECTOR,
                                                          '[role="button"] .selectable-text.copyable-text')
                        if users:
                            numbers = users.get_attribute('title').split('،')
                            if numbers.__len__() == 1:
                                numbers = numbers[0].split(',')

                    if numbers.__len__() > 1:
                        old_number = [self.tableWidget.item(i, 0).text() for i in range(self.tableWidget.rowCount())]
                        for data in numbers:
                            data = data.replace('⁩', '').replace('⁦', '').replace(' ', '')
                            if '+' in data and data not in old_number:
                                r = self.tableWidget.rowCount()
                                if self.limit and self.limit <= r:
                                    self.limit_message.emit()
                                    break
                                self.tableWidget.insertRow(r)
                                self.tableWidget.setItem(r, 0, QTableWidgetItem(str(data)))
                        self.final_message.emit()
                    else:
                        self.not_group.emit()
                        print(' Not Group')
                else:
                    self.not_group.emit()
                    print(' Not Group')

            except Exception as a:
                self.error.emit(a)
                error_Text(traceback.format_exc())
        else:
            self.driver_error.emit()
        self.Try = False
        self.final.emit()
