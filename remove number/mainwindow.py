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
        MainWindow.resize(1248, 706)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color: rgb(81, 216, 255);\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(244, 243, 242);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(244, 243, 242);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding:2px;\n"
"}\n"
"\n"
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
"QLabel{\n"
"    background: transparent;\n"
"    border:0;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    background: transparent;\n"
"    border:0;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.318, x2:1, y2:0.443409, stop:0 rgba(0, 59, 255, 255), stop:1 rgba(86, 227, 255, 255));\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    background: transparent;\n"
"\n"
"}\n"
"\n"
"QTextEdit{\n"
"background-col"
                        "or: rgb(244, 243, 242);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"gridline-color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"border : 1px solid white;\n"
"\n"
"paddingg: 3 3px;\n"
"}\n"
"QHeaderView::section{\n"
"border : 1px solid white;\n"
"background: transparent;\n"
"}\n"
"QTableWidget::item {\n"
" border -radius: 9px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"	background: transparent;\n"
"\n"
"}\n"
"QSpinBox{\n"
"background: transparent;\n"
"}\n"
"QRadioButton{\n"
"background: transparent;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)
        self.pushButton_7.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.pushButton_7, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 2, 1, 1, 1)

        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.gridLayout_6.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_5, 2, 2, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_4, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 3)

        self.tableWidget_3 = QTableWidget(self.frame_5)
        if (self.tableWidget_3.columnCount() < 1):
            self.tableWidget_3.setColumnCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_7.addWidget(self.tableWidget_3, 1, 0, 1, 3)


        self.gridLayout_6.addWidget(self.frame_5, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)

        self.tableWidget_2 = QTableWidget(self.frame_4)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_3.addWidget(self.tableWidget_2, 1, 0, 1, 2)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(0, 50))

        self.gridLayout_4.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setMinimumSize(QSize(0, 50))

        self.gridLayout_4.addWidget(self.pushButton_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_7, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_4, 0, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy6)
        self.pushButton_5.setMinimumSize(QSize(200, 50))

        self.gridLayout_5.addWidget(self.pushButton_5, 0, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy6.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy6)
        self.pushButton_6.setMinimumSize(QSize(200, 50))

        self.gridLayout_5.addWidget(self.pushButton_6, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_6, 3, 1, 1, 1, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1248, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0645\u0644\u0641", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062c", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0641 \u0645\u0633\u0627\u0631", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0644\u0641", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0645\u0648\u062f", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0627\u0631\u0642\u0627\u0645", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0644\u0641\u0627\u062a \u0627\u0644\u062a\u064a \u062a\u062d\u062a\u0648\u064a \u0639\u0644\u064a \u0627\u0644\u0627\u0631\u0642\u0627\u0645 \u0627\u0644\u0645\u0643\u0631\u0631\u0647", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0627\u0631\u0642\u0627\u0645:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0631\u0642\u0627\u0645 \u0627\u0644\u062c\u062f\u064a\u062f\u0629", None))
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0631\u0642\u0627\u0645", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0644\u0641\u0627\u062a \u0627\u0644\u0627\u0633\u0627\u0633\u064a\u0629", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0644\u0641", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0645\u0648\u062f", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0627\u0631\u0642\u0627\u0645", None));
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0645\u0644\u0641", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062c", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0628\u062f\u0621", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
    # retranslateUi

