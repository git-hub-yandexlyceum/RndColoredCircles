from PyQt6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PyQt6.QtGui import QCursor, QFont
from PyQt6.QtWidgets import QWidget, QPushButton, QMenuBar, QStatusBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(579, 510)
        font = QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QFont.StyleStrategy.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CursorShape.WaitCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drawButton = QPushButton(self.centralwidget)
        self.drawButton.setObjectName(u"drawButton")
        self.drawButton.setGeometry(QRect(190, 420, 171, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe Script")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.StyleStrategy.PreferDefault)
        self.drawButton.setFont(font1)
        self.drawButton.setCursor(QCursor(Qt.CursorShape.WaitCursor))
        self.drawButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.drawButton.setAutoFillBackground(False)
        self.drawButton.setCheckable(False)
        self.drawButton.setAutoDefault(False)
        self.drawButton.setFlat(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 579, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.drawButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.drawButton.setWhatsThis("")
        self.drawButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041d\u041e\u041f\u041a\u0410", None))
