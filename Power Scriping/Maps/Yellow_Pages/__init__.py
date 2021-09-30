from PySide2.QtWidgets import QHeaderView, QTableWidget, QPushButton, QMessageBox, QFileDialog, QCheckBox
from Maps.Yellow_Pages.OpenDriverYellow import OpenDriverYellow
from Maps.Yellow_Pages.SaveDataYellow import SaveAs
from Maps.Yellow_Pages.StartYellow import StartYellow


class WindowYellow:
    data_yellow: dict
    tableWidget_3: QTableWidget
    pushButton_12: QPushButton
    pushButton_13: QPushButton
    pushButton_14: QPushButton
    pushButton_15: QPushButton
    pushButton_16: QPushButton
    pushButton_18: QPushButton
    pushButton_19: QPushButton
    checkBox_3: QCheckBox

    def __init__(self):

        self.Handel_Button_Yellow()
        self.Handel_Default_Yellow()
        self.Handel_Ui_Yellow()

        self.OpenDriverYellow = OpenDriverYellow()
        self.OpenDriverYellow.final.connect(self.Final_Open_Driver_Yellow)
        self.OpenDriverYellow.error.connect(self.Driver_Error_Yellow)
        self.OpenDriverYellow.wait.connect(self.Driver_Download_Yellow)

        self.StartYellow = StartYellow()
        self.StartYellow.final.connect(self.Final_Yellow)
        self.StartYellow.error_driver.connect(self.Driver_Error_Yellow)

        self.save_yellow = SaveAs()
        self.save_yellow.final.connect(self.Save_alert_Yellow)

    def Handel_Default_Yellow(self):
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(True)
        self.pushButton_15.setDisabled(True)

    def Handel_Ui_Yellow(self):
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def Handel_Button_Yellow(self):
        self.pushButton_12.clicked.connect(self.Start_Yellow)
        self.pushButton_13.clicked.connect(self.Pause_Start_Yellow)
        self.pushButton_14.clicked.connect(self.Restart_Start_Yellow)
        self.pushButton_15.clicked.connect(self.Stop_Start_Yellow)
        self.pushButton_16.clicked.connect(self.Open_Driver_Yellow)
        self.pushButton_18.clicked.connect(self.Clear_Yellow)
        self.pushButton_19.clicked.connect(self.Save_File_Yellow)

    def Open_Driver_Yellow(self):
        self.OpenDriverYellow.pushButton_16 = self.pushButton_16
        if not self.OpenDriverYellow.driver or not self.OpenDriverYellow.check():
            self.OpenDriverYellow.start()
            self.pushButton_16.setDisabled(True)
        else:
            self.Found_Open_Driver_Yellow()

    def Final_Open_Driver_Yellow(self):
        self.pushButton_16.setDisabled(False)
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تم")
        Box.setText("تم فتح الموقع")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Found_Open_Driver_Yellow(self):
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("تحذير")
        Box.setText("الموقع مفتوح مسبقا\n هل تريد اعادة فتح المتصفح ؟")
        Box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Open)
        ret = Box.exec_()
        if ret == QMessageBox.Open:
            self.OpenDriverYellow.do_reopen = True
            self.OpenDriverYellow.start()
            self.pushButton_16.setDisabled(True)

    @staticmethod
    def Driver_Download_Yellow():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تنبيه")
        Box.setText(" جاري تنزيل بعض الملفات \n قد يستغرق ذالك بضع دقائق")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    @staticmethod
    def Driver_Error_Yellow():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("خطأ")
        Box.setText("يجب فتح الموقع اولا")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ##############################################################

    def Start_Yellow(self):
        self.StartYellow.tableWidget_3 = self.tableWidget_3
        self.StartYellow.driver = self.OpenDriverYellow.driver
        self.StartYellow.check = self.OpenDriverYellow.check
        self.StartYellow.pause = False
        self.StartYellow.stop = False
        self.StartYellow.skip = False
        self.StartYellow.start()
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(False)
        self.pushButton_14.setDisabled(True)
        self.pushButton_15.setDisabled(False)
        self.pushButton_16.setDisabled(True)
        self.pushButton_18.setDisabled(True)
        self.pushButton_19.setDisabled(True)

    @staticmethod
    def Cant_Save_Yellow():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("تنبيه")
        Box.setText("لا يوجد شئ لحفظه...")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Save_File_Yellow(self):
        try:
            try:
                if not self.data_yellow:
                    self.Cant_Save_Yellow()
                    return
            except:
                self.Cant_Save_Yellow()
                return
            save_file = QFileDialog.getSaveFileName(parent=self, caption="حفظ ك", dir='result.xlsx', filter='*.xlsx')[0]
            if save_file != '':
                if self.checkBox_3.isChecked():
                    download_img = True
                else:
                    download_img = False

                self.save_yellow.data = self.data_yellow
                self.save_yellow.download_img = download_img
                self.save_yellow.save_file = save_file
                self.save_yellow.start()
                self.pushButton_18.setDisabled(True)
                self.pushButton_19.setDisabled(True)

        except Exception as e:
            print(e)

    def Save_alert_Yellow(self):
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تنبيه")
        Box.setText("تم حفظ الملف")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()
        self.pushButton_18.setDisabled(False)
        self.pushButton_19.setDisabled(False)

    def Clear_Yellow(self):
        self.data_yellow = dict()
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(0)
        self.StartYellow.data = dict()

    def Pause_Start_Yellow(self):
        self.StartYellow.pause = True
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(False)

    def Restart_Start_Yellow(self):
        self.StartYellow.pause = False
        self.pushButton_13.setDisabled(False)
        self.pushButton_14.setDisabled(True)

    def Stop_Start_Yellow(self):
        self.StartYellow.stop = True
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(True)
        self.pushButton_15.setDisabled(True)

    def Final_Yellow(self, data):
        self.data_yellow = data
        self.pushButton_12.setDisabled(False)
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_16.setDisabled(False)
        self.pushButton_18.setDisabled(False)
        self.pushButton_19.setDisabled(False)
        if data:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Information)
            Box.setWindowTitle("تنبيه")
            Box.setText("تم الانتهاء")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

