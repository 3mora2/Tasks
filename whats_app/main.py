# pip install PySide2 selenium webdriver_manager
import random
import traceback
from time import sleep
from typing import Union
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QMetaObject, QThread, Signal
from PySide2.QtGui import QCursor, QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget, QFileDialog, QMessageBox, \
    QTextEdit, QHeaderView, QPushButton, QRadioButton, QLineEdit, QTabWidget, QSizePolicy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import sys
import warnings
import chromedriver_autoinstaller
# import win32gui
import win32con
import datetime
import psutil
import os
import start
from mainwindow import Ui_MainWindow
# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


os.environ['WDM_LOG_LEVEL'] = '0'
if not sys.warnoptions:
    warnings.simplefilter("ignore")

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
script = """var elm = arguments[0],
txt = arguments[1];
elm.textContent = txt;
elm.dispatchEvent(new Event('keydown', {bubbles: true}));
elm.dispatchEvent(new Event('keypress', {bubbles: true}));
elm.dispatchEvent(new Event('input', {bubbles: true}));
elm.dispatchEvent(new Event('keyup', {bubbles: true}));"""


def error_Text(error):
    with open('log.log', 'a+', encoding="utf-8") as f:
        f.write(f'{datetime.datetime.now()}: {str(error)} \n')


def close_chrome_driver():
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            if 'chromedriver' in processName.lower():
                proc.kill()

        except:
            error_Text(traceback.format_exc())


# def enumWindowFunc(hwnd, windowList):
#     try:
#         """ win32gui.EnumWindows() callback """
#         text = win32gui.GetWindowText(hwnd)
#         className = win32gui.GetClassName(hwnd)
#         if 'chromedriver' in text.lower() or 'chromedriver' in className.lower():
#             win32gui.ShowWindow(hwnd, False)
#             # win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
#     except:
#         error_Text(traceback.format_exc())


def hind_all():
    for file in os.listdir():
        if file == 'main.exe':
            continue

        try:
            os.popen('attrib +h '+str(file))
        except:
            pass

# hind_all()


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


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow, Ui_MainWindow):
    Box_Limit: Union[QMessageBox, QMessageBox]
    Box: Union[QMessageBox, QMessageBox]
    tableWidget: QTableWidget
    tableWidget_2: QTableWidget
    tableWidget_3: QTableWidget
    tableWidget_4: QTableWidget
    textEdit: QTextEdit
    textEdit_3: QTextEdit
    lineEdit: QLineEdit
    lineEdit_4: QLineEdit
    lineEdit_5: QLineEdit
    radioButton: QRadioButton
    radioButton_2: QRadioButton
    tabWidget: QTabWidget

    # def __init__(self, *args, **kwargs):
    def __init__(self, parent=None):
        # super().__init__(*args, **kwargs)
        QMainWindow.__init__(self, parent)
        # loadUi(os.path.join(SCRIPT_DIRECTORY, 'Other/ui.ui'), self)
        self.setupUi(self)

        self.limit = 5
        self.Handel_Ui()
        self.Handel_Button()
        self.Handel_Default()
        self.Handel_check()

        self.OpenDriver = OpenDriver()
        self.OpenDriver.final.connect(self.Final_Open_Driver)
        self.OpenDriver.found.connect(self.Found_Open_Driver)
        self.OpenDriver.wait.connect(self.Driver_Download)

        self.ExtractGroup = ExtractGroup()
        self.ExtractGroup.final.connect(self.Final_Extract_Group)
        self.ExtractGroup.error.connect(self.Error_Single)
        self.ExtractGroup.driver_error.connect(self.Driver_Error)
        self.ExtractGroup.final_message.connect(self.Final_Extract_Group_Message)
        self.ExtractGroup.not_group.connect(self.Not_Group)
        self.ExtractGroup.limit_message.connect(self.show_limit)

        self.TestNumbers = TestNumber()
        self.TestNumbers.error.connect(self.Error_Single)
        self.TestNumbers.driver_error.connect(self.Driver_Error)
        self.TestNumbers.final.connect(self.final_single_Test)
        self.TestNumbers.final_message.connect(self.final_single_Message_Test)
        self.TestNumbers.limit_message.connect(self.show_limit)

        self.SenderNumber = SenderNumber()
        self.SenderNumber.error.connect(self.Error_Single)
        self.SenderNumber.final.connect(self.final_single_Private_Send)
        self.SenderNumber.driver_error.connect(self.Driver_Error)
        self.SenderNumber.final_message.connect(self.final_single_Message_Private_Send)
        self.SenderNumber.limit_message.connect(self.show_limit)

        self.GroupSender = GroupSender()
        self.GroupSender.error.connect(self.Error_Single)
        self.GroupSender.final.connect(self.final_single_GroupSender)
        self.GroupSender.driver_error.connect(self.Driver_Error)
        self.GroupSender.final_message.connect(self.final_single_Message_GroupSender)
        self.GroupSender.limit_message.connect(self.show_limit)

        self.ExtractContant = ExtractContent()
        self.ExtractContant.error.connect(self.Error_Single)
        self.ExtractContant.final.connect(self.final_single_Extract_Content)
        self.ExtractContant.driver_error.connect(self.Driver_Error)
        self.ExtractContant.final_message.connect(self.final_single_Message_Extract_Content)
        self.ExtractContant.limit_message.connect(self.show_limit)
        self.cu = 0

    def Handel_Ui(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'logo.png'))
        self.setWindowTitle(" ")
        self.tabWidget.tabBar().setVisible(False)

        self.tableWidget_4.setColumnWidth(0, 110)
        self.tableWidget_4.setColumnWidth(1, 110)
        self.tableWidget_4.setColumnWidth(2, 20)
        self.tableWidget_4.setColumnWidth(3, 20)

        self.tableWidget_7.setColumnWidth(0, 110)
        self.tableWidget_7.setColumnWidth(1, 110)
        self.tableWidget_7.setColumnWidth(2, 20)
        self.tableWidget_7.setColumnWidth(3, 20)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tableWidget_7.verticalHeader().setVisible(False)
        self.tableWidget_8.verticalHeader().setVisible(False)
        self.tableWidget_9.verticalHeader().setVisible(False)
        self.tableWidget_10.verticalHeader().setVisible(False)
        self.tableWidget_11.verticalHeader().setVisible(False)

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_8.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_9.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_10.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_11.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_8.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_9.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setFixedSize(self.size().width(), self.size().height())
        self.Box = QMessageBox()
        self.Box.setIcon(QMessageBox.Information)
        self.Box.setWindowTitle("???? ??????????")
        self.Box.setText("???? ?????? ??????????")
        self.Box.setStandardButtons(QMessageBox.Ok)
        self.Box_Limit = QMessageBox()
        self.Box_Limit.setIcon(QMessageBox.Information)
        self.Box_Limit.setWindowTitle("??????????")
        self.Box_Limit.setText("?????? ???????????? ?????????????? \n?????? ?????????? ???????????????? ????????????????.")
        self.Box_Limit.setStandardButtons(QMessageBox.Ok)

    def Handel_Default(self):
        self.pushButton_10.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)

        self.pushButton_16.setDisabled(True)
        self.pushButton_17.setDisabled(True)
        self.pushButton_21.setDisabled(True)

        self.pushButton_31.setDisabled(True)
        self.pushButton_33.setDisabled(True)
        self.pushButton_35.setDisabled(True)

        self.radioButton_2.click()
        self.radioButton_3.click()

        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)

    def Handel_Button(self):
        self.pushButton_49.clicked.connect(self.check_serial)

        self.pushButton_48.clicked.connect(self.Main_Tab)
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

        self.pushButton_29.clicked.connect(self.Open_File_GroupSender)
        self.pushButton_28.clicked.connect(self.Add_Message_GroupSender)
        self.pushButton_30.clicked.connect(self.Group_Sender)
        self.pushButton_31.clicked.connect(self.Pause_GroupSender)
        self.pushButton_32.clicked.connect(self.Add_Image_GroupSender)
        self.pushButton_33.clicked.connect(self.Restart_GroupSender)
        self.pushButton_35.clicked.connect(self.Stop_GroupSender)
        self.pushButton_34.clicked.connect(self.Delete_GroupSender)

        self.pushButton_4.clicked.connect(self.Extract_Tab)
        self.pushButton_6.clicked.connect(self.Extract_Group)
        self.pushButton_8.clicked.connect(self.Save_Extract_Group)
        self.pushButton_44.clicked.connect(self.Delete_Extract_Group)
        self.pushButton_45.clicked.connect(self.Save_VCF)
        self.pushButton_46.clicked.connect(self.Save_VCF)
        self.pushButton_47.clicked.connect(self.Save_VCF)

        self.pushButton_24.clicked.connect(self.Extract_Content_Tab)
        self.pushButton_25.clicked.connect(self.Extract_Content)
        self.pushButton_26.clicked.connect(self.Save_Group_Names)
        self.pushButton_27.clicked.connect(self.Delete_Group_Names)
        self.pushButton_40.clicked.connect(self.Delete_Contact_Name)
        self.pushButton_41.clicked.connect(self.Save_Contact_Name)
        self.pushButton_39.clicked.connect(self.Save_Numbers_Extract)
        self.pushButton_38.clicked.connect(self.Delete_Numbers_Extract)

        self.pushButton_9.clicked.connect(self.Open_File_Test)
        self.pushButton_7.clicked.connect(self.Start_Test_Numbers)
        self.pushButton_10.clicked.connect(self.Pause_Test_Numbers)
        self.pushButton_11.clicked.connect(self.Restart_Test_Numbers)
        self.pushButton_12.clicked.connect(self.Stop_Test_Numbers)
        self.pushButton_13.clicked.connect(self.Save_Numbers_Correct)
        self.pushButton_36.clicked.connect(self.Save_Numbers_UnCorrect)
        self.pushButton_14.clicked.connect(self.Delete_Test_Numbers)
        self.pushButton_23.clicked.connect(self.Delete_Numbers)
        self.pushButton_37.clicked.connect(self.Delete_Un_Numbers)
        self.pushButton_42.clicked.connect(self.Delete_Add_Number_Test)
        self.pushButton_43.clicked.connect(self.Add_Number_Test)

        self.radioButton.toggled.connect(self.radio_Privet)
        self.radioButton_2.toggled.connect(self.radio_Privet)

        self.radioButton_3.toggled.connect(self.radio_Group)
        self.radioButton_4.toggled.connect(self.radio_Group)

    def Handel_check(self):
        if os.path.isfile(start.path_file):
            res = start.open_file()
            try:
                if res[0] and res[1]:
                    self.lineEdit_5.setText(
                        f' ?????????? ???????????? ???????????????? :{res[0].year}/{res[0].month}/{res[0].day}')
                    self.lineEdit_4.hide()
                    self.pushButton_49.hide()
                    self.limit = None
                elif res[0] is False and res[1]:
                    self.lineEdit_5.setText('?????????? ???????????? ???????????????? ?????? ???????????? ??????????????')
                    self.lineEdit_4.show()
                    self.pushButton_49.show()
                    self.limit = 5

                else:
                    self.lineEdit_5.setText('?????? ???????????? ??????????????')
                    self.lineEdit_4.show()
                    self.pushButton_49.show()
                    self.limit = 5
            except Exception as e:
                print(e)
        else:
            self.lineEdit_4.show()
            self.pushButton_49.show()
            self.lineEdit_5.setText('?????? ???????????? ??????????????')

    def check_serial(self):
        text = self.lineEdit_4.text()
        if text == '' or text is None:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????????")
            Box.setText("???? ???????? ???????? ????????????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            if start.add_new(text):
                Box = QMessageBox()
                Box.setIcon(QMessageBox.Information)
                Box.setWindowTitle("??????????")
                Box.setText("???? ?????????? ?????????????? ??????????")
                Box.setStandardButtons(QMessageBox.Ok)
                Box.exec()
                self.Handel_check()
            else:
                Box = QMessageBox()
                Box.setIcon(QMessageBox.Warning)
                Box.setWindowTitle("??????")
                Box.setText(" ?????? ?????? \n?????? ???????????????? ?????? ????????.")
                Box.setStandardButtons(QMessageBox.Ok)
                Box.exec()

    def show_limit(self):
        self.Box_Limit.exec()

    ####################################################################################################################
    ####################################################################################################################

    def Main_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Test_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Group_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Privet_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Extract_Tab(self):
        self.tabWidget.setCurrentIndex(4)

    def Extract_Content_Tab(self):
        self.tabWidget.setCurrentIndex(5)

    ####################################################################################################################
    ####################################################################################################################

    def Open_Driver(self):
        if not self.OpenDriver.Try:
            self.OpenDriver.start()
        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????????")
            Box.setText("???????? ?????? ????????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

    def Final_Open_Driver(self):
        self.OpenDriver.reopen = False
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("????")
        Box.setText("???? ?????? ????????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Found_Open_Driver(self):
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("??????????")
        Box.setText("???????????? ?????????? ??????????\n ???? ???????? ?????????? ?????? ?????????????? ??")
        Box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Open)
        ret = Box.exec_()
        if ret == QMessageBox.Open:
            self.OpenDriver.reopen = True
            self.OpenDriver.start()

    @staticmethod
    def Driver_Error():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("??????")
        Box.setText("?????? ?????? ???????????? ????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    @staticmethod
    def Driver_Download():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("??????????")
        Box.setText(" ???????? ?????????? ?????? ?????????????? \n ???? ???????????? ???????? ?????? ??????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ####################################################################################################################
    ####################################################################################################################

    def Extract_Group(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????")
            Box.setText("???? ???????? ?????????? ???????????? ???? ?????? ????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            if not self.ExtractGroup.Try:
                self.pushButton_6.setDisabled(True)
                self.pushButton_8.setDisabled(True)
                self.pushButton_44.setDisabled(True)
                self.pushButton_45.setDisabled(True)

                self.ExtractGroup.tableWidget = self.tableWidget
                self.ExtractGroup.driver = self.OpenDriver.driver
                self.ExtractGroup.check_live = self.OpenDriver.check_live
                self.ExtractGroup.limit = self.limit
                self.ExtractGroup.start()
                self.OpenDriver.is_used_now = True
            else:
                print('- found ext')

    def Save_Extract_Group(self):
        if self.tableWidget.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "?????? ??", 'numbers.txt', '*.txt')[0]
            if save_file != '':
                with open(save_file, 'w', encoding="utf-8") as f:
                    for i in range(self.tableWidget.rowCount()):
                        f.write(self.tableWidget.item(i, 0).text().strip() + '\n')
                self.Box.exec()

    def Delete_Extract_Group(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

    def Final_Extract_Group(self):
        self.OpenDriver.is_used_now = False
        self.pushButton_6.setDisabled(False)
        self.pushButton_8.setDisabled(False)
        self.pushButton_44.setDisabled(False)
        self.pushButton_45.setDisabled(False)

    @staticmethod
    def Final_Extract_Group_Message():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("????")
        Box.setText("???? ?????????????? ???????? ??????????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    @staticmethod
    def Not_Group():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("?????? ??????????")
        Box.setText("?????? ??????????\n?????? ?????? ???????????? ???????????? ?????????????? ?????????????? ??????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    @staticmethod
    def Error_Single(error):
        print('- You should open whatsapp', error)

    @staticmethod
    def error_vcf():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("??????")
        Box.setText("???????? ?????? ??????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Save_VCF_(self, text, tableWidget: QTableWidget):
        if tableWidget.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "?????? ??", 'numbers.vcf', '*.vcf')[0]
            if save_file != '':
                with open(save_file, 'w', encoding="utf-8") as output:
                    for i in range(tableWidget.rowCount()):
                        output.write("BEGIN:VCARD\n")
                        output.write("VERSION:3.0\n")
                        output.write("FN:" + str(text + ' ' + str(i)) + "\n")
                        output.write("TEL;TYPE=HOME,VOICE:" + str(tableWidget.item(i, 0).text().strip()) + "\n")
                        output.write("END:VCARD\n")

    def Save_VCF(self):
        if self.tabWidget.currentWidget().objectName() == 'tab_4':
            text = self.lineEdit.text()
            if text == '' or text is None:
                self.error_vcf()
            else:
                self.Save_VCF_(text, self.tableWidget)

        elif self.tabWidget.currentWidget().objectName() == 'tab_2':
            text = self.lineEdit_2.text()
            if text == '' or text is None:
                self.error_vcf()
            else:
                self.Save_VCF_(text, self.tableWidget_8)

        elif self.tabWidget.currentWidget().objectName() == 'tab_5':
            text = self.lineEdit_3.text()
            if text == '' or text is None:
                self.error_vcf()
            else:
                self.Save_VCF_(text, self.tableWidget_10)

    ####################################################################################################################
    ####################################################################################################################

    def Extract_Content(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????")
            Box.setText("???? ???????? ?????????? ???????????? ???? ?????? ????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            if not self.ExtractContant.Try:
                self.pushButton_25.setDisabled(True)
                self.pushButton_26.setDisabled(True)
                self.pushButton_27.setDisabled(True)
                self.pushButton_40.setDisabled(True)
                self.pushButton_41.setDisabled(True)
                self.pushButton_39.setDisabled(True)
                self.pushButton_38.setDisabled(True)

                self.ExtractContant.tableWidget_5 = self.tableWidget_5
                self.ExtractContant.tableWidget_10 = self.tableWidget_10
                self.ExtractContant.tableWidget_11 = self.tableWidget_11
                self.ExtractContant.driver = self.OpenDriver.driver
                self.ExtractContant.check_live = self.OpenDriver.check_live
                self.ExtractContant.limit = self.limit
                self.ExtractContant.start()
                self.OpenDriver.is_used_now = True
            else:
                print('- found', self.SenderNumber.Try)

    def Save_Group_Names(self):
        if self.tableWidget_5.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "?????? ??", 'Groups.txt', '*.txt')[0]
            if save_file != '':
                with open(save_file, 'w', encoding="utf-8") as f:
                    for i in range(self.tableWidget_5.rowCount()):
                        f.write(self.tableWidget_5.item(i, 0).text().strip() + '\n')
                self.Box.exec()

    def Delete_Group_Names(self):
        self.tableWidget_5.clearContents()
        self.tableWidget_5.setRowCount(0)

    def Save_Contact_Name(self):
        if self.tableWidget_11.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "?????? ??", 'Groups.txt', '*.txt')[0]
            if save_file != '':
                with open(save_file, 'w', encoding="utf-8") as f:
                    for i in range(self.tableWidget_11.rowCount()):
                        f.write(self.tableWidget_11.item(i, 0).text().strip() + '\n')
                self.Box.exec()

    def Delete_Contact_Name(self):
        self.tableWidget_11.clearContents()
        self.tableWidget_11.setRowCount(0)

    def Save_Numbers_Extract(self):
        if self.tableWidget_10.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "?????? ??", 'Groups.txt', '*.txt')[0]
            if save_file != '':
                with open(save_file, 'w', encoding="utf-8") as f:
                    for i in range(self.tableWidget_10.rowCount()):
                        f.write(self.tableWidget_10.item(i, 0).text().strip() + '\n')
                self.Box.exec()

    def Delete_Numbers_Extract(self):
        self.tableWidget_10.clearContents()
        self.tableWidget_10.setRowCount(0)

    def final_single_Extract_Content(self):
        self.OpenDriver.is_used_now = False
        self.pushButton_25.setDisabled(False)
        self.pushButton_26.setDisabled(False)
        self.pushButton_27.setDisabled(False)
        self.pushButton_40.setDisabled(False)
        self.pushButton_41.setDisabled(False)
        self.pushButton_39.setDisabled(False)
        self.pushButton_38.setDisabled(False)

    @staticmethod
    def final_single_Message_Extract_Content():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("???? ????????????????")
        Box.setText("???? ???????????????? ???? ?????????????? ???????? ??????????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ####################################################################################################################
    ####################################################################################################################

    def Group_Sender(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????")
            Box.setText("???? ???????? ?????????? ???????????? ???? ?????? ????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            self.GroupSender.stop = False
            if not self.GroupSender.Try:
                self.pushButton_29.setDisabled(True)
                self.pushButton_28.setDisabled(True)
                self.pushButton_30.setDisabled(True)
                self.pushButton_31.setDisabled(False)
                self.pushButton_32.setDisabled(True)
                self.pushButton_33.setDisabled(True)
                self.pushButton_35.setDisabled(False)
                self.pushButton_34.setDisabled(True)

                self.GroupSender.tableWidget_7 = self.tableWidget_7
                self.GroupSender.tableWidget_6 = self.tableWidget_6
                self.GroupSender.spinBox = self.spinBox
                self.GroupSender.spinBox_3 = self.spinBox_3
                self.GroupSender.driver = self.OpenDriver.driver
                self.GroupSender.check_live = self.OpenDriver.check_live
                self.GroupSender.limit = self.limit
                self.GroupSender.start()
                self.OpenDriver.is_used_now = True
            else:
                print('- found', self.GroupSender.Try)

    def radio_Group(self):
        if self.radioButton_3.isChecked():
            self.pushButton_32.setDisabled(True)
            self.pushButton_28.setDisabled(False)
        if self.radioButton_4.isChecked():
            self.pushButton_32.setDisabled(False)
            self.pushButton_28.setDisabled(True)

    def Add_Message_GroupSender(self):
        text = self.textEdit_2.toPlainText().strip()
        if text != '':
            r = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(r)
            self.tableWidget_7.setItem(r, 0, QTableWidgetItem(str(text)))
            self.tableWidget_7.setItem(r, 2, QTableWidgetItem(str('text')))

            deleteButton = QPushButton("??????")
            deleteButton.setStyleSheet('border-radius: 20px;')
            deleteButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.delete_clicked_GroupSender)
            self.tableWidget_7.setCellWidget(r, 3, deleteButton)

    def Add_Image_GroupSender(self):
        text = self.textEdit_2.toPlainText().strip()

        save_file = QFileDialog.getOpenFileName(self, "??????????", '', '*.*')[0]
        if save_file != '':
            r = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(r)
            if text != '':
                self.tableWidget_7.setItem(r, 0, QTableWidgetItem(str(text)))
            self.tableWidget_7.setItem(r, 1, QTableWidgetItem(str(save_file)))
            self.tableWidget_7.setItem(r, 2, QTableWidgetItem(str('img')))

            deleteButton = QPushButton("??????")
            deleteButton.setStyleSheet('border-radius: 20px;')
            deleteButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.delete_clicked_GroupSender)
            self.tableWidget_7.setCellWidget(r, 3, deleteButton)

    def delete_clicked_GroupSender(self):
        button = self.sender()
        if button:
            row = self.tableWidget_7.indexAt(button.pos()).row()
            self.tableWidget_7.removeRow(row)

    def Pause_GroupSender(self):
        self.GroupSender.pause = True
        self.pushButton_31.setDisabled(True)
        self.pushButton_33.setDisabled(False)

    def Restart_GroupSender(self):
        self.GroupSender.pause = False
        self.pushButton_31.setDisabled(False)
        self.pushButton_33.setDisabled(True)

    def Stop_GroupSender(self):
        self.GroupSender.Stop()
        self.pushButton_35.setDisabled(True)

    def Open_File_GroupSender(self):
        save_file = QFileDialog.getOpenFileName(self, "??????????", '', '*.txt')[0]
        if save_file != '':
            old_number = [self.tableWidget_6.item(i, 0).text() for i in range(self.tableWidget_6.rowCount())]
            with open(save_file, 'r', encoding="utf-8") as f:
                for num in f.read().split('\n'):
                    if num not in old_number and num.strip() != '':
                        r = self.tableWidget_6.rowCount()
                        self.tableWidget_6.insertRow(r)
                        self.tableWidget_6.setItem(r, 0, QTableWidgetItem(str(num)))

    def Delete_GroupSender(self):
        self.tableWidget_6.clearContents()
        self.tableWidget_6.setRowCount(0)

    def final_single_GroupSender(self):
        self.OpenDriver.is_used_now = False
        self.pushButton_29.setDisabled(False)
        self.pushButton_28.setDisabled(False)
        self.pushButton_30.setDisabled(False)
        self.pushButton_31.setDisabled(True)
        self.pushButton_33.setDisabled(True)
        self.pushButton_35.setDisabled(True)
        self.pushButton_32.setDisabled(False)
        self.pushButton_34.setDisabled(False)

    @staticmethod
    def final_single_Message_GroupSender():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("???? ????????????????")
        Box.setText("???? ???????????????? ???? ??????????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ####################################################################################################################
    ####################################################################################################################

    def Privet_Sender(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????")
            Box.setText("???? ???????? ?????????? ???????????? ???? ?????? ????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            self.SenderNumber.stop = False
            if not self.SenderNumber.Try:
                self.pushButton_19.setDisabled(True)
                self.pushButton_15.setDisabled(True)
                self.pushButton_17.setDisabled(False)
                self.pushButton_16.setDisabled(True)
                self.pushButton_21.setDisabled(False)
                self.pushButton_18.setDisabled(True)
                self.pushButton_20.setDisabled(True)
                self.pushButton_22.setDisabled(True)

                self.SenderNumber.tableWidget_3 = self.tableWidget_3
                self.SenderNumber.tableWidget_4 = self.tableWidget_4
                self.SenderNumber.driver = self.OpenDriver.driver
                self.SenderNumber.check_live = self.OpenDriver.check_live
                self.SenderNumber.limit = self.limit
                self.SenderNumber.spinBox_2 = self.spinBox_2
                self.SenderNumber.spinBox_4 = self.spinBox_4
                self.SenderNumber.start()
                self.OpenDriver.is_used_now = True
            else:
                print('- found', self.SenderNumber.Try)

    def radio_Privet(self):
        if self.radioButton.isChecked():
            self.pushButton_20.setDisabled(True)
            self.pushButton_22.setDisabled(False)
        if self.radioButton_2.isChecked():
            self.pushButton_20.setDisabled(False)
            self.pushButton_22.setDisabled(True)

    def Add_Message_Private_Send(self):
        text = self.textEdit.toPlainText().strip()
        if text != '':
            r = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(r)
            self.tableWidget_4.setItem(r, 0, QTableWidgetItem(str(text)))
            self.tableWidget_4.setItem(r, 2, QTableWidgetItem(str('text')))

            deleteButton = QPushButton("??????")
            deleteButton.setStyleSheet('border-radius: 20px;')
            deleteButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.delete_clicked)
            self.tableWidget_4.setCellWidget(r, 3, deleteButton)
        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????????")
            Box.setText("?????? ?????????? ????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

    def Add_Image_Private_Send(self):
        text = self.textEdit.toPlainText().strip()

        save_file = QFileDialog.getOpenFileName(self, "?????????? ????????/????????", '', '*.*')[0]
        if save_file != '':
            r = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(r)
            if text != '':
                self.tableWidget_4.setItem(r, 0, QTableWidgetItem(str(text)))
            self.tableWidget_4.setItem(r, 1, QTableWidgetItem(str(save_file)))
            self.tableWidget_4.setItem(r, 2, QTableWidgetItem(str('img')))

            deleteButton = QPushButton("??????")
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
        self.pushButton_16.setDisabled(False)
        self.pushButton_17.setDisabled(True)

    def Restart_Private_Send(self):
        self.SenderNumber.pause = False
        self.pushButton_16.setDisabled(True)
        self.pushButton_17.setDisabled(False)

    def Stop_Private_Send(self):
        self.SenderNumber.Stop()
        self.pushButton_21.setDisabled(True)

    def Open_File_Private_Send(self):
        save_file = QFileDialog.getOpenFileName(self, "??????????", 'numbers.txt', '*.txt')[0]
        if save_file != '':
            old_number = [self.tableWidget_3.item(i, 0).text() for i in range(self.tableWidget_3.rowCount())]
            with open(save_file, 'r', encoding="utf-8") as f:
                for num in f.read().split('\n'):
                    if num not in old_number and num.strip() != '':
                        r = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(r)
                        self.tableWidget_3.setItem(r, 0, QTableWidgetItem(str(num)))

    def Delete_Private_Send(self):
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(0)

    def final_single_Private_Send(self):
        self.OpenDriver.is_used_now = False

        self.pushButton_19.setDisabled(False)
        self.pushButton_15.setDisabled(False)
        self.pushButton_16.setDisabled(True)
        self.pushButton_17.setDisabled(True)
        self.pushButton_21.setDisabled(True)
        self.pushButton_18.setDisabled(False)
        self.pushButton_20.setDisabled(False)
        self.pushButton_22.setDisabled(False)

    @staticmethod
    def final_single_Message_Private_Send():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("???? ????????????????")
        Box.setText("???? ???????????????? ???? ??????????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ####################################################################################################################
    ####################################################################################################################

    def Start_Test_Numbers(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????")
            Box.setText("???? ???????? ?????????? ???????????? ???? ?????? ????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        elif self.tableWidget_2.rowCount() == 0:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????")
            Box.setText("?????? ?????????? ?????????????? ????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            self.TestNumbers.stop = False
            if not self.TestNumbers.Try:

                self.pushButton_9.setDisabled(True)
                self.pushButton_7.setDisabled(True)
                self.pushButton_10.setDisabled(False)
                self.pushButton_11.setDisabled(True)
                self.pushButton_12.setDisabled(False)
                self.pushButton_13.setDisabled(True)
                self.pushButton_36.setDisabled(True)
                self.pushButton_14.setDisabled(True)
                self.pushButton_23.setDisabled(True)
                self.pushButton_37.setDisabled(True)
                self.pushButton_42.setDisabled(True)
                self.pushButton_43.setDisabled(True)

                self.TestNumbers.tableWidget_2 = self.tableWidget_2
                self.TestNumbers.tableWidget_8 = self.tableWidget_8
                self.TestNumbers.tableWidget_9 = self.tableWidget_9
                self.TestNumbers.driver = self.OpenDriver.driver
                self.TestNumbers.check_live = self.OpenDriver.check_live
                self.TestNumbers.limit = self.limit
                self.TestNumbers.start()
                self.OpenDriver.is_used_now = True
            else:
                print('- found', self.TestNumbers.Try)

    def Delete_Add_Number_Test(self):
        self.textEdit_3.clear()

    def Add_Number_Test(self):
        text = self.textEdit_3.toPlainText().strip()
        if text != '':
            for num in text.split('\n'):
                old_number = [self.tableWidget_2.item(i, 0).text() for i in range(self.tableWidget_2.rowCount())]
                if num not in old_number and num.strip() != '' and num.startswith('+'):
                    r = self.tableWidget_2.rowCount()
                    self.tableWidget_2.insertRow(r)
                    self.tableWidget_2.setItem(r, 0, QTableWidgetItem(str(num)))
        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("??????????")
            Box.setText("?????? ?????? ?????????????? ????????")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

    @staticmethod
    def Save_Error():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("??????????")
        Box.setText("???? ???????? ???? ??????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Pause_Test_Numbers(self):
        self.TestNumbers.pause = True
        self.pushButton_10.setDisabled(True)
        self.pushButton_11.setDisabled(False)

    def Restart_Test_Numbers(self):
        self.TestNumbers.pause = False
        self.pushButton_10.setDisabled(False)
        self.pushButton_11.setDisabled(True)

    def Stop_Test_Numbers(self):
        self.TestNumbers.Stop()
        self.pushButton_12.setDisabled(True)

    def Open_File_Test(self):
        save_file = QFileDialog.getOpenFileName(self, "??????????", 'numbers.txt', '*.txt')[0]
        if save_file != '':
            old_number = [self.tableWidget_2.item(i, 0).text() for i in range(self.tableWidget_2.rowCount())]
            with open(save_file, 'r', encoding="utf-8") as f:
                for num in f.read().split('\n'):
                    if num not in old_number and num.strip() != '':
                        r = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(r)
                        self.tableWidget_2.setItem(r, 0, QTableWidgetItem(str(num)))

    def Delete_Test_Numbers(self):
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)

    def Delete_Numbers(self):
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)

    def Delete_Un_Numbers(self):
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)

    def Save_Numbers_Correct(self):
        if self.tableWidget_8.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "?????? ??", 'Numbers.txt', '*.txt')[0]
            if save_file != '':
                with open(save_file, 'w', encoding="utf-8") as f:
                    for i in range(self.tableWidget_8.rowCount()):
                        f.write(self.tableWidget_8.item(i, 0).text().strip() + '\n')
                self.Box.exec()

    def Save_Numbers_UnCorrect(self):
        if self.tableWidget_9.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "?????? ??", 'UnNumbers.txt', '*.txt')[0]
            if save_file != '':
                with open(save_file, 'w', encoding="utf-8") as f:
                    for i in range(self.tableWidget_9.rowCount()):
                        f.write(self.tableWidget_9.item(i, 0).text().strip() + '\n')
                self.Box.exec()

    def final_single_Test(self):
        self.OpenDriver.is_used_now = False
        self.pushButton_9.setDisabled(False)
        self.pushButton_7.setDisabled(False)
        self.pushButton_10.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(False)
        self.pushButton_36.setDisabled(False)
        self.pushButton_14.setDisabled(False)
        self.pushButton_23.setDisabled(False)
        self.pushButton_37.setDisabled(False)
        self.pushButton_42.setDisabled(False)
        self.pushButton_43.setDisabled(False)

    @staticmethod
    def final_single_Message_Test():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("???? ????????????????")
        Box.setText("???? ???????????????? ???? ???????????? ???????? ??????????????")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

'''
https://web.whatsapp.com/send?phone=%2B201068009959&text&app_absent=0
1- ?????? ????????????.
 2- ???????????? ?????????? ???????????? ???????????? ???? ????. 
 3- ???????? ?????????? ????????????????. 
 4- ???????? ?????????? ??????????. 
 5-?????? ?????????????? ???? ???????????????? 
'''
r'''
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
pyside2-uic ui.ui -o mainwindow.py
pyside6-rcc icons.rc -o rc_icons.py

C:\Users\3mora\anaconda3\envs\python6\Lib\site-packages\selenium\webdriver\common\service.py
'''

'''
        # pixmap = QPixmap(32, 32)
        # pixmap.fill(Qt.transparent)
        # self.setWindowIcon(QIcon(pixmap))

pyinstaller --windowed --icon "C:/Users/3mora/Dropbox/All/whats_app/logo.ico" --add-data "C:/Users/3mora/Dropbox/All/whats_app/logo.png;."  "C:/Users/3mora/Dropbox/All/whats_app/main.py"
'''
