# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1107, 650)
        MainWindow.setStyleSheet(u"background-color: rgb(66, 133, 244);\n"
"QPushButton::pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setStyleSheet(u"\n"
"background-color: rgb(26, 115, 232);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"Almarai")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(251, 188, 4);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"\n"
"QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(114, 159, 207);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 100)
        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMaximumSize(QSize(16777215, 50))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QSize(16777215, 50))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #76797C;\n"
"    padding: 5px;\n"
"    margin: 0px;\n"
"\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"")
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_2 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_8 = QFrame(self.tabWidgetPage1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_4 = QLineEdit(self.frame_9)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Almarai")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_4.setClearButtonEnabled(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_4)

        self.pushButton_49 = QPushButton(self.frame_9)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy)
        self.pushButton_49.setMaximumSize(QSize(100, 16777215))
        font3 = QFont()
        font3.setFamily(u"Almarai")
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_49.setFont(font3)
        self.pushButton_49.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_49.setStyleSheet(u"background-color: rgb(52, 168, 83);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/Desktop/like pro/\u0641\u062a\u062d \u0645\u0648\u0642\u0639 \u0627\u0644\u0648\u0627\u062a\u0633\u0627\u0628.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_49.setIcon(icon)
        self.pushButton_49.setIconSize(QSize(283, 65))

        self.horizontalLayout_6.addWidget(self.pushButton_49)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 70))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_5 = QLineEdit(self.frame_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setFont(font2)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_5)

        self.label_18 = QLabel(self.frame_10)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setFont(font3)
        self.label_18.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.label_18)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_7 = QFrame(self.tab)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet(u"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(26, 115, 232);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(114, 159, 207);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(25, -1, 25, -1)
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(100, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 50))
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(100, 40))
        self.pushButton_4.setMaximumSize(QSize(16777215, 50))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(100, 40))
        self.pushButton_3.setMaximumSize(QSize(16777215, 50))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(100, 40))
        self.pushButton_8.setMaximumSize(QSize(16777215, 50))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(100, 40))
        self.pushButton_2.setMaximumSize(QSize(16777215, 50))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.pushButton_2)


        self.gridLayout_4.addWidget(self.frame_5, 1, 2, 1, 1)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 100))
        self.frame_11.setLayoutDirection(Qt.RightToLeft)
        self.frame_11.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox = QCheckBox(self.frame_12)
        self.checkBox.setObjectName(u"checkBox")
        font4 = QFont()
        font4.setPointSize(9)
        self.checkBox.setFont(font4)
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_12)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font4)
        self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_2.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.checkBox_2)


        self.verticalLayout.addWidget(self.frame_12)

        self.lineEdit_6 = QLineEdit(self.frame_11)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setFamily(u"Almarai")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.lineEdit_6.setFont(font5)
        self.lineEdit_6.setStyleSheet(u"")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_6.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_6.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_6)


        self.gridLayout_4.addWidget(self.frame_11, 0, 2, 1, 1)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QSize(0, 50))
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(40, -1, 40, -1)
        self.pushButton_10 = QPushButton(self.frame_13)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QSize(100, 40))
        self.pushButton_10.setMaximumSize(QSize(16777215, 50))
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.pushButton_10)


        self.gridLayout_2.addWidget(self.frame_13, 2, 1, 1, 1)

        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(219, 227, 255);")

        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 3, 1)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.frame_6)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(219, 227, 255);")

        self.gridLayout_2.addWidget(self.tableWidget_2, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 2, 1)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1107, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GOOGLE MAP", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u0631\u0626\u0633\u064a\u0629", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0648\u062c\u0644 \u0645\u0627\u0628", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"SOON", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0623\u062f\u062e\u0644 \u0633\u064a\u0631\u064a\u0627\u0644", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"\u0641\u062d\u0635", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_5.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.lineEdit_5.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.lineEdit_5.setPlaceholderText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0627\u0644\u0629 \u0627\u0644\u0627\u0634\u062a\u0631\u0627\u0643 :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0626\u0633\u064a\u0629", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0628\u062f\u0621", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0642\u0641 \u0645\u0624\u0642\u062a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0645\u0631\u0627\u0631", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062e\u0637\u0649", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0642\u0641", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062d\u0645\u064a\u0644 \u0627\u0644\u0635\u0648\u0631", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0648\u0642\u0639 \u0643\u0627\u0645\u0644", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b \u0639\u0646", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0627\u0628\u0637", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062a\u0641\u0627\u0635\u064a\u0644", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0648\u0627\u0628\u0637", None))
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u062c\u0648\u062c\u0644 \u0645\u0627\u0628", None))
    # retranslateUi

