from PySide2.QtCore import QThread


class Login(QThread):

    def run(self):
        print(self.username, self.password)
