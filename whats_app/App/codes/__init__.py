script = """var elm = arguments[0],
txt = arguments[1];
elm.textContent = txt;
elm.dispatchEvent(new Event('keydown', {bubbles: true}));
elm.dispatchEvent(new Event('keypress', {bubbles: true}));
elm.dispatchEvent(new Event('input', {bubbles: true}));
elm.dispatchEvent(new Event('keyup', {bubbles: true}));"""
import webbrowser
from typing import Union
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
import warnings
import os
from codes.ExtractContent import ExtractContent
from codes.ExtractGroup import ExtractGroup
from codes.GroupSender import GroupSender
from codes.OpenDriver import OpenDriver
from codes.SenderNumber import SenderNumber
from codes.TestNumber import TestNumber
from codes.AddMemmbers import AddMembers
import start
from codes.mainwindow import Ui_MainWindow
from codes.phone_number import countries
os.environ['WDM_LOG_LEVEL'] = '0'
if not sys.warnoptions:
    warnings.simplefilter("ignore")

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


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

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
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

        self.ExtractContent = ExtractContent()
        self.ExtractContent.error.connect(self.Error_Single)
        self.ExtractContent.final.connect(self.final_single_Extract_Content)
        self.ExtractContent.driver_error.connect(self.Driver_Error)
        self.ExtractContent.final_message.connect(self.final_single_Message_Extract_Content)
        self.ExtractContent.limit_message.connect(self.show_limit)

        self.AddMember = AddMembers()
        self.AddMember.error.connect(self.Error_Single)
        self.AddMember.error_group.connect(self.error_group_AddMember)
        self.AddMember.final.connect(self.final_single_AddMember)
        self.AddMember.driver_error.connect(self.Driver_Error)
        self.AddMember.final_message.connect(self.final_single_Message_AddMember)
        self.AddMember.limit_message.connect(self.show_limit)

    def Handel_Ui(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon('logo.ico'))
        # self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'logo.ico'))
        self.setWindowTitle(" ")
        self.tabWidget.tabBar().setVisible(False)
        self.showMaximized()

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
        self.tableWidget_12.verticalHeader().setVisible(False)

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
        self.tableWidget_12.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_8.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_9.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_12.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.setFixedSize(self.size().width(), self.size().height())
        self.Box = QMessageBox()
        self.Box.setIcon(QMessageBox.Information)
        self.Box.setWindowTitle("تم الحفظ")
        self.Box.setText("تم حفظ الملف")
        self.Box.setStandardButtons(QMessageBox.Ok)
        self.Box_Limit = QMessageBox()
        self.Box_Limit.setIcon(QMessageBox.Information)
        self.Box_Limit.setWindowTitle("تنبيه")
        self.Box_Limit.setText("هذه النسخة تجريبية \nيجب ادخال السيريال للانتهاء.")
        self.Box_Limit.setStandardButtons(QMessageBox.Ok)

    def Handel_Default(self):
        self.tabWidget.setCurrentIndex(0)

        self.pushButton_10.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)

        self.pushButton_16.setDisabled(True)
        self.pushButton_17.setDisabled(True)
        self.pushButton_21.setDisabled(True)

        self.pushButton_31.setDisabled(True)
        self.pushButton_33.setDisabled(True)
        self.pushButton_35.setDisabled(True)

        self.pushButton_53.setDisabled(True)
        self.pushButton_54.setDisabled(True)
        self.pushButton_55.setDisabled(True)

        self.pushButton_58.setDisabled(True)

        self.radioButton_2.click()
        self.radioButton_3.click()

        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)

    def Handel_Button(self):
        self.pushButton_49.clicked.connect(self.check_serial)
        self.pushButton_57.clicked.connect(self.open_whatsapp)

        self.pushButton_48.clicked.connect(self.Main_Tab)
        self.pushButton.clicked.connect(self.Test_Tab)
        self.pushButton_2.clicked.connect(self.Group_Tab)

        self.pushButton_5.clicked.connect(self.Open_Driver)

        self.pushButton_3.clicked.connect(self.Privet_Tab)
        self.pushButton_19.clicked.connect(self.Dialog_1)
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
        self.pushButton_58.clicked.connect(self.Stop_Extract_Content)
        self.pushButton_26.clicked.connect(self.Save_Group_Names)
        self.pushButton_27.clicked.connect(self.Delete_Group_Names)
        self.pushButton_40.clicked.connect(self.Delete_Contact_Name)
        self.pushButton_41.clicked.connect(self.Save_Contact_Name)
        self.pushButton_39.clicked.connect(self.Save_Numbers_Extract)
        self.pushButton_38.clicked.connect(self.Delete_Numbers_Extract)

        self.pushButton_9.clicked.connect(self.Dialog_1)
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

        self.pushButton_56.clicked.connect(self.Add_Member_Tab)
        self.pushButton_50.clicked.connect(self.Delete_AddMember)
        self.pushButton_51.clicked.connect(self.Dialog_1)
        self.pushButton_52.clicked.connect(self.Add_Member)
        self.pushButton_53.clicked.connect(self.Pause_AddMember)
        self.pushButton_54.clicked.connect(self.Restart_AddMember)
        self.pushButton_55.clicked.connect(self.Stop_AddMember)

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
                        f' تاريخ انتهاء الاشتراك :{res[0].year}/{res[0].month}/{res[0].day}')
                    self.lineEdit_4.hide()
                    self.pushButton_49.hide()
                    self.limit = None
                elif res[0] is False and res[1]:
                    self.lineEdit_5.setText('انتهت صلاحية السيريال هذه النسخة تجريبية')
                    self.lineEdit_4.show()
                    self.pushButton_49.show()
                    self.limit = 5

                else:
                    self.lineEdit_5.setText('هذه النسخة تجريبية')
                    self.lineEdit_4.show()
                    self.pushButton_49.show()
                    self.limit = 5
            except Exception as e:
                print(e)
        else:
            self.lineEdit_4.show()
            self.pushButton_49.show()
            self.lineEdit_5.setText('هذه النسخة تجريبية')

    def check_serial(self):
        text = self.lineEdit_4.text()
        if text == '' or text is None:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("تحذير")
            Box.setText("من فضلك ادخل السيريال")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            if start.add_new(text):
                Box = QMessageBox()
                Box.setIcon(QMessageBox.Information)
                Box.setWindowTitle("تنبيه")
                Box.setText("تم تفعيل السريال بنجاح")
                Box.setStandardButtons(QMessageBox.Ok)
                Box.exec()
                self.Handel_check()
            else:
                Box = QMessageBox()
                Box.setIcon(QMessageBox.Warning)
                Box.setWindowTitle("خطا")
                Box.setText(" حدث خطأ \nهذا السيريال غير صحيح.")
                Box.setStandardButtons(QMessageBox.Ok)
                Box.exec()

    def show_limit(self):
        self.Box_Limit.exec()

    def open_whatsapp(self):
        webbrowser.open("https://wa.me/message/EWGPANBBSM5PM1")

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

    def Add_Member_Tab(self):
        self.tabWidget.setCurrentIndex(6)

    ####################################################################################################################
    ####################################################################################################################

    def Open_Driver(self):
        if not self.OpenDriver.Try:
            self.OpenDriver.start()
        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("تحذير")
            Box.setText("جاري فتح الموقع")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

    def Final_Open_Driver(self):
        self.OpenDriver.reopen = False
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تم")
        Box.setText("تم فتح الموقع")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Found_Open_Driver(self):
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("تحذير")
        Box.setText("الموقع مفتوح مسبقا\n هل تريد اعادة فتح المتصفح ؟")
        Box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Open)
        ret = Box.exec_()
        if ret == QMessageBox.Open:
            self.OpenDriver.reopen = True
            self.OpenDriver.start()

    @staticmethod
    def Driver_Error():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("خطأ")
        Box.setText("يجب فتح الموقع اولا")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    @staticmethod
    def Driver_Download():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تنبيه")
        Box.setText(" جاري تنزيل بعض الملفات \n قد يستغرق ذالك بضع دقائق")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ####################################################################################################################
    ####################################################################################################################

    def Extract_Group(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("خطأ")
            Box.setText("لا يمكن تنفيذ عملتين في وقت واحد")
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
            save_file = QFileDialog.getSaveFileName(self, "حفظ ك", 'numbers.txt', '*.txt')[0]
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
        Box.setWindowTitle("تم")
        Box.setText("تم استخراج جميع الاعضاء")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    @staticmethod
    def Not_Group():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("غير موجود")
        Box.setText("غير موجود\nيجب فتح القروب المراد استخراج الاعضاء منه")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    @staticmethod
    def Error_Single(error):
        print('- You should open whatsapp', error)

    @staticmethod
    def error_vcf():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("خطأ")
        Box.setText("ادخل اسم للحفظ")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Save_VCF_(self, text, tableWidget: QTableWidget):
        if tableWidget.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "حفظ ك", 'numbers.vcf', '*.vcf')[0]
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
            Box.setWindowTitle("خطأ")
            Box.setText("لا يمكن تنفيذ عملتين في وقت واحد")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            if not self.ExtractContent.Try:
                self.pushButton_25.setDisabled(True)
                self.pushButton_26.setDisabled(True)
                self.pushButton_27.setDisabled(True)
                self.pushButton_40.setDisabled(True)
                self.pushButton_41.setDisabled(True)
                self.pushButton_39.setDisabled(True)
                self.pushButton_38.setDisabled(True)
                self.pushButton_58.setDisabled(False)

                self.ExtractContent.tableWidget_5 = self.tableWidget_5
                self.ExtractContent.tableWidget_10 = self.tableWidget_10
                self.ExtractContent.tableWidget_11 = self.tableWidget_11
                self.ExtractContent.driver = self.OpenDriver.driver
                self.ExtractContent.check_live = self.OpenDriver.check_live
                self.ExtractContent.limit = self.limit
                self.ExtractContent.start()
                self.OpenDriver.is_used_now = True
            else:
                print('- found', self.SenderNumber.Try)

    def Stop_Extract_Content(self):
        self.ExtractContent.stop = True
        self.pushButton_25.setDisabled(True)

    def Save_Group_Names(self):
        if self.tableWidget_5.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "حفظ ك", 'Groups.txt', '*.txt')[0]
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
            save_file = QFileDialog.getSaveFileName(self, "حفظ ك", 'Groups.txt', '*.txt')[0]
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
            save_file = QFileDialog.getSaveFileName(self, "حفظ ك", 'Groups.txt', '*.txt')[0]
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
        self.pushButton_58.setDisabled(True)

    @staticmethod
    def final_single_Message_Extract_Content():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تم الانتهاء")
        Box.setText("تم الانتهاء من استخراج جميع الاسماء")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ####################################################################################################################
    ####################################################################################################################

    def Group_Sender(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("خطأ")
            Box.setText("لا يمكن تنفيذ عملتين في وقت واحد")
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

            deleteButton = QPushButton("حذف")

            deleteButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.delete_clicked_GroupSender)
            self.tableWidget_7.setCellWidget(r, 3, deleteButton)

    def Add_Image_GroupSender(self):
        text = self.textEdit_2.toPlainText().strip()

        save_file = QFileDialog.getOpenFileName(self, "اختار", '', '*.*')[0]
        if save_file != '':
            r = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(r)
            if text != '':
                self.tableWidget_7.setItem(r, 0, QTableWidgetItem(str(text)))
            self.tableWidget_7.setItem(r, 1, QTableWidgetItem(str(save_file)))
            self.tableWidget_7.setItem(r, 2, QTableWidgetItem(str('img')))

            deleteButton = QPushButton("حذف")

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
        save_file = QFileDialog.getOpenFileName(self, "اختار", '', '*.txt')[0]
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
        Box.setWindowTitle("تم الانتهاء")
        Box.setText("تم الانتهاء من الارسال")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ####################################################################################################################
    ####################################################################################################################

    def Privet_Sender(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("خطأ")
            Box.setText("لا يمكن تنفيذ عملتين في وقت واحد")
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

            deleteButton = QPushButton("حذف")

            deleteButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.delete_clicked)
            self.tableWidget_4.setCellWidget(r, 3, deleteButton)
        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("تحذير")
            Box.setText("يجب ادخال النص")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

    def Add_Image_Private_Send(self):
        text = self.textEdit.toPlainText().strip()

        save_file = QFileDialog.getOpenFileName(self, "اختار صورة/فديو", '', '*.*')[0]
        if save_file != '':
            r = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(r)
            if text != '':
                self.tableWidget_4.setItem(r, 0, QTableWidgetItem(str(text)))
            self.tableWidget_4.setItem(r, 1, QTableWidgetItem(str(save_file)))
            self.tableWidget_4.setItem(r, 2, QTableWidgetItem(str('img')))

            deleteButton = QPushButton("حذف")

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
        save_file = QFileDialog.getOpenFileName(self, "اختار", 'numbers.txt', '*.txt')[0]
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
        Box.setWindowTitle("تم الانتهاء")
        Box.setText("تم الانتهاء من الارسال")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ####################################################################################################################
    ####################################################################################################################

    def Start_Test_Numbers(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("خطأ")
            Box.setText("لا يمكن تنفيذ عملتين في وقت واحد")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        elif self.tableWidget_2.rowCount() == 0:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("خطأ")
            Box.setText("يجب ادخال الارقام اولا")
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
                self.TestNumbers.sleep = self.spinBox_5.value()
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
            Box.setWindowTitle("تحذير")
            Box.setText("يجب لصق الارقام اولا")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

    @staticmethod
    def Save_Error():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("تحذير")
        Box.setText("لا يوجد شئ لحفظه")
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
        save_file = QFileDialog.getOpenFileName(self, "اختار", 'numbers.txt', '*.txt')[0]
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
        self.tableWidget_8.clearContents()
        self.tableWidget_8.setRowCount(0)

    def Delete_Un_Numbers(self):
        self.tableWidget_9.clearContents()
        self.tableWidget_9.setRowCount(0)

    def Save_Numbers_Correct(self):
        if self.tableWidget_8.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "حفظ ك", 'Numbers.txt', '*.txt')[0]
            if save_file != '':
                with open(save_file, 'w', encoding="utf-8") as f:
                    for i in range(self.tableWidget_8.rowCount()):
                        f.write(self.tableWidget_8.item(i, 0).text().strip() + '\n')
                self.Box.exec()

    def Save_Numbers_UnCorrect(self):
        if self.tableWidget_9.rowCount() == 0:
            self.Save_Error()
        else:
            save_file = QFileDialog.getSaveFileName(self, "حفظ ك", 'UnNumbers.txt', '*.txt')[0]
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
        Box.setWindowTitle("تم الانتهاء")
        Box.setText("تم الانتهاء من اختبار جميع الارقام")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    #########################################################################################

    def Add_Member(self):
        if self.OpenDriver.is_used_now:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("خطأ")
            Box.setText("لا يمكن تنفيذ عملتين في وقت واحد")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            self.AddMember.stop = False
            if not self.AddMember.Try:
                self.pushButton_50.setDisabled(True)
                self.pushButton_51.setDisabled(True)
                self.pushButton_52.setDisabled(True)
                self.pushButton_53.setDisabled(False)
                self.pushButton_54.setDisabled(True)
                self.pushButton_55.setDisabled(False)

                self.AddMember.tableWidget_12 = self.tableWidget_12
                self.AddMember.driver = self.OpenDriver.driver
                self.AddMember.check_live = self.OpenDriver.check_live
                self.AddMember.limit = self.limit
                self.AddMember.start()
                self.OpenDriver.is_used_now = True
            else:
                print('- found', self.AddMember.Try)

    def Pause_AddMember(self):
        self.AddMember.pause = True
        self.pushButton_53.setDisabled(True)
        self.pushButton_54.setDisabled(False)

    def Restart_AddMember(self):
        self.AddMember.pause = False
        self.pushButton_53.setDisabled(False)
        self.pushButton_54.setDisabled(True)

    def Stop_AddMember(self):
        self.AddMember.Stop()
        self.pushButton_55.setDisabled(True)

    def Open_File_AddMember(self):
        pass
        # self.Dialog_1()
        # save_file = QFileDialog.getOpenFileName(self, "اختار", '', '*.txt')[0]
        # if save_file != '':
        #     old_number = [self.tableWidget_12.item(i, 0).text() for i in range(self.tableWidget_12.rowCount())]
        #     with open(save_file, 'r', encoding="utf-8") as f:
        #         for num in f.read().split('\n'):
        #             if num not in old_number and num.strip() != '':
        #                 r = self.tableWidget_12.rowCount()
        #                 self.tableWidget_12.insertRow(r)
        #                 self.tableWidget_12.setItem(r, 0, QTableWidgetItem(str(num)))

    def Delete_AddMember(self):
        self.tableWidget_12.clearContents()
        self.tableWidget_12.setRowCount(0)

    @staticmethod
    def error_group_AddMember():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("تنبيه")
        Box.setText("افتح الجروب اولا..")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def final_single_AddMember(self):
        self.OpenDriver.is_used_now = False
        self.pushButton_50.setDisabled(False)
        self.pushButton_51.setDisabled(False)
        self.pushButton_52.setDisabled(False)
        self.pushButton_53.setDisabled(True)
        self.pushButton_54.setDisabled(True)
        self.pushButton_55.setDisabled(True)

    @staticmethod
    def final_single_Message_AddMember():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تم الانتهاء")
        Box.setText("تم الانتهاء")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Dialog_1(self):
        self.Dialog = Dialog = QDialog()
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(651, 505)
        Dialog.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(77, 137, 197);\n"
"color: rgb(244, 243, 242);\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"       background-color: rgb(114, 159, 207);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"gridline-color: #fffff8;\n"
"\n"
"background: transparent;\n"
"border : 1px solid rgb(77, 137, 197);\n"
"border-radius: 10px;\n"
"paddingg: 3 3px;\n"
"}\n"
"QHeaderView::section{\n"
" border-radius:7px;\n"
" background-color: rgb(77, 137, 197);\n"
"       color: rgb(244, 243, 242);\n"
"}\n"
"QTableWidget::item {\n"
"border : 1px solid rgb(77, 137, 197);\n"
"color: rgb(0, 0, 0);\n"
"       \n"
"}")
        gridLayout = QGridLayout(Dialog)
        gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_dialog = QTableWidget(Dialog)
        if (self.tableWidget_dialog.columnCount() < 3):
            self.tableWidget_dialog.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_dialog.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_dialog.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_dialog.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_dialog.setObjectName(u"tableWidget")
        self.tableWidget_dialog.horizontalHeader().setVisible(True)
        self.tableWidget_dialog.horizontalHeader().setHighlightSections(True)
        self.tableWidget_dialog.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_dialog.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_dialog.verticalHeader().setVisible(True)
        self.tableWidget_dialog.verticalHeader().setHighlightSections(True)

        gridLayout.addWidget(self.tableWidget_dialog, 0, 0, 2, 1)

        frame = QFrame(Dialog)
        frame.setObjectName(u"frame")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        gridLayout_2 = QGridLayout(frame)
        gridLayout_2.setObjectName(u"gridLayout_2")
        gridLayout_2.setContentsMargins(20, 10, 20, 10)
        pushButton_3 = QPushButton(frame)
        pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pushButton_3.sizePolicy().hasHeightForWidth())
        pushButton_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Almarai")
        font.setPointSize(11)
        pushButton_3.setFont(font)

        gridLayout_2.addWidget(pushButton_3, 0, 0, 1, 1)

        pushButton_2 = QPushButton(frame)
        pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(pushButton_2.sizePolicy().hasHeightForWidth())
        pushButton_2.setSizePolicy(sizePolicy)
        pushButton_2.setFont(font)

        gridLayout_2.addWidget(pushButton_2, 0, 1, 1, 1)


        gridLayout.addWidget(frame, 2, 0, 1, 2)

        frame_2 = QFrame(Dialog)
        frame_2.setObjectName(u"frame_2")
        frame_2.setFrameShape(QFrame.StyledPanel)
        frame_2.setFrameShadow(QFrame.Raised)
        gridLayout_3 = QGridLayout(frame_2)
        gridLayout_3.setObjectName(u"gridLayout_3")
        pushButton = QPushButton(frame_2)
        pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
        pushButton.setSizePolicy(sizePolicy)
        pushButton.setFont(font)

        gridLayout_3.addWidget(pushButton, 0, 0, 1, 1)
        gridLayout.addWidget(frame_2, 1, 1, 1, 1)

        gridLayout.setRowStretch(0, 4)
        gridLayout.setRowStretch(1, 1)
        gridLayout.setRowStretch(2, 1)
        gridLayout.setColumnStretch(0, 3)
        gridLayout.setColumnStretch(1, 1)
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.tableWidget_dialog.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u0627\u0644\u0643\u0648\u062f", None));
        ___qtablewidgetitem1 = self.tableWidget_dialog.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u0627\u0644\u0628\u0644\u062f", None));
        ___qtablewidgetitem2 = self.tableWidget_dialog.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u0627\u0644\u0645\u0644\u0641", None));
        pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u0627\u063a\u0644\u0627\u0642", None))
        pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0627\u0636\u0627\u0641\u0629", None))
        pushButton.setText(QCoreApplication.translate("Dialog", u"\u0627\u062e\u062a\u0631 \u0645\u0644\u0641", None))

        pushButton.clicked.connect(self.open_file)
        pushButton_2.clicked.connect(self.add_to_table)
        pushButton_3.clicked.connect(self.close_dialog)
        self.tableWidget_dialog.verticalHeader().setVisible(False)
        self.tableWidget_dialog.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dialog.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        QMetaObject.connectSlotsByName(Dialog)
        self.sender_dialog = self.sender().objectName()
        Dialog.exec_()

    def open_file(self):
        old_number = [self.tableWidget_dialog.item(i, 0).text() for i in range(self.tableWidget_dialog.rowCount())]
        openfile = QFileDialog.getOpenFileName(self, "اختار", 'numbers.txt', '*.txt')[0]
        if openfile != '':
            with open(openfile, 'r', encoding="utf-8") as f:
                for num in f.read().split('\n'):
                    if num.strip() != '' and num.startswith('+'):
                        num = num.replace(' ', '')
                        result = list(filter(lambda x: num.startswith('+' + str(x).replace(' ', '')), countries.keys()))
                        if result:
                            really = max(result, key=lambda x: len(x))
                            country = countries[really]
                            really = '+' + str(really)
                            if really not in old_number:
                                old_number.append(really)
                                r = self.tableWidget_dialog.rowCount()
                                self.tableWidget_dialog.insertRow(r)
                                __q_tablewidget_item = QTableWidgetItem(str(really))
                                __q_tablewidget_item.setCheckState(Qt.Checked)
                                self.tableWidget_dialog.setItem(r, 0, __q_tablewidget_item)
                                self.tableWidget_dialog.setItem(r, 1, QTableWidgetItem(str(country)))
                                self.tableWidget_dialog.setItem(r, 2, QTableWidgetItem(str(openfile)))

    def add_to_table(self):
        tableWidget = None
        if self.sender_dialog == 'pushButton_9':
            tableWidget = self.tableWidget_2
        elif self.sender_dialog == 'pushButton_19':
            tableWidget = self.tableWidget_3
        elif self.sender_dialog == 'pushButton_51':
            tableWidget = self.tableWidget_12

        if tableWidget:
            table_codes = [self.tableWidget_dialog.item(i, 0).text() for i in range(self.tableWidget_dialog.rowCount()) if self.tableWidget_dialog.item(i, 0).checkState() == Qt.CheckState.Checked]
            file_name = set(self.tableWidget_dialog.item(i, 2).text() for i in range(self.tableWidget_dialog.rowCount()) if self.tableWidget_dialog.item(i, 0).checkState() == Qt.CheckState.Checked)
            for openfile in file_name:
                with open(openfile, 'r', encoding="utf-8") as f:
                    for num in f.read().split('\n'):
                        if num.strip() != '' and num.startswith('+'):
                            num = num.replace(' ', '')
                            result = list(filter(lambda x: num.startswith('+' + str(x).replace(' ', '')), countries.keys()))
                            if result:
                                really = max(result, key=lambda x: len(x))
                                really = '+' + str(really)
                                if really in table_codes:
                                    old_number = [tableWidget.item(i, 0).text() for i in range(tableWidget.rowCount())]
                                    if num not in old_number:
                                        r = tableWidget.rowCount()
                                        tableWidget.insertRow(r)
                                        tableWidget.setItem(r, 0, QTableWidgetItem(str(num)))
        self.close_dialog()

    def close_dialog(self):
        self.Dialog.close()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


'''
pip install phonenumbers

pyside2-uic ui.ui -o mainwindow.py
pyside2-rcc icons.rc -o rc_icons.py
pyinstaller --windowed --icon "C:/Users/3mora/Dropbox/All/whats_app/logo.ico" --add-data "C:/Users/3mora/Dropbox/All/whats_app/logo.png;."  "C:/Users/3mora/Dropbox/All/whats_app/main.py"
'''

