import os
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from Social.Instagram import InstagramWindow
from loader_ui import loadUi

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class SocialMainWindow(QMainWindow, InstagramWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi(os.path.join(SCRIPT_DIRECTORY, 'Social_ui.ui'), self)

        InstagramWindow.__init__(self)

        self.Handel_Button_Social()
        self.Handel_Default_Social()
        self.Handel_Ui_Social()

    def Handel_Ui_Social(self):
        pass

    def Handel_Default_Social(self):
        pass

    def Handel_Button_Social(self):
        self.pushButton_5.clicked.connect(self.Facebook_tab)
        self.pushButton_6.clicked.connect(self.MainWindow_tab)
        self.pushButton_7.clicked.connect(self.Instagram_tab)

    def MainWindow_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Instagram_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Facebook_tab(self):
        self.tabWidget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SocialMainWindow()
    window.show()
    app.exec_()
