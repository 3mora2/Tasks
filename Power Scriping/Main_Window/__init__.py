import os
import sys

from PySide2.QtWidgets import QMainWindow, QApplication

from Maps import MapsMainWindow
from Social import SocialMainWindow
from Webs import WebMainWindow
from loader_ui import loadUi

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi(os.path.join(SCRIPT_DIRECTORY, 'main_ui.ui'), self)
        self.Handel_Button()

    def Handel_Button(self):
        self.pushButton.clicked.connect(self.Webs)
        self.pushButton_2.clicked.connect(self.Social)
        self.pushButton_3.clicked.connect(self.Maps)

    def Maps(self):
        self.close()
        start.window = MapsMainWindow()
        start.window.show()

    def Social(self):
        self.close()
        start.window = SocialMainWindow()
        start.window.show()

    def Webs(self):
        self.close()
        start.window = WebMainWindow()
        start.window.show()


class Run:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

    def run(self):
        self.window.show()
        self.app.exec_()


start = Run()
