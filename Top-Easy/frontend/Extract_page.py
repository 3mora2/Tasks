import json

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *

from backend.Login import Login
from backend.Save_Aqar_To_Excel import SaveAqarExcel
from backend.start_extract import StartAqar


class WindowExtract:
    lineEdit_11: QLineEdit
    pushButton_20: QPushButton
    tableWidget_2: QTableWidget
    tabWidget: QTabWidget

    def __init__(self):
        self.Handel_Button_Aqar()
        self.Handel_Default_Aqar()
        self.Handel_Ui_Aqar()

        self.Login = Login()
        self.Login.final.connect(self.Final_Message_Login_Aqar)
        self.Login.error.connect(self.Login_Error_Aqar)

        self.StartAqar = StartAqar()
        self.StartAqar.final.connect(self.Final_Aqar_Message)
        self.StartAqar.error.connect(self.Error_Aqar)

        self.SaveAqarExcel = SaveAqarExcel()
        self.SaveAqarExcel.final.connect(self.Save_alert_Aqar)

    def Handel_Ui_Aqar(self):
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.setWindowIcon(QIcon('logo.ico'))

    def Handel_Default_Aqar(self):
        self.Read_data()

    def Handel_Button_Aqar(self):
        self.pushButton_19.clicked.connect(self.Save_Username)
        self.pushButton_25.clicked.connect(self.Save_Email)

        self.pushButton_20.clicked.connect(self.Login_Aqar)

        self.pushButton_14.clicked.connect(self.Start_Aqar)
        self.pushButton_12.clicked.connect(self.Pause_StartAqar_Aqar)
        self.pushButton_13.clicked.connect(self.Restart_StartAqar_Aqar)
        self.pushButton_15.clicked.connect(self.Stop_StartAqar_Aqar)
        self.pushButton_16.clicked.connect(self.Skip_StartAqar_Aqar)
        self.pushButton_18.clicked.connect(self.Clear_Aqar)
        self.pushButton_17.clicked.connect(self.Save_File_Aqar)

    def Read_data(self):
        try:
            with open('username', 'r') as f:
                d = f.read()
                d = json.loads(d)
                username = d.get('username')
                password = d.get('password')
                self.lineEdit_11.setText(username)
                self.lineEdit_12.setText(password)
        except:
            pass
        try:
            with open('emails', 'r') as f:
                d = f.read()
                d = json.loads(d)
                emails = d.get('emails')
                password = d.get('password')
                emailr = d.get('emailr')

                self.lineEdit_13.setText(emails)
                self.lineEdit_14.setText(password)
                self.lineEdit_15.setText(emailr)
        except:
            pass

    def Save_Username(self):
        username = self.lineEdit_11.text()
        password = self.lineEdit_12.text()
        if username and password:
            with open('username', 'w') as f:
                f.write(json.dumps({'username': username, 'password': password}))
        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("تحذير")
            Box.setText("ادخل اسم المستخدم وكلمة المرور!")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec_()

    def Save_Email(self):
        emails = self.lineEdit_13.text()
        password = self.lineEdit_14.text()
        emailr = self.lineEdit_15.text()
        if emails and password and emailr:
            with open('emails', 'w') as f:
                f.write(json.dumps({'emails': emails, 'password': password, 'emailr': emailr}))
        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("تحذير")
            Box.setText("ادخل كل البيانات!")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec_()

    def Login_Aqar(self):
        email = self.lineEdit_11.text()
        password = self.lineEdit_12.text()
        if email and password:
            self.Login.email = email
            self.Login.password = password
            self.Login.start()
            self.pushButton_20.setDisabled(True)
            self.pushButton_19.setDisabled(True)

            self.pushButton_16.setDisabled(True)
            self.pushButton_12.setDisabled(True)
            self.pushButton_13.setDisabled(True)
            self.pushButton_14.setDisabled(True)
            self.pushButton_15.setDisabled(True)
            self.pushButton_18.setDisabled(True)
            self.pushButton_17.setDisabled(True)

        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("تحذير")
            Box.setText("ادخل اسم المستخدم وكلمة المرور")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec_()

    def Final_Login_Aqar(self):
        self.pushButton_20.setDisabled(False)
        self.pushButton_19.setDisabled(False)

        self.pushButton_16.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(False)
        self.pushButton_15.setDisabled(True)
        self.pushButton_18.setDisabled(False)
        self.pushButton_17.setDisabled(False)

    def Final_Message_Login_Aqar(self):
        self.Final_Login_Aqar()
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تم")
        Box.setText("تم فتح الموقع")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Login_Error_Aqar(self):
        self.Final_Login_Aqar()
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("خطأ")
        Box.setText(" خطا في تسجيل الدخول \nمن فضل اكمل تسجيل الدخول يدويا!")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    ##############################################################

    def Start_Aqar(self):
        init = self.spinBox_4.value()
        num = self.spinBox_3.value()

        if init > 0 and num > 0:
            self.StartAqar.tableWidget_2 = self.tableWidget_2
            self.StartAqar.driver = self.Login.driver
            self.StartAqar.check = self.Login.check
            self.StartAqar.init = init
            self.StartAqar.num = num
            self.StartAqar.sleep = self.spinBox_5.value()
            self.StartAqar.is_send_email = self.checkBox.isChecked()
            self.StartAqar.SENDER_EMAIL = self.lineEdit_13.text()
            self.StartAqar.APP_PASSWORD = self.lineEdit_14.text()
            self.StartAqar.Recipient_email = self.lineEdit_15.text()
            self.StartAqar.start()
            self.pushButton_16.setDisabled(False)
            self.pushButton_12.setDisabled(False)
            self.pushButton_13.setDisabled(True)
            self.pushButton_14.setDisabled(True)
            self.pushButton_15.setDisabled(False)

            self.pushButton_20.setDisabled(True)
            self.pushButton_18.setDisabled(True)
            self.pushButton_17.setDisabled(True)

        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle("تنبيه")
            Box.setText("عدد الصفح لا يجب ان يساوي (0)!")
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

    @staticmethod
    def Cant_Save():
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("تنبيه")
        Box.setText("لا يوجد شئ لحفظه...")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Save_File_Aqar(self):
        try:
            if self.tableWidget_2.rowCount() == 0:
                self.Cant_Save()
            else:
                save_file = QFileDialog.getSaveFileName(self, caption="حفظ ك", dir='result.xlsx', filter='*.xlsx')[0]
                if save_file != '':
                    self.SaveAqarExcel.tableWidget_2 = self.tableWidget_2
                    self.SaveAqarExcel.filename = save_file
                    self.SaveAqarExcel.start()
                    self.pushButton_18.setDisabled(True)
                    self.pushButton_17.setDisabled(True)


        except Exception as e:
            print(e)

    def Clear_Aqar(self):
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)

    def Pause_StartAqar_Aqar(self):
        self.StartAqar.pause = True
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(False)

    def Restart_StartAqar_Aqar(self):
        self.StartAqar.pause = False
        self.pushButton_12.setDisabled(False)
        self.pushButton_13.setDisabled(True)

    def Skip_StartAqar_Aqar(self):
        self.StartAqar.skip = True
        self.pushButton_16.setDisabled(True)

    def Stop_StartAqar_Aqar(self):
        self.StartAqar.stop = True
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_15.setDisabled(True)

    def Final_Aqar(self):
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(False)
        self.pushButton_20.setDisabled(False)
        self.pushButton_15.setDisabled(True)

        self.pushButton_18.setDisabled(False)
        self.pushButton_17.setDisabled(False)

    def Final_Aqar_Message(self):
        self.Final_Aqar()
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تنبيه")
        Box.setText("تم الانتهاء")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Error_Aqar(self):
        self.Final_Aqar()
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setWindowTitle("خطأ")
        Box.setText("حدث خطا")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

    def Save_alert_Aqar(self):
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تنبيه")
        Box.setText("تم")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()
        self.pushButton_18.setDisabled(False)
        self.pushButton_17.setDisabled(False)
