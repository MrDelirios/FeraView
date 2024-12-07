# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IDE.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QTabWidget,
    QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(618, 463)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionNew_2 = QAction(MainWindow)
        self.actionNew_2.setObjectName(u"actionNew_2")
        self.actionNew_2.setCheckable(False)
        self.actionCaneta = QAction(MainWindow)
        self.actionCaneta.setObjectName(u"actionCaneta")
        self.actionCaneta.setCheckable(True)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.actionCaneta.setIcon(icon)
        self.actionBorracha = QAction(MainWindow)
        self.actionBorracha.setObjectName(u"actionBorracha")
        self.actionBorracha.setCheckable(True)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Battery))
        self.actionBorracha.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.Page = QWidget()
        self.Page.setObjectName(u"Page")
        sizePolicy.setHeightForWidth(self.Page.sizePolicy().hasHeightForWidth())
        self.Page.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.Page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.graphicsView = QGraphicsView(self.Page)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)

        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Page, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy1)
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 618, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCaneta)
        self.toolBar.addAction(self.actionBorracha)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew_2)
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FeraVision-Alpha", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNew_2.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionCaneta.setText(QCoreApplication.translate("MainWindow", u"Caneta", None))
        self.actionBorracha.setText(QCoreApplication.translate("MainWindow", u"Borracha", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Page), QCoreApplication.translate("MainWindow", u"Page", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

