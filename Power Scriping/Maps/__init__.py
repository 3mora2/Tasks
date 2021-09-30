import os
import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QApplication

from Maps.Google_Maps import WindowGoogle
from Maps.Yellow_Pages import WindowYellow
from Maps.Maps_window import WindowMaps
from loader_ui import loadUi

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class MapsMainWindow(QMainWindow, WindowGoogle, WindowYellow, WindowMaps):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi(os.path.join(SCRIPT_DIRECTORY, 'Maps_ui.ui'), self)
        WindowGoogle.__init__(self)
        WindowYellow.__init__(self)
        WindowMaps.__init__(self)

        self.Handel_Button()
        self.Handel_Ui()

    def Handel_Button(self):
        self.pushButton_5.clicked.connect(self.Yellow_Tab)
        self.pushButton_6.clicked.connect(self.Main_Tab)
        self.pushButton_7.clicked.connect(self.Google_Tab)

    def Handel_Ui(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'logo.ico'))
        self.tabWidget.tabBar().setVisible(False)

    def Main_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Google_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Yellow_Tab(self):
        self.tabWidget.setCurrentIndex(2)


# def run_maps():
#     window = MapsMainWindow()
#     window.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapsMainWindow()
    window.show()
    app.exec_()