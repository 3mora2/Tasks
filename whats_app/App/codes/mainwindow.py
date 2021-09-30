# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_ui 2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from . import qrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1044, 672)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(Qt.CustomContextMenu)
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.543, y2:0, stop:0.570115 rgba(0, 106, 177, 255), stop:1 rgba(251, 253, 254, 255));")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks | QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(0, 0, 0, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        palette = QPalette()
        brush = QBrush(QColor(192, 192, 192, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(232, 232, 232, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(238, 238, 238, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(110, 110, 110, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(147, 147, 147, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(61, 142, 201, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(128, 128, 128, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        brush10 = QBrush(QColor(221, 221, 221, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.tabWidget.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        # if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(u"")
        # endif // QT_CONFIG(tooltip)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QLineEdit{\n"
                                     "border-radius: 15px;\n"
                                     "border : 1px solid rgb(29, 29, 27);\n"
                                     "background-color: rgb(255, 255, 255, 0);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton{\n"
                                     "background-color: rgb(77, 137, 197);\n"
                                     "color: rgb(244, 243, 242);\n"
                                     "border-radius: 12px;\n"
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
                                     "   \n"
                                     "    border:0;\n"
                                     "	background-color: rgb(232, 232, 232);\n"
                                     "\n"
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
                                     "background-color: rgb(244, 243, 242);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "border-radius: 10px;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QTableWidget{\n"
                                     "gridline-color: #fffff8;\n"
                                     "\n"
                                     "background: transparent;\n"
                                     "border : 1px solid "
                                     "rgb(77, 137, 197);\n"
                                     "border-radius: 10px;\n"
                                     "paddingg: 3 3px;\n"
                                     "}\n"
                                     "QHeaderView::section{\n"
                                     " border-radius:7px;\n"
                                     " background-color: rgb(77, 137, 197);\n"
                                     "	color: rgb(244, 243, 242);\n"
                                     "}\n"
                                     "QTableWidget::item {\n"
                                     "border : 1px solid rgb(77, 137, 197);\n"
                                     "	\n"
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
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_3)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_4 = QLineEdit(self.frame_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Almarai")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setStyleSheet(u"")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_4.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.lineEdit_4, 0, 0, 1, 1)

        self.pushButton_49 = QPushButton(self.frame_6)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy)
        self.pushButton_49.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"Almarai")
        font2.setPointSize(17)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton_49.setFont(font2)
        self.pushButton_49.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_49.setMouseTracking(False)
        self.pushButton_49.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);\n"
                                         "color: rgb(0, 0, 0);")
        self.pushButton_49.setIconSize(QSize(283, 65))

        self.gridLayout_4.addWidget(self.pushButton_49, 0, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 12)
        self.gridLayout_4.setColumnStretch(1, 2)

        self.gridLayout_38.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_31 = QFrame(self.frame_3)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setMaximumSize(QSize(16777215, 16777215))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_31)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_5 = QLineEdit(self.frame_31)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_5.setFont(font1)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setInputMethodHints(Qt.ImhNone)

        self.gridLayout_5.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.label_18 = QLabel(self.frame_31)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMaximumSize(QSize(16777215, 16777215))
        self.label_18.setFont(font2)
        self.label_18.setLayoutDirection(Qt.LeftToRight)
        self.label_18.setStyleSheet(u"")
        self.label_18.setTextFormat(Qt.AutoText)

        self.gridLayout_5.addWidget(self.label_18, 0, 2, 1, 1)

        self.gridLayout_5.setColumnStretch(1, 10)
        self.gridLayout_5.setColumnStretch(2, 1)

        self.gridLayout_38.addWidget(self.frame_31, 2, 0, 1, 1)

        self.frame_32 = QFrame(self.frame_3)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy1)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_32)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.label_4 = QLabel(self.frame_32)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(15)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_39.addWidget(self.label_4, 0, 1, 1, 1)

        self.pushButton_57 = QPushButton(self.frame_32)
        self.pushButton_57.setObjectName(u"pushButton_57")
        sizePolicy.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy)
        self.pushButton_57.setMinimumSize(QSize(150, 70))
        font4 = QFont()
        font4.setPointSize(14)
        self.pushButton_57.setFont(font4)
        self.pushButton_57.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_57.setStyleSheet(u"background-color: rgb(80, 206, 86);\n"
                                         "color: rgb(247, 235, 245);\n"
                                         "border : 2px solid rgb(255, 255, 255);")

        self.gridLayout_39.addWidget(self.pushButton_57, 0, 0, 1, 1)

        self.gridLayout_38.addWidget(self.frame_32, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 102, 64);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_38.addWidget(self.label_3, 0, 0, 1, 1)

        self.gridLayout_38.setRowStretch(0, 4)
        self.gridLayout_38.setRowStretch(1, 1)
        self.gridLayout_38.setRowStretch(2, 1)
        self.gridLayout_38.setRowStretch(3, 1)
        self.gridLayout_38.setRowMinimumHeight(0, 10)

        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_9 = QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_8 = QFrame(self.tab_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_8)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_33)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_34)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setVerticalSpacing(0)
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.frame_34)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"Almarai")
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setWeight(50)
        self.pushButton_14.setFont(font5)
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setIconSize(QSize(200, 50))

        self.gridLayout_41.addWidget(self.pushButton_14, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_34)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_9.setFont(font5)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setIconSize(QSize(200, 50))

        self.gridLayout_41.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.gridLayout_40.addWidget(self.frame_34, 2, 0, 1, 1)

        self.textEdit_3 = QTextEdit(self.frame_33)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMinimumSize(QSize(0, 0))
        self.textEdit_3.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(11)
        self.textEdit_3.setFont(font6)

        self.gridLayout_40.addWidget(self.textEdit_3, 3, 0, 1, 2)

        self.tableWidget_2 = QTableWidget(self.frame_33)
        if (self.tableWidget_2.columnCount() < 1):
            self.tableWidget_2.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setTextElideMode(Qt.ElideRight)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)

        self.gridLayout_40.addWidget(self.tableWidget_2, 1, 0, 1, 2)

        self.frame_38 = QFrame(self.frame_33)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_38)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.pushButton_42 = QPushButton(self.frame_38)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        self.pushButton_42.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_42.setFont(font5)
        self.pushButton_42.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_42.setIconSize(QSize(200, 50))

        self.gridLayout_44.addWidget(self.pushButton_42, 0, 0, 1, 1)

        self.pushButton_43 = QPushButton(self.frame_38)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy)
        self.pushButton_43.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_43.setFont(font5)
        self.pushButton_43.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_43.setIconSize(QSize(200, 50))

        self.gridLayout_44.addWidget(self.pushButton_43, 0, 1, 1, 1)

        self.gridLayout_40.addWidget(self.frame_38, 4, 0, 1, 1)

        self.label_8 = QLabel(self.frame_33)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamily(u"Almarai")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_8.setFont(font7)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.label_8, 0, 0, 1, 2)

        self.gridLayout_40.setRowStretch(1, 8)
        self.gridLayout_40.setRowStretch(2, 2)
        self.gridLayout_40.setRowStretch(3, 8)
        self.gridLayout_40.setRowStretch(4, 2)

        self.gridLayout_6.addWidget(self.frame_33, 1, 0, 3, 1)

        self.frame_39 = QFrame(self.frame_8)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_39)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.pushButton_23 = QPushButton(self.frame_39)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_23.setFont(font5)
        self.pushButton_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_23.setIconSize(QSize(200, 50))

        self.gridLayout_45.addWidget(self.pushButton_23, 2, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_39)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_13.setFont(font5)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setIconSize(QSize(200, 50))

        self.gridLayout_45.addWidget(self.pushButton_13, 2, 1, 1, 1)

        self.tableWidget_8 = QTableWidget(self.frame_39)
        if (self.tableWidget_8.columnCount() < 1):
            self.tableWidget_8.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        sizePolicy.setHeightForWidth(self.tableWidget_8.sizePolicy().hasHeightForWidth())
        self.tableWidget_8.setSizePolicy(sizePolicy)
        self.tableWidget_8.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_8.setAutoFillBackground(False)
        self.tableWidget_8.setStyleSheet(u"")
        self.tableWidget_8.setTextElideMode(Qt.ElideRight)
        self.tableWidget_8.setSortingEnabled(False)
        self.tableWidget_8.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_8.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_45.addWidget(self.tableWidget_8, 1, 0, 1, 2)

        self.label_9 = QLabel(self.frame_39)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setFont(font7)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.label_9, 0, 0, 1, 2)

        self.gridLayout_45.setRowStretch(1, 10)
        self.gridLayout_45.setRowStretch(2, 1)

        self.gridLayout_6.addWidget(self.frame_39, 1, 1, 3, 1)

        self.frame_40 = QFrame(self.frame_8)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_40)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_9 = QTableWidget(self.frame_40)
        if (self.tableWidget_9.columnCount() < 1):
            self.tableWidget_9.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.tableWidget_9.setObjectName(u"tableWidget_9")
        sizePolicy.setHeightForWidth(self.tableWidget_9.sizePolicy().hasHeightForWidth())
        self.tableWidget_9.setSizePolicy(sizePolicy)
        self.tableWidget_9.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_9.setAutoFillBackground(False)
        self.tableWidget_9.setTextElideMode(Qt.ElideRight)
        self.tableWidget_9.horizontalHeader().setStretchLastSection(False)

        self.gridLayout_46.addWidget(self.tableWidget_9, 1, 0, 1, 2)

        self.label_10 = QLabel(self.frame_40)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        self.label_10.setFont(font7)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_46.addWidget(self.label_10, 0, 0, 1, 2)

        self.pushButton_36 = QPushButton(self.frame_40)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy)
        self.pushButton_36.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_36.setFont(font5)
        self.pushButton_36.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_36.setIconSize(QSize(200, 50))

        self.gridLayout_46.addWidget(self.pushButton_36, 2, 1, 2, 1)

        self.pushButton_37 = QPushButton(self.frame_40)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy)
        self.pushButton_37.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_37.setFont(font5)
        self.pushButton_37.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_37.setIconSize(QSize(200, 50))

        self.gridLayout_46.addWidget(self.pushButton_37, 2, 0, 2, 1)

        self.gridLayout_46.setRowStretch(1, 10)
        self.gridLayout_46.setRowStretch(2, 1)

        self.gridLayout_6.addWidget(self.frame_40, 1, 2, 3, 3)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(2, 1)

        self.gridLayout_9.addWidget(self.frame_8, 0, 0, 3, 1)

        self.frame_7 = QFrame(self.tab_2)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 30, 0, 40)
        self.frame_35 = QFrame(self.frame_7)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_35)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setHorizontalSpacing(0)
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.frame_35)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setFont(font6)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_42.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.label_16 = QLabel(self.frame_35)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMaximumSize(QSize(16777215, 16777215))
        self.label_16.setFont(font7)

        self.gridLayout_42.addWidget(self.label_16, 0, 1, 1, 1)

        self.pushButton_46 = QPushButton(self.frame_35)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy)
        self.pushButton_46.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamily(u"Almarai")
        font8.setPointSize(8)
        font8.setBold(False)
        font8.setWeight(50)
        self.pushButton_46.setFont(font8)
        self.pushButton_46.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_42.addWidget(self.pushButton_46, 1, 0, 1, 2)

        self.gridLayout_7.addWidget(self.frame_35, 6, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_7)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_12.setFont(font5)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setIconSize(QSize(200, 50))

        self.gridLayout_7.addWidget(self.pushButton_12, 5, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.frame_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_10.setFont(font5)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setIconSize(QSize(200, 50))

        self.gridLayout_7.addWidget(self.pushButton_10, 3, 0, 1, 2)

        self.pushButton_11 = QPushButton(self.frame_7)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_11.setFont(font5)
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setIconSize(QSize(200, 50))

        self.gridLayout_7.addWidget(self.pushButton_11, 4, 0, 1, 2)

        self.pushButton_7 = QPushButton(self.frame_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_7.setFont(font5)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setIconSize(QSize(200, 50))

        self.gridLayout_7.addWidget(self.pushButton_7, 2, 0, 1, 2)

        self.spinBox_5 = QSpinBox(self.frame_7)
        self.spinBox_5.setObjectName(u"spinBox_5")
        sizePolicy.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.spinBox_5, 1, 0, 1, 1)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.label_14, 0, 0, 1, 1)

        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setRowStretch(2, 1)
        self.gridLayout_7.setRowStretch(3, 1)
        self.gridLayout_7.setRowStretch(4, 1)
        self.gridLayout_7.setRowStretch(5, 1)
        self.gridLayout_7.setRowStretch(6, 2)

        self.gridLayout_9.addWidget(self.frame_7, 1, 1, 1, 1)

        self.gridLayout_9.setColumnStretch(0, 12)
        self.gridLayout_9.setColumnStretch(1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_11 = QFrame(self.tab_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_11)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.tableWidget_6 = QTableWidget(self.frame_11)
        if (self.tableWidget_6.columnCount() < 2):
            self.tableWidget_6.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        sizePolicy.setHeightForWidth(self.tableWidget_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_6.setSizePolicy(sizePolicy)
        self.tableWidget_6.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget_6.setAutoFillBackground(False)
        self.tableWidget_6.setTextElideMode(Qt.ElideRight)

        self.gridLayout_10.addWidget(self.tableWidget_6, 0, 0, 2, 2)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_13)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_34 = QPushButton(self.frame_13)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy)
        self.pushButton_34.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_34.setFont(font7)
        self.pushButton_34.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_34.setIconSize(QSize(200, 50))

        self.gridLayout_14.addWidget(self.pushButton_34, 0, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.frame_13)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        self.pushButton_29.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_29.setFont(font7)
        self.pushButton_29.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_29.setIconSize(QSize(200, 50))

        self.gridLayout_14.addWidget(self.pushButton_29, 0, 1, 1, 1)

        self.gridLayout_10.addWidget(self.frame_13, 2, 0, 1, 2)

        self.gridLayout_10.setRowStretch(0, 8)
        self.gridLayout_10.setRowStretch(2, 1)

        self.gridLayout_8.addWidget(self.frame_11, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.tab_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 60, 0, 60)
        self.pushButton_33 = QPushButton(self.frame_10)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        self.pushButton_33.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_33.setFont(font7)
        self.pushButton_33.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_33.setIconSize(QSize(200, 50))

        self.gridLayout_12.addWidget(self.pushButton_33, 6, 0, 1, 2)

        self.pushButton_35 = QPushButton(self.frame_10)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy)
        self.pushButton_35.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_35.setFont(font7)
        self.pushButton_35.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_35.setIconSize(QSize(200, 50))

        self.gridLayout_12.addWidget(self.pushButton_35, 7, 0, 1, 2)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setFont(font7)

        self.gridLayout_12.addWidget(self.label_6, 0, 0, 1, 2)

        self.label_20 = QLabel(self.frame_10)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMaximumSize(QSize(16777215, 16777215))
        self.label_20.setFont(font7)

        self.gridLayout_12.addWidget(self.label_20, 1, 0, 1, 1, Qt.AlignRight)

        self.pushButton_30 = QPushButton(self.frame_10)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)
        self.pushButton_30.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_30.setFont(font7)
        self.pushButton_30.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_30.setIconSize(QSize(200, 50))

        self.gridLayout_12.addWidget(self.pushButton_30, 4, 0, 1, 2)

        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMaximumSize(QSize(16777215, 16777215))
        self.label_19.setFont(font7)

        self.gridLayout_12.addWidget(self.label_19, 1, 1, 1, 1, Qt.AlignRight)

        self.spinBox = QSpinBox(self.frame_10)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_12.addWidget(self.spinBox, 2, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.frame_10)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        self.spinBox_3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_12.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.pushButton_31 = QPushButton(self.frame_10)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy)
        self.pushButton_31.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_31.setFont(font7)
        self.pushButton_31.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_31.setIconSize(QSize(200, 50))

        self.gridLayout_12.addWidget(self.pushButton_31, 5, 0, 1, 2)

        self.gridLayout_12.setRowStretch(0, 2)
        self.gridLayout_12.setRowStretch(1, 2)
        self.gridLayout_12.setRowStretch(2, 2)
        self.gridLayout_12.setRowStretch(3, 2)
        self.gridLayout_12.setRowStretch(4, 6)
        self.gridLayout_12.setRowStretch(5, 6)
        self.gridLayout_12.setRowStretch(6, 6)
        self.gridLayout_12.setRowStretch(7, 6)

        self.gridLayout_8.addWidget(self.frame_10, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.tab_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.radioButton_4 = QRadioButton(self.frame_9)
        self.radioButton_4.setObjectName(u"radioButton_4")
        sizePolicy.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy)
        self.radioButton_4.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setPointSize(9)
        self.radioButton_4.setFont(font9)
        self.radioButton_4.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_11.addWidget(self.radioButton_4, 0, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.frame_9)
        self.radioButton_3.setObjectName(u"radioButton_3")
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        self.radioButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_3.setFont(font9)
        self.radioButton_3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_11.addWidget(self.radioButton_3, 0, 1, 1, 1)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButton_32 = QPushButton(self.frame_12)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy)
        self.pushButton_32.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_32.setFont(font7)
        self.pushButton_32.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_32.setIconSize(QSize(200, 50))

        self.gridLayout_13.addWidget(self.pushButton_32, 0, 0, 1, 1)

        self.pushButton_28 = QPushButton(self.frame_12)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        self.pushButton_28.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_28.setFont(font7)
        self.pushButton_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_28.setIconSize(QSize(200, 50))

        self.gridLayout_13.addWidget(self.pushButton_28, 0, 1, 1, 1)

        self.gridLayout_11.addWidget(self.frame_12, 2, 0, 1, 2)

        self.textEdit_2 = QTextEdit(self.frame_9)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_2.setFont(font6)
        self.textEdit_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_11.addWidget(self.textEdit_2, 1, 0, 1, 2)

        self.tableWidget_7 = QTableWidget(self.frame_9)
        if (self.tableWidget_7.columnCount() < 4):
            self.tableWidget_7.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        sizePolicy.setHeightForWidth(self.tableWidget_7.sizePolicy().hasHeightForWidth())
        self.tableWidget_7.setSizePolicy(sizePolicy)
        self.tableWidget_7.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget_7.setAutoFillBackground(False)
        self.tableWidget_7.setStyleSheet(u"QPushButton{\n"
                                         "    background: transparent;\n"
                                         "	color: rgb(0, 0, 0);\n"
                                         "}")
        self.tableWidget_7.setTextElideMode(Qt.ElideRight)

        self.gridLayout_11.addWidget(self.tableWidget_7, 3, 0, 1, 2)

        self.gridLayout_11.setRowStretch(0, 1)
        self.gridLayout_11.setRowStretch(1, 6)
        self.gridLayout_11.setRowStretch(2, 2)
        self.gridLayout_11.setRowStretch(3, 10)

        self.gridLayout_8.addWidget(self.frame_9, 0, 2, 1, 1)

        self.gridLayout_8.setColumnStretch(0, 5)
        self.gridLayout_8.setColumnStretch(1, 2)
        self.gridLayout_8.setColumnStretch(2, 5)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_15 = QGridLayout(self.tab_7)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_16 = QFrame(self.tab_7)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_16)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMaximumSize(QSize(16777215, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_17)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.frame_17)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setFont(font7)
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_18.setIconSize(QSize(200, 50))

        self.gridLayout_19.addWidget(self.pushButton_18, 0, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.frame_17)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setFont(font7)
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_19.setIconSize(QSize(200, 50))

        self.gridLayout_19.addWidget(self.pushButton_19, 0, 1, 1, 1)

        self.gridLayout_18.addWidget(self.frame_17, 1, 0, 1, 1)

        self.tableWidget_3 = QTableWidget(self.frame_16)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_3.setAutoFillBackground(False)
        self.tableWidget_3.setTextElideMode(Qt.ElideRight)

        self.gridLayout_18.addWidget(self.tableWidget_3, 0, 0, 1, 2)

        self.gridLayout_18.setRowStretch(0, 8)
        self.gridLayout_18.setRowStretch(1, 1)

        self.gridLayout_15.addWidget(self.frame_16, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.tab_7)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMaximumSize(QSize(16777215, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_15)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 60, 0, 60)
        self.spinBox_2 = QSpinBox(self.frame_15)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.spinBox_2, 2, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.frame_15)
        self.spinBox_4.setObjectName(u"spinBox_4")
        sizePolicy.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy)
        self.spinBox_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.spinBox_4, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font7)

        self.gridLayout_16.addWidget(self.label_7, 0, 0, 1, 2)

        self.pushButton_17 = QPushButton(self.frame_15)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_17.setFont(font7)
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_17.setIconSize(QSize(200, 50))

        self.gridLayout_16.addWidget(self.pushButton_17, 5, 0, 1, 2)

        self.label_21 = QLabel(self.frame_15)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMaximumSize(QSize(16777215, 16777215))
        self.label_21.setFont(font7)

        self.gridLayout_16.addWidget(self.label_21, 1, 0, 1, 1, Qt.AlignRight)

        self.pushButton_15 = QPushButton(self.frame_15)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_15.setFont(font7)
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setIconSize(QSize(200, 50))

        self.gridLayout_16.addWidget(self.pushButton_15, 4, 0, 1, 2)

        self.label_22 = QLabel(self.frame_15)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMaximumSize(QSize(16777215, 16777215))
        self.label_22.setFont(font7)

        self.gridLayout_16.addWidget(self.label_22, 1, 1, 1, 1, Qt.AlignRight)

        self.pushButton_21 = QPushButton(self.frame_15)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_21.setFont(font7)
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_21.setIconSize(QSize(200, 50))

        self.gridLayout_16.addWidget(self.pushButton_21, 7, 0, 1, 2)

        self.pushButton_16 = QPushButton(self.frame_15)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_16.setFont(font7)
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setIconSize(QSize(200, 50))

        self.gridLayout_16.addWidget(self.pushButton_16, 6, 0, 1, 2)

        self.frame_37 = QFrame(self.frame_15)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.gridLayout_16.addWidget(self.frame_37, 3, 0, 1, 2)

        self.gridLayout_16.setRowStretch(0, 2)
        self.gridLayout_16.setRowStretch(1, 2)
        self.gridLayout_16.setRowStretch(2, 2)
        self.gridLayout_16.setRowStretch(3, 2)
        self.gridLayout_16.setRowStretch(4, 6)
        self.gridLayout_16.setRowStretch(5, 6)
        self.gridLayout_16.setRowStretch(6, 6)
        self.gridLayout_16.setRowStretch(7, 6)

        self.gridLayout_15.addWidget(self.frame_15, 0, 1, 1, 1)

        self.frame_14 = QFrame(self.tab_7)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_14)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.radioButton = QRadioButton(self.frame_14)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton.setFont(font9)
        self.radioButton.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.frame_14)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_2.setFont(font9)
        self.radioButton_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton_2, 0, 1, 1, 1)

        self.tableWidget_4 = QTableWidget(self.frame_14)
        if (self.tableWidget_4.columnCount() < 4):
            self.tableWidget_4.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget_4.setAutoFillBackground(False)
        self.tableWidget_4.setStyleSheet(u"QPushButton{\n"
                                         "    background: transparent;\n"
                                         "	color: rgb(0, 0, 0);\n"
                                         "}")
        self.tableWidget_4.setTextElideMode(Qt.ElideRight)

        self.gridLayout_17.addWidget(self.tableWidget_4, 3, 0, 1, 2)

        self.textEdit = QTextEdit(self.frame_14)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        font10 = QFont()
        font10.setPointSize(10)
        self.textEdit.setFont(font10)
        self.textEdit.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.textEdit, 1, 0, 1, 2)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_18)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton_22 = QPushButton(self.frame_18)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setFont(font7)
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_22.setIconSize(QSize(200, 50))

        self.gridLayout_20.addWidget(self.pushButton_22, 0, 0, 1, 1)

        self.pushButton_20 = QPushButton(self.frame_18)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setFont(font7)
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_20.setIconSize(QSize(200, 50))

        self.gridLayout_20.addWidget(self.pushButton_20, 0, 1, 1, 1)

        self.gridLayout_17.addWidget(self.frame_18, 2, 0, 1, 2)

        self.gridLayout_17.setRowStretch(0, 1)
        self.gridLayout_17.setRowStretch(1, 6)
        self.gridLayout_17.setRowStretch(2, 2)
        self.gridLayout_17.setRowStretch(3, 10)

        self.gridLayout_15.addWidget(self.frame_14, 0, 2, 1, 1)

        self.gridLayout_15.setColumnStretch(0, 5)
        self.gridLayout_15.setColumnStretch(1, 2)
        self.gridLayout_15.setColumnStretch(2, 5)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_21 = QGridLayout(self.tab_4)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_20 = QFrame(self.tab_4)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_20)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tableWidget = QTableWidget(self.frame_20)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setTextElideMode(Qt.ElideRight)

        self.gridLayout_22.addWidget(self.tableWidget, 0, 0, 2, 2)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 60))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_21)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.pushButton_44 = QPushButton(self.frame_21)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy)
        self.pushButton_44.setFont(font7)
        self.pushButton_44.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_44.setIconSize(QSize(200, 50))

        self.gridLayout_24.addWidget(self.pushButton_44, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_21)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setFont(font7)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setIconSize(QSize(200, 50))

        self.gridLayout_24.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.gridLayout_22.addWidget(self.frame_21, 2, 0, 1, 1)

        self.gridLayout_21.addWidget(self.frame_20, 0, 0, 2, 1)

        self.frame_19 = QFrame(self.tab_4)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMaximumSize(QSize(250, 16777215))
        self.frame_19.setFont(font10)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_19)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.pushButton_6 = QPushButton(self.frame_19)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QSize(16777215, 50))
        self.pushButton_6.setFont(font7)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setIconSize(QSize(200, 50))

        self.gridLayout_23.addWidget(self.pushButton_6, 0, 1, 1, 1)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMaximumSize(QSize(200, 130))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_22)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.lineEdit = QLineEdit(self.frame_22)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QSize(16777215, 50))
        self.lineEdit.setFont(font10)

        self.gridLayout_25.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.label_15 = QLabel(self.frame_22)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMaximumSize(QSize(16777215, 50))
        self.label_15.setFont(font7)

        self.gridLayout_25.addWidget(self.label_15, 0, 1, 1, 1)

        self.pushButton_45 = QPushButton(self.frame_22)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy)
        self.pushButton_45.setMaximumSize(QSize(16777215, 70))
        self.pushButton_45.setFont(font5)
        self.pushButton_45.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_45.setIconSize(QSize(200, 50))

        self.gridLayout_25.addWidget(self.pushButton_45, 1, 0, 1, 2)

        self.gridLayout_23.addWidget(self.frame_22, 1, 1, 1, 1)

        self.gridLayout_21.addWidget(self.frame_19, 0, 1, 2, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_26 = QGridLayout(self.tab_5)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.frame_24 = QFrame(self.tab_5)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_24)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMaximumSize(QSize(16777215, 16777215))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_25)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.pushButton_26 = QPushButton(self.frame_25)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setFont(font7)
        self.pushButton_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_26.setIconSize(QSize(200, 50))

        self.gridLayout_29.addWidget(self.pushButton_26, 0, 0, 1, 1)

        self.pushButton_41 = QPushButton(self.frame_25)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy)
        self.pushButton_41.setFont(font7)
        self.pushButton_41.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_41.setIconSize(QSize(200, 50))

        self.gridLayout_29.addWidget(self.pushButton_41, 0, 2, 1, 1)

        self.pushButton_27 = QPushButton(self.frame_25)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        self.pushButton_27.setFont(font7)
        self.pushButton_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_27.setIconSize(QSize(200, 50))

        self.gridLayout_29.addWidget(self.pushButton_27, 0, 1, 1, 1)

        self.pushButton_40 = QPushButton(self.frame_25)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy)
        self.pushButton_40.setFont(font7)
        self.pushButton_40.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_40.setIconSize(QSize(200, 50))

        self.gridLayout_29.addWidget(self.pushButton_40, 0, 3, 1, 1)

        self.pushButton_38 = QPushButton(self.frame_25)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy)
        self.pushButton_38.setFont(font7)
        self.pushButton_38.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_38.setIconSize(QSize(200, 50))

        self.gridLayout_29.addWidget(self.pushButton_38, 0, 5, 1, 1)

        self.pushButton_39 = QPushButton(self.frame_25)
        self.pushButton_39.setObjectName(u"pushButton_39")
        sizePolicy.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy)
        self.pushButton_39.setFont(font7)
        self.pushButton_39.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_39.setIconSize(QSize(200, 50))

        self.gridLayout_29.addWidget(self.pushButton_39, 0, 4, 1, 1)

        self.gridLayout_27.addWidget(self.frame_25, 1, 0, 1, 2)

        self.frame_36 = QFrame(self.frame_24)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_36)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_36)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QSize(16777215, 40))
        self.label_11.setFont(font7)
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.frame_36)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QSize(16777215, 40))
        self.label_12.setFont(font7)
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_13 = QLabel(self.frame_36)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QSize(16777215, 40))
        self.label_13.setFont(font7)
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.label_13, 0, 2, 1, 1)

        self.tableWidget_5 = QTableWidget(self.frame_36)
        if (self.tableWidget_5.columnCount() < 1):
            self.tableWidget_5.setColumnCount(1)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        sizePolicy.setHeightForWidth(self.tableWidget_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_5.setSizePolicy(sizePolicy)
        self.tableWidget_5.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget_5.setAutoFillBackground(False)
        self.tableWidget_5.setTextElideMode(Qt.ElideRight)

        self.gridLayout_43.addWidget(self.tableWidget_5, 1, 0, 1, 1)

        self.tableWidget_11 = QTableWidget(self.frame_36)
        if (self.tableWidget_11.columnCount() < 1):
            self.tableWidget_11.setColumnCount(1)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        self.tableWidget_11.setObjectName(u"tableWidget_11")
        sizePolicy.setHeightForWidth(self.tableWidget_11.sizePolicy().hasHeightForWidth())
        self.tableWidget_11.setSizePolicy(sizePolicy)
        self.tableWidget_11.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget_11.setAutoFillBackground(False)
        self.tableWidget_11.setTextElideMode(Qt.ElideRight)

        self.gridLayout_43.addWidget(self.tableWidget_11, 1, 1, 1, 1)

        self.tableWidget_10 = QTableWidget(self.frame_36)
        if (self.tableWidget_10.columnCount() < 1):
            self.tableWidget_10.setColumnCount(1)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        self.tableWidget_10.setObjectName(u"tableWidget_10")
        sizePolicy.setHeightForWidth(self.tableWidget_10.sizePolicy().hasHeightForWidth())
        self.tableWidget_10.setSizePolicy(sizePolicy)
        self.tableWidget_10.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_10.setAutoFillBackground(False)
        self.tableWidget_10.setTextElideMode(Qt.ElideRight)

        self.gridLayout_43.addWidget(self.tableWidget_10, 1, 2, 1, 1)

        self.gridLayout_43.setRowStretch(0, 1)
        self.gridLayout_43.setRowStretch(1, 8)

        self.gridLayout_27.addWidget(self.frame_36, 0, 0, 1, 1)

        self.gridLayout_27.setRowStretch(0, 5)
        self.gridLayout_27.setRowStretch(1, 1)

        self.gridLayout_26.addWidget(self.frame_24, 0, 0, 1, 1)

        self.frame_23 = QFrame(self.tab_5)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_23)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.pushButton_25 = QPushButton(self.frame_23)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.pushButton_25.setMaximumSize(QSize(16777215, 60))
        self.pushButton_25.setFont(font7)
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_25.setIconSize(QSize(200, 50))

        self.gridLayout_28.addWidget(self.pushButton_25, 0, 0, 1, 2)

        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMaximumSize(QSize(200, 120))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_26)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_26)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setFont(font10)

        self.gridLayout_30.addWidget(self.lineEdit_3, 0, 0, 1, 1)

        self.label_17 = QLabel(self.frame_26)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setFont(font7)

        self.gridLayout_30.addWidget(self.label_17, 0, 1, 1, 1)

        self.pushButton_47 = QPushButton(self.frame_26)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy)
        self.pushButton_47.setFont(font5)
        self.pushButton_47.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_47.setIconSize(QSize(200, 50))

        self.gridLayout_30.addWidget(self.pushButton_47, 1, 0, 1, 2)

        self.gridLayout_28.addWidget(self.frame_26, 2, 0, 1, 1)

        self.pushButton_58 = QPushButton(self.frame_23)
        self.pushButton_58.setObjectName(u"pushButton_58")
        sizePolicy.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy)
        self.pushButton_58.setMaximumSize(QSize(16777215, 60))
        font11 = QFont()
        font11.setFamily(u"Almarai")
        font11.setPointSize(10)
        self.pushButton_58.setFont(font11)

        self.gridLayout_28.addWidget(self.pushButton_58, 1, 0, 1, 1)

        self.gridLayout_26.addWidget(self.frame_23, 0, 1, 1, 1)

        self.gridLayout_26.setColumnStretch(0, 5)
        self.gridLayout_26.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_35 = QGridLayout(self.tab_6)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.frame_28 = QFrame(self.tab_6)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_28)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.tableWidget_12 = QTableWidget(self.frame_28)
        if (self.tableWidget_12.columnCount() < 2):
            self.tableWidget_12.setColumnCount(2)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        self.tableWidget_12.setObjectName(u"tableWidget_12")
        sizePolicy.setHeightForWidth(self.tableWidget_12.sizePolicy().hasHeightForWidth())
        self.tableWidget_12.setSizePolicy(sizePolicy)
        self.tableWidget_12.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget_12.setAutoFillBackground(False)
        self.tableWidget_12.setTextElideMode(Qt.ElideRight)

        self.gridLayout_32.addWidget(self.tableWidget_12, 2, 0, 1, 1)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_29)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setHorizontalSpacing(20)
        self.gridLayout_33.setContentsMargins(30, -1, 30, -1)
        self.pushButton_50 = QPushButton(self.frame_29)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy)
        self.pushButton_50.setMaximumSize(QSize(16777215, 70))
        self.pushButton_50.setFont(font7)
        self.pushButton_50.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_50.setIconSize(QSize(200, 50))

        self.gridLayout_33.addWidget(self.pushButton_50, 0, 0, 1, 1)

        self.pushButton_51 = QPushButton(self.frame_29)
        self.pushButton_51.setObjectName(u"pushButton_51")
        sizePolicy.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy)
        self.pushButton_51.setMaximumSize(QSize(16777215, 70))
        self.pushButton_51.setFont(font7)
        self.pushButton_51.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_51.setIconSize(QSize(200, 50))

        self.gridLayout_33.addWidget(self.pushButton_51, 0, 1, 1, 1)

        self.gridLayout_32.addWidget(self.frame_29, 3, 0, 1, 1)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_30)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(-1, 50, -1, 50)
        self.pushButton_53 = QPushButton(self.frame_30)
        self.pushButton_53.setObjectName(u"pushButton_53")
        sizePolicy.setHeightForWidth(self.pushButton_53.sizePolicy().hasHeightForWidth())
        self.pushButton_53.setSizePolicy(sizePolicy)
        self.pushButton_53.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_53.setFont(font7)
        self.pushButton_53.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_53.setIconSize(QSize(200, 50))

        self.gridLayout_34.addWidget(self.pushButton_53, 1, 0, 1, 1)

        self.pushButton_54 = QPushButton(self.frame_30)
        self.pushButton_54.setObjectName(u"pushButton_54")
        sizePolicy.setHeightForWidth(self.pushButton_54.sizePolicy().hasHeightForWidth())
        self.pushButton_54.setSizePolicy(sizePolicy)
        self.pushButton_54.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_54.setFont(font7)
        self.pushButton_54.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_54.setIconSize(QSize(200, 50))

        self.gridLayout_34.addWidget(self.pushButton_54, 2, 0, 1, 1)

        self.pushButton_52 = QPushButton(self.frame_30)
        self.pushButton_52.setObjectName(u"pushButton_52")
        sizePolicy.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy)
        self.pushButton_52.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_52.setFont(font7)
        self.pushButton_52.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_52.setIconSize(QSize(200, 50))

        self.gridLayout_34.addWidget(self.pushButton_52, 0, 0, 1, 1)

        self.pushButton_55 = QPushButton(self.frame_30)
        self.pushButton_55.setObjectName(u"pushButton_55")
        sizePolicy.setHeightForWidth(self.pushButton_55.sizePolicy().hasHeightForWidth())
        self.pushButton_55.setSizePolicy(sizePolicy)
        self.pushButton_55.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_55.setFont(font7)
        self.pushButton_55.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_55.setIconSize(QSize(200, 50))

        self.gridLayout_34.addWidget(self.pushButton_55, 3, 0, 1, 1)

        self.gridLayout_32.addWidget(self.frame_30, 1, 2, 2, 1)

        self.label_2 = QLabel(self.frame_28)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        font12 = QFont()
        font12.setFamily(u"Almarai")
        font12.setPointSize(13)
        font12.setBold(False)
        font12.setWeight(50)
        self.label_2.setFont(font12)
        self.label_2.setStyleSheet(u"color: rgb(255, 102, 64);\n"
                                   "color: rgb(122, 183, 229);\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "color: rgb(255, 0, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayout_32.setRowStretch(2, 5)
        self.gridLayout_32.setRowStretch(3, 1)
        self.gridLayout_32.setColumnStretch(0, 3)
        self.gridLayout_32.setColumnStretch(2, 1)

        self.gridLayout_35.addWidget(self.frame_28, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 2)

        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.294, y1:0.21, x2:0.886, y2:0.419455, stop:0 rgba(21, 79, 156, 255), stop:1 rgba(122, 183, 229, 255));\n"
                                   "border : 0;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_37 = QGridLayout(self.frame_5)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"QFrame\n"
                                   "{\n"
                                   "background-color: rgb(255, 255, 255, 0);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton\n"
                                   "{\n"
                                   "	background: transparent;\n"
                                   "	color: rgb(244, 243, 242);\n"
                                   "	border-color: rgb(244, 243, 242);\n"
                                   "	border-radius: 15px;\n"
                                   "border : 1px solid rgb(244, 243, 242);\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_4)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setSizeConstraint(QLayout.SetMinimumSize)
        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(0, 0))
        self.pushButton_5.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_5.setBaseSize(QSize(0, 0))
        font13 = QFont()
        font13.setFamily(u"Almarai")
        font13.setPointSize(17)
        font13.setBold(False)
        font13.setItalic(False)
        font13.setUnderline(False)
        font13.setWeight(50)
        self.pushButton_5.setFont(font13)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"")

        self.gridLayout_36.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.gridLayout_37.addWidget(self.frame_4, 1, 1, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(120, 100))
        self.label.setMaximumSize(QSize(200, 120))
        self.label.setStyleSheet(u"background: transparent;\n"
                                 "image: url(:/newPrefix/1.png);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.label, 1, 0, 1, 1, Qt.AlignLeft)

        self.gridLayout_37.setColumnStretch(0, 5)
        self.gridLayout_37.setColumnStretch(1, 3)

        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"QFrame\n"
                                   "{\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.226, y1:0.999773, x2:0.567818, y2:0.147, stop:0 rgba(0, 120, 188, 255), stop:1 rgba(117, 180, 227, 255));\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton\n"
                                   "{\n"
                                   "background-color: rgb(244, 243, 242);\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "border-radius: 15px;\n"
                                   "    padding:9px;\n"
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
                                   "}\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_48 = QPushButton(self.frame_2)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy)
        self.pushButton_48.setMaximumSize(QSize(16777215, 60))
        font14 = QFont()
        font14.setFamily(u"Almarai")
        font14.setPointSize(14)
        font14.setBold(False)
        font14.setWeight(50)
        self.pushButton_48.setFont(font14)
        self.pushButton_48.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_48.setIconSize(QSize(200, 50))

        self.verticalLayout.addWidget(self.pushButton_48)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QSize(16777215, 60))
        self.pushButton_4.setFont(font14)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setIconSize(QSize(200, 50))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(16777215, 60))
        self.pushButton.setFont(font14)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_24 = QPushButton(self.frame_2)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setMaximumSize(QSize(16777215, 60))
        font15 = QFont()
        font15.setFamily(u"Almarai")
        font15.setPointSize(14)
        font15.setBold(False)
        font15.setItalic(False)
        font15.setWeight(50)
        self.pushButton_24.setFont(font15)
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pushButton_24)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(16777215, 60))
        self.pushButton_2.setFont(font14)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(16777215, 60))
        self.pushButton_3.setFont(font14)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_56 = QPushButton(self.frame_2)
        self.pushButton_56.setObjectName(u"pushButton_56")
        sizePolicy.setHeightForWidth(self.pushButton_56.sizePolicy().hasHeightForWidth())
        self.pushButton_56.setSizePolicy(sizePolicy)
        self.pushButton_56.setMaximumSize(QSize(16777215, 60))
        self.pushButton_56.setFont(font14)
        self.pushButton_56.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_56)

        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 2)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 16)
        self.gridLayout.setColumnStretch(0, 12)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_4.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0623\u062f\u062e\u0644 \u0633\u064a\u0631\u064a\u0627\u0644",
                                       None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"\u0641\u062d\u0635", None))
        # if QT_CONFIG(tooltip)
        self.lineEdit_5.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.lineEdit_5.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(accessibility)
        self.lineEdit_5.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.lineEdit_5.setPlaceholderText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u062d\u0627\u0644\u0629 \u0627\u0644\u0627\u0634\u062a\u0631\u0627\u0643 :",
                                                         None))
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"\u0644\u0644\u062f\u0639\u0645 \u0627\u0644\u0641\u0646\u064a:",
                                       None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"Whatsapp", None))
        self.label_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow",
                                                                                               u"\u0627\u0644\u0631\u0626\u0633\u064a\u0629",
                                                                                               None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062d", None))
        self.pushButton_9.setText(
            QCoreApplication.translate("MainWindow", u"\u062c\u0644\u0628 \u0627\u0644\u0627\u0631\u0642\u0627\u0645",
                                       None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0642\u0645", None));
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062d", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u062c\u0645\u064a\u0639 \u0627\u0644\u0627\u0631\u0642\u0627\u0645",
                                                        None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062d", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        ___qtablewidgetitem1 = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0642\u0645", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0627\u0631\u0642\u0627\u0645 \u0645\u0648\u062c\u0648\u062f\u0629",
                                                        None))
        ___qtablewidgetitem2 = self.tableWidget_9.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0642\u0645", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u0627\u0631\u0642\u0627\u0645 \u063a\u064a\u0631 \u0645\u0648\u062c\u0648\u062f\u0629",
                                                         None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062d", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645:", None))
        self.pushButton_46.setText(
            QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638 \u0644\u0644\u0647\u0627\u062a\u0641", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0642\u0641", None))
        self.pushButton_10.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u064a\u0642\u0627\u0641 \u0645\u0624\u0642\u062a", None))
        self.pushButton_11.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0626\u0646\u0627\u0641", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0628\u062f\u0627", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u0641\u0627\u0635\u0644 \u0627\u0644\u062b\u0648\u0627\u0646\u064a:",
                                                         None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u0641\u062d\u0635 \u0627\u0644\u0627\u0631\u0642\u0627\u0645",
                                                                                                 None))
        ___qtablewidgetitem3 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645", None));
        ___qtablewidgetitem4 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062d\u0627\u0644\u0629", None));
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062d", None))
        self.pushButton_29.setText(
            QCoreApplication.translate("MainWindow", u"\u062c\u0644\u0628 \u0627\u0644\u0627\u0633\u0645\u0627\u0621",
                                       None))
        self.pushButton_33.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0626\u0646\u0627\u0641", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0642\u0641", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0627\u0644\u0641\u0627\u0635\u0644 \u0627\u0644\u0632\u0645\u0646\u064a:",
                                                        None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u064a:", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0628\u062f\u0627", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646:", None))
        self.pushButton_31.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u064a\u0642\u0627\u0641 \u0645\u0624\u0642\u062a", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0648\u0631\u0647", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0635", None))
        self.pushButton_32.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0635\u0648\u0631\u0647", None))
        self.pushButton_28.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0647 \u0627\u0644\u0646\u0635", None))
        ___qtablewidgetitem5 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0646\u0635", None));
        ___qtablewidgetitem6 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0631\u0641\u0642", None));
        ___qtablewidgetitem7 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0646\u0648\u0639", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u0627\u0631\u0633\u0627\u0644 \u0644\u0644\u062c\u0631\u0648\u0628\u0627\u062a",
                                                                                                 None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062d", None))
        self.pushButton_19.setText(
            QCoreApplication.translate("MainWindow", u"\u062c\u0644\u0628 \u0627\u0644\u0627\u0631\u0642\u0627\u0645",
                                       None))
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0642\u0645", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062d\u0627\u0644\u0629", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0627\u0644\u0641\u0627\u0635\u0644 \u0627\u0644\u0632\u0645\u0646\u064a:",
                                                        None))
        self.pushButton_17.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u064a\u0642\u0627\u0641 \u0645\u0624\u0642\u062a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u064a:", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0628\u062f\u0627", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646:", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0642\u0641", None))
        self.pushButton_16.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0626\u0646\u0627\u0641", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0648\u0631\u0647", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0635", None))
        ___qtablewidgetitem10 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0646\u0635", None));
        ___qtablewidgetitem11 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0631\u0641\u0642", None));
        ___qtablewidgetitem12 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0646\u0648\u0639", None));
        self.pushButton_22.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0635\u0648\u0631\u0647", None))
        self.pushButton_20.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0647 \u0627\u0644\u0646\u0635", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u0627\u0631\u0633\u0627\u0644 \u0644\u0644\u0627\u0631\u0642\u0627\u0645",
                                                                                                 None))
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0642\u0645", None));
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062d", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.pushButton_6.setText(
            QCoreApplication.translate("MainWindow", u"\u0628\u062f\u0623 \u0633\u062d\u0628", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645:", None))
        self.pushButton_45.setText(
            QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638 \u0644\u0644\u0647\u0627\u062a\u0641", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u0633\u062d\u0628 \u0627\u0644\u0627\u0631\u0642\u0627\u0645",
                                                                                                 None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638", None))
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0642\u0631\u0648\u0628\u0627\u062a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u062c\u0647\u0627\u062a \u0627\u0644\u0627\u062a\u0635\u0627\u0644",
                                                         None))
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0631\u0642\u0627\u0645", None))
        ___qtablewidgetitem14 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645", None));
        ___qtablewidgetitem15 = self.tableWidget_11.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645", None));
        ___qtablewidgetitem16 = self.tableWidget_10.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0642\u0645", None));
        self.pushButton_25.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0628\u062f\u0623 \u0633\u062d\u0628 ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645:", None))
        self.pushButton_47.setText(
            QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638 \u0644\u0644\u0647\u0627\u062a\u0641", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0642\u0641", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u0633\u062d\u0628 \u062c\u0647\u0627\u062a \u0627\u0644\u0627\u062a\u0635\u0627\u0644",
                                                                                                 None))
        ___qtablewidgetitem17 = self.tableWidget_12.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645", None));
        ___qtablewidgetitem18 = self.tableWidget_12.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062d\u0627\u0644\u0629", None));
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u062d", None))
        self.pushButton_51.setText(
            QCoreApplication.translate("MainWindow", u"\u062c\u0644\u0628 \u0627\u0644\u0627\u0633\u0645\u0627\u0621",
                                       None))
        self.pushButton_53.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u064a\u0642\u0627\u0641 \u0645\u0624\u0642\u062a", None))
        self.pushButton_54.setText(
            QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0626\u0646\u0627\u0641", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0627\u0636\u0627\u0641\u0629 \u0627\u0644\u0627\u0639\u0636\u0627\u0621",
                                                              None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0642\u0641", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0647\u0630\u0647 \u0627\u0644\u0645\u064a\u0632\u0647 \u062a\u062d\u062a\u0627\u062c \u0625\u0644\u0649 \u062d\u0641\u0638 \u0627\u0644\u0623\u0631\u0642\u0627\u0645 \u0641\u064a \u0627\u0644\u0645\u0648\u0628\u064a\u0644",
                                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u0627\u0636\u0627\u0641\u0629 \u0627\u0639\u0636\u0627\u0621 \u0644\u0644\u062c\u0631\u0648\u0628",
                                                                                                 None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0641\u062a\u062d \u0645\u0648\u0642\u0639 \u0627\u0644\u0648\u0627\u062a\u0633\u0627\u0628",
                                                             None))
        self.label.setText("")
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u0631\u0626\u0633\u064a\u0629",
                                                              None))
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", u"\u0633\u062d\u0628 \u0627\u0644\u0623\u0631\u0642\u0627\u0645",
                                       None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0627\u062e\u062a\u0628\u0627\u0631 \u0627\u0644\u0627\u0631\u0642\u0627\u0645",
                                                           None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0627\u0633\u062a\u062e\u0631\u0627\u062c \u062c\u0647\u0627\u062a \u0627\u0644\u0627\u062a\u0635\u0627\u0644",
                                                              None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0627\u0644\u0625\u0631\u0633\u0627\u0644 \u0644\u0644\u0642\u0631\u0648\u0628\u0627\u062a",
                                                             None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0625\u0631\u0633\u0627\u0644 \u0627\u0644\u0631\u0633\u0627\u0626\u0644",
                                                             None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0627\u0636\u0627\u0641\u0629 \u0627\u0644\u0627\u0639\u0636\u0627\u0621",
                                                              None))
    # retranslateUi
