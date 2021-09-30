from PySide2.QtWidgets import QPushButton, QTabWidget, QMessageBox, QFileDialog, QHeaderView
from Maps.Google_Maps.OpenDriverGoogle import OpenDriverGoogle
from Maps.Google_Maps.StartGoogle import StartGoogle
from Maps.Google_Maps.SaveDataGoogle import SaveAsGoogle


class WindowGoogle:
    data_google: dict
    pushButton: QPushButton
    tabWidget: QTabWidget

    def __init__(self):
        self.Handel_Button_Google()
        self.Handel_Default_Google()
        self.Handel_Ui_Google()

        self.OpenDriverGoogle = OpenDriverGoogle()
        self.OpenDriverGoogle.final.connect(self.Final_Open_Driver_Google)
        self.OpenDriverGoogle.error.connect(self.Driver_Error_Google)
        self.OpenDriverGoogle.wait.connect(self.Driver_Download_Google)

        self.StartGoogle = StartGoogle()
        self.StartGoogle.final.connect(self.Final_Google)
        self.StartGoogle.error_driver.connect(self.Driver_Error_Google)

        self.save_google = SaveAsGoogle()
        self.save_google.final.connect(self.Save_alert_Google)

    def Handel_Ui_Google(self):
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def Handel_Default_Google(self):
        self.lineEdit_6.setDisabled(False)
        self.pushButton.setDisabled(False)
        self.pushButton_4.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        self.pushButton_10.setDisabled(True)

    def Handel_Button_Google(self):
        self.pushButton.clicked.connect(self.Start_Google)
        self.pushButton_4.clicked.connect(self.Pause_StartGoogle_Google)
        self.pushButton_3.clicked.connect(self.Restart_StartGoogle_Google)
        self.pushButton_2.clicked.connect(self.Stop_StartGoogle_Google)
        self.pushButton_8.clicked.connect(self.Skip_StartGoogle_Google)
        self.pushButton_9.clicked.connect(self.Open_Driver_Google)
        self.pushButton_10.clicked.connect(self.Save_File_Google)
        self.pushButton_11.clicked.connect(self.Clear_Google)

    #############################################################

    def Open_Driver_Google(self):
        self.OpenDriverGoogle.pushButton_9 = self.pushButton_9
        if not self.OpenDriverGoogle.driver or not self.OpenDriverGoogle.check():
            self.OpenDriverGoogle.start()
        else:
            self.Found_Open_Driver_Google()

    @staticmethod
    def Final_Open_Driver_Google():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تم")
        Box.setText("تم فتح الموقع")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Found_Open_Driver_Google(self):
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("تحذير")
        Box.setText("الموقع مفتوح مسبقا\n هل تريد اعادة فتح المتصفح ؟")
        Box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Open)
        ret = Box.exec_()
        if ret == QMessageBox.Open:
            self.OpenDriverGoogle.do_reopen = True
            self.OpenDriverGoogle.start()

    @staticmethod
    def Driver_Download_Google():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تنبيه")
        Box.setText(" جاري تنزيل بعض الملفات \n قد يستغرق ذالك بضع دقائق")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    @staticmethod
    def Driver_Error_Google():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("خطأ")
        Box.setText("يجب فتح الموقع اولا")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ##############################################################

    def Start_Google(self):
        text = self.lineEdit_6.text()
        if text == '' or text is None:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("تحذير")
            Box.setText("من فضلك ادخل كلمات للبحث")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()
        else:
            if self.checkBox_2.isChecked():
                self.StartGoogle.open_url = True
            else:
                self.StartGoogle.open_url = False

            self.StartGoogle.tableWidget = self.tableWidget
            self.StartGoogle.tableWidget_2 = self.tableWidget_2
            self.StartGoogle.text = text
            self.StartGoogle.driver = self.OpenDriverGoogle.driver
            self.StartGoogle.check = self.OpenDriverGoogle.check
            self.StartGoogle.pause = False
            self.StartGoogle.stop = False
            self.StartGoogle.skip = False
            self.StartGoogle.start()
            self.lineEdit_6.setDisabled(True)
            self.pushButton.setDisabled(True)
            self.pushButton_4.setDisabled(False)
            self.pushButton_3.setDisabled(True)
            self.pushButton_2.setDisabled(False)
            self.pushButton_8.setDisabled(False)
            self.pushButton_9.setDisabled(True)
            self.pushButton_10.setDisabled(True)
            self.pushButton_11.setDisabled(True)

    @staticmethod
    def Cant_Save():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("تنبيه")
        Box.setText("لا يوجد شئ لحفظه...")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Save_File_Google(self):
        try:
            try:
                if not self.data_google:
                    self.Cant_Save()
                    return
            except:
                self.Cant_Save()
                return
            save_file = QFileDialog.getSaveFileName(parent=self, caption="حفظ ك", dir='result.xlsx', filter='*.xlsx')[0]
            if save_file != '':
                if self.checkBox.isChecked():
                    download_img = True
                else:
                    download_img = False

                self.save_google.data = self.data_google
                self.save_google.download_img = download_img
                self.save_google.save_file = save_file
                self.save_google.start()
                self.pushButton_10.setDisabled(True)
                self.pushButton_11.setDisabled(True)

        except Exception as e:
            print(e)

    def Clear_Google(self):
        self.data_google = dict()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)
        self.StartGoogle.data = dict()

    def Pause_StartGoogle_Google(self):
        self.StartGoogle.pause = True
        self.pushButton_4.setDisabled(True)
        self.pushButton_3.setDisabled(False)

    def Restart_StartGoogle_Google(self):
        self.StartGoogle.pause = False
        self.pushButton_4.setDisabled(False)
        self.pushButton_3.setDisabled(True)

    def Skip_StartGoogle_Google(self):
        self.StartGoogle.skip = True
        self.pushButton_8.setDisabled(True)

    def Stop_StartGoogle_Google(self):
        self.StartGoogle.stop = True
        self.pushButton_4.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)

    def Final_Google(self, data):
        self.data_google = data
        self.lineEdit_6.setDisabled(False)
        self.pushButton.setDisabled(False)
        self.pushButton_4.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        self.pushButton_9.setDisabled(False)
        self.pushButton_10.setDisabled(False)
        self.pushButton_11.setDisabled(False)
        if data:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Information)
            Box.setWindowTitle("تنبيه")
            Box.setText("تم الانتهاء")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

    def Save_alert_Google(self):
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تنبيه")
        Box.setText("تم حفظ الملف")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()
        self.pushButton_10.setDisabled(False)
        self.pushButton_11.setDisabled(False)
