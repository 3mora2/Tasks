import json
import sqlite3

from PySide2.QtCore import QRect, QSize
from PySide2.QtGui import Qt, QCursor, QClipboard
from PySide2.QtWidgets import *

from aqar_way import FULL_NAMES_RE, FULL_NAMES
from backend.add_from_file import AddFromFile
from backend.add_from_url import AddFromURL
from settings import DB_URL


class WindowOfferHandle:
    id_db_edit = None
    tableWidget: QTableWidget
    tabWidget_2: QTabWidget
    lineEdit_30: QLineEdit
    textEdit_2: QTextEdit
    textEdit: QTextEdit
    scrollArea: QScrollArea
    scrollAreaWidgetContents: QWidget

    def __init__(self):
        self.names = FULL_NAMES.copy()
        self.HandelButtonOffer()
        self.HandelDefaultOffer()
        self.HandelUiOffer()
        self.Show_All()
        self.AddFromURL = AddFromURL()
        self.AddFromURL.final.connect(self.add_from_url_update_page)

        self.AddFromFile = AddFromFile()
        self.AddFromFile.final.connect(self.add_succed)
        self.DialogDetails = QDialog()
        self.DialogAddURL = QDialog()

    def HandelButtonOffer(self):
        self.pushButton_2.clicked.connect(self.add_page_load)
        self.pushButton_3.clicked.connect(self.show_page_load)
        self.pushButton_10.clicked.connect(self.add_page)

        self.pushButton_6.clicked.connect(self.add_from_url_dialog)
        self.pushButton_7.clicked.connect(self.save_edit_page)
        self.pushButton_5.clicked.connect(self.add_from_file)

    def HandelDefaultOffer(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabWidget_2.tabBar().setVisible(False)
        self.tabWidget_2.setCurrentIndex(0)

    def HandelUiOffer(self):
        self.add_scroll()
        self.edit_scroll()

    def add_scroll(self):
        self.names.pop('refresh')
        self.names.pop('premium')
        self.names.pop('content')
        self.names.pop('has_img')
        self.names.pop('user_name')
        self.names.pop('user_id')
        self.names.pop('user_type')
        self.names.pop('views')

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 503, 1236))

        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.RightToLeft)
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")

        vboxLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        vboxLayout.setObjectName(u"vboxLayout")
        vboxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        for key in self.names.keys():
            frame_10 = QFrame(self.scrollAreaWidgetContents)
            frame_10.setObjectName(u"frame_" + str(key))
            sizePolicy.setHeightForWidth(frame_10.sizePolicy().hasHeightForWidth())
            frame_10.setSizePolicy(sizePolicy)
            frame_10.setMinimumSize(QSize(0, 30))
            frame_10.setMaximumSize(QSize(16777215, 16777215))
            frame_10.setFrameShape(QFrame.StyledPanel)
            frame_10.setFrameShadow(QFrame.Raised)

            gridLayout_6 = QGridLayout(frame_10)
            gridLayout_6.setObjectName(u"gridLayout_61" + str(key))
            gridLayout_6.setContentsMargins(0, 0, 0, 0)

            label = QLabel(frame_10)
            label.setObjectName(u"label" + str(key))
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setLayoutDirection(Qt.RightToLeft)
            label.setText(str(self.names.get(key).get('name').get('ar')))
            lineEdit_5 = QLineEdit(frame_10)
            lineEdit_5.setObjectName(u"lineEdit_" + str(key))
            sizePolicy.setHeightForWidth(lineEdit_5.sizePolicy().hasHeightForWidth())
            lineEdit_5.setSizePolicy(sizePolicy)
            lineEdit_5.setAlignment(Qt.AlignCenter)

            gridLayout_6.addWidget(label, 0, 0, 1, 1)
            gridLayout_6.addWidget(lineEdit_5, 0, 1, 1, 1)

            gridLayout_6.setColumnStretch(0, 1)
            gridLayout_6.setColumnStretch(1, 4)

            vboxLayout.addWidget(frame_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def edit_scroll(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 503, 1236))

        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setLayoutDirection(Qt.RightToLeft)
        self.scrollAreaWidgetContents_2.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")

        vboxLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        vboxLayout.setObjectName(u"vboxLayout")
        vboxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        for key in self.names.keys():
            frame_10 = QFrame(self.scrollAreaWidgetContents_2)
            frame_10.setObjectName(u"frame_" + str(key)+'edit')
            sizePolicy.setHeightForWidth(frame_10.sizePolicy().hasHeightForWidth())
            frame_10.setSizePolicy(sizePolicy)
            frame_10.setMinimumSize(QSize(0, 30))
            frame_10.setMaximumSize(QSize(16777215, 16777215))
            frame_10.setFrameShape(QFrame.StyledPanel)
            frame_10.setFrameShadow(QFrame.Raised)

            gridLayout_6 = QGridLayout(frame_10)
            gridLayout_6.setObjectName(u"gridLayout_61" + str(key)+'_edit')
            gridLayout_6.setContentsMargins(0, 0, 0, 0)

            label = QLabel(frame_10)
            label.setObjectName(u"label" + str(key)+'edit')
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setLayoutDirection(Qt.RightToLeft)
            label.setText(str(self.names.get(key).get('name').get('ar')))
            lineEdit_5 = QLineEdit(frame_10)
            lineEdit_5.setObjectName(u"lineEdit_" + str(key)+'edit')
            sizePolicy.setHeightForWidth(lineEdit_5.sizePolicy().hasHeightForWidth())
            lineEdit_5.setSizePolicy(sizePolicy)
            lineEdit_5.setAlignment(Qt.AlignCenter)

            gridLayout_6.addWidget(label, 0, 0, 1, 1)
            gridLayout_6.addWidget(lineEdit_5, 0, 1, 1, 1)

            gridLayout_6.setColumnStretch(0, 1)
            gridLayout_6.setColumnStretch(1, 4)

            vboxLayout.addWidget(frame_10)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

    def add_page_load(self):
        self.tabWidget_2.setCurrentIndex(0)

    def show_page_load(self):
        self.tabWidget_2.setCurrentIndex(1)
        self.Show_All()

    def Show_All(self):

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        db = sqlite3.connect(DB_URL)
        cur = db.cursor()
        cur.execute("SELECT * FROM REAL_OFFERS")
        rows = cur.fetchall()
        for row, data in enumerate(rows):
            id_ = data[0]
            user_id = data[3]
            user_name = data[1]
            user_phone = data[2]
            post_id = data[8]
            post_name = data[6]
            r = self.tableWidget.rowCount()
            self.tableWidget.insertRow(r)
            for c, item in enumerate([id_, user_id, user_name, user_phone, post_id, post_name]):
                if item is not None:
                    qt1 = QTableWidgetItem(str(item))
                    qt1.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(r, c, qt1)

            deleteButton = QPushButton("عرض")
            deleteButton.setCursor(QCursor(Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.show_offer_button)
            self.tableWidget.setCellWidget(r, 6, deleteButton)
            deleteButton = QPushButton("تعديل")
            deleteButton.setCursor(QCursor(Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.edit_offer_button)
            self.tableWidget.setCellWidget(r, 7, deleteButton)

            deleteButton = QPushButton("حذف")
            deleteButton.setCursor(QCursor(Qt.PointingHandCursor))
            deleteButton.clicked.connect(self.delete_offer_button)
            self.tableWidget.setCellWidget(r, 8, deleteButton)
        cur.close()
        db.close()

    def delete_offer_button(self):
        button = self.sender()
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()
            id_db = self.tableWidget.item(row, 0).text()
            db = sqlite3.connect(DB_URL)
            dbc = db.cursor()
            dbc.execute("DELETE from REAL_OFFERS where ID =?", (id_db,))
            db.commit()
            dbc.close()
            db.close()
            self.Show_All()
            print('delete')

    def edit_offer_button(self):
        button = self.sender()
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()
            id_db = self.tableWidget.item(row, 0).text()
            self.edit_page(id_db)

    def show_offer_button(self):
        button = self.sender()
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()
            id_db = self.tableWidget.item(row, 0).text()
            db = sqlite3.connect(DB_URL)
            cur = db.cursor()
            cur.execute("SELECT * FROM REAL_OFFERS WHERE ID=?", (id_db,))
            row = cur.fetchone()
            if row:
                data = json.loads(row[9])
                text = ''
                for key in data.keys():
                    value = data.get(key)
                    if key in FULL_NAMES:
                        key = FULL_NAMES.get(key, {}).get('name', {}).get('ar')

                    if value and value != '':
                        text += f'{key}: {value}\n'
                self.show_dialog(text)

    def show_dialog(self, text):
        if not self.DialogDetails.objectName():
            self.DialogDetails.setObjectName(u"Dialog")
            self.DialogDetails.resize(651, 505)

            self.DialogDetails.setLayout(QVBoxLayout())
            self.DialogDetails.layout().addWidget(QLabel('تفاصيل العرض'))
            self.textEdit_DialogDetails = QTextEdit()
            self.textEdit_DialogDetails.setAlignment(Qt.AlignRight)
            self.DialogDetails.layout().addWidget(self.textEdit_DialogDetails)

            buttonLayout = QHBoxLayout()
            buttonLayout.addStretch()
            self.cancelButton_DialogDetails = QPushButton('اغلاق')
            buttonLayout.addWidget(self.cancelButton_DialogDetails)
            self.copyButton_DialogDetails = QPushButton('نسخ')
            self.copyButton_DialogDetails.focusPolicy()
            buttonLayout.addWidget(self.copyButton_DialogDetails)
            self.DialogDetails.layout().addLayout(buttonLayout)
            self.copyButton_DialogDetails.clicked.connect(self.copy_textEdit_DialogDetails)
            self.cancelButton_DialogDetails.clicked.connect(self.DialogDetails.reject)

        self.textEdit_DialogDetails.setPlainText(text)
        self.DialogDetails.exec_()

    def copy_textEdit_DialogDetails(self):
        text = self.textEdit_DialogDetails.toPlainText()
        cb = QClipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(text, mode=cb.Clipboard)

    def edit_page(self, id_db):
        self.id_db_edit = id_db
        db = sqlite3.connect(DB_URL)
        cur = db.cursor()
        cur.execute("SELECT * FROM REAL_OFFERS WHERE ID=?", (id_db,))
        row = cur.fetchone()
        if row:
            user_name = row[1]
            phone = row[2]
            user_info_id = row[3]
            email = row[4]
            extra_phone = row[5]
            offer_name = row[6]
            offer_id = row[8]

            documents = row[7]
            data = json.loads(row[9])
            content = data.pop('content')
            data['id'] = offer_id
            data['title'] = offer_name
            self.lineEdit_30.setText(user_name)
            self.lineEdit_41.setText(user_info_id)
            self.lineEdit_31.setText(phone)
            self.lineEdit_32.setText(extra_phone)
            self.lineEdit_33.setText(email)
            self.textEdit_2.setText(content)
            self.lineEdit_10.setText(documents)
            for frame in self.scrollAreaWidgetContents_2.children():
                if type(frame) == QFrame:
                    label = list(filter(lambda x: type(x) == QLabel, frame.children()))[0].text()
                    if label in FULL_NAMES_RE:
                        label = FULL_NAMES_RE.get(label)
                    if label in data.keys():
                        list(filter(lambda x: type(x) == QLineEdit, frame.children()))[0].setText(data[label.strip()])

        self.tabWidget_2.setCurrentIndex(2)

    def save_edit_page(self):
        if self.id_db_edit:
            data = dict()
            user_name = self.lineEdit_30.text()
            user_info_id = self.lineEdit_41.text()
            phone = self.lineEdit_31.text()
            extra_phone = self.lineEdit_32.text()
            email = self.lineEdit_33.text()
            content = self.textEdit_2.toPlainText()
            documents = self.lineEdit_10.text()
            for frame in self.scrollAreaWidgetContents_2.children():
                if type(frame) == QFrame:
                    label = list(filter(lambda x: type(x) == QLabel, frame.children()))[0].text()
                    line_edit = list(filter(lambda x: type(x) == QLineEdit, frame.children()))[0].text()
                    if label in FULL_NAMES_RE:
                        label = FULL_NAMES_RE.get(label)
                    data[label] = line_edit

            data['content'] = content
            title = data.pop('title')
            id_ = data.pop('id')
            sql = ''' Update REAL_OFFERS set NAME = ?, PHONE = ?, EXTRA_NUMBER = ?, ID_NUMBER = ?, EMAIL = ? , OFFER_NAME = ?, DOCUMENTS = ?, OFFER_ID = ?, DATA = ?  where ID = ?'''
            data = json.dumps(data)
            db = sqlite3.connect(DB_URL)
            cur = db.cursor()
            cur.execute(sql, (
                user_name, phone, extra_phone, user_info_id, email, title, documents, id_, data, self.id_db_edit))
            db.commit()
            cur.close()
            db.close()
            print('- Update')
            self.clean_edit_page()
            self.show_page_load()

    def clean_edit_page(self):
        self.lineEdit_30.setText('')
        self.lineEdit_41.setText('')
        self.lineEdit_31.setText('')
        self.lineEdit_32.setText('')
        self.lineEdit_33.setText('')
        self.textEdit_2.setText('')
        self.lineEdit_10.setText('')
        for frame in self.scrollAreaWidgetContents_2.children():
            if type(frame) == QFrame:
                list(filter(lambda x: type(x) == QLineEdit, frame.children()))[0].setText('')

    def add_page(self):
        data = dict()
        frame: QFrame
        user_name = self.lineEdit.text()
        phone = self.lineEdit_2.text()
        user_info_id = self.lineEdit_40.text()
        extra_phone = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        content = self.textEdit.toPlainText()
        documents = self.lineEdit_36.text()
        for frame in self.scrollAreaWidgetContents.children():
            if type(frame) == QFrame:
                label = list(filter(lambda x: type(x) == QLabel, frame.children()))[0].text()
                line_edit = list(filter(lambda x: type(x) == QLineEdit, frame.children()))[0].text()
                if label in FULL_NAMES_RE:
                    label = FULL_NAMES_RE.get(label)
                data[label.strip()] = line_edit

        data['content'] = content
        title = data.pop('title')
        id_ = data.pop('id')

        sql_data = '''INSERT INTO REAL_OFFERS(NAME, PHONE, EXTRA_NUMBER, ID_NUMBER, EMAIL , OFFER_NAME, DOCUMENTS, OFFER_ID, DATA)
        SELECT ?, ?, ?, ?, ?, ?, ?, ?, ?
        WHERE NOT EXISTS(SELECT 1 FROM REAL_OFFERS WHERE NAME = ? AND DATA = ?)'''
        sql_user = '''INSERT INTO REAL_USER(NAME, ID_NUMBER, PHONE, EXTRA_NUMBER, EMAIL) 
                    SELECT ?, ?, ?, ?, ?
                    WHERE NOT EXISTS(SELECT 1 FROM REAL_USER WHERE NAME = ? AND ID_NUMBER = ?)'''
        data = json.dumps(data)
        db = sqlite3.connect(DB_URL)
        cur = db.cursor()
        # Add offer to db
        cur.execute(sql_data, (
        user_name, phone, extra_phone, user_info_id, email, title, documents, id_, data, user_name, data))
        db.commit()
        # Add User to db
        cur.execute(sql_user, (user_name, user_info_id, phone, extra_phone, email, user_name, user_info_id))
        db.commit()

        cur.close()
        db.close()
        print('- add')
        self.clean_add_page()

    def clean_add_page(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_40.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.textEdit.setText('')
        self.lineEdit_36.setText('')
        for frame in self.scrollAreaWidgetContents.children():
            if type(frame) == QFrame:
                list(filter(lambda x: type(x) == QLineEdit, frame.children()))[0].setText('')

    def add_from_url_dialog(self):
        if not self.DialogAddURL.objectName():
            self.DialogAddURL.setObjectName(u"Dialog")
            self.DialogAddURL.resize(400, 100)
            self.DialogAddURL.setLayout(QVBoxLayout())
            self.DialogAddURL.layout().addWidget(QLabel('ادخل الرابط'))
            self.LineEdit_DialogAddURL = QLineEdit()
            self.DialogAddURL.layout().addWidget(self.LineEdit_DialogAddURL)

            buttonLayout = QHBoxLayout()
            buttonLayout.addStretch()
            self.cancelButton_DialogAddURL = QPushButton('اغلاق')
            self.copyButton_DialogAddURL = QPushButton('اضافة')
            buttonLayout.addWidget(self.cancelButton_DialogAddURL)
            buttonLayout.addWidget(self.copyButton_DialogAddURL)
            self.DialogAddURL.layout().addLayout(buttonLayout)
            self.copyButton_DialogAddURL.clicked.connect(self.DialogAddURL.accept)
            self.cancelButton_DialogAddURL.clicked.connect(self.DialogAddURL.reject)

        result = self.DialogAddURL.exec_()
        text = self.LineEdit_DialogAddURL.text()
        if result == 1 and text and 'sa.aqar.fm/' in text:
            self.AddFromURL.url = text
            self.AddFromURL.start()

    def add_from_url_update_page(self, data):
        user = data.get('user_name')
        user_id = data.get('user_id')
        data_info = data.get('data_info')

        content = data_info.pop('content')
        self.lineEdit.setText(user)
        self.lineEdit_40.setText(str(user_id))
        self.textEdit.setText(content)
        for frame in self.scrollAreaWidgetContents.children():
            if type(frame) == QFrame:
                label = list(filter(lambda x: type(x) == QLabel, frame.children()))[0].text()
                if label in FULL_NAMES_RE:
                    label = FULL_NAMES_RE.get(label)
                if label in data_info.keys() and data_info[label] is not None:

                    list(filter(lambda x: type(x) == QLineEdit, frame.children()))[0].setText(str(data_info[label]))

        self.message_succed()

    def add_from_file(self):
        file = QFileDialog.getOpenFileName(self, "اختار", '', '*.xlsx')[0]
        if file != '':
            self.AddFromFile.file = file
            self.AddFromFile.start()

    def add_succed(self):
        self.message_succed()
        self.show_page_load()

    def message_succed(self):
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Information)
        Box.setWindowTitle("تنبيه")
        Box.setText("تم الانتهاء")
        Box.setStandardButtons(QMessageBox.Ok)
        Box.exec()

