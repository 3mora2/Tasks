import os
import sys
from time import sleep
from typing import Union

from PySide2 import QtCore
from PySide2.QtCore import QMetaObject, QThread, Signal
from PySide2.QtGui import QCursor
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget, QFileDialog, QMessageBox, \
    QTextEdit, QHeaderView, QPushButton, QRadioButton
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
import warnings

os.environ['WDM_LOG_LEVEL'] = '0'
if not sys.warnoptions:
    warnings.simplefilter("ignore")

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class UiLoader(QUiLoader):
    """
    Subclass :class:`~PySide.QtUiTools.QUiLoader` to create the user interface
    in a base instance.
    Unlike :class:`~PySide.QtUiTools.QUiLoader` itself this class does not
    create a new instance of the top-level widget, but creates the user
    interface in an existing instance of the top-level class.
    This mimics the behaviour of :func:`PyQt4.uic.loadUi`.
    """

    def __init__(self, baseinstance, customWidgets=None):

        QUiLoader.__init__(self, baseinstance)
        self.baseinstance = baseinstance
        self.customWidgets = customWidgets

    def createWidget(self, class_name, parent=None, name=''):
        """
        Function that is called for each widget defined in ui file,
        overridden here to populate baseinstance instead.
        """

        if parent is None and self.baseinstance:
            # supposed to create the top-level widget, return the base instance
            # instead
            return self.baseinstance

        else:
            if class_name in self.availableWidgets():
                # create a new widget for child widgets
                widget = QUiLoader.createWidget(self, class_name, parent, name)

            else:
                # if not in the list of availableWidgets, must be a custom widget
                # this will raise KeyError if the user has not supplied the
                # relevant class_name in the dictionary, or TypeError, if
                # customWidgets is None
                try:
                    widget = self.customWidgets[class_name](parent)

                except (TypeError, KeyError) as e:
                    raise Exception(
                        'No custom widget ' + class_name + ' found in customWidgets param of UiLoader __init__.')

            if self.baseinstance:
                # set an attribute for the new child widget on the base
                # instance, just like PyQt4.uic.loadUi does.
                setattr(self.baseinstance, name, widget)

                # this outputs the various widget names, e.g.
                # sampleGraphicsView, dockWidget, samplesTableView etc.
                # print(name)

            return widget


def loadUi(uifile, baseinstance=None, customWidgets=None, workingDirectory=None):
    loader = UiLoader(baseinstance, customWidgets)

    if workingDirectory is not None:
        loader.setWorkingDirectory(workingDirectory)

    widget = loader.load(uifile)
    QMetaObject.connectSlotsByName(widget)
    return widget


class MainWindow(QMainWindow):
    Box: Union[QMessageBox, QMessageBox]
    tableWidget: QTableWidget
    tableWidget_2: QTableWidget
    tableWidget_3: QTableWidget
    tableWidget_4: QTableWidget
    textEdit: QTextEdit
    radioButton: QRadioButton
    radioButton_2: QRadioButton

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi(os.path.join(SCRIPT_DIRECTORY, 'ui.ui'), self)
        self.Handel_Ui()
        self.Handel_Button()
        self.Handel_Default()
        self.OpenDriver = OpenDriver()
        self.ExtractNumbers = ExtractGroup()
        self.ExtractNumbers.error.connect(self.Error_Single)
        self.TestNumbers = TestNumber()
        self.TestNumbers.error.connect(self.Error_Single)
        self.TestNumbers.final.connect(self.final_single_Test)
        self.SenderNumber = SenderNumber()
        self.SenderNumber.error.connect(self.Error_Single)
        self.SenderNumber.final.connect(self.final_single_Private_Send)
        self.cu = 0

    def Handel_Ui(self):
        # self.setWindowIcon(QIcon('brosser.png'))  ##icon program
        self.setWindowTitle("WhatsApp")
        self.tabWidget.tabBar().setVisible(False)
        self.tableWidget_4.setColumnWidth(0, 110)
        self.tableWidget_4.setColumnWidth(1, 110)
        self.tableWidget_4.setColumnWidth(2, 20)
        self.tableWidget_4.setColumnWidth(3, 20)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setVisible(False)

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        # self.setFixedSize(703, 483)
        self.Box = QMessageBox()
        self.Box.setIcon(QMessageBox.Information)
        self.Box.setWindowTitle("تم الحفظ")
        self.Box.setText("تم حفظ الملف")
        self.Box.setStandardButtons(QMessageBox.Ok)

    def Handel_Default(self):
        self.radioButton_2.click()

    def Handel_Button(self):
        self.pushButton.clicked.connect(self.Test_Tab)
        self.pushButton_2.clicked.connect(self.Group_Tab)

        self.pushButton_5.clicked.connect(self.Open_Driver)

        self.pushButton_3.clicked.connect(self.Privet_Tab)
        self.pushButton_19.clicked.connect(self.Open_File_Private_Send)
        self.pushButton_15.clicked.connect(self.Privet_Sender)
        self.pushButton_17.clicked.connect(self.Pause_Private_Send)
        self.pushButton_16.clicked.connect(self.Restart_Private_Send)
        self.pushButton_21.clicked.connect(self.Stop_Private_Send)
        self.pushButton_18.clicked.connect(self.Delete_Private_Send)
        self.pushButton_20.clicked.connect(self.Add_Message_Private_Send)
        self.pushButton_22.clicked.connect(self.Add_Image_Private_Send)

        self.pushButton_4.clicked.connect(self.Extract_Tab)
        self.pushButton_6.clicked.connect(self.Extract_Numbers)
        self.pushButton_8.clicked.connect(self.Save_Extract_Numbers)

        self.pushButton_9.clicked.connect(self.Open_File_Test)
        self.pushButton_7.clicked.connect(self.Start_Test_Numbers)
        self.pushButton_10.clicked.connect(self.Pause_Test_Numbers)
        self.pushButton_11.clicked.connect(self.Restart_Test_Numbers)
        self.pushButton_12.clicked.connect(self.Stop_Test_Numbers)
        self.pushButton_13.clicked.connect(self.Save_Test_Numbers)
        self.pushButton_14.clicked.connect(self.Delete_Test_Numbers)

        self.radioButton.toggled.connect(self.radio_Privet)
        self.radioButton_2.toggled.connect(self.radio_Privet)

    def Extract_Tab(self):
        self.tabWidget.setCurrentIndex(4)

    def Group_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Privet_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def radio_Privet(self):
        if self.radioButton.isChecked():
            self.pushButton_20.setDisabled(True)
            self.pushButton_22.setDisabled(False)
        if self.radioButton_2.isChecked():
            self.pushButton_20.setDisabled(False)
            self.pushButton_22.setDisabled(True)

    def Test_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Driver(self):
        if not self.OpenDriver.Try:
            self.OpenDriver.start()
        else:
            print('opening')

    def Extract_Numbers(self):
        if not self.ExtractNumbers.Try:
            self.ExtractNumbers.tableWidget = self.tableWidget
            self.ExtractNumbers.start()
        else:
            print('- found ext')

    def Save_Extract_Numbers(self):
        save_file = QFileDialog.getSaveFileName(self, "حفظ ك", 'numbers.txt', '*.txt')[0]
        if save_file != '':
            with open(save_file, 'w') as f:
                for i in range(self.tableWidget.rowCount()):
                    f.write(self.tableWidget.item(i, 0).text().strip() + '\n')
            self.Box.exec()

    def Error_Single(self, error):
        print('- You should open whatsapp', error)

    def Group_Sender(self):
        pass

    def Privet_Sender(self):
        self.SenderNumber.stop = False
        if not self.SenderNumber.Try:
            self.SenderNumber.tableWidget_3 = self.tableWidget_3
            self.SenderNumber.tableWidget_4 = self.tableWidget_4
            self.SenderNumber.driver = self.OpenDriver.driver
            self.SenderNumber.check_live = self.OpenDriver.check_live
            self.SenderNumber.start()
        else:
            print('- found', self.SenderNumber.Try)

    def Add_Message_Private_Send(self):
        text = self.textEdit.toPlainText().strip()
        if text != '':
            r = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(r)
            self.tableWidget_4.setItem(r, 0, QTableWidgetItem(str(text)))
            self.tableWidget_4.setItem(r, 2, QTableWidgetItem(str('text')))

            deleteButton = QPushButton("حذف")
            deleteButton.setStyleSheet('border-radius: 20px;')
            deleteButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.delete_clicked)
            self.tableWidget_4.setCellWidget(r, 3, deleteButton)

    def Add_Image_Private_Send(self):
        text = self.textEdit.toPlainText().strip()

        save_file = QFileDialog.getOpenFileName(self, "اختار", '', '*.*')[0]
        if save_file != '':
            r = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(r)
            if text != '':
                self.tableWidget_4.setItem(r, 0, QTableWidgetItem(str(text)))
            self.tableWidget_4.setItem(r, 1, QTableWidgetItem(str(save_file)))
            self.tableWidget_4.setItem(r, 2, QTableWidgetItem(str('img')))

            deleteButton = QPushButton("حذف")
            deleteButton.setStyleSheet('border-radius: 20px;')
            deleteButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.delete_clicked)
            self.tableWidget_4.setCellWidget(r, 3, deleteButton)

    def delete_clicked(self):
        button = self.sender()
        if button:
            row = self.tableWidget_4.indexAt(button.pos()).row()
            self.tableWidget_4.removeRow(row)

    def Pause_Private_Send(self):
        self.SenderNumber.pause = True

    def Restart_Private_Send(self):
        self.SenderNumber.pause = False

    def Stop_Private_Send(self):
        self.SenderNumber.Stop()

    def Open_File_Private_Send(self):
        save_file = QFileDialog.getOpenFileName(self, "اختار", 'numbers.txt', '*.txt')[0]
        if save_file != '':
            old_number = [self.tableWidget_3.item(i, 0).text() for i in range(self.tableWidget_3.rowCount())]
            with open(save_file, 'r') as f:
                for num in f.read().split('\n'):
                    if num not in old_number and num.strip() != '':
                        r = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(r)
                        self.tableWidget_3.setItem(r, 0, QTableWidgetItem(str(num)))

    def Delete_Private_Send(self):
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(0)

    @staticmethod
    def final_single_Private_Send():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تم الانتهاء")
        Box.setText("تم الانتهاء من الارسال")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ###################################

    def Start_Test_Numbers(self):
        self.TestNumbers.stop = False
        if not self.TestNumbers.Try:
            self.TestNumbers.tableWidget_2 = self.tableWidget_2
            self.TestNumbers.driver = self.OpenDriver.driver
            self.TestNumbers.check_live = self.OpenDriver.check_live
            self.TestNumbers.start()
        else:
            print('- found', self.TestNumbers.Try)

    def Pause_Test_Numbers(self):
        self.TestNumbers.pause = True

    def Restart_Test_Numbers(self):
        self.TestNumbers.pause = False

    def Stop_Test_Numbers(self):
        self.TestNumbers.Stop()

    def Open_File_Test(self):
        save_file = QFileDialog.getOpenFileName(self, "اختار", 'numbers.txt', '*.txt')[0]
        if save_file != '':
            old_number = [self.tableWidget_2.item(i, 0).text() for i in range(self.tableWidget_2.rowCount())]
            with open(save_file, 'r') as f:
                for num in f.read().split('\n'):
                    if num not in old_number and num.strip() != '':
                        r = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(r)
                        self.tableWidget_2.setItem(r, 0, QTableWidgetItem(str(num)))

    def Delete_Test_Numbers(self):
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)

    def Save_Test_Numbers(self):
        save_file = QFileDialog.getSaveFileName(self, "حفظ ك", 'Test Numbers.txt', '*.txt')[0]
        if save_file != '':
            with open(save_file, 'w') as f:
                for i in range(self.tableWidget_2.rowCount()):
                    f.write(self.tableWidget_2.item(i, 0).text().strip() + ' , ' + self.tableWidget_2.item(i,
                                                                                                           1).text().strip() + '\n')
            self.Box.exec()

    @staticmethod
    def final_single_Test():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تم الانتهاء")
        Box.setText("تم الانتهاء من اختبار جميع الارقام")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()


class OpenDriver(QThread):
    driver: WebDriver = None
    count_change_Prog = Signal(int)
    Try: bool = False

    def run(self):
        self.Try = True
        if not self.driver or not self.check_live():
            try:
                # chrome_options = Options()
                # chrome_options.add_argument("--disable-infobars")
                # chrome_options.add_argument("--disable-notifications")
                # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
                # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
                # chrome_options.add_experimental_option('useAutomationExtension', False)
                # chrome_options.add_argument('--no-sandbox')
                # chrome_options.add_argument('--disable-gpu')
                # chrome_options.add_argument('--disable-plugins')
                # chrome_options.add_argument('--disable-popup-blocking')
                # chrome_options.add_argument("--user-data-dir={}".format(r'C:\selenium\AutomationProfile'))
                # self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
                # self.driver.get('https://web.whatsapp.com/')
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument("--disable-infobars")
                chrome_options.add_argument("--disable-notifications")
                chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
                print('- done')
            except Exception as a:
                print(a)
        else:
            print('- found')
        self.Try = False

    def check_live(self):
        if not self.driver:
            return False
        try:
            return self.driver.title
        except:
            return False

    def close(self):
        if self.driver.session_id:
            try:
                self.driver.quit()
            except:
                pass


class ExtractGroup(QThread):
    driver: WebDriver
    error = Signal(object)
    Try = False

    def safe_find_element_by(self, by, elem):
        try:
            return self.driver.find_element(by, elem)
        except NoSuchElementException:
            return None

    def run(self):
        self.driver = window.OpenDriver.driver
        self.Try = True
        if self.driver or not window.OpenDriver.check_live():
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

                    if numbers.__len__() > 1:
                        old_number = [self.tableWidget.item(i, 0).text() for i in range(self.tableWidget.rowCount())]
                        for data in numbers:
                            data = data.replace('⁩', '').replace('⁦', '').replace(' ', '')
                            if '+' in data and data not in old_number:
                                r = self.tableWidget.rowCount()
                                self.tableWidget.insertRow(r)
                                self.tableWidget.setItem(r, 0, QTableWidgetItem(str(data)))
                    else:
                        print(' Not Group')
                else:
                    print(' Not Group')
            except Exception as a:
                self.error.emit(a)
        else:
            self.error.emit('Driver Not Found')
        self.Try = False


class TestNumber(QThread):
    tableWidget_2: QTableWidget
    driver: WebDriver
    error = Signal(object)
    final = Signal()
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
                    sleep(1)
                    if not len(self.driver.find_elements_by_css_selector('div[data-animate-modal-body="true"]')):
                        state = 'موجود'
                    else:
                        state = 'غير موجود'
                    self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(state)))

                except Exception as a:
                    self.error.emit(a)
                self.tableWidget_2.item(i, 0).setSelected(False)
        else:
            self.error.emit('Driver Not Found')
        self.Try = False
        self.final.emit()

    def Stop(self):
        self.stop = True


class SenderNumber(QThread):
    tableWidget_3: QTableWidget
    driver: WebDriver
    error = Signal(object)
    final = Signal()
    Try = False
    pause = False
    stop = False

    def safe_find_element_by(self, by, elem):
        try:
            return self.driver.find_element(by, elem)
        except NoSuchElementException:
            return None

    def com(self, phone, text=''):
        return '''
        if (!document.querySelector('header > a')){
        header = document.querySelector('header');
        newlink = document.createElement('a');
        header.appendChild(newlink);
        }
        a = document.querySelector('header > a');
        a.setAttribute('href', '''+f'"https://web.whatsapp.com/send?phone={phone}&text={text}&app_absent=0"'+''');
        document.querySelector('header > a').click()
        '''

    def run(self):
        state = ''
        sleep(1)
        if self.driver or self.check_live():
            self.Try = True
            for i in range(self.tableWidget_3.rowCount()):
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

                    self.tableWidget_4.item(im, 0).setSelected(True)
                    if self.tableWidget_4.item(im, 2).text().strip() == 'text':
                        text = self.tableWidget_4.item(im, 0).text().strip()
                        state = self.send_text(number, text)

                    elif self.tableWidget_4.item(im, 2).text().strip() == 'img':
                        img = self.tableWidget_4.item(im, 1).text().strip()
                        text = self.tableWidget_4.item(im, 0).text().strip()
                        state = self.send_img(number, img, text)

                    self.tableWidget_4.item(im, 0).setSelected(False)

                self.tableWidget_3.setItem(i, 1, QTableWidgetItem(str(state)))
                self.tableWidget_3.item(i, 0).setSelected(False)
                sleep(2)
        else:
            self.error.emit('Driver Not Found')
        self.Try = False
        self.final.emit()

    def check_number(self):
        sleep(1)
        return False if len(self.driver.find_elements_by_css_selector('div[data-animate-modal-body="true"]')) > 0 else True

    def send_text(self, number, text):
        self.driver.execute_script(self.com(number, text))
        if self.check_number():
            WebDriverWait(self.driver, 5).until(
                (ec.element_to_be_clickable((By.CSS_SELECTOR, 'button > [data-testid="send"]')))).click()
            # self.driver.find_element_by_css_selector('[role="button"]>[data-testid="send"]').click()

            return 'تم الارسال'
        else:
            return 'لم يتم الارسال'

    def send_img(self, number, img, text):
        self.driver.execute_script(self.com(number))
        if self.check_number():
            WebDriverWait(self.driver, 5).until(
                (ec.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'div[role="button"][title="إرفاق"]')))).click()
            WebDriverWait(self.driver, 5).until(
                (ec.presence_of_element_located(
                    (By.CSS_SELECTOR, '[data-testid="attach-image"]+input')))).send_keys(img)
            sleep(1)
            WebDriverWait(self.driver, 5).until(
                (ec.visibility_of_element_located(
                    (By.CSS_SELECTOR, '[class="_13NKt copyable-text selectable-text"][data-tab="6"]')))).send_keys(text)
            sleep(1)
            WebDriverWait(self.driver, 5).until(
                (ec.element_to_be_clickable((By.CSS_SELECTOR, '[role="button"]>[data-testid="send"]')))).click()
            # self.driver.find_element_by_css_selector('div[role="button"][title="إرفاق"]').click()
            # self.driver.find_element_by_css_selector('[data-testid="attach-image"]+input').send_keys(
            #     self.tableWidget_4.item(i, 1).text().strip())
            # self.driver.find_element_by_css_selector('[role="button"]>[data-testid="send"]').click()

            return 'تم الارسال'
        else:
            return 'لم يتم الارسال'

    def Stop(self):
        self.stop = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

'''
https://web.whatsapp.com/send?phone=%2B201068009959&text&app_absent=0
1- فتح الواتس.
 2- اختبار ارقام تستعمل الواتس او لا. 
 3- ترسل رسائل للغروبات. 
 4- ترسل رسائل للخاص. 
 5-سحب الاعضاء من الجروبات 
'''
'''
https://web.whatsapp.com/send?phone=+201068009959&text&app_absent=0
if (!document.querySelector('header > a')){
header = document.querySelector('header');
newlink = document.createElement('a');
newlink.setAttribute('href', 'https://web.whatsapp.com/send?phone=+2010680095959&text&app_absent=0');
header.appendChild(newlink);
}
else{
a = document.querySelector('header > a');
a.setAttribute('href', 'https://web.whatsapp.com/send?phone=+2010680039959&text&app_absent=0');
}
document.querySelector('header > a').click()



<a href="https://web.whatsapp.com/send?phone=+20106i98009959&amp;text&amp;app_absent=0"> vl </a>
<a href="https://wa.me/201068009959/?text=urlencodedtext"> v2 </a> No +
<a href="https://api.WhatsApp.com/send?phone=201068009959"> v3 </a>

import subprocess
try:
    pros = subprocess.Popen(
        '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
        rf' --user-data-dir="C:\selenium\AutomationProfile" '
        ' --remote-debugging-port=9222')
except:
    pros = subprocess.Popen(
        '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
        rf' --user-data-dir="C:\selenium\AutomationProfile"'
        '  --remote-debugging-port=9222')
   
2500 >>> 
50  >>> 5 
'''
