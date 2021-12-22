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
#Scroll

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 715)
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

        self.gridLayout_24.addWidget(self.pushButton_17, 0, 2, 1, 1)

        self.pushButton_21 = QPushButton(self.frame_22)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy2.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy2)
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_24.addWidget(self.pushButton_21, 0, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_22)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy2.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy2)
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_24.addWidget(self.pushButton_18, 0, 3, 1, 1)


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

        self.lineEdit_208 = QLineEdit(self.frame_6)
        self.lineEdit_208.setObjectName(u"lineEdit_208")
        sizePolicy.setHeightForWidth(self.lineEdit_208.sizePolicy().hasHeightForWidth())
        self.lineEdit_208.setSizePolicy(sizePolicy)
        self.lineEdit_208.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_208, 3, 0, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_7, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_6, 2, 0, 1, 1)

        self.gridLayout_7.setRowStretch(0, 3)
        self.gridLayout_7.setRowStretch(1, 2)
        self.gridLayout_7.setRowStretch(2, 2)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 503, 1236))

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
        self.lineEdit_5 = QLineEdit(self.frame_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 4)

        self.vboxLayout.addWidget(self.frame_10)

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
        self.frame_52 = QFrame(self.tab_7)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_52)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_54)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, -1, 0, -1)
        self.lineEdit_17 = QLineEdit(self.frame_54)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        sizePolicy.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy)

        self.gridLayout_39.addWidget(self.lineEdit_17, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_54)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)

        self.gridLayout_39.addWidget(self.pushButton_9, 0, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_54)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_39.addWidget(self.comboBox_3, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.frame_54, 0, 0, 1, 2)

        self.frame_56 = QFrame(self.frame_52)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_56)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.comboBox_4 = QComboBox(self.frame_56)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)

        self.gridLayout_40.addWidget(self.comboBox_4, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.frame_56, 0, 2, 1, 1, Qt.AlignRight)


        self.gridLayout_16.addWidget(self.frame_52, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.tab_7)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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

        self.gridLayout_16.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.gridLayout_16.setRowStretch(0, 1)
        self.gridLayout_16.setRowStretch(1, 8)
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -668, 513, 1236))
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
        self.label_24 = QLabel(self.frame_92)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)

        self.gridLayout_46.addWidget(self.label_24, 0, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_92)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_46.addWidget(self.lineEdit_10, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_92)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_46.addWidget(self.lineEdit_8, 3, 0, 1, 1)

        self.label_25 = QLabel(self.frame_92)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)

        self.gridLayout_46.addWidget(self.label_25, 2, 0, 1, 1)


        self.gridLayout_44.addWidget(self.frame_92, 2, 0, 1, 1)

        self.gridLayout_44.setRowStretch(0, 3)
        self.gridLayout_44.setRowStretch(1, 2)
        self.gridLayout_44.setRowStretch(2, 2)

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
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638 \u0641\u064a \u0645\u0644\u0641", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0635\u0648\u0631", None))
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
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0644\u0627\u0633\u0645", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0628\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0628\u0627\u0626\u0639 ", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0639\u0631\u0636", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0643\u0644 \u0627\u0644\u0639\u0631\u0648\u0636", None))

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
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0631\u0636", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u064a\u0644", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None));
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
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0635\u0648\u0631", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0631\u0648\u0636", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

