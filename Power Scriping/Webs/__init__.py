import os
from PySide2.QtWidgets import QMainWindow, QApplication
from loader_ui import loadUi

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class WebMainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi(os.path.join(SCRIPT_DIRECTORY, 'Web_ui.ui'), self)




