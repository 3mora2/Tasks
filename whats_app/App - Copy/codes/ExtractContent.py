import traceback
from time import sleep

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from codes.error import error_Text


class ExtractContent(QThread):
    tableWidget_5: QTableWidget
    tableWidget_10: QTableWidget
    driver: WebDriver
    error = Signal(object)
    driver_error = Signal()
    final_message = Signal()
    final = Signal()
    limit_message = Signal()
    Try = False
    stop = False

    def safe_find_element_by(self, by, elem):
        try:
            return self.driver.find_element(by, elem)
        except NoSuchElementException:
            return None

    def run(self):
        self.Try = True
        self.stop = False
        cont = True
        if self.driver or not self.check_live():
            try:

                list_num = []
                old = 0
                error = 0
                while cont:
                    if self.stop:
                        break
                    r = self.tableWidget_5.rowCount()
                    if self.limit and self.limit <= r:

                        self.limit_message.emit()
                        break

                    for element in self.driver.find_elements_by_xpath('//div/div[@role="row"]'):
                        if self.stop:
                            break
                        # text = element.find_element_by_css_selector('div[role="gridcell"] > div > span').text
                        text = element.find_elements_by_css_selector('div[role="gridcell"] > div  span')[-1].get_attribute('title')
                        if "default-group" in element.find_element_by_css_selector('span').get_attribute('data-testid'):
                            old_number = [self.tableWidget_5.item(i, 0).text() for i in
                                          range(self.tableWidget_5.rowCount())]
                            if text in old_number:
                                continue

                            r = self.tableWidget_5.rowCount()
                            if self.limit and self.limit <= r:
                                break
                            self.tableWidget_5.insertRow(r)
                            self.tableWidget_5.setItem(r, 0, QTableWidgetItem(str(text)))

                        elif text.strip().find('+') >= 0:
                            text = text.replace('⁩', '').replace('⁦', '').replace(' ', '')
                            old_number = [self.tableWidget_10.item(i, 0).text() for i in
                                          range(self.tableWidget_10.rowCount())]
                            if text in old_number:
                                continue

                            r = self.tableWidget_10.rowCount()
                            self.tableWidget_10.insertRow(r)
                            self.tableWidget_10.setItem(r, 0, QTableWidgetItem(str(text)))
                        else:
                            old_number = [self.tableWidget_11.item(i, 0).text() for i in
                                          range(self.tableWidget_11.rowCount())]
                            if text in old_number:
                                continue

                            r = self.tableWidget_11.rowCount()
                            self.tableWidget_11.insertRow(r)
                            self.tableWidget_11.setItem(r, 0, QTableWidgetItem(str(text)))

                        if text not in list_num:
                            list_num.append(text)

                    if old == list_num.__len__():
                        error += 1
                        sleep(1)
                        print('-same')
                    else:
                        error = 0
                    if error == 2:
                        break
                    old = list_num.__len__()
                    self.driver.find_element_by_xpath('//div[@id="pane-side"]/ div[.//div[@role="row"]]').send_keys(
                        Keys.PAGE_DOWN)
                    sleep(1)
                self.final_message.emit()

            except Exception as a:
                self.error.emit(a)
                error_Text(traceback.format_exc())
        else:
            self.driver_error.emit()
        self.Try = False
        self.final.emit()
