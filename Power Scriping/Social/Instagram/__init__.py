from PySide2.QtWidgets import *

from Social.Instagram.login import Login


class InstagramWindow:
    tabWidget_2: QTabWidget
    tabWidget_2: QTabWidget
    pushButton: QPushButton
    pushButton_2: QPushButton
    pushButton_3: QPushButton
    pushButton_4: QPushButton
    pushButton_5: QPushButton
    pushButton_6: QPushButton
    pushButton_7: QPushButton
    pushButton_8: QPushButton
    pushButton_9: QPushButton
    pushButton_10: QPushButton
    pushButton_11: QPushButton
    pushButton_12: QPushButton
    pushButton_13: QPushButton

    lineEdit: QLineEdit
    lineEdit_2: QLineEdit

    def __init__(self):
        self.Handel_Button_Instagram()
        # self.Handel_Default_Instagram()
        # self.Handel_Ui_Instagram()
        self.Login_account = Login()

    def Handel_Ui_Instagram(self):
        pass

    def Handel_Default_Instagram(self):
        pass

    def Handel_Button_Instagram(self):
        self.pushButton.clicked.connect(self.Manage_account_tab)
        self.pushButton_2.clicked.connect(self.Extract_likes_tab)
        self.pushButton_3.clicked.connect(self.Extract_follows_tab)
        self.pushButton_4.clicked.connect(self.Extract_posts_tab)
        # self.pushButton_5.clicked.connect(self.Start_Instagram)
        # self.pushButton_6.clicked.connect(self.Start_Instagram)
        # self.pushButton_7.clicked.connect(self.Start_Instagram)
        self.pushButton_8.clicked.connect(self.Extract_comments_tab)
        self.pushButton_9.clicked.connect(self.Extract_information_id_tab)
        self.pushButton_10.clicked.connect(self.Login)
        self.pushButton_11.clicked.connect(self.Download_posts_tab)
        self.pushButton_12.clicked.connect(self.Start_login_from_table)

    def Manage_account_tab(self):
        self.tabWidget_2.setCurrentIndex(0)

    def Extract_likes_tab(self):
        self.tabWidget_2.setCurrentIndex(2)

    def Extract_follows_tab(self):
        self.tabWidget_2.setCurrentIndex(1)

    def Extract_posts_tab(self):
        self.tabWidget_2.setCurrentIndex(5)

    def Extract_comments_tab(self):
        self.tabWidget_2.setCurrentIndex(3)

    def Extract_information_id_tab(self):
        self.tabWidget_2.setCurrentIndex(4)

    def Download_posts_tab(self):
        self.tabWidget_2.setCurrentIndex(6)

    def Login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username and password:
            self.Login_account.username = username
            self.Login_account.password = password
            self.Login_account.start()
        else:
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setWindowTitle('تنبيه!')
            Box.setText('ادخل اسم المستخدم وكلمة المرور')
            Box.setStandardButtons(QMessageBox.Ok)
            Box.exec()

    def Start_login_from_table(self):
        pass
