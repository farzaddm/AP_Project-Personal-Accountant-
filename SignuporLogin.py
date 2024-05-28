# Form implementation generated from reading ui file 'mainwindow3.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from Login_ui import Ui_MainWindow2


class Ui_MainWindow(object):
    def open_window(self):
        class MainWindow2(QtWidgets.QMainWindow, Ui_MainWindow2):

            def __init__(self):
                super().__init__()

                self.setupUi(self)
        self.ui = MainWindow2()
        self.ui.show()
        self.hide()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Welcome = QtWidgets.QLabel(parent=self.centralwidget)
        self.Welcome.setGeometry(QtCore.QRect(150, 350, 251, 111))
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(38)
        self.Welcome.setFont(font)
        self.Welcome.setScaledContents(False)
        self.Welcome.setObjectName("Welcome")
        self.ToMyApp = QtWidgets.QLabel(parent=self.centralwidget)
        self.ToMyApp.setGeometry(QtCore.QRect(165, 440, 211, 71))
        self.Welcome.setStyleSheet("color:white")
        self.ToMyApp.setStyleSheet("color:white")

        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(29)
        self.ToMyApp.setFont(font)
        self.ToMyApp.setScaledContents(False)
        self.ToMyApp.setObjectName("ToMyApp")
        self.Pic = QtWidgets.QLabel(parent=self.centralwidget)
        self.Pic.setGeometry(QtCore.QRect(0, -110, 491, 1000))
        self.Pic.setText("")
        self.Pic.setPixmap(QtGui.QPixmap(r"pictures\Capture.png"))
        self.Pic.setObjectName("Pic")
        self.signup = QtWidgets.QPushButton(parent=self.centralwidget)
        self.signup.setStyleSheet("""
                    QPushButton {
                        background-color: #ffffff;
                        color: #000000;
                        border-radius: 15px;
                        border: 2px #1AA7EC;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color: #0763e5;
                    }
                    QPushButton:pressed {
                        background-color: #1AA7EC;
                    }
                """)
        self.signup.setGeometry(QtCore.QRect(80, 550, 341, 31))
        self.signup.setObjectName("signup")
        self.login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login.setGeometry(QtCore.QRect(80, 600, 341, 31))
        self.login.setObjectName("login")
        self.login.setStyleSheet("""
                    QPushButton {
                        background-color: #ffffff;
                        color: #000000;
                        border-radius: 15px;
                        border: 2px #1AA7EC;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color: #0763e5;
                    }
                    QPushButton:pressed {
                        background-color: #1AA7EC;
                    }
                """)
        self.login.clicked.connect(self.login_btn_clicked)
        self.Pic.raise_()
        self.Welcome.raise_()
        self.ToMyApp.raise_()
        self.signup.raise_()
        self.login.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Welcome.setText(_translate("MainWindow", "Welcome"))
        self.ToMyApp.setText(_translate("MainWindow", "To My App"))
        self.signup.setText(_translate("MainWindow", "Sign Up"))
        self.login.setText(_translate("MainWindow", "Login"))
    def login_btn_clicked(self):
        self.open_window()
