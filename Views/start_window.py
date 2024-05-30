from PyQt6 import QtCore, QtGui, QtWidgets
from Views.login_ui import *
from Views import sign_up


class Signupandlogin(object):
    def open_window_login(self):
        class LoginPage(QtWidgets.QMainWindow, Ui_Login):
            def __init__(self):
                super().__init__()
                self.setupUi(self)

        self.ui = LoginPage()
        self.ui.setWindowTitle("Login Page")
        self.ui.show()
        self.hide()

    def open_window_signup(self):
        class SignupPage(QtWidgets.QMainWindow, sign_up.Ui_SignUp):
            def __init__(self):
                super().__init__()
                self.setupUi(self)

        self.ui = SignupPage()
        self.ui.setWindowTitle("SignUp Page")
        self.ui.show()
        self.hide()

    def setupUi(self, MainWindow):
        MainWindow.resize(480, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("""
                    QPushButton {
                        background-color: #ffffff;
                        color: #000000;
                        border-radius: 15px;
                        border: 2px #1AA7EC;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color:#1AA7EC ;
                    }
                    QPushButton:pressed {
                        background-color: #1AA7EC;
                    }
                """)
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(38)

        self.Welcome_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.Welcome_lbl.setGeometry(QtCore.QRect(150, 350, 251, 111))
        self.Welcome_lbl.setFont(font)
        self.Welcome_lbl.setScaledContents(False)
        self.Welcome_lbl.setStyleSheet("color:white")

        font.setPointSize(29)
        self.wellcome2_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.wellcome2_lbl.setGeometry(QtCore.QRect(165, 440, 211, 71))
        self.wellcome2_lbl.setStyleSheet("color:white")
        self.wellcome2_lbl.setFont(font)
        self.wellcome2_lbl.setScaledContents(False)

        self.Pic_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.Pic_lbl.setGeometry(QtCore.QRect(0, -110, 491, 1000))
        self.Pic_lbl.setText("")
        self.Pic_lbl.setPixmap(QtGui.QPixmap("pictures/start.png"))

        self.signup_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.signup_btn.setGeometry(QtCore.QRect(80, 550, 341, 31))
        self.signup_btn.clicked.connect(self.signup_btn_clicked)


        self.login_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(80, 600, 341, 31))
        self.login_btn.clicked.connect(self.login_btn_clicked)


        self.Pic_lbl.raise_()
        self.Welcome_lbl.raise_()
        self.wellcome2_lbl.raise_()
        self.signup_btn.raise_()
        self.login_btn.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 25))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Welcome_lbl.setText(_translate("MainWindow", "Welcome"))
        self.wellcome2_lbl.setText(_translate("MainWindow", "To My App"))
        self.signup_btn.setText(_translate("MainWindow", "Sign Up"))
        self.login_btn.setText(_translate("MainWindow", "Login"))

    def login_btn_clicked(self):
        self.open_window_login()

    def signup_btn_clicked(self):
        self.open_window_signup()
