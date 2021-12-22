# from PySide2.QtCore import QSize, QRect
# from PySide2.QtGui import Qt
from PySide2.QtWidgets import *
# from aqar_way import FULL_NAMES
from frontend.Extract_page import WindowExtract
# from frontend.Offers_Handle_Page import WindowOfferHandle
# from frontend.loader_ui import loadUi
# from settings import DB_URL
import os
# import sqlite3
import sys

from frontend.mainwindow import Ui_MainWindow

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class MainWindow(QMainWindow, WindowExtract, Ui_MainWindow):  # , WindowOfferHandle):

    def __init__(self, parent=None):
        # self.DataBase()
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # loadUi(os.path.join(SCRIPT_DIRECTORY, 'main.ui'), self)
        # loadUi('main.ui', self)
        WindowExtract.__init__(self)
        # WindowOfferHandle.__init__(self)

    # @staticmethod
    # def DataBase():
    #     db = sqlite3.connect(DB_URL)
    #     db.execute('''CREATE TABLE IF NOT EXISTS PRIMARY_OFFERS (
    #                     ID INTEGER PRIMARY KEY NOT NULL,
    #                     NAME TEXT NOT NULL,
    #                     PHONE TEXT,
    #                     ID_NUMBER TEXT,
    #                     IS_AQAR BOOLEAN NOT NULL DEFAULT TRUE,
    #                     DATA json
    #                     );
    #                     ''')
    #     db.commit()
    #     db.execute('''CREATE TABLE IF NOT EXISTS PRIMARY_USER (
    #                     ID INTEGER PRIMARY KEY NOT NULL,
    #                     NAME TEXT NOT NULL,
    #                     PHONE TEXT,
    #                     ID_NUMBER TEXT,
    #                     EMAIL TEXT,
    #                     IS_SENT BOOLEAN NOT NULL DEFAULT FALSE,
    #                     IS_DONE BOOLEAN NOT NULL DEFAULT FALSE
    #                     );''')
    #     db.commit()
    #     # Create table for Real offers
    #     db.execute('''CREATE TABLE IF NOT EXISTS REAL_OFFERS (
    #                     ID INTEGER PRIMARY KEY NOT NULL,
    #                     NAME TEXT NOT NULL,
    #                     PHONE TEXT,
    #                     ID_NUMBER TEXT,
    #                     EMAIL TEXT,
    #                     EXTRA_NUMBER TEXT,
    #                     OFFER_NAME TEXT,
    #                     DOCUMENTS TEXT,
    #                     OFFER_ID TEXT,
    #                     DATA json
    #                     );''')
    #     db.commit()
    #     # Create table for Real users
    #     db.execute('''CREATE TABLE IF NOT EXISTS REAL_USER (
    #                     ID INTEGER PRIMARY KEY NOT NULL,
    #                     NAME TEXT NOT NULL,
    #                     PHONE TEXT,
    #                     EXTRA_NUMBER TEXT,
    #                     ID_NUMBER TEXT,
    #                     EMAIL TEXT
    #                     );''')
    #     db.commit()
    #     db.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     app.exec_()
# pyinstaller --windowed