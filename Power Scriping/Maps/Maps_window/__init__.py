from PySide2 import QtCore
from PySide2.QtWidgets import QMessageBox

from Activations.check import Check
from Activations.Add import Add


class WindowMaps:

    def __init__(self):
        self.Handel_Button_Maps()
        self.Handel_Default_Maps()
        self.Check = Check(__name__)
        self.Add = Add(__name__)
        self.Handel_check()

    def Handel_Default_Maps(self):
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)

    def Handel_Button_Maps(self):
        self.pushButton_49.clicked.connect(self.check_serial)

    def Handel_check(self):
        res = self.Check.start()
        try:
            if res[0] and res[1]:
                self.lineEdit_5.setText(
                    f' تاريخ انتهاء الاشتراك :{res[0].year}/{res[0].month}/{res[0].day}')
                self.lineEdit_4.hide()
                self.pushButton_49.hide()

            elif res[0] is False and res[1]:
                self.lineEdit_5.setText('انتهت صلاحية السيريال هذه النسخة تجريبية')
                self.lineEdit_4.show()
                self.pushButton_49.show()

            else:
                self.lineEdit_5.setText('هذه النسخة تجريبية')
                self.lineEdit_4.show()
                self.pushButton_49.show()

        except Exception as e:
            print(e)

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
            if self.Add.start(text):
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
