import traceback
from time import sleep

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

from codes.error import error_Text


class TestNumber(QThread):
    tableWidget_2: QTableWidget
    tableWidget_8: QTableWidget
    tableWidget_9: QTableWidget
    driver: WebDriver
    error = Signal(object)
    driver_error = Signal()
    final = Signal()
    final_message = Signal()
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
        if self.driver or self.check_live():
            self.Try = True
            for i in range(self.tableWidget_2.rowCount()):
                print(i)
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

                number = self.tableWidget_2.item(i, 0).text().strip()
                # if self.tableWidget_2.item(i, 1) is not None or number == '':
                if number == '':
                    continue

                self.tableWidget_2.item(i, 0).setSelected(True)
                try:
                    com = '''
                    if (!document.querySelector('header > a')){
                    header = document.querySelector('header');
                    newlink = document.createElement('a');
                    header.appendChild(newlink);
                    }
                    a = document.querySelector('header > a');''' + f'''
                    a.setAttribute('href', 'https://web.whatsapp.com/send?phone={number}&text&app_absent=0');
                    ''' + '''
                    document.querySelector('header > a').click()
                    '''
                    self.driver.execute_script(com)
                    sleep(.5)
                    sleep(self.sleep)
                    if not len(self.driver.find_elements_by_css_selector('div[data-animate-modal-body="true"]')) or \
                            'ستبد' in self.driver.find_element_by_css_selector(
                                                                            'div[data-animate-modal-body="true"]').text:
                        old_number = [self.tableWidget_8.item(i, 0).text() for i in
                                      range(self.tableWidget_8.rowCount())]
                        if number not in old_number:
                            r = self.tableWidget_8.rowCount()
                            self.tableWidget_8.insertRow(r)
                            self.tableWidget_8.setItem(r, 0, QTableWidgetItem(str(number)))

                            # state = 'موجود'
                    else:
                        old_number = [self.tableWidget_9.item(i, 0).text() for i in
                                      range(self.tableWidget_9.rowCount())]
                        if number not in old_number:
                            r = self.tableWidget_9.rowCount()
                            self.tableWidget_9.insertRow(r)
                            self.tableWidget_9.setItem(r, 0, QTableWidgetItem(str(number)))
                    print(number)

                        # state = 'غير موجود'
                # self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(state)))
                # sleep(self.sleep)

                except Exception as a:
                    self.error.emit(a)
                    error_Text(traceback.format_exc())
                self.tableWidget_2.item(i, 0).setSelected(False)
            self.final_message.emit()
        else:
            self.driver_error.emit()
        self.Try = False
        self.final.emit()

    def Stop(self):
        self.stop = True
