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
        """Configura a interface principal."""
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")

        # Configuração inicial
        MainWindow.resize(618, 463)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        # 1. Configuração central
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 2. Layout principal
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # 3. Adicionar TabWidget
        self.setup_tab_widget()
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        # 4. Adicionar barra de ferramentas
        self.setup_toolbar(MainWindow)

        # 5. Configurar barra de menus
        self.setup_menu_bar(MainWindow)

        # Finalizar setup
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)


    def setup_tab_widget(self):
        """Configura o TabWidget e suas páginas."""
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)

    def setup_toolbar(self, MainWindow):
        """Configura a barra de ferramentas."""
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")

        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy1)

        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar)

        # Adicionar ações
        self.actionCaneta = QAction(MainWindow)
        self.actionCaneta.setObjectName("actionCaneta")
        self.actionCaneta.setCheckable(True)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.actionCaneta.setIcon(icon)

        self.actionBorracha = QAction(MainWindow)
        self.actionBorracha.setObjectName("actionBorracha")
        self.actionBorracha.setCheckable(True)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Battery))
        self.actionBorracha.setIcon(icon1)

        # Adicionar à barra de ferramentas
        self.toolBar.addAction(self.actionCaneta)
        self.toolBar.addAction(self.actionBorracha)
        self.toolBar.addSeparator()

    def setup_menu_bar(self, MainWindow):
        """Configura a barra de menus."""
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 618, 22))

        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menubar.addAction(self.menuFile.menuAction())

        # Configurar ações
        self.actionNew_2 = QAction(MainWindow)
        self.actionNew_2.setObjectName("actionNew_2")
        self.actionNew_2.setCheckable(False)

        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        
        self.actionInsert = QAction(MainWindow)
        self.actionInsert.setObjectName("actionInsert")
        
        # Adicionar ações ao menu
        self.menuFile.addAction(self.actionNew_2)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionInsert)

        MainWindow.setMenuBar(self.menubar)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FeraVision-Alpha", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNew_2.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionInsert.setText(QCoreApplication.translate("MainWindow", u"Insert-Image", None))
        self.actionCaneta.setText(QCoreApplication.translate("MainWindow", u"Caneta", None))
        self.actionBorracha.setText(QCoreApplication.translate("MainWindow", u"Borracha", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

