# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        MainWindow.resize(1124, 713)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.tabWidget.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(77, 137, 197);\n"
"color: rgb(244, 243, 242);\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(114, 159, 207);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius: 12px;\n"
"border : 1px solid rgb(29, 29, 27);\n"
"background-color: rgb(255, 255, 255, 0);\n"
"}\n"
"QTextEdit{\n"
"border-radius: 12px;\n"
"border : 1px solid rgb(29, 29, 27);\n"
"background-color: rgb(255, 255, 255, 0);\n"
"}\n"
"QScrollArea{\n"
"border-radius: 4px;\n"
"border : 1px solid rgb(29, 29, 27);\n"
"background-color: rgb(255, 255, 255, 0);\n"
"}")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_27 = QGridLayout(self.tab_14)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.frame_21 = QFrame(self.tab_14)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_21)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_22)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.pushButton_17 = QPushButton(self.frame_22)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy2)
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_24.addWidget(self.pushButton_17, 0, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_22)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy2.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy2)
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_24.addWidget(self.pushButton_18, 0, 2, 1, 1)


        self.gridLayout_23.addWidget(self.frame_22, 1, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.frame_21)
        if (self.tableWidget_2.columnCount() < 1):
            self.tableWidget_2.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)

        self.gridLayout_23.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.gridLayout_23.setRowStretch(0, 8)
        self.gridLayout_23.setRowStretch(1, 1)

        self.gridLayout_27.addWidget(self.frame_21, 0, 1, 2, 1)

        self.frame_17 = QFrame(self.tab_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_17)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.frame_23 = QFrame(self.frame_17)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy1.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy1)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_23)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.frame_18 = QFrame(self.frame_23)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setLayoutDirection(Qt.LeftToRight)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_18)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_11 = QLineEdit(self.frame_18)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.lineEdit_11, 0, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.frame_18)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.lineEdit_12, 1, 0, 1, 1)

        self.label_36 = QLabel(self.frame_18)
        self.label_36.setObjectName(u"label_36")
        sizePolicy1.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_36, 0, 1, 1, 1)

        self.label_37 = QLabel(self.frame_18)
        self.label_37.setObjectName(u"label_37")
        sizePolicy1.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_37, 1, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.frame_18)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy2.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy2)
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_19.addWidget(self.pushButton_19, 2, 0, 1, 2)


        self.gridLayout_25.addWidget(self.frame_18, 0, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_23)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_19)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, -1, 0, -1)
        self.pushButton_20 = QPushButton(self.frame_19)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy2.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy2)
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_20.addWidget(self.pushButton_20, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.frame_19, 1, 0, 1, 1)

        self.gridLayout_25.setRowStretch(0, 4)
        self.gridLayout_25.setRowStretch(1, 2)

        self.gridLayout_28.addWidget(self.frame_23, 0, 0, 1, 1)

        self.frame_24 = QFrame(self.frame_17)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy1.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy1)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_24)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_35 = QLabel(self.frame_24)
        self.label_35.setObjectName(u"label_35")
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)

        self.gridLayout_26.addWidget(self.label_35, 1, 1, 1, 1)

        self.label_34 = QLabel(self.frame_24)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)

        self.gridLayout_26.addWidget(self.label_34, 0, 1, 1, 1)

        self.spinBox_4 = QSpinBox(self.frame_24)
        self.spinBox_4.setObjectName(u"spinBox_4")
        sizePolicy.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(999999999)
        self.spinBox_4.setValue(1)

        self.gridLayout_26.addWidget(self.spinBox_4, 1, 3, 1, 1)

        self.spinBox_3 = QSpinBox(self.frame_24)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy2.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy2)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(999999999)

        self.gridLayout_26.addWidget(self.spinBox_3, 0, 3, 1, 1)

        self.label_16 = QLabel(self.frame_24)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_26.addWidget(self.label_16, 0, 4, 1, 1)

        self.spinBox_5 = QSpinBox(self.frame_24)
        self.spinBox_5.setObjectName(u"spinBox_5")
        sizePolicy.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy)
        self.spinBox_5.setMinimum(0)
        self.spinBox_5.setMaximum(999999999)

        self.gridLayout_26.addWidget(self.spinBox_5, 0, 5, 1, 1)


        self.gridLayout_28.addWidget(self.frame_24, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.frame_17)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_25)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.pushButton_14 = QPushButton(self.frame_25)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy2.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy2)
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_21.addWidget(self.pushButton_14, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_25)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy2.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy2)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_21.addWidget(self.pushButton_13, 3, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_25)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy2.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy2)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_21.addWidget(self.pushButton_12, 2, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_25)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy2.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy2)
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_21.addWidget(self.pushButton_15, 4, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_25)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_21.addWidget(self.pushButton_16, 1, 0, 1, 1)


        self.gridLayout_28.addWidget(self.frame_25, 2, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_20)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.lineEdit_13 = QLineEdit(self.frame_20)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.lineEdit_13, 0, 1, 1, 1)

        self.pushButton_25 = QPushButton(self.frame_20)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy2.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy2)
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_22.addWidget(self.pushButton_25, 3, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.frame_20)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy)
        self.lineEdit_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.lineEdit_15, 2, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.frame_20)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy)
        self.lineEdit_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.lineEdit_14, 1, 1, 1, 1)

        self.label_38 = QLabel(self.frame_20)
        self.label_38.setObjectName(u"label_38")
        sizePolicy1.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy1)

        self.gridLayout_22.addWidget(self.label_38, 0, 0, 1, 1)

        self.label_39 = QLabel(self.frame_20)
        self.label_39.setObjectName(u"label_39")
        sizePolicy1.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy1)

        self.gridLayout_22.addWidget(self.label_39, 1, 0, 1, 1)

        self.label_40 = QLabel(self.frame_20)
        self.label_40.setObjectName(u"label_40")
        sizePolicy1.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy1)

        self.gridLayout_22.addWidget(self.label_40, 2, 0, 1, 1)

        self.checkBox = QCheckBox(self.frame_20)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_22.addWidget(self.checkBox, 3, 0, 1, 1)


        self.gridLayout_28.addWidget(self.frame_20, 3, 0, 1, 1)

        self.gridLayout_28.setRowStretch(0, 4)
        self.gridLayout_28.setRowStretch(1, 1)
        self.gridLayout_28.setRowStretch(2, 4)
        self.gridLayout_28.setRowStretch(3, 4)

        self.gridLayout_27.addWidget(self.frame_17, 0, 0, 1, 1)

        self.gridLayout_27.setColumnStretch(0, 1)
        self.gridLayout_27.setColumnStretch(1, 2)
        self.tabWidget.addTab(self.tab_14, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setLayoutDirection(Qt.RightToLeft)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_148 = QGridLayout(self.frame_3)
        self.gridLayout_148.setObjectName(u"gridLayout_148")
        self.gridLayout_148.setContentsMargins(50, -1, 50, 0)
        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)

        self.gridLayout_148.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.gridLayout_148.addWidget(self.pushButton_5, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.tab_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.lineEdit_4, 4, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.lineEdit_3, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.lineEdit_2, 2, 0, 1, 1)

        self.lineEdit_40 = QLineEdit(self.frame_7)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        sizePolicy.setHeightForWidth(self.lineEdit_40.sizePolicy().hasHeightForWidth())
        self.lineEdit_40.setSizePolicy(sizePolicy)
        self.lineEdit_40.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.lineEdit_40, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_58 = QGridLayout(self.frame_5)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout_58.addWidget(self.label_5, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.frame_5)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setLayoutDirection(Qt.RightToLeft)
        self.textEdit.setOverwriteMode(False)

        self.gridLayout_58.addWidget(self.textEdit, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_8, 0, 0, 1, 1)

        self.lineEdit_36 = QLineEdit(self.frame_6)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        sizePolicy.setHeightForWidth(self.lineEdit_36.sizePolicy().hasHeightForWidth())
        self.lineEdit_36.setSizePolicy(sizePolicy)
        self.lineEdit_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_36, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_6, 2, 0, 1, 1)

        self.gridLayout_7.setRowStretch(0, 3)
        self.gridLayout_7.setRowStretch(1, 3)
        self.gridLayout_7.setRowStretch(2, 1)

        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.RightToLeft)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-126, 0, 135, 1236))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.RightToLeft)
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")
        self.vboxLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QSize(0, 30))
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_10)

        self.frame_98 = QFrame(self.scrollAreaWidgetContents)
        self.frame_98.setObjectName(u"frame_98")
        sizePolicy.setHeightForWidth(self.frame_98.sizePolicy().hasHeightForWidth())
        self.frame_98.setSizePolicy(sizePolicy)
        self.frame_98.setMinimumSize(QSize(0, 30))
        self.frame_98.setMaximumSize(QSize(16777215, 16777215))
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.gridLayout_57 = QGridLayout(self.frame_98)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_39 = QLineEdit(self.frame_98)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        sizePolicy.setHeightForWidth(self.lineEdit_39.sizePolicy().hasHeightForWidth())
        self.lineEdit_39.setSizePolicy(sizePolicy)
        self.lineEdit_39.setAlignment(Qt.AlignCenter)

        self.gridLayout_57.addWidget(self.lineEdit_39, 0, 1, 1, 1)

        self.label_32 = QLabel(self.frame_98)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_57.addWidget(self.label_32, 0, 0, 1, 1)

        self.gridLayout_57.setColumnStretch(0, 1)
        self.gridLayout_57.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_98)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(0, 30))
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_7 = QLineEdit(self.frame_11)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lineEdit_7, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_12)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_12.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_12)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.lineEdit_9, 0, 1, 1, 1)

        self.gridLayout_12.setColumnStretch(0, 1)
        self.gridLayout_12.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QSize(0, 30))
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_16 = QLineEdit(self.frame_13)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        sizePolicy.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy)
        self.lineEdit_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.lineEdit_16, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_13.addWidget(self.label_4, 0, 0, 1, 1)

        self.gridLayout_13.setColumnStretch(0, 1)
        self.gridLayout_13.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_13)

        self.frame_26 = QFrame(self.scrollAreaWidgetContents)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QSize(0, 30))
        self.frame_26.setMaximumSize(QSize(16777215, 16777215))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_26)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_18 = QLineEdit(self.frame_26)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        sizePolicy.setHeightForWidth(self.lineEdit_18.sizePolicy().hasHeightForWidth())
        self.lineEdit_18.setSizePolicy(sizePolicy)
        self.lineEdit_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.lineEdit_18, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_26)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.gridLayout_14.addWidget(self.label_6, 0, 0, 1, 1)

        self.gridLayout_14.setColumnStretch(0, 1)
        self.gridLayout_14.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.scrollAreaWidgetContents)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setMinimumSize(QSize(0, 30))
        self.frame_27.setMaximumSize(QSize(16777215, 16777215))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_27)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_27)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.gridLayout_15.addWidget(self.label_9, 0, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.frame_27)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        sizePolicy.setHeightForWidth(self.lineEdit_20.sizePolicy().hasHeightForWidth())
        self.lineEdit_20.setSizePolicy(sizePolicy)
        self.lineEdit_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.lineEdit_20, 0, 1, 1, 1)

        self.gridLayout_15.setColumnStretch(0, 1)
        self.gridLayout_15.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.scrollAreaWidgetContents)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMinimumSize(QSize(0, 30))
        self.frame_28.setMaximumSize(QSize(16777215, 16777215))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_28)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_24 = QLineEdit(self.frame_28)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        sizePolicy.setHeightForWidth(self.lineEdit_24.sizePolicy().hasHeightForWidth())
        self.lineEdit_24.setSizePolicy(sizePolicy)
        self.lineEdit_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.lineEdit_24, 0, 1, 1, 1)

        self.label_10 = QLabel(self.frame_28)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_29.addWidget(self.label_10, 0, 0, 1, 1)

        self.gridLayout_29.setColumnStretch(0, 1)
        self.gridLayout_29.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.scrollAreaWidgetContents)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setMinimumSize(QSize(0, 30))
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_29)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_26 = QLineEdit(self.frame_29)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        sizePolicy.setHeightForWidth(self.lineEdit_26.sizePolicy().hasHeightForWidth())
        self.lineEdit_26.setSizePolicy(sizePolicy)
        self.lineEdit_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.lineEdit_26, 0, 1, 1, 1)

        self.label_11 = QLabel(self.frame_29)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.gridLayout_30.addWidget(self.label_11, 0, 0, 1, 1)

        self.gridLayout_30.setColumnStretch(0, 1)
        self.gridLayout_30.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.scrollAreaWidgetContents)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMinimumSize(QSize(0, 30))
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_30)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_28 = QLineEdit(self.frame_30)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        sizePolicy.setHeightForWidth(self.lineEdit_28.sizePolicy().hasHeightForWidth())
        self.lineEdit_28.setSizePolicy(sizePolicy)
        self.lineEdit_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.lineEdit_28, 0, 1, 1, 1)

        self.label_12 = QLabel(self.frame_30)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)

        self.gridLayout_31.addWidget(self.label_12, 0, 0, 1, 1)

        self.gridLayout_31.setColumnStretch(0, 1)
        self.gridLayout_31.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_30)

        self.frame_34 = QFrame(self.scrollAreaWidgetContents)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QSize(0, 30))
        self.frame_34.setMaximumSize(QSize(16777215, 16777215))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_116 = QGridLayout(self.frame_34)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.gridLayout_116.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_200 = QLineEdit(self.frame_34)
        self.lineEdit_200.setObjectName(u"lineEdit_200")
        sizePolicy.setHeightForWidth(self.lineEdit_200.sizePolicy().hasHeightForWidth())
        self.lineEdit_200.setSizePolicy(sizePolicy)
        self.lineEdit_200.setAlignment(Qt.AlignCenter)

        self.gridLayout_116.addWidget(self.lineEdit_200, 0, 1, 1, 1)

        self.label_109 = QLabel(self.frame_34)
        self.label_109.setObjectName(u"label_109")
        sizePolicy.setHeightForWidth(self.label_109.sizePolicy().hasHeightForWidth())
        self.label_109.setSizePolicy(sizePolicy)

        self.gridLayout_116.addWidget(self.label_109, 0, 0, 1, 1)

        self.gridLayout_116.setColumnStretch(0, 1)
        self.gridLayout_116.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_34)

        self.frame_44 = QFrame(self.scrollAreaWidgetContents)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy)
        self.frame_44.setMinimumSize(QSize(0, 30))
        self.frame_44.setMaximumSize(QSize(16777215, 16777215))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_125 = QGridLayout(self.frame_44)
        self.gridLayout_125.setObjectName(u"gridLayout_125")
        self.gridLayout_125.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_218 = QLineEdit(self.frame_44)
        self.lineEdit_218.setObjectName(u"lineEdit_218")
        sizePolicy.setHeightForWidth(self.lineEdit_218.sizePolicy().hasHeightForWidth())
        self.lineEdit_218.setSizePolicy(sizePolicy)
        self.lineEdit_218.setAlignment(Qt.AlignCenter)

        self.gridLayout_125.addWidget(self.lineEdit_218, 0, 1, 1, 1)

        self.label_118 = QLabel(self.frame_44)
        self.label_118.setObjectName(u"label_118")
        sizePolicy.setHeightForWidth(self.label_118.sizePolicy().hasHeightForWidth())
        self.label_118.setSizePolicy(sizePolicy)

        self.gridLayout_125.addWidget(self.label_118, 0, 0, 1, 1)

        self.gridLayout_125.setColumnStretch(0, 1)
        self.gridLayout_125.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_44)

        self.frame_37 = QFrame(self.scrollAreaWidgetContents)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy)
        self.frame_37.setMinimumSize(QSize(0, 30))
        self.frame_37.setMaximumSize(QSize(16777215, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_118 = QGridLayout(self.frame_37)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.gridLayout_118.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_204 = QLineEdit(self.frame_37)
        self.lineEdit_204.setObjectName(u"lineEdit_204")
        sizePolicy.setHeightForWidth(self.lineEdit_204.sizePolicy().hasHeightForWidth())
        self.lineEdit_204.setSizePolicy(sizePolicy)
        self.lineEdit_204.setAlignment(Qt.AlignCenter)

        self.gridLayout_118.addWidget(self.lineEdit_204, 0, 1, 1, 1)

        self.label_111 = QLabel(self.frame_37)
        self.label_111.setObjectName(u"label_111")
        sizePolicy.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy)

        self.gridLayout_118.addWidget(self.label_111, 0, 0, 1, 1)

        self.gridLayout_118.setColumnStretch(0, 1)
        self.gridLayout_118.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_37)

        self.frame_33 = QFrame(self.scrollAreaWidgetContents)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setMinimumSize(QSize(0, 30))
        self.frame_33.setMaximumSize(QSize(16777215, 16777215))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_115 = QGridLayout(self.frame_33)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.gridLayout_115.setContentsMargins(0, 0, 0, 0)
        self.label_108 = QLabel(self.frame_33)
        self.label_108.setObjectName(u"label_108")
        sizePolicy.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy)

        self.gridLayout_115.addWidget(self.label_108, 0, 0, 1, 1)

        self.lineEdit_198 = QLineEdit(self.frame_33)
        self.lineEdit_198.setObjectName(u"lineEdit_198")
        sizePolicy.setHeightForWidth(self.lineEdit_198.sizePolicy().hasHeightForWidth())
        self.lineEdit_198.setSizePolicy(sizePolicy)
        self.lineEdit_198.setAlignment(Qt.AlignCenter)

        self.gridLayout_115.addWidget(self.lineEdit_198, 0, 1, 1, 1)

        self.gridLayout_115.setColumnStretch(0, 1)
        self.gridLayout_115.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_33)

        self.frame_47 = QFrame(self.scrollAreaWidgetContents)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy)
        self.frame_47.setMinimumSize(QSize(0, 30))
        self.frame_47.setMaximumSize(QSize(16777215, 16777215))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.gridLayout_128 = QGridLayout(self.frame_47)
        self.gridLayout_128.setObjectName(u"gridLayout_128")
        self.gridLayout_128.setContentsMargins(0, 0, 0, 0)
        self.label_121 = QLabel(self.frame_47)
        self.label_121.setObjectName(u"label_121")
        sizePolicy.setHeightForWidth(self.label_121.sizePolicy().hasHeightForWidth())
        self.label_121.setSizePolicy(sizePolicy)

        self.gridLayout_128.addWidget(self.label_121, 0, 0, 1, 1)

        self.lineEdit_224 = QLineEdit(self.frame_47)
        self.lineEdit_224.setObjectName(u"lineEdit_224")
        sizePolicy.setHeightForWidth(self.lineEdit_224.sizePolicy().hasHeightForWidth())
        self.lineEdit_224.setSizePolicy(sizePolicy)
        self.lineEdit_224.setAlignment(Qt.AlignCenter)

        self.gridLayout_128.addWidget(self.lineEdit_224, 0, 1, 1, 1)

        self.gridLayout_128.setColumnStretch(0, 1)
        self.gridLayout_128.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.scrollAreaWidgetContents)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy)
        self.frame_48.setMinimumSize(QSize(0, 30))
        self.frame_48.setMaximumSize(QSize(16777215, 16777215))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_129 = QGridLayout(self.frame_48)
        self.gridLayout_129.setObjectName(u"gridLayout_129")
        self.gridLayout_129.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_226 = QLineEdit(self.frame_48)
        self.lineEdit_226.setObjectName(u"lineEdit_226")
        sizePolicy.setHeightForWidth(self.lineEdit_226.sizePolicy().hasHeightForWidth())
        self.lineEdit_226.setSizePolicy(sizePolicy)
        self.lineEdit_226.setAlignment(Qt.AlignCenter)

        self.gridLayout_129.addWidget(self.lineEdit_226, 0, 1, 1, 1)

        self.label_122 = QLabel(self.frame_48)
        self.label_122.setObjectName(u"label_122")
        sizePolicy.setHeightForWidth(self.label_122.sizePolicy().hasHeightForWidth())
        self.label_122.setSizePolicy(sizePolicy)

        self.gridLayout_129.addWidget(self.label_122, 0, 0, 1, 1)

        self.gridLayout_129.setColumnStretch(0, 1)
        self.gridLayout_129.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_48)

        self.frame_40 = QFrame(self.scrollAreaWidgetContents)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy)
        self.frame_40.setMinimumSize(QSize(0, 30))
        self.frame_40.setMaximumSize(QSize(16777215, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_121 = QGridLayout(self.frame_40)
        self.gridLayout_121.setObjectName(u"gridLayout_121")
        self.gridLayout_121.setContentsMargins(0, 0, 0, 0)
        self.label_114 = QLabel(self.frame_40)
        self.label_114.setObjectName(u"label_114")
        sizePolicy.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy)

        self.gridLayout_121.addWidget(self.label_114, 0, 0, 1, 1)

        self.lineEdit_210 = QLineEdit(self.frame_40)
        self.lineEdit_210.setObjectName(u"lineEdit_210")
        sizePolicy.setHeightForWidth(self.lineEdit_210.sizePolicy().hasHeightForWidth())
        self.lineEdit_210.setSizePolicy(sizePolicy)
        self.lineEdit_210.setAlignment(Qt.AlignCenter)

        self.gridLayout_121.addWidget(self.lineEdit_210, 0, 1, 1, 1)

        self.gridLayout_121.setColumnStretch(0, 1)
        self.gridLayout_121.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_40)

        self.frame_42 = QFrame(self.scrollAreaWidgetContents)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy)
        self.frame_42.setMinimumSize(QSize(0, 30))
        self.frame_42.setMaximumSize(QSize(16777215, 16777215))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_123 = QGridLayout(self.frame_42)
        self.gridLayout_123.setObjectName(u"gridLayout_123")
        self.gridLayout_123.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_214 = QLineEdit(self.frame_42)
        self.lineEdit_214.setObjectName(u"lineEdit_214")
        sizePolicy.setHeightForWidth(self.lineEdit_214.sizePolicy().hasHeightForWidth())
        self.lineEdit_214.setSizePolicy(sizePolicy)
        self.lineEdit_214.setAlignment(Qt.AlignCenter)

        self.gridLayout_123.addWidget(self.lineEdit_214, 0, 1, 1, 1)

        self.label_116 = QLabel(self.frame_42)
        self.label_116.setObjectName(u"label_116")
        sizePolicy.setHeightForWidth(self.label_116.sizePolicy().hasHeightForWidth())
        self.label_116.setSizePolicy(sizePolicy)

        self.gridLayout_123.addWidget(self.label_116, 0, 0, 1, 1)

        self.gridLayout_123.setColumnStretch(0, 1)
        self.gridLayout_123.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_42)

        self.frame_45 = QFrame(self.scrollAreaWidgetContents)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy)
        self.frame_45.setMinimumSize(QSize(0, 30))
        self.frame_45.setMaximumSize(QSize(16777215, 16777215))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_126 = QGridLayout(self.frame_45)
        self.gridLayout_126.setObjectName(u"gridLayout_126")
        self.gridLayout_126.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_220 = QLineEdit(self.frame_45)
        self.lineEdit_220.setObjectName(u"lineEdit_220")
        sizePolicy.setHeightForWidth(self.lineEdit_220.sizePolicy().hasHeightForWidth())
        self.lineEdit_220.setSizePolicy(sizePolicy)
        self.lineEdit_220.setAlignment(Qt.AlignCenter)

        self.gridLayout_126.addWidget(self.lineEdit_220, 0, 1, 1, 1)

        self.label_119 = QLabel(self.frame_45)
        self.label_119.setObjectName(u"label_119")
        sizePolicy.setHeightForWidth(self.label_119.sizePolicy().hasHeightForWidth())
        self.label_119.setSizePolicy(sizePolicy)

        self.gridLayout_126.addWidget(self.label_119, 0, 0, 1, 1)

        self.gridLayout_126.setColumnStretch(0, 1)
        self.gridLayout_126.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_45)

        self.frame_32 = QFrame(self.scrollAreaWidgetContents)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setMinimumSize(QSize(0, 30))
        self.frame_32.setMaximumSize(QSize(16777215, 16777215))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_114 = QGridLayout(self.frame_32)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.gridLayout_114.setContentsMargins(0, 0, 0, 0)
        self.label_107 = QLabel(self.frame_32)
        self.label_107.setObjectName(u"label_107")
        sizePolicy.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy)

        self.gridLayout_114.addWidget(self.label_107, 0, 0, 1, 1)

        self.lineEdit_196 = QLineEdit(self.frame_32)
        self.lineEdit_196.setObjectName(u"lineEdit_196")
        sizePolicy.setHeightForWidth(self.lineEdit_196.sizePolicy().hasHeightForWidth())
        self.lineEdit_196.setSizePolicy(sizePolicy)
        self.lineEdit_196.setAlignment(Qt.AlignCenter)

        self.gridLayout_114.addWidget(self.lineEdit_196, 0, 1, 1, 1)

        self.gridLayout_114.setColumnStretch(0, 1)
        self.gridLayout_114.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_32)

        self.frame_46 = QFrame(self.scrollAreaWidgetContents)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy)
        self.frame_46.setMinimumSize(QSize(0, 30))
        self.frame_46.setMaximumSize(QSize(16777215, 16777215))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.gridLayout_127 = QGridLayout(self.frame_46)
        self.gridLayout_127.setObjectName(u"gridLayout_127")
        self.gridLayout_127.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_222 = QLineEdit(self.frame_46)
        self.lineEdit_222.setObjectName(u"lineEdit_222")
        sizePolicy.setHeightForWidth(self.lineEdit_222.sizePolicy().hasHeightForWidth())
        self.lineEdit_222.setSizePolicy(sizePolicy)
        self.lineEdit_222.setAlignment(Qt.AlignCenter)

        self.gridLayout_127.addWidget(self.lineEdit_222, 0, 1, 1, 1)

        self.label_120 = QLabel(self.frame_46)
        self.label_120.setObjectName(u"label_120")
        sizePolicy.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy)

        self.gridLayout_127.addWidget(self.label_120, 0, 0, 1, 1)

        self.gridLayout_127.setColumnStretch(0, 1)
        self.gridLayout_127.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_46)

        self.frame_35 = QFrame(self.scrollAreaWidgetContents)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMinimumSize(QSize(0, 30))
        self.frame_35.setMaximumSize(QSize(16777215, 16777215))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_117 = QGridLayout(self.frame_35)
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.gridLayout_117.setContentsMargins(0, 0, 0, 0)
        self.label_110 = QLabel(self.frame_35)
        self.label_110.setObjectName(u"label_110")
        sizePolicy.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy)

        self.gridLayout_117.addWidget(self.label_110, 0, 0, 1, 1)

        self.lineEdit_202 = QLineEdit(self.frame_35)
        self.lineEdit_202.setObjectName(u"lineEdit_202")
        sizePolicy.setHeightForWidth(self.lineEdit_202.sizePolicy().hasHeightForWidth())
        self.lineEdit_202.setSizePolicy(sizePolicy)
        self.lineEdit_202.setAlignment(Qt.AlignCenter)

        self.gridLayout_117.addWidget(self.lineEdit_202, 0, 1, 1, 1)

        self.gridLayout_117.setColumnStretch(0, 1)
        self.gridLayout_117.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_35)

        self.frame_43 = QFrame(self.scrollAreaWidgetContents)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setMinimumSize(QSize(0, 30))
        self.frame_43.setMaximumSize(QSize(16777215, 16777215))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_124 = QGridLayout(self.frame_43)
        self.gridLayout_124.setObjectName(u"gridLayout_124")
        self.gridLayout_124.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_216 = QLineEdit(self.frame_43)
        self.lineEdit_216.setObjectName(u"lineEdit_216")
        sizePolicy.setHeightForWidth(self.lineEdit_216.sizePolicy().hasHeightForWidth())
        self.lineEdit_216.setSizePolicy(sizePolicy)
        self.lineEdit_216.setAlignment(Qt.AlignCenter)

        self.gridLayout_124.addWidget(self.lineEdit_216, 0, 1, 1, 1)

        self.label_117 = QLabel(self.frame_43)
        self.label_117.setObjectName(u"label_117")
        sizePolicy.setHeightForWidth(self.label_117.sizePolicy().hasHeightForWidth())
        self.label_117.setSizePolicy(sizePolicy)

        self.gridLayout_124.addWidget(self.label_117, 0, 0, 1, 1)

        self.gridLayout_124.setColumnStretch(0, 1)
        self.gridLayout_124.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_43)

        self.frame_41 = QFrame(self.scrollAreaWidgetContents)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy)
        self.frame_41.setMinimumSize(QSize(0, 30))
        self.frame_41.setMaximumSize(QSize(16777215, 16777215))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_122 = QGridLayout(self.frame_41)
        self.gridLayout_122.setObjectName(u"gridLayout_122")
        self.gridLayout_122.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_212 = QLineEdit(self.frame_41)
        self.lineEdit_212.setObjectName(u"lineEdit_212")
        sizePolicy.setHeightForWidth(self.lineEdit_212.sizePolicy().hasHeightForWidth())
        self.lineEdit_212.setSizePolicy(sizePolicy)
        self.lineEdit_212.setAlignment(Qt.AlignCenter)

        self.gridLayout_122.addWidget(self.lineEdit_212, 0, 1, 1, 1)

        self.label_115 = QLabel(self.frame_41)
        self.label_115.setObjectName(u"label_115")
        sizePolicy.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy)

        self.gridLayout_122.addWidget(self.label_115, 0, 0, 1, 1)

        self.gridLayout_122.setColumnStretch(0, 1)
        self.gridLayout_122.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_41)

        self.frame_36 = QFrame(self.scrollAreaWidgetContents)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setMinimumSize(QSize(0, 30))
        self.frame_36.setMaximumSize(QSize(16777215, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_112 = QGridLayout(self.frame_36)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.gridLayout_112.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_192 = QLineEdit(self.frame_36)
        self.lineEdit_192.setObjectName(u"lineEdit_192")
        sizePolicy.setHeightForWidth(self.lineEdit_192.sizePolicy().hasHeightForWidth())
        self.lineEdit_192.setSizePolicy(sizePolicy)
        self.lineEdit_192.setAlignment(Qt.AlignCenter)

        self.gridLayout_112.addWidget(self.lineEdit_192, 0, 1, 1, 1)

        self.label_105 = QLabel(self.frame_36)
        self.label_105.setObjectName(u"label_105")
        sizePolicy.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy)

        self.gridLayout_112.addWidget(self.label_105, 0, 0, 1, 1)

        self.gridLayout_112.setColumnStretch(0, 1)
        self.gridLayout_112.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_36)

        self.frame_31 = QFrame(self.scrollAreaWidgetContents)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setMinimumSize(QSize(0, 30))
        self.frame_31.setMaximumSize(QSize(16777215, 16777215))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_113 = QGridLayout(self.frame_31)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.gridLayout_113.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_194 = QLineEdit(self.frame_31)
        self.lineEdit_194.setObjectName(u"lineEdit_194")
        sizePolicy.setHeightForWidth(self.lineEdit_194.sizePolicy().hasHeightForWidth())
        self.lineEdit_194.setSizePolicy(sizePolicy)
        self.lineEdit_194.setAlignment(Qt.AlignCenter)

        self.gridLayout_113.addWidget(self.lineEdit_194, 0, 1, 1, 1)

        self.label_106 = QLabel(self.frame_31)
        self.label_106.setObjectName(u"label_106")
        sizePolicy.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy)

        self.gridLayout_113.addWidget(self.label_106, 0, 0, 1, 1)

        self.gridLayout_113.setColumnStretch(0, 1)
        self.gridLayout_113.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_31)

        self.frame_39 = QFrame(self.scrollAreaWidgetContents)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy)
        self.frame_39.setMinimumSize(QSize(0, 30))
        self.frame_39.setMaximumSize(QSize(16777215, 16777215))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_119 = QGridLayout(self.frame_39)
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.gridLayout_119.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_206 = QLineEdit(self.frame_39)
        self.lineEdit_206.setObjectName(u"lineEdit_206")
        sizePolicy.setHeightForWidth(self.lineEdit_206.sizePolicy().hasHeightForWidth())
        self.lineEdit_206.setSizePolicy(sizePolicy)
        self.lineEdit_206.setAlignment(Qt.AlignCenter)

        self.gridLayout_119.addWidget(self.lineEdit_206, 0, 1, 1, 1)

        self.label_112 = QLabel(self.frame_39)
        self.label_112.setObjectName(u"label_112")
        sizePolicy.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy)

        self.gridLayout_119.addWidget(self.label_112, 0, 0, 1, 1)

        self.gridLayout_119.setColumnStretch(0, 1)
        self.gridLayout_119.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_39)

        self.frame_61 = QFrame(self.scrollAreaWidgetContents)
        self.frame_61.setObjectName(u"frame_61")
        sizePolicy.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy)
        self.frame_61.setMinimumSize(QSize(0, 30))
        self.frame_61.setMaximumSize(QSize(16777215, 16777215))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.gridLayout_160 = QGridLayout(self.frame_61)
        self.gridLayout_160.setObjectName(u"gridLayout_160")
        self.gridLayout_160.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_288 = QLineEdit(self.frame_61)
        self.lineEdit_288.setObjectName(u"lineEdit_288")
        sizePolicy.setHeightForWidth(self.lineEdit_288.sizePolicy().hasHeightForWidth())
        self.lineEdit_288.setSizePolicy(sizePolicy)
        self.lineEdit_288.setAlignment(Qt.AlignCenter)

        self.gridLayout_160.addWidget(self.lineEdit_288, 0, 1, 1, 1)

        self.label_153 = QLabel(self.frame_61)
        self.label_153.setObjectName(u"label_153")
        sizePolicy.setHeightForWidth(self.label_153.sizePolicy().hasHeightForWidth())
        self.label_153.setSizePolicy(sizePolicy)

        self.gridLayout_160.addWidget(self.label_153, 0, 0, 1, 1)

        self.gridLayout_160.setColumnStretch(0, 1)
        self.gridLayout_160.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_61)

        self.frame_53 = QFrame(self.scrollAreaWidgetContents)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy)
        self.frame_53.setMinimumSize(QSize(0, 30))
        self.frame_53.setMaximumSize(QSize(16777215, 16777215))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.gridLayout_152 = QGridLayout(self.frame_53)
        self.gridLayout_152.setObjectName(u"gridLayout_152")
        self.gridLayout_152.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_272 = QLineEdit(self.frame_53)
        self.lineEdit_272.setObjectName(u"lineEdit_272")
        sizePolicy.setHeightForWidth(self.lineEdit_272.sizePolicy().hasHeightForWidth())
        self.lineEdit_272.setSizePolicy(sizePolicy)
        self.lineEdit_272.setAlignment(Qt.AlignCenter)

        self.gridLayout_152.addWidget(self.lineEdit_272, 0, 1, 1, 1)

        self.label_145 = QLabel(self.frame_53)
        self.label_145.setObjectName(u"label_145")
        sizePolicy.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy)

        self.gridLayout_152.addWidget(self.label_145, 0, 0, 1, 1)

        self.gridLayout_152.setColumnStretch(0, 1)
        self.gridLayout_152.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_53)

        self.frame_63 = QFrame(self.scrollAreaWidgetContents)
        self.frame_63.setObjectName(u"frame_63")
        sizePolicy.setHeightForWidth(self.frame_63.sizePolicy().hasHeightForWidth())
        self.frame_63.setSizePolicy(sizePolicy)
        self.frame_63.setMinimumSize(QSize(0, 30))
        self.frame_63.setMaximumSize(QSize(16777215, 16777215))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.gridLayout_162 = QGridLayout(self.frame_63)
        self.gridLayout_162.setObjectName(u"gridLayout_162")
        self.gridLayout_162.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_292 = QLineEdit(self.frame_63)
        self.lineEdit_292.setObjectName(u"lineEdit_292")
        sizePolicy.setHeightForWidth(self.lineEdit_292.sizePolicy().hasHeightForWidth())
        self.lineEdit_292.setSizePolicy(sizePolicy)
        self.lineEdit_292.setAlignment(Qt.AlignCenter)

        self.gridLayout_162.addWidget(self.lineEdit_292, 0, 1, 1, 1)

        self.label_155 = QLabel(self.frame_63)
        self.label_155.setObjectName(u"label_155")
        sizePolicy.setHeightForWidth(self.label_155.sizePolicy().hasHeightForWidth())
        self.label_155.setSizePolicy(sizePolicy)

        self.gridLayout_162.addWidget(self.label_155, 0, 0, 1, 1)

        self.gridLayout_162.setColumnStretch(0, 1)
        self.gridLayout_162.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_63)

        self.frame_57 = QFrame(self.scrollAreaWidgetContents)
        self.frame_57.setObjectName(u"frame_57")
        sizePolicy.setHeightForWidth(self.frame_57.sizePolicy().hasHeightForWidth())
        self.frame_57.setSizePolicy(sizePolicy)
        self.frame_57.setMinimumSize(QSize(0, 30))
        self.frame_57.setMaximumSize(QSize(16777215, 16777215))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.gridLayout_156 = QGridLayout(self.frame_57)
        self.gridLayout_156.setObjectName(u"gridLayout_156")
        self.gridLayout_156.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_280 = QLineEdit(self.frame_57)
        self.lineEdit_280.setObjectName(u"lineEdit_280")
        sizePolicy.setHeightForWidth(self.lineEdit_280.sizePolicy().hasHeightForWidth())
        self.lineEdit_280.setSizePolicy(sizePolicy)
        self.lineEdit_280.setAlignment(Qt.AlignCenter)

        self.gridLayout_156.addWidget(self.lineEdit_280, 0, 1, 1, 1)

        self.label_149 = QLabel(self.frame_57)
        self.label_149.setObjectName(u"label_149")
        sizePolicy.setHeightForWidth(self.label_149.sizePolicy().hasHeightForWidth())
        self.label_149.setSizePolicy(sizePolicy)

        self.gridLayout_156.addWidget(self.label_149, 0, 0, 1, 1)

        self.gridLayout_156.setColumnStretch(0, 1)
        self.gridLayout_156.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_57)

        self.frame_64 = QFrame(self.scrollAreaWidgetContents)
        self.frame_64.setObjectName(u"frame_64")
        sizePolicy.setHeightForWidth(self.frame_64.sizePolicy().hasHeightForWidth())
        self.frame_64.setSizePolicy(sizePolicy)
        self.frame_64.setMinimumSize(QSize(0, 30))
        self.frame_64.setMaximumSize(QSize(16777215, 16777215))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.gridLayout_163 = QGridLayout(self.frame_64)
        self.gridLayout_163.setObjectName(u"gridLayout_163")
        self.gridLayout_163.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_294 = QLineEdit(self.frame_64)
        self.lineEdit_294.setObjectName(u"lineEdit_294")
        sizePolicy.setHeightForWidth(self.lineEdit_294.sizePolicy().hasHeightForWidth())
        self.lineEdit_294.setSizePolicy(sizePolicy)
        self.lineEdit_294.setAlignment(Qt.AlignCenter)

        self.gridLayout_163.addWidget(self.lineEdit_294, 0, 1, 1, 1)

        self.label_156 = QLabel(self.frame_64)
        self.label_156.setObjectName(u"label_156")
        sizePolicy.setHeightForWidth(self.label_156.sizePolicy().hasHeightForWidth())
        self.label_156.setSizePolicy(sizePolicy)

        self.gridLayout_163.addWidget(self.label_156, 0, 0, 1, 1)

        self.gridLayout_163.setColumnStretch(0, 2)
        self.gridLayout_163.setColumnStretch(1, 7)

        self.vboxLayout.addWidget(self.frame_64)

        self.frame_62 = QFrame(self.scrollAreaWidgetContents)
        self.frame_62.setObjectName(u"frame_62")
        sizePolicy.setHeightForWidth(self.frame_62.sizePolicy().hasHeightForWidth())
        self.frame_62.setSizePolicy(sizePolicy)
        self.frame_62.setMinimumSize(QSize(0, 30))
        self.frame_62.setMaximumSize(QSize(16777215, 16777215))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.gridLayout_161 = QGridLayout(self.frame_62)
        self.gridLayout_161.setObjectName(u"gridLayout_161")
        self.gridLayout_161.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_290 = QLineEdit(self.frame_62)
        self.lineEdit_290.setObjectName(u"lineEdit_290")
        sizePolicy.setHeightForWidth(self.lineEdit_290.sizePolicy().hasHeightForWidth())
        self.lineEdit_290.setSizePolicy(sizePolicy)
        self.lineEdit_290.setAlignment(Qt.AlignCenter)

        self.gridLayout_161.addWidget(self.lineEdit_290, 0, 1, 1, 1)

        self.label_154 = QLabel(self.frame_62)
        self.label_154.setObjectName(u"label_154")
        sizePolicy.setHeightForWidth(self.label_154.sizePolicy().hasHeightForWidth())
        self.label_154.setSizePolicy(sizePolicy)

        self.gridLayout_161.addWidget(self.label_154, 0, 0, 1, 1)

        self.gridLayout_161.setColumnStretch(0, 1)
        self.gridLayout_161.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_62)

        self.frame_55 = QFrame(self.scrollAreaWidgetContents)
        self.frame_55.setObjectName(u"frame_55")
        sizePolicy.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy)
        self.frame_55.setMinimumSize(QSize(0, 30))
        self.frame_55.setMaximumSize(QSize(16777215, 16777215))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.gridLayout_154 = QGridLayout(self.frame_55)
        self.gridLayout_154.setObjectName(u"gridLayout_154")
        self.gridLayout_154.setContentsMargins(0, 0, 0, 0)
        self.label_147 = QLabel(self.frame_55)
        self.label_147.setObjectName(u"label_147")
        sizePolicy.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy)

        self.gridLayout_154.addWidget(self.label_147, 0, 0, 1, 1)

        self.lineEdit_276 = QLineEdit(self.frame_55)
        self.lineEdit_276.setObjectName(u"lineEdit_276")
        sizePolicy.setHeightForWidth(self.lineEdit_276.sizePolicy().hasHeightForWidth())
        self.lineEdit_276.setSizePolicy(sizePolicy)
        self.lineEdit_276.setAlignment(Qt.AlignCenter)

        self.gridLayout_154.addWidget(self.lineEdit_276, 0, 1, 1, 1)

        self.gridLayout_154.setColumnStretch(0, 1)
        self.gridLayout_154.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_55)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 1, 2, 1)

        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.pushButton_10, 1, 0, 1, 1)

        self.gridLayout_5.setRowStretch(0, 9)
        self.gridLayout_5.setRowStretch(1, 1)

        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 2, 1)

        self.gridLayout_4.setRowStretch(0, 3)
        self.gridLayout_4.setRowStretch(1, 29)
        self.gridLayout_4.setRowStretch(2, 4)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_16 = QGridLayout(self.tab_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.tableWidget = QTableWidget(self.tab_7)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.DashDotLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_16.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.gridLayout_16.setRowStretch(0, 1)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_53 = QGridLayout(self.tab_5)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.scrollArea_2 = QScrollArea(self.tab_5)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setLayoutDirection(Qt.RightToLeft)
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Sunken)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(-116, 0, 135, 1236))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setLayoutDirection(Qt.RightToLeft)
        self.scrollAreaWidgetContents_2.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")
        self._2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self._2.setObjectName(u"_2")
        self._2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_14 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QSize(0, 30))
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_14)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.label_18, 0, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.frame_14)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        sizePolicy.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy)
        self.lineEdit_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.lineEdit_19, 0, 1, 1, 1)

        self.gridLayout_17.setColumnStretch(0, 1)
        self.gridLayout_17.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_14)

        self.frame_99 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_99.setObjectName(u"frame_99")
        sizePolicy.setHeightForWidth(self.frame_99.sizePolicy().hasHeightForWidth())
        self.frame_99.setSizePolicy(sizePolicy)
        self.frame_99.setMinimumSize(QSize(0, 30))
        self.frame_99.setMaximumSize(QSize(16777215, 16777215))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_99)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_42 = QLineEdit(self.frame_99)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        sizePolicy.setHeightForWidth(self.lineEdit_42.sizePolicy().hasHeightForWidth())
        self.lineEdit_42.setSizePolicy(sizePolicy)
        self.lineEdit_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.lineEdit_42, 0, 1, 1, 1)

        self.label_33 = QLabel(self.frame_99)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_59.addWidget(self.label_33, 0, 0, 1, 1)

        self.gridLayout_59.setColumnStretch(0, 1)
        self.gridLayout_59.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_99)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QSize(0, 30))
        self.frame_15.setMaximumSize(QSize(16777215, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_15)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_21 = QLineEdit(self.frame_15)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        sizePolicy.setHeightForWidth(self.lineEdit_21.sizePolicy().hasHeightForWidth())
        self.lineEdit_21.setSizePolicy(sizePolicy)
        self.lineEdit_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.lineEdit_21, 0, 1, 1, 1)

        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_18.addWidget(self.label_19, 0, 0, 1, 1)

        self.gridLayout_18.setColumnStretch(0, 1)
        self.gridLayout_18.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QSize(0, 30))
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_16)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_32.addWidget(self.label_20, 0, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.frame_16)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        sizePolicy.setHeightForWidth(self.lineEdit_22.sizePolicy().hasHeightForWidth())
        self.lineEdit_22.setSizePolicy(sizePolicy)
        self.lineEdit_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.lineEdit_22, 0, 1, 1, 1)

        self.gridLayout_32.setColumnStretch(0, 1)
        self.gridLayout_32.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_16)

        self.frame_58 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy)
        self.frame_58.setMinimumSize(QSize(0, 30))
        self.frame_58.setMaximumSize(QSize(16777215, 16777215))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_58)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_23 = QLineEdit(self.frame_58)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        sizePolicy.setHeightForWidth(self.lineEdit_23.sizePolicy().hasHeightForWidth())
        self.lineEdit_23.setSizePolicy(sizePolicy)
        self.lineEdit_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.lineEdit_23, 0, 1, 1, 1)

        self.label_21 = QLabel(self.frame_58)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_34.addWidget(self.label_21, 0, 0, 1, 1)

        self.gridLayout_34.setColumnStretch(0, 1)
        self.gridLayout_34.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy)
        self.frame_59.setMinimumSize(QSize(0, 30))
        self.frame_59.setMaximumSize(QSize(16777215, 16777215))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_59)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_25 = QLineEdit(self.frame_59)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        sizePolicy.setHeightForWidth(self.lineEdit_25.sizePolicy().hasHeightForWidth())
        self.lineEdit_25.setSizePolicy(sizePolicy)
        self.lineEdit_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_41.addWidget(self.lineEdit_25, 0, 1, 1, 1)

        self.label_22 = QLabel(self.frame_59)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)

        self.gridLayout_41.addWidget(self.label_22, 0, 0, 1, 1)

        self.gridLayout_41.setColumnStretch(0, 1)
        self.gridLayout_41.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_60.setObjectName(u"frame_60")
        sizePolicy.setHeightForWidth(self.frame_60.sizePolicy().hasHeightForWidth())
        self.frame_60.setSizePolicy(sizePolicy)
        self.frame_60.setMinimumSize(QSize(0, 30))
        self.frame_60.setMaximumSize(QSize(16777215, 16777215))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_60)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_60)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)

        self.gridLayout_43.addWidget(self.label_26, 0, 0, 1, 1)

        self.lineEdit_27 = QLineEdit(self.frame_60)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        sizePolicy.setHeightForWidth(self.lineEdit_27.sizePolicy().hasHeightForWidth())
        self.lineEdit_27.setSizePolicy(sizePolicy)
        self.lineEdit_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.lineEdit_27, 0, 1, 1, 1)

        self.gridLayout_43.setColumnStretch(0, 1)
        self.gridLayout_43.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_60)

        self.frame_65 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_65.setObjectName(u"frame_65")
        sizePolicy.setHeightForWidth(self.frame_65.sizePolicy().hasHeightForWidth())
        self.frame_65.setSizePolicy(sizePolicy)
        self.frame_65.setMinimumSize(QSize(0, 30))
        self.frame_65.setMaximumSize(QSize(16777215, 16777215))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_65)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_29 = QLineEdit(self.frame_65)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        sizePolicy.setHeightForWidth(self.lineEdit_29.sizePolicy().hasHeightForWidth())
        self.lineEdit_29.setSizePolicy(sizePolicy)
        self.lineEdit_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_48.addWidget(self.lineEdit_29, 0, 1, 1, 1)

        self.label_27 = QLabel(self.frame_65)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)

        self.gridLayout_48.addWidget(self.label_27, 0, 0, 1, 1)

        self.gridLayout_48.setColumnStretch(0, 1)
        self.gridLayout_48.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_66.setObjectName(u"frame_66")
        sizePolicy.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy)
        self.frame_66.setMinimumSize(QSize(0, 30))
        self.frame_66.setMaximumSize(QSize(16777215, 16777215))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.frame_66)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_34 = QLineEdit(self.frame_66)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        sizePolicy.setHeightForWidth(self.lineEdit_34.sizePolicy().hasHeightForWidth())
        self.lineEdit_34.setSizePolicy(sizePolicy)
        self.lineEdit_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_50.addWidget(self.lineEdit_34, 0, 1, 1, 1)

        self.label_28 = QLabel(self.frame_66)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)

        self.gridLayout_50.addWidget(self.label_28, 0, 0, 1, 1)

        self.gridLayout_50.setColumnStretch(0, 1)
        self.gridLayout_50.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_67.setObjectName(u"frame_67")
        sizePolicy.setHeightForWidth(self.frame_67.sizePolicy().hasHeightForWidth())
        self.frame_67.setSizePolicy(sizePolicy)
        self.frame_67.setMinimumSize(QSize(0, 30))
        self.frame_67.setMaximumSize(QSize(16777215, 16777215))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.frame_67)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_35 = QLineEdit(self.frame_67)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        sizePolicy.setHeightForWidth(self.lineEdit_35.sizePolicy().hasHeightForWidth())
        self.lineEdit_35.setSizePolicy(sizePolicy)
        self.lineEdit_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_52.addWidget(self.lineEdit_35, 0, 1, 1, 1)

        self.label_29 = QLabel(self.frame_67)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)

        self.gridLayout_52.addWidget(self.label_29, 0, 0, 1, 1)

        self.gridLayout_52.setColumnStretch(0, 1)
        self.gridLayout_52.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_68.setObjectName(u"frame_68")
        sizePolicy.setHeightForWidth(self.frame_68.sizePolicy().hasHeightForWidth())
        self.frame_68.setSizePolicy(sizePolicy)
        self.frame_68.setMinimumSize(QSize(0, 30))
        self.frame_68.setMaximumSize(QSize(16777215, 16777215))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.gridLayout_120 = QGridLayout(self.frame_68)
        self.gridLayout_120.setObjectName(u"gridLayout_120")
        self.gridLayout_120.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_201 = QLineEdit(self.frame_68)
        self.lineEdit_201.setObjectName(u"lineEdit_201")
        sizePolicy.setHeightForWidth(self.lineEdit_201.sizePolicy().hasHeightForWidth())
        self.lineEdit_201.setSizePolicy(sizePolicy)
        self.lineEdit_201.setAlignment(Qt.AlignCenter)

        self.gridLayout_120.addWidget(self.lineEdit_201, 0, 1, 1, 1)

        self.label_113 = QLabel(self.frame_68)
        self.label_113.setObjectName(u"label_113")
        sizePolicy.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy)

        self.gridLayout_120.addWidget(self.label_113, 0, 0, 1, 1)

        self.gridLayout_120.setColumnStretch(0, 1)
        self.gridLayout_120.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_69.setObjectName(u"frame_69")
        sizePolicy.setHeightForWidth(self.frame_69.sizePolicy().hasHeightForWidth())
        self.frame_69.setSizePolicy(sizePolicy)
        self.frame_69.setMinimumSize(QSize(0, 30))
        self.frame_69.setMaximumSize(QSize(16777215, 16777215))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.gridLayout_130 = QGridLayout(self.frame_69)
        self.gridLayout_130.setObjectName(u"gridLayout_130")
        self.gridLayout_130.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_219 = QLineEdit(self.frame_69)
        self.lineEdit_219.setObjectName(u"lineEdit_219")
        sizePolicy.setHeightForWidth(self.lineEdit_219.sizePolicy().hasHeightForWidth())
        self.lineEdit_219.setSizePolicy(sizePolicy)
        self.lineEdit_219.setAlignment(Qt.AlignCenter)

        self.gridLayout_130.addWidget(self.lineEdit_219, 0, 1, 1, 1)

        self.label_123 = QLabel(self.frame_69)
        self.label_123.setObjectName(u"label_123")
        sizePolicy.setHeightForWidth(self.label_123.sizePolicy().hasHeightForWidth())
        self.label_123.setSizePolicy(sizePolicy)

        self.gridLayout_130.addWidget(self.label_123, 0, 0, 1, 1)

        self.gridLayout_130.setColumnStretch(0, 1)
        self.gridLayout_130.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_70.setObjectName(u"frame_70")
        sizePolicy.setHeightForWidth(self.frame_70.sizePolicy().hasHeightForWidth())
        self.frame_70.setSizePolicy(sizePolicy)
        self.frame_70.setMinimumSize(QSize(0, 30))
        self.frame_70.setMaximumSize(QSize(16777215, 16777215))
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.gridLayout_131 = QGridLayout(self.frame_70)
        self.gridLayout_131.setObjectName(u"gridLayout_131")
        self.gridLayout_131.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_205 = QLineEdit(self.frame_70)
        self.lineEdit_205.setObjectName(u"lineEdit_205")
        sizePolicy.setHeightForWidth(self.lineEdit_205.sizePolicy().hasHeightForWidth())
        self.lineEdit_205.setSizePolicy(sizePolicy)
        self.lineEdit_205.setAlignment(Qt.AlignCenter)

        self.gridLayout_131.addWidget(self.lineEdit_205, 0, 1, 1, 1)

        self.label_124 = QLabel(self.frame_70)
        self.label_124.setObjectName(u"label_124")
        sizePolicy.setHeightForWidth(self.label_124.sizePolicy().hasHeightForWidth())
        self.label_124.setSizePolicy(sizePolicy)

        self.gridLayout_131.addWidget(self.label_124, 0, 0, 1, 1)

        self.gridLayout_131.setColumnStretch(0, 1)
        self.gridLayout_131.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_70)

        self.frame_71 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_71.setObjectName(u"frame_71")
        sizePolicy.setHeightForWidth(self.frame_71.sizePolicy().hasHeightForWidth())
        self.frame_71.setSizePolicy(sizePolicy)
        self.frame_71.setMinimumSize(QSize(0, 30))
        self.frame_71.setMaximumSize(QSize(16777215, 16777215))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.gridLayout_132 = QGridLayout(self.frame_71)
        self.gridLayout_132.setObjectName(u"gridLayout_132")
        self.gridLayout_132.setContentsMargins(0, 0, 0, 0)
        self.label_125 = QLabel(self.frame_71)
        self.label_125.setObjectName(u"label_125")
        sizePolicy.setHeightForWidth(self.label_125.sizePolicy().hasHeightForWidth())
        self.label_125.setSizePolicy(sizePolicy)

        self.gridLayout_132.addWidget(self.label_125, 0, 0, 1, 1)

        self.lineEdit_199 = QLineEdit(self.frame_71)
        self.lineEdit_199.setObjectName(u"lineEdit_199")
        sizePolicy.setHeightForWidth(self.lineEdit_199.sizePolicy().hasHeightForWidth())
        self.lineEdit_199.setSizePolicy(sizePolicy)
        self.lineEdit_199.setAlignment(Qt.AlignCenter)

        self.gridLayout_132.addWidget(self.lineEdit_199, 0, 1, 1, 1)

        self.gridLayout_132.setColumnStretch(0, 1)
        self.gridLayout_132.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_72.setObjectName(u"frame_72")
        sizePolicy.setHeightForWidth(self.frame_72.sizePolicy().hasHeightForWidth())
        self.frame_72.setSizePolicy(sizePolicy)
        self.frame_72.setMinimumSize(QSize(0, 30))
        self.frame_72.setMaximumSize(QSize(16777215, 16777215))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.gridLayout_133 = QGridLayout(self.frame_72)
        self.gridLayout_133.setObjectName(u"gridLayout_133")
        self.gridLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_126 = QLabel(self.frame_72)
        self.label_126.setObjectName(u"label_126")
        sizePolicy.setHeightForWidth(self.label_126.sizePolicy().hasHeightForWidth())
        self.label_126.setSizePolicy(sizePolicy)

        self.gridLayout_133.addWidget(self.label_126, 0, 0, 1, 1)

        self.lineEdit_225 = QLineEdit(self.frame_72)
        self.lineEdit_225.setObjectName(u"lineEdit_225")
        sizePolicy.setHeightForWidth(self.lineEdit_225.sizePolicy().hasHeightForWidth())
        self.lineEdit_225.setSizePolicy(sizePolicy)
        self.lineEdit_225.setAlignment(Qt.AlignCenter)

        self.gridLayout_133.addWidget(self.lineEdit_225, 0, 1, 1, 1)

        self.gridLayout_133.setColumnStretch(0, 1)
        self.gridLayout_133.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_73.setObjectName(u"frame_73")
        sizePolicy.setHeightForWidth(self.frame_73.sizePolicy().hasHeightForWidth())
        self.frame_73.setSizePolicy(sizePolicy)
        self.frame_73.setMinimumSize(QSize(0, 30))
        self.frame_73.setMaximumSize(QSize(16777215, 16777215))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.gridLayout_134 = QGridLayout(self.frame_73)
        self.gridLayout_134.setObjectName(u"gridLayout_134")
        self.gridLayout_134.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_227 = QLineEdit(self.frame_73)
        self.lineEdit_227.setObjectName(u"lineEdit_227")
        sizePolicy.setHeightForWidth(self.lineEdit_227.sizePolicy().hasHeightForWidth())
        self.lineEdit_227.setSizePolicy(sizePolicy)
        self.lineEdit_227.setAlignment(Qt.AlignCenter)

        self.gridLayout_134.addWidget(self.lineEdit_227, 0, 1, 1, 1)

        self.label_127 = QLabel(self.frame_73)
        self.label_127.setObjectName(u"label_127")
        sizePolicy.setHeightForWidth(self.label_127.sizePolicy().hasHeightForWidth())
        self.label_127.setSizePolicy(sizePolicy)

        self.gridLayout_134.addWidget(self.label_127, 0, 0, 1, 1)

        self.gridLayout_134.setColumnStretch(0, 1)
        self.gridLayout_134.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_73)

        self.frame_74 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_74.setObjectName(u"frame_74")
        sizePolicy.setHeightForWidth(self.frame_74.sizePolicy().hasHeightForWidth())
        self.frame_74.setSizePolicy(sizePolicy)
        self.frame_74.setMinimumSize(QSize(0, 30))
        self.frame_74.setMaximumSize(QSize(16777215, 16777215))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.gridLayout_135 = QGridLayout(self.frame_74)
        self.gridLayout_135.setObjectName(u"gridLayout_135")
        self.gridLayout_135.setContentsMargins(0, 0, 0, 0)
        self.label_128 = QLabel(self.frame_74)
        self.label_128.setObjectName(u"label_128")
        sizePolicy.setHeightForWidth(self.label_128.sizePolicy().hasHeightForWidth())
        self.label_128.setSizePolicy(sizePolicy)

        self.gridLayout_135.addWidget(self.label_128, 0, 0, 1, 1)

        self.lineEdit_211 = QLineEdit(self.frame_74)
        self.lineEdit_211.setObjectName(u"lineEdit_211")
        sizePolicy.setHeightForWidth(self.lineEdit_211.sizePolicy().hasHeightForWidth())
        self.lineEdit_211.setSizePolicy(sizePolicy)
        self.lineEdit_211.setAlignment(Qt.AlignCenter)

        self.gridLayout_135.addWidget(self.lineEdit_211, 0, 1, 1, 1)

        self.gridLayout_135.setColumnStretch(0, 1)
        self.gridLayout_135.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_75.setObjectName(u"frame_75")
        sizePolicy.setHeightForWidth(self.frame_75.sizePolicy().hasHeightForWidth())
        self.frame_75.setSizePolicy(sizePolicy)
        self.frame_75.setMinimumSize(QSize(0, 30))
        self.frame_75.setMaximumSize(QSize(16777215, 16777215))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.gridLayout_136 = QGridLayout(self.frame_75)
        self.gridLayout_136.setObjectName(u"gridLayout_136")
        self.gridLayout_136.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_215 = QLineEdit(self.frame_75)
        self.lineEdit_215.setObjectName(u"lineEdit_215")
        sizePolicy.setHeightForWidth(self.lineEdit_215.sizePolicy().hasHeightForWidth())
        self.lineEdit_215.setSizePolicy(sizePolicy)
        self.lineEdit_215.setAlignment(Qt.AlignCenter)

        self.gridLayout_136.addWidget(self.lineEdit_215, 0, 1, 1, 1)

        self.label_129 = QLabel(self.frame_75)
        self.label_129.setObjectName(u"label_129")
        sizePolicy.setHeightForWidth(self.label_129.sizePolicy().hasHeightForWidth())
        self.label_129.setSizePolicy(sizePolicy)

        self.gridLayout_136.addWidget(self.label_129, 0, 0, 1, 1)

        self.gridLayout_136.setColumnStretch(0, 1)
        self.gridLayout_136.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_76.setObjectName(u"frame_76")
        sizePolicy.setHeightForWidth(self.frame_76.sizePolicy().hasHeightForWidth())
        self.frame_76.setSizePolicy(sizePolicy)
        self.frame_76.setMinimumSize(QSize(0, 30))
        self.frame_76.setMaximumSize(QSize(16777215, 16777215))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.gridLayout_137 = QGridLayout(self.frame_76)
        self.gridLayout_137.setObjectName(u"gridLayout_137")
        self.gridLayout_137.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_221 = QLineEdit(self.frame_76)
        self.lineEdit_221.setObjectName(u"lineEdit_221")
        sizePolicy.setHeightForWidth(self.lineEdit_221.sizePolicy().hasHeightForWidth())
        self.lineEdit_221.setSizePolicy(sizePolicy)
        self.lineEdit_221.setAlignment(Qt.AlignCenter)

        self.gridLayout_137.addWidget(self.lineEdit_221, 0, 1, 1, 1)

        self.label_130 = QLabel(self.frame_76)
        self.label_130.setObjectName(u"label_130")
        sizePolicy.setHeightForWidth(self.label_130.sizePolicy().hasHeightForWidth())
        self.label_130.setSizePolicy(sizePolicy)

        self.gridLayout_137.addWidget(self.label_130, 0, 0, 1, 1)

        self.gridLayout_137.setColumnStretch(0, 1)
        self.gridLayout_137.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_77.setObjectName(u"frame_77")
        sizePolicy.setHeightForWidth(self.frame_77.sizePolicy().hasHeightForWidth())
        self.frame_77.setSizePolicy(sizePolicy)
        self.frame_77.setMinimumSize(QSize(0, 30))
        self.frame_77.setMaximumSize(QSize(16777215, 16777215))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.gridLayout_138 = QGridLayout(self.frame_77)
        self.gridLayout_138.setObjectName(u"gridLayout_138")
        self.gridLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_131 = QLabel(self.frame_77)
        self.label_131.setObjectName(u"label_131")
        sizePolicy.setHeightForWidth(self.label_131.sizePolicy().hasHeightForWidth())
        self.label_131.setSizePolicy(sizePolicy)

        self.gridLayout_138.addWidget(self.label_131, 0, 0, 1, 1)

        self.lineEdit_197 = QLineEdit(self.frame_77)
        self.lineEdit_197.setObjectName(u"lineEdit_197")
        sizePolicy.setHeightForWidth(self.lineEdit_197.sizePolicy().hasHeightForWidth())
        self.lineEdit_197.setSizePolicy(sizePolicy)
        self.lineEdit_197.setAlignment(Qt.AlignCenter)

        self.gridLayout_138.addWidget(self.lineEdit_197, 0, 1, 1, 1)

        self.gridLayout_138.setColumnStretch(0, 1)
        self.gridLayout_138.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_78.setObjectName(u"frame_78")
        sizePolicy.setHeightForWidth(self.frame_78.sizePolicy().hasHeightForWidth())
        self.frame_78.setSizePolicy(sizePolicy)
        self.frame_78.setMinimumSize(QSize(0, 30))
        self.frame_78.setMaximumSize(QSize(16777215, 16777215))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.gridLayout_139 = QGridLayout(self.frame_78)
        self.gridLayout_139.setObjectName(u"gridLayout_139")
        self.gridLayout_139.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_223 = QLineEdit(self.frame_78)
        self.lineEdit_223.setObjectName(u"lineEdit_223")
        sizePolicy.setHeightForWidth(self.lineEdit_223.sizePolicy().hasHeightForWidth())
        self.lineEdit_223.setSizePolicy(sizePolicy)
        self.lineEdit_223.setAlignment(Qt.AlignCenter)

        self.gridLayout_139.addWidget(self.lineEdit_223, 0, 1, 1, 1)

        self.label_132 = QLabel(self.frame_78)
        self.label_132.setObjectName(u"label_132")
        sizePolicy.setHeightForWidth(self.label_132.sizePolicy().hasHeightForWidth())
        self.label_132.setSizePolicy(sizePolicy)

        self.gridLayout_139.addWidget(self.label_132, 0, 0, 1, 1)

        self.gridLayout_139.setColumnStretch(0, 1)
        self.gridLayout_139.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_79.setObjectName(u"frame_79")
        sizePolicy.setHeightForWidth(self.frame_79.sizePolicy().hasHeightForWidth())
        self.frame_79.setSizePolicy(sizePolicy)
        self.frame_79.setMinimumSize(QSize(0, 30))
        self.frame_79.setMaximumSize(QSize(16777215, 16777215))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.gridLayout_140 = QGridLayout(self.frame_79)
        self.gridLayout_140.setObjectName(u"gridLayout_140")
        self.gridLayout_140.setContentsMargins(0, 0, 0, 0)
        self.label_133 = QLabel(self.frame_79)
        self.label_133.setObjectName(u"label_133")
        sizePolicy.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy)

        self.gridLayout_140.addWidget(self.label_133, 0, 0, 1, 1)

        self.lineEdit_203 = QLineEdit(self.frame_79)
        self.lineEdit_203.setObjectName(u"lineEdit_203")
        sizePolicy.setHeightForWidth(self.lineEdit_203.sizePolicy().hasHeightForWidth())
        self.lineEdit_203.setSizePolicy(sizePolicy)
        self.lineEdit_203.setAlignment(Qt.AlignCenter)

        self.gridLayout_140.addWidget(self.lineEdit_203, 0, 1, 1, 1)

        self.gridLayout_140.setColumnStretch(0, 1)
        self.gridLayout_140.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_79)

        self.frame_80 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_80.setObjectName(u"frame_80")
        sizePolicy.setHeightForWidth(self.frame_80.sizePolicy().hasHeightForWidth())
        self.frame_80.setSizePolicy(sizePolicy)
        self.frame_80.setMinimumSize(QSize(0, 30))
        self.frame_80.setMaximumSize(QSize(16777215, 16777215))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.gridLayout_141 = QGridLayout(self.frame_80)
        self.gridLayout_141.setObjectName(u"gridLayout_141")
        self.gridLayout_141.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_217 = QLineEdit(self.frame_80)
        self.lineEdit_217.setObjectName(u"lineEdit_217")
        sizePolicy.setHeightForWidth(self.lineEdit_217.sizePolicy().hasHeightForWidth())
        self.lineEdit_217.setSizePolicy(sizePolicy)
        self.lineEdit_217.setAlignment(Qt.AlignCenter)

        self.gridLayout_141.addWidget(self.lineEdit_217, 0, 1, 1, 1)

        self.label_134 = QLabel(self.frame_80)
        self.label_134.setObjectName(u"label_134")
        sizePolicy.setHeightForWidth(self.label_134.sizePolicy().hasHeightForWidth())
        self.label_134.setSizePolicy(sizePolicy)

        self.gridLayout_141.addWidget(self.label_134, 0, 0, 1, 1)

        self.gridLayout_141.setColumnStretch(0, 1)
        self.gridLayout_141.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_81.setObjectName(u"frame_81")
        sizePolicy.setHeightForWidth(self.frame_81.sizePolicy().hasHeightForWidth())
        self.frame_81.setSizePolicy(sizePolicy)
        self.frame_81.setMinimumSize(QSize(0, 30))
        self.frame_81.setMaximumSize(QSize(16777215, 16777215))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.gridLayout_142 = QGridLayout(self.frame_81)
        self.gridLayout_142.setObjectName(u"gridLayout_142")
        self.gridLayout_142.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_213 = QLineEdit(self.frame_81)
        self.lineEdit_213.setObjectName(u"lineEdit_213")
        sizePolicy.setHeightForWidth(self.lineEdit_213.sizePolicy().hasHeightForWidth())
        self.lineEdit_213.setSizePolicy(sizePolicy)
        self.lineEdit_213.setAlignment(Qt.AlignCenter)

        self.gridLayout_142.addWidget(self.lineEdit_213, 0, 1, 1, 1)

        self.label_135 = QLabel(self.frame_81)
        self.label_135.setObjectName(u"label_135")
        sizePolicy.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy)

        self.gridLayout_142.addWidget(self.label_135, 0, 0, 1, 1)

        self.gridLayout_142.setColumnStretch(0, 1)
        self.gridLayout_142.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_81)

        self.frame_82 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_82.setObjectName(u"frame_82")
        sizePolicy.setHeightForWidth(self.frame_82.sizePolicy().hasHeightForWidth())
        self.frame_82.setSizePolicy(sizePolicy)
        self.frame_82.setMinimumSize(QSize(0, 30))
        self.frame_82.setMaximumSize(QSize(16777215, 16777215))
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.gridLayout_143 = QGridLayout(self.frame_82)
        self.gridLayout_143.setObjectName(u"gridLayout_143")
        self.gridLayout_143.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_193 = QLineEdit(self.frame_82)
        self.lineEdit_193.setObjectName(u"lineEdit_193")
        sizePolicy.setHeightForWidth(self.lineEdit_193.sizePolicy().hasHeightForWidth())
        self.lineEdit_193.setSizePolicy(sizePolicy)
        self.lineEdit_193.setAlignment(Qt.AlignCenter)

        self.gridLayout_143.addWidget(self.lineEdit_193, 0, 1, 1, 1)

        self.label_136 = QLabel(self.frame_82)
        self.label_136.setObjectName(u"label_136")
        sizePolicy.setHeightForWidth(self.label_136.sizePolicy().hasHeightForWidth())
        self.label_136.setSizePolicy(sizePolicy)

        self.gridLayout_143.addWidget(self.label_136, 0, 0, 1, 1)

        self.gridLayout_143.setColumnStretch(0, 1)
        self.gridLayout_143.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_82)

        self.frame_83 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_83.setObjectName(u"frame_83")
        sizePolicy.setHeightForWidth(self.frame_83.sizePolicy().hasHeightForWidth())
        self.frame_83.setSizePolicy(sizePolicy)
        self.frame_83.setMinimumSize(QSize(0, 30))
        self.frame_83.setMaximumSize(QSize(16777215, 16777215))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.gridLayout_144 = QGridLayout(self.frame_83)
        self.gridLayout_144.setObjectName(u"gridLayout_144")
        self.gridLayout_144.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_195 = QLineEdit(self.frame_83)
        self.lineEdit_195.setObjectName(u"lineEdit_195")
        sizePolicy.setHeightForWidth(self.lineEdit_195.sizePolicy().hasHeightForWidth())
        self.lineEdit_195.setSizePolicy(sizePolicy)
        self.lineEdit_195.setAlignment(Qt.AlignCenter)

        self.gridLayout_144.addWidget(self.lineEdit_195, 0, 1, 1, 1)

        self.label_137 = QLabel(self.frame_83)
        self.label_137.setObjectName(u"label_137")
        sizePolicy.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy)

        self.gridLayout_144.addWidget(self.label_137, 0, 0, 1, 1)

        self.gridLayout_144.setColumnStretch(0, 1)
        self.gridLayout_144.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_83)

        self.frame_84 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_84.setObjectName(u"frame_84")
        sizePolicy.setHeightForWidth(self.frame_84.sizePolicy().hasHeightForWidth())
        self.frame_84.setSizePolicy(sizePolicy)
        self.frame_84.setMinimumSize(QSize(0, 30))
        self.frame_84.setMaximumSize(QSize(16777215, 16777215))
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.gridLayout_145 = QGridLayout(self.frame_84)
        self.gridLayout_145.setObjectName(u"gridLayout_145")
        self.gridLayout_145.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_207 = QLineEdit(self.frame_84)
        self.lineEdit_207.setObjectName(u"lineEdit_207")
        sizePolicy.setHeightForWidth(self.lineEdit_207.sizePolicy().hasHeightForWidth())
        self.lineEdit_207.setSizePolicy(sizePolicy)
        self.lineEdit_207.setAlignment(Qt.AlignCenter)

        self.gridLayout_145.addWidget(self.lineEdit_207, 0, 1, 1, 1)

        self.label_138 = QLabel(self.frame_84)
        self.label_138.setObjectName(u"label_138")
        sizePolicy.setHeightForWidth(self.label_138.sizePolicy().hasHeightForWidth())
        self.label_138.setSizePolicy(sizePolicy)

        self.gridLayout_145.addWidget(self.label_138, 0, 0, 1, 1)

        self.gridLayout_145.setColumnStretch(0, 1)
        self.gridLayout_145.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_85.setObjectName(u"frame_85")
        sizePolicy.setHeightForWidth(self.frame_85.sizePolicy().hasHeightForWidth())
        self.frame_85.setSizePolicy(sizePolicy)
        self.frame_85.setMinimumSize(QSize(0, 30))
        self.frame_85.setMaximumSize(QSize(16777215, 16777215))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.gridLayout_164 = QGridLayout(self.frame_85)
        self.gridLayout_164.setObjectName(u"gridLayout_164")
        self.gridLayout_164.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_289 = QLineEdit(self.frame_85)
        self.lineEdit_289.setObjectName(u"lineEdit_289")
        sizePolicy.setHeightForWidth(self.lineEdit_289.sizePolicy().hasHeightForWidth())
        self.lineEdit_289.setSizePolicy(sizePolicy)
        self.lineEdit_289.setAlignment(Qt.AlignCenter)

        self.gridLayout_164.addWidget(self.lineEdit_289, 0, 1, 1, 1)

        self.label_157 = QLabel(self.frame_85)
        self.label_157.setObjectName(u"label_157")
        sizePolicy.setHeightForWidth(self.label_157.sizePolicy().hasHeightForWidth())
        self.label_157.setSizePolicy(sizePolicy)

        self.gridLayout_164.addWidget(self.label_157, 0, 0, 1, 1)

        self.gridLayout_164.setColumnStretch(0, 1)
        self.gridLayout_164.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_86.setObjectName(u"frame_86")
        sizePolicy.setHeightForWidth(self.frame_86.sizePolicy().hasHeightForWidth())
        self.frame_86.setSizePolicy(sizePolicy)
        self.frame_86.setMinimumSize(QSize(0, 30))
        self.frame_86.setMaximumSize(QSize(16777215, 16777215))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.gridLayout_153 = QGridLayout(self.frame_86)
        self.gridLayout_153.setObjectName(u"gridLayout_153")
        self.gridLayout_153.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_273 = QLineEdit(self.frame_86)
        self.lineEdit_273.setObjectName(u"lineEdit_273")
        sizePolicy.setHeightForWidth(self.lineEdit_273.sizePolicy().hasHeightForWidth())
        self.lineEdit_273.setSizePolicy(sizePolicy)
        self.lineEdit_273.setAlignment(Qt.AlignCenter)

        self.gridLayout_153.addWidget(self.lineEdit_273, 0, 1, 1, 1)

        self.label_146 = QLabel(self.frame_86)
        self.label_146.setObjectName(u"label_146")
        sizePolicy.setHeightForWidth(self.label_146.sizePolicy().hasHeightForWidth())
        self.label_146.setSizePolicy(sizePolicy)

        self.gridLayout_153.addWidget(self.label_146, 0, 0, 1, 1)

        self.gridLayout_153.setColumnStretch(0, 1)
        self.gridLayout_153.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_87.setObjectName(u"frame_87")
        sizePolicy.setHeightForWidth(self.frame_87.sizePolicy().hasHeightForWidth())
        self.frame_87.setSizePolicy(sizePolicy)
        self.frame_87.setMinimumSize(QSize(0, 30))
        self.frame_87.setMaximumSize(QSize(16777215, 16777215))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.gridLayout_165 = QGridLayout(self.frame_87)
        self.gridLayout_165.setObjectName(u"gridLayout_165")
        self.gridLayout_165.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_293 = QLineEdit(self.frame_87)
        self.lineEdit_293.setObjectName(u"lineEdit_293")
        sizePolicy.setHeightForWidth(self.lineEdit_293.sizePolicy().hasHeightForWidth())
        self.lineEdit_293.setSizePolicy(sizePolicy)
        self.lineEdit_293.setAlignment(Qt.AlignCenter)

        self.gridLayout_165.addWidget(self.lineEdit_293, 0, 1, 1, 1)

        self.label_158 = QLabel(self.frame_87)
        self.label_158.setObjectName(u"label_158")
        sizePolicy.setHeightForWidth(self.label_158.sizePolicy().hasHeightForWidth())
        self.label_158.setSizePolicy(sizePolicy)

        self.gridLayout_165.addWidget(self.label_158, 0, 0, 1, 1)

        self.gridLayout_165.setColumnStretch(0, 1)
        self.gridLayout_165.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_88.setObjectName(u"frame_88")
        sizePolicy.setHeightForWidth(self.frame_88.sizePolicy().hasHeightForWidth())
        self.frame_88.setSizePolicy(sizePolicy)
        self.frame_88.setMinimumSize(QSize(0, 30))
        self.frame_88.setMaximumSize(QSize(16777215, 16777215))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.gridLayout_157 = QGridLayout(self.frame_88)
        self.gridLayout_157.setObjectName(u"gridLayout_157")
        self.gridLayout_157.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_281 = QLineEdit(self.frame_88)
        self.lineEdit_281.setObjectName(u"lineEdit_281")
        sizePolicy.setHeightForWidth(self.lineEdit_281.sizePolicy().hasHeightForWidth())
        self.lineEdit_281.setSizePolicy(sizePolicy)
        self.lineEdit_281.setAlignment(Qt.AlignCenter)

        self.gridLayout_157.addWidget(self.lineEdit_281, 0, 1, 1, 1)

        self.label_150 = QLabel(self.frame_88)
        self.label_150.setObjectName(u"label_150")
        sizePolicy.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy)

        self.gridLayout_157.addWidget(self.label_150, 0, 0, 1, 1)

        self.gridLayout_157.setColumnStretch(0, 1)
        self.gridLayout_157.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_88)

        self.frame_95 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_95.setObjectName(u"frame_95")
        sizePolicy.setHeightForWidth(self.frame_95.sizePolicy().hasHeightForWidth())
        self.frame_95.setSizePolicy(sizePolicy)
        self.frame_95.setMinimumSize(QSize(0, 30))
        self.frame_95.setMaximumSize(QSize(16777215, 16777215))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.gridLayout_166 = QGridLayout(self.frame_95)
        self.gridLayout_166.setObjectName(u"gridLayout_166")
        self.gridLayout_166.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_295 = QLineEdit(self.frame_95)
        self.lineEdit_295.setObjectName(u"lineEdit_295")
        sizePolicy.setHeightForWidth(self.lineEdit_295.sizePolicy().hasHeightForWidth())
        self.lineEdit_295.setSizePolicy(sizePolicy)
        self.lineEdit_295.setAlignment(Qt.AlignCenter)

        self.gridLayout_166.addWidget(self.lineEdit_295, 0, 1, 1, 1)

        self.label_159 = QLabel(self.frame_95)
        self.label_159.setObjectName(u"label_159")
        sizePolicy.setHeightForWidth(self.label_159.sizePolicy().hasHeightForWidth())
        self.label_159.setSizePolicy(sizePolicy)

        self.gridLayout_166.addWidget(self.label_159, 0, 0, 1, 1)

        self.gridLayout_166.setColumnStretch(0, 1)
        self.gridLayout_166.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_95)

        self.frame_96 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_96.setObjectName(u"frame_96")
        sizePolicy.setHeightForWidth(self.frame_96.sizePolicy().hasHeightForWidth())
        self.frame_96.setSizePolicy(sizePolicy)
        self.frame_96.setMinimumSize(QSize(0, 30))
        self.frame_96.setMaximumSize(QSize(16777215, 16777215))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.gridLayout_167 = QGridLayout(self.frame_96)
        self.gridLayout_167.setObjectName(u"gridLayout_167")
        self.gridLayout_167.setContentsMargins(0, 0, 0, 0)
        self.label_160 = QLabel(self.frame_96)
        self.label_160.setObjectName(u"label_160")
        sizePolicy.setHeightForWidth(self.label_160.sizePolicy().hasHeightForWidth())
        self.label_160.setSizePolicy(sizePolicy)

        self.gridLayout_167.addWidget(self.label_160, 0, 0, 1, 1)

        self.lineEdit_291 = QLineEdit(self.frame_96)
        self.lineEdit_291.setObjectName(u"lineEdit_291")
        sizePolicy.setHeightForWidth(self.lineEdit_291.sizePolicy().hasHeightForWidth())
        self.lineEdit_291.setSizePolicy(sizePolicy)
        self.lineEdit_291.setAlignment(Qt.AlignCenter)

        self.gridLayout_167.addWidget(self.lineEdit_291, 0, 1, 1, 1)

        self.gridLayout_167.setColumnStretch(0, 1)
        self.gridLayout_167.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_96)

        self.frame_97 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_97.setObjectName(u"frame_97")
        sizePolicy.setHeightForWidth(self.frame_97.sizePolicy().hasHeightForWidth())
        self.frame_97.setSizePolicy(sizePolicy)
        self.frame_97.setMinimumSize(QSize(0, 30))
        self.frame_97.setMaximumSize(QSize(16777215, 16777215))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.gridLayout_155 = QGridLayout(self.frame_97)
        self.gridLayout_155.setObjectName(u"gridLayout_155")
        self.gridLayout_155.setContentsMargins(0, 0, 0, 0)
        self.label_148 = QLabel(self.frame_97)
        self.label_148.setObjectName(u"label_148")
        sizePolicy.setHeightForWidth(self.label_148.sizePolicy().hasHeightForWidth())
        self.label_148.setSizePolicy(sizePolicy)

        self.gridLayout_155.addWidget(self.label_148, 0, 0, 1, 1)

        self.lineEdit_277 = QLineEdit(self.frame_97)
        self.lineEdit_277.setObjectName(u"lineEdit_277")
        sizePolicy.setHeightForWidth(self.lineEdit_277.sizePolicy().hasHeightForWidth())
        self.lineEdit_277.setSizePolicy(sizePolicy)
        self.lineEdit_277.setAlignment(Qt.AlignCenter)

        self.gridLayout_155.addWidget(self.lineEdit_277, 0, 1, 1, 1)

        self.gridLayout_155.setColumnStretch(0, 1)
        self.gridLayout_155.setColumnStretch(1, 4)

        self._2.addWidget(self.frame_97)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_53.addWidget(self.scrollArea_2, 0, 1, 2, 1)

        self.frame_38 = QFrame(self.tab_5)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_38)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.frame_89 = QFrame(self.frame_38)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_89)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_91 = QFrame(self.frame_89)
        self.frame_91.setObjectName(u"frame_91")
        sizePolicy.setHeightForWidth(self.frame_91.sizePolicy().hasHeightForWidth())
        self.frame_91.setSizePolicy(sizePolicy)
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.gridLayout_180 = QGridLayout(self.frame_91)
        self.gridLayout_180.setObjectName(u"gridLayout_180")
        self.gridLayout_180.setHorizontalSpacing(0)
        self.gridLayout_180.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_91)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)

        self.gridLayout_180.addWidget(self.label_23, 0, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame_91)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setLayoutDirection(Qt.RightToLeft)
        self.textEdit_2.setOverwriteMode(False)

        self.gridLayout_180.addWidget(self.textEdit_2, 1, 0, 1, 1)


        self.gridLayout_44.addWidget(self.frame_91, 1, 0, 1, 1)

        self.frame_90 = QFrame(self.frame_89)
        self.frame_90.setObjectName(u"frame_90")
        sizePolicy.setHeightForWidth(self.frame_90.sizePolicy().hasHeightForWidth())
        self.frame_90.setSizePolicy(sizePolicy)
        self.frame_90.setLayoutDirection(Qt.LeftToRight)
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_90)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.lineEdit_30 = QLineEdit(self.frame_90)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        sizePolicy.setHeightForWidth(self.lineEdit_30.sizePolicy().hasHeightForWidth())
        self.lineEdit_30.setSizePolicy(sizePolicy)
        self.lineEdit_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.lineEdit_30, 0, 0, 1, 1)

        self.label_13 = QLabel(self.frame_90)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_45.addWidget(self.label_13, 0, 1, 1, 1)

        self.lineEdit_31 = QLineEdit(self.frame_90)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        sizePolicy.setHeightForWidth(self.lineEdit_31.sizePolicy().hasHeightForWidth())
        self.lineEdit_31.setSizePolicy(sizePolicy)
        self.lineEdit_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.lineEdit_31, 2, 0, 1, 1)

        self.label_14 = QLabel(self.frame_90)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_45.addWidget(self.label_14, 2, 1, 1, 1)

        self.label_15 = QLabel(self.frame_90)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_45.addWidget(self.label_15, 3, 1, 1, 1)

        self.lineEdit_32 = QLineEdit(self.frame_90)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        sizePolicy.setHeightForWidth(self.lineEdit_32.sizePolicy().hasHeightForWidth())
        self.lineEdit_32.setSizePolicy(sizePolicy)
        self.lineEdit_32.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.lineEdit_32, 3, 0, 1, 1)

        self.lineEdit_33 = QLineEdit(self.frame_90)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        sizePolicy.setHeightForWidth(self.lineEdit_33.sizePolicy().hasHeightForWidth())
        self.lineEdit_33.setSizePolicy(sizePolicy)
        self.lineEdit_33.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.lineEdit_33, 4, 0, 1, 1)

        self.label_17 = QLabel(self.frame_90)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_45.addWidget(self.label_17, 4, 1, 1, 1)

        self.label_30 = QLabel(self.frame_90)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_45.addWidget(self.label_30, 1, 1, 1, 1)

        self.lineEdit_41 = QLineEdit(self.frame_90)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        sizePolicy.setHeightForWidth(self.lineEdit_41.sizePolicy().hasHeightForWidth())
        self.lineEdit_41.setSizePolicy(sizePolicy)
        self.lineEdit_41.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.lineEdit_41, 1, 0, 1, 1)


        self.gridLayout_44.addWidget(self.frame_90, 0, 0, 1, 1)

        self.frame_92 = QFrame(self.frame_89)
        self.frame_92.setObjectName(u"frame_92")
        sizePolicy.setHeightForWidth(self.frame_92.sizePolicy().hasHeightForWidth())
        self.frame_92.setSizePolicy(sizePolicy)
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_92)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_10 = QLineEdit(self.frame_92)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_46.addWidget(self.lineEdit_10, 1, 0, 1, 1)

        self.label_24 = QLabel(self.frame_92)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)

        self.gridLayout_46.addWidget(self.label_24, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.frame_92, 2, 0, 1, 1)

        self.gridLayout_44.setRowStretch(0, 3)
        self.gridLayout_44.setRowStretch(1, 3)
        self.gridLayout_44.setRowStretch(2, 1)

        self.gridLayout_9.addWidget(self.frame_89, 0, 0, 1, 1)

        self.frame_94 = QFrame(self.frame_38)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_94)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_94)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)

        self.gridLayout_49.addWidget(self.pushButton_7, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_94, 1, 0, 1, 1)

        self.gridLayout_9.setRowStretch(0, 10)
        self.gridLayout_9.setRowStretch(1, 1)

        self.gridLayout_53.addWidget(self.frame_38, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.gridLayout_2.addWidget(self.tabWidget_2, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 12)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_87 = QGridLayout(self.tab_2)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.frame_177 = QFrame(self.tab_2)
        self.frame_177.setObjectName(u"frame_177")
        sizePolicy.setHeightForWidth(self.frame_177.sizePolicy().hasHeightForWidth())
        self.frame_177.setSizePolicy(sizePolicy)
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.gridLayout_86 = QGridLayout(self.frame_177)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.gridLayout_86.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_4 = QPushButton(self.frame_177)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.gridLayout_86.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.pushButton_24 = QPushButton(self.frame_177)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)

        self.gridLayout_86.addWidget(self.pushButton_24, 0, 0, 1, 1)


        self.gridLayout_87.addWidget(self.frame_177, 0, 0, 1, 1)

        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy)
        self.tabWidget_3.setLayoutDirection(Qt.RightToLeft)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_33 = QGridLayout(self.tab_4)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.frame_9 = QFrame(self.tab_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_9)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(-1, -1, -1, 0)
        self.frame_49 = QFrame(self.frame_9)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_49)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy)
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_60 = QGridLayout(self.frame_51)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_51)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout_60.addWidget(self.label_7, 0, 0, 1, 1)

        self.textEdit_3 = QTextEdit(self.frame_51)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setLayoutDirection(Qt.RightToLeft)
        self.textEdit_3.setOverwriteMode(False)

        self.gridLayout_60.addWidget(self.textEdit_3, 1, 0, 1, 1)


        self.gridLayout_36.addWidget(self.frame_51, 2, 0, 1, 1)

        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy)
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_50)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_44 = QLineEdit(self.frame_50)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        sizePolicy.setHeightForWidth(self.lineEdit_44.sizePolicy().hasHeightForWidth())
        self.lineEdit_44.setSizePolicy(sizePolicy)
        self.lineEdit_44.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.lineEdit_44, 5, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_50)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.lineEdit_6, 4, 0, 1, 1)

        self.lineEdit_37 = QLineEdit(self.frame_50)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        sizePolicy.setHeightForWidth(self.lineEdit_37.sizePolicy().hasHeightForWidth())
        self.lineEdit_37.setSizePolicy(sizePolicy)
        self.lineEdit_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.lineEdit_37, 0, 0, 1, 1)

        self.lineEdit_38 = QLineEdit(self.frame_50)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        sizePolicy.setHeightForWidth(self.lineEdit_38.sizePolicy().hasHeightForWidth())
        self.lineEdit_38.setSizePolicy(sizePolicy)
        self.lineEdit_38.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.lineEdit_38, 2, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_50)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.lineEdit_8, 3, 0, 1, 1)

        self.lineEdit_43 = QLineEdit(self.frame_50)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        sizePolicy.setHeightForWidth(self.lineEdit_43.sizePolicy().hasHeightForWidth())
        self.lineEdit_43.setSizePolicy(sizePolicy)
        self.lineEdit_43.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.lineEdit_43, 1, 0, 1, 1)

        self.lineEdit_45 = QLineEdit(self.frame_50)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        sizePolicy.setHeightForWidth(self.lineEdit_45.sizePolicy().hasHeightForWidth())
        self.lineEdit_45.setSizePolicy(sizePolicy)
        self.lineEdit_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.lineEdit_45, 6, 0, 1, 1)


        self.gridLayout_36.addWidget(self.frame_50, 0, 0, 1, 1)

        self.gridLayout_36.setRowStretch(0, 3)

        self.gridLayout_35.addWidget(self.frame_49, 0, 0, 2, 1)

        self.gridLayout_35.setRowStretch(0, 9)

        self.gridLayout_33.addWidget(self.frame_9, 0, 0, 3, 1)

        self.frame_8 = QFrame(self.tab_4)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_149 = QGridLayout(self.frame_8)
        self.gridLayout_149.setObjectName(u"gridLayout_149")
        self.gridLayout_149.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_11 = QPushButton(self.frame_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)

        self.gridLayout_149.addWidget(self.pushButton_11, 0, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.frame_8)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)

        self.gridLayout_149.addWidget(self.pushButton_21, 0, 1, 1, 1)


        self.gridLayout_33.addWidget(self.frame_8, 3, 0, 1, 1)

        self.gridLayout_33.setRowStretch(0, 1)
        self.gridLayout_33.setRowStretch(1, 8)
        self.gridLayout_33.setRowStretch(2, 1)
        self.gridLayout_33.setRowStretch(3, 1)
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_66 = QGridLayout(self.tab_8)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.tableWidget_3 = QTableWidget(self.tab_8)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setTabKeyNavigation(False)
        self.tableWidget_3.setShowGrid(True)
        self.tableWidget_3.setGridStyle(Qt.DashDotLine)
        self.tableWidget_3.setSortingEnabled(True)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)

        self.gridLayout_66.addWidget(self.tableWidget_3, 0, 0, 1, 1)

        self.gridLayout_66.setRowStretch(0, 1)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_42 = QGridLayout(self.tab_6)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.frame_52 = QFrame(self.tab_6)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy)
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_52)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(-1, -1, -1, 0)
        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_54)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.frame_54)
        self.frame_56.setObjectName(u"frame_56")
        sizePolicy.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy)
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.gridLayout_61 = QGridLayout(self.frame_56)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_56)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)

        self.gridLayout_61.addWidget(self.label_25, 0, 0, 1, 1)

        self.textEdit_4 = QTextEdit(self.frame_56)
        self.textEdit_4.setObjectName(u"textEdit_4")
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        self.textEdit_4.setLayoutDirection(Qt.RightToLeft)
        self.textEdit_4.setOverwriteMode(False)

        self.gridLayout_61.addWidget(self.textEdit_4, 1, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_56, 2, 0, 1, 1)

        self.frame_93 = QFrame(self.frame_54)
        self.frame_93.setObjectName(u"frame_93")
        sizePolicy.setHeightForWidth(self.frame_93.sizePolicy().hasHeightForWidth())
        self.frame_93.setSizePolicy(sizePolicy)
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_93)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_46 = QLineEdit(self.frame_93)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        sizePolicy.setHeightForWidth(self.lineEdit_46.sizePolicy().hasHeightForWidth())
        self.lineEdit_46.setSizePolicy(sizePolicy)
        self.lineEdit_46.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.lineEdit_46, 5, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.frame_93)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        sizePolicy.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy)
        self.lineEdit_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.lineEdit_17, 4, 0, 1, 1)

        self.lineEdit_47 = QLineEdit(self.frame_93)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        sizePolicy.setHeightForWidth(self.lineEdit_47.sizePolicy().hasHeightForWidth())
        self.lineEdit_47.setSizePolicy(sizePolicy)
        self.lineEdit_47.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.lineEdit_47, 0, 0, 1, 1)

        self.lineEdit_48 = QLineEdit(self.frame_93)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        sizePolicy.setHeightForWidth(self.lineEdit_48.sizePolicy().hasHeightForWidth())
        self.lineEdit_48.setSizePolicy(sizePolicy)
        self.lineEdit_48.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.lineEdit_48, 2, 0, 1, 1)

        self.lineEdit_49 = QLineEdit(self.frame_93)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        sizePolicy.setHeightForWidth(self.lineEdit_49.sizePolicy().hasHeightForWidth())
        self.lineEdit_49.setSizePolicy(sizePolicy)
        self.lineEdit_49.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.lineEdit_49, 3, 0, 1, 1)

        self.lineEdit_50 = QLineEdit(self.frame_93)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        sizePolicy.setHeightForWidth(self.lineEdit_50.sizePolicy().hasHeightForWidth())
        self.lineEdit_50.setSizePolicy(sizePolicy)
        self.lineEdit_50.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.lineEdit_50, 1, 0, 1, 1)

        self.lineEdit_51 = QLineEdit(self.frame_93)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        sizePolicy.setHeightForWidth(self.lineEdit_51.sizePolicy().hasHeightForWidth())
        self.lineEdit_51.setSizePolicy(sizePolicy)
        self.lineEdit_51.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.lineEdit_51, 6, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_93, 0, 0, 1, 1)

        self.gridLayout_39.setRowStretch(0, 3)

        self.gridLayout_38.addWidget(self.frame_54, 0, 0, 2, 1)

        self.gridLayout_38.setRowStretch(0, 9)

        self.gridLayout_42.addWidget(self.frame_52, 0, 0, 1, 1)

        self.pushButton_23 = QPushButton(self.tab_6)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)

        self.gridLayout_42.addWidget(self.pushButton_23, 1, 0, 1, 1)

        self.gridLayout_42.setRowStretch(0, 10)
        self.gridLayout_42.setRowStretch(1, 1)
        self.tabWidget_3.addTab(self.tab_6, "")

        self.gridLayout_87.addWidget(self.tabWidget_3, 1, 0, 1, 1)

        self.gridLayout_87.setRowStretch(0, 1)
        self.gridLayout_87.setRowStretch(1, 12)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_69 = QGridLayout(self.tab_9)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.frame_178 = QFrame(self.tab_9)
        self.frame_178.setObjectName(u"frame_178")
        sizePolicy.setHeightForWidth(self.frame_178.sizePolicy().hasHeightForWidth())
        self.frame_178.setSizePolicy(sizePolicy)
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.gridLayout_88 = QGridLayout(self.frame_178)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.gridLayout_88.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_8 = QPushButton(self.frame_178)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)

        self.gridLayout_88.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_26 = QPushButton(self.frame_178)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)

        self.gridLayout_88.addWidget(self.pushButton_26, 0, 0, 1, 1)


        self.gridLayout_69.addWidget(self.frame_178, 0, 0, 1, 1)

        self.tabWidget_4 = QTabWidget(self.tab_9)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        sizePolicy.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy)
        self.tabWidget_4.setLayoutDirection(Qt.RightToLeft)
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.frame_100 = QFrame(self.tab_10)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setGeometry(QRect(603, 130, 263, 40))
        self.frame_100.setLayoutDirection(Qt.LeftToRight)
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_100)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.comboBox_2 = QComboBox(self.frame_100)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_47.addWidget(self.comboBox_2, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_100)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_47.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_41 = QLabel(self.frame_100)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_47.addWidget(self.label_41, 0, 2, 1, 1)

        self.frame_101 = QFrame(self.tab_10)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setGeometry(QRect(540, 190, 387, 40))
        self.frame_101.setLayoutDirection(Qt.LeftToRight)
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.frame_101)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.lineEdit_53 = QLineEdit(self.frame_101)
        self.lineEdit_53.setObjectName(u"lineEdit_53")

        self.gridLayout_51.addWidget(self.lineEdit_53, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_101)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_51.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.frame_101)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_51.addWidget(self.comboBox_4, 0, 2, 1, 1)

        self.label_42 = QLabel(self.frame_101)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_51.addWidget(self.label_42, 0, 3, 1, 1)

        self.frame_102 = QFrame(self.tab_10)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setGeometry(QRect(610, 70, 198, 38))
        self.frame_102.setLayoutDirection(Qt.LeftToRight)
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.gridLayout_54 = QGridLayout(self.frame_102)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.lineEdit_52 = QLineEdit(self.frame_102)
        self.lineEdit_52.setObjectName(u"lineEdit_52")

        self.gridLayout_54.addWidget(self.lineEdit_52, 0, 0, 1, 1)

        self.label_31 = QLabel(self.frame_102)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_54.addWidget(self.label_31, 0, 1, 1, 1)

        self.frame_103 = QFrame(self.tab_10)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setGeometry(QRect(630, 250, 181, 38))
        self.frame_103.setLayoutDirection(Qt.LeftToRight)
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.gridLayout_55 = QGridLayout(self.frame_103)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.lineEdit_54 = QLineEdit(self.frame_103)
        self.lineEdit_54.setObjectName(u"lineEdit_54")

        self.gridLayout_55.addWidget(self.lineEdit_54, 0, 0, 1, 1)

        self.label_43 = QLabel(self.frame_103)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_55.addWidget(self.label_43, 0, 1, 1, 1)

        self.frame_104 = QFrame(self.tab_10)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setGeometry(QRect(640, 310, 181, 38))
        self.frame_104.setLayoutDirection(Qt.LeftToRight)
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.gridLayout_62 = QGridLayout(self.frame_104)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.lineEdit_55 = QLineEdit(self.frame_104)
        self.lineEdit_55.setObjectName(u"lineEdit_55")

        self.gridLayout_62.addWidget(self.lineEdit_55, 0, 0, 1, 1)

        self.label_44 = QLabel(self.frame_104)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_62.addWidget(self.label_44, 0, 1, 1, 1)

        self.tabWidget_4.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_67 = QGridLayout(self.tab_11)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.tableWidget_4 = QTableWidget(self.tab_11)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setTabKeyNavigation(False)
        self.tableWidget_4.setShowGrid(True)
        self.tableWidget_4.setGridStyle(Qt.DashDotLine)
        self.tableWidget_4.setSortingEnabled(True)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_4.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_4.verticalHeader().setStretchLastSection(False)

        self.gridLayout_67.addWidget(self.tableWidget_4, 0, 0, 1, 1)

        self.gridLayout_67.setRowStretch(0, 1)
        self.tabWidget_4.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_56 = QGridLayout(self.tab_12)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.tabWidget_4.addTab(self.tab_12, "")

        self.gridLayout_69.addWidget(self.tabWidget_4, 1, 0, 1, 1)

        self.gridLayout_69.setRowStretch(0, 1)
        self.gridLayout_69.setRowStretch(1, 10)
        self.tabWidget.addTab(self.tab_9, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638 \u0641\u064a \u0645\u0644\u0641", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062d", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"url", None));
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0633\u062c\u064a\u0644 \u062f\u062e\u0648\u0644", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0628\u062f\u0621 \u0645\u0646 ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0635\u0641\u062d", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0648\u0627\u0646\u064a \u0627\u0644\u0627\u0646\u062a\u0638\u0627\u0631", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0628\u062f\u0621", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0626\u0646\u0627\u0641", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0627\u064a\u0642\u0627\u0641 \u0645\u0624\u0642\u062a", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0642\u0641", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062e\u0637\u064a", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u064a\u0645\u064a\u0644 \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u064a\u0645\u064a\u0644 \u0627\u0644\u0645\u0631\u0633\u0644 \u0627\u0644\u064a\u0647", None))
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0633\u0631", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u064a\u0645\u064a\u0644 \u0627\u0644\u0645\u0631\u0633\u0644", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0633\u0631", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u064a\u0645\u064a\u0644 \u0627\u0644\u0645\u0631\u0633\u0644 \u0627\u0644\u064a\u0647", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0631\u0633\u0627\u0644 \u062a\u0644\u0642\u0627\u0626\u064a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u0633\u062d\u0628 \u0627\u0644\u0639\u0642\u0627\u0631\u0627\u062a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636 \u0627\u0644\u0643\u0644", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0627\u0644\u0639\u0631\u0636 \u0645\u0646 \u0631\u0627\u0628\u0637", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0627\u0644\u0639\u0631\u0648\u0636 \u0645\u0646 \u0645\u0644\u0641 ", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0647\u0627\u062a\u0641 \u0627\u0636\u0627\u0641\u064a", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0645\u0627\u0644\u0643 \u0627\u0644\u0639\u0642\u0627\u0631", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.lineEdit_40.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641\u064a \u0644\u0645\u0627\u0644\u0643 \u0627\u0644\u0639\u0642\u0627\u0631", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0648\u0635\u0641 \u0643\u0627\u0645\u0644:", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0633\u062a\u0646\u062f\u0627\u062a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0639\u0631\u0636", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0648\u0639 \u0627\u0644\u0639\u0642\u0627\u0631", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0645\u0631 \u0627\u0644\u0639\u0642\u0627\u0631", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0633\u0627\u062d\u0629", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0642\u0637\u0639\u0629", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0645\u062e\u0637\u0637", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0648\u0627\u062c\u0647\u0647", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636 \u0627\u0644\u0634\u0627\u0631\u0639", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0634\u0642\u0642", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0635\u0627\u0644\u0627\u062a", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0648\u0631\u0627\u0629 \u0627\u0644\u0645\u064a\u0627\u0629", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"\u063a\u0631\u0641\u0629 \u0633\u0627\u0626\u0642", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"\u063a\u0631\u0641\u0629 \u062e\u0627\u062f\u0645\u0629", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u0628\u062d", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u062e\u0644 \u0633\u064a\u0627\u0631\u0629", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0624\u062b\u062b\u0647", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0628", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0648\u0634", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0637\u0628\u062e", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0644\u062d\u0642", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"\u0642\u0628\u0648", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0635\u0639\u062f", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0628\u0644\u0643\u0633", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u0639\u0631 \u0627\u0644\u0627\u062c\u0645\u0627\u0644\u064a", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0641\u0627\u0635\u064a\u0644 \u0627\u0644\u0634\u0642\u0642 ", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u063a\u0631\u0641", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0635\u0627\u0644\u0627\u062a", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0648\u0631\u0627\u062a \u0627\u0644\u0645\u064a\u0627\u0629 ", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u062f\u062e\u0644", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0644 \u062a\u0642\u0628\u0644 \u0627\u0644\u0628\u0646\u0643", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0624\u062c\u0631\u0629", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0627\u0644\u0643 \u0633\u0627\u0643\u0646 \u0641\u064a\u0647\u0627", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0644\u064a\u0647\u0627 \u0631\u0647\u0646 \u0639\u0642\u0627\u0631\u064a", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"\u0643\u0645", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0628\u0627\u0626\u0639", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0628\u0627\u0626\u0639", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0647\u0627\u062a\u0641", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0639\u0642\u0627\u0631", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u0627\u0644\u0639\u0642\u0627\u0631", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0637\u0644\u0628", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u064a\u0644", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636 \u0627\u0644\u0643\u0644", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0639\u0631\u0636", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0648\u0639 \u0627\u0644\u0639\u0642\u0627\u0631", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0645\u0631 \u0627\u0644\u0639\u0642\u0627\u0631", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0633\u0627\u062d\u0629", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0642\u0637\u0639\u0629", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0645\u062e\u0637\u0637", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0648\u0627\u062c\u0647\u0647", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636 \u0627\u0644\u0634\u0627\u0631\u0639", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0634\u0642\u0642", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0635\u0627\u0644\u0627\u062a", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0648\u0631\u0627\u0629 \u0627\u0644\u0645\u064a\u0627\u0629", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"\u063a\u0631\u0641\u0629 \u0633\u0627\u0626\u0642", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"\u063a\u0631\u0641\u0629 \u062e\u0627\u062f\u0645\u0629", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u0628\u062d", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u062e\u0644 \u0633\u064a\u0627\u0631\u0629", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0624\u062b\u062b\u0647", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0628", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0648\u0634", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0637\u0628\u062e", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0644\u062d\u0642", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"\u0642\u0628\u0648", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0635\u0639\u062f", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0628\u0644\u0643\u0633", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u0639\u0631 \u0627\u0644\u0627\u062c\u0645\u0627\u0644\u064a", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0641\u0627\u0635\u064a\u0644 \u0627\u0644\u0634\u0642\u0642 ", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u063a\u0631\u0641", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0635\u0627\u0644\u0627\u062a", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0648\u0631\u0627\u062a \u0627\u0644\u0645\u064a\u0627\u0629 ", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u062f\u062e\u0644", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0644 \u062a\u0642\u0628\u0644 \u0627\u0644\u0628\u0646\u0643", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0624\u062c\u0631\u0629", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0627\u0644\u0643 \u0633\u0627\u0643\u0646 \u0641\u064a\u0647\u0627", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0644\u064a\u0647\u0627 \u0631\u0647\u0646 \u0639\u0642\u0627\u0631\u064a", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"\u0643\u0645", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0648\u0635\u0641 \u0643\u0627\u0645\u0644:", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_2.setPlaceholderText("")
        self.lineEdit_30.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0645\u0627\u0644\u0643 \u0627\u0644\u0639\u0642\u0627\u0631", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0645\u0627\u0644\u0643 \u0627\u0644\u0639\u0642\u0627\u0631:", None))
        self.lineEdit_31.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0647\u0627\u062a\u0641 \u0627\u0636\u0627\u0641\u064a:", None))
        self.lineEdit_32.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0647\u0627\u062a\u0641 \u0627\u0636\u0627\u0641\u064a", None))
        self.lineEdit_33.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a: ", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641\u064a", None))
        self.lineEdit_41.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641\u064a \u0644\u0645\u0627\u0644\u0643 \u0627\u0644\u0639\u0642\u0627\u0631", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0633\u062a\u0646\u062f\u0627\u062a", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0631\u0648\u0636", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636 \u0627\u0644\u0643\u0644", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0648\u0627\u0635\u0641\u0627\u062a \u0627\u062e\u0631\u0649", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_3.setPlaceholderText("")
        self.lineEdit_44.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062d\u064a \u0627\u0644\u0645\u0631\u063a\u0648\u0628 \u0627\u0644\u0639\u0645\u0644 \u0641\u064a\u0647 \u0648\u062a\u063a\u0637\u064a\u062a\u0647 \u0645\u064a\u062f\u0627\u0646\u064a\u0627", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.lineEdit_37.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u0648\u0642", None))
        self.lineEdit_38.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0647\u0627\u062a\u0641 \u0627\u0636\u0627\u0641\u064a", None))
        self.lineEdit_43.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u062c\u0644 \u0627\u0644\u0645\u062f\u0646\u064a \u0644\u0644\u0645\u0633\u0648\u0642", None))
        self.lineEdit_45.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0647\u0644 \u0633\u0628\u0642 \u0644\u0643 \u0627\u0644\u0639\u0645\u0644 \u0645\u064a\u062f\u0646\u064a\u0627 ", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0627\u0644\u0645\u0633\u0648\u0642\u064a\u0646 \u0645\u0646 \u0645\u0644\u0641 ", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0628\u0627\u0626\u0639", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0647\u0627\u062a\u0641", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u064a\u0644", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636 \u0627\u0644\u0643\u0644", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0648\u0627\u0635\u0641\u0627\u062a \u0627\u062e\u0631\u0649", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_4.setPlaceholderText("")
        self.lineEdit_46.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062d\u064a \u0627\u0644\u0645\u0631\u063a\u0648\u0628 \u0627\u0644\u0639\u0645\u0644 \u0641\u064a\u0647 \u0648\u062a\u063a\u0637\u064a\u062a\u0647 \u0645\u064a\u062f\u0627\u0646\u064a\u0627", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.lineEdit_47.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u0648\u0642", None))
        self.lineEdit_48.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.lineEdit_49.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0647\u0627\u062a\u0641 \u0627\u0636\u0627\u0641\u064a", None))
        self.lineEdit_50.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u062c\u0644 \u0627\u0644\u0645\u062f\u0646\u064a \u0644\u0644\u0645\u0633\u0648\u0642", None))
        self.lineEdit_51.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0647\u0644 \u0633\u0628\u0642 \u0644\u0643 \u0627\u0644\u0639\u0645\u0644 \u0645\u064a\u062f\u0646\u064a\u0627 ", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0633\u0648\u0642\u064a\u0646", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636 \u0627\u0644\u0643\u0644", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1- \u0641\u064a\u0644\u0627 \u0644\u0644\u0628\u064a\u0639", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"2-\u0634\u0642\u0647 \u0644\u0644\u0628\u064a\u0639.....", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0643\u0644 \u0627\u0644\u0639\u0631\u0648\u0636", None))

        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0639\u0631\u0636", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1- \u0639\u0645\u0627\u0631", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"2- \u0641\u0647\u062f", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645\u0627\u0621 \u0643\u0644 \u0627\u0644\u0645\u0633\u0648\u0642\u064a\u0646", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0627\u0631\u0642\u0627\u0645 \u0643\u0644 \u0627\u0644\u0645\u0633\u0648\u0642\u064a\u0646", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0645\u0633\u0648\u0642", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0645\u0634\u062a\u0631\u064a", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0644\u0627\u0642\u062a\u0643 \u0628\u0627\u0644\u0645\u0634\u062a\u0631\u064a", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0634\u0631\u0641 \u0627\u0644\u0645\u062f\u0646\u064a", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
        ___qtablewidgetitem16 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0628\u0627\u0626\u0639", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0647\u0627\u062a\u0641", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u064a\u0644", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None));
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636 \u0627\u0644\u0643\u0644", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a", None))
    # retranslateUi

