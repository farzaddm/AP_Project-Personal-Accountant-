from PyQt6 import QtCore, QtGui, QtWidgets
from Views.forget_password import *
from Controlers.user_controller import UserController


class Ui_Login(object):
    def open_window_forgetpage(self):
        class Forgetpage(QtWidgets.QMainWindow, ForgetPassword):
            def __init__(self):
                super().__init__()
                self.setupUi(self)

        self.ui = Forgetpage()
        self.ui.show()
        self.ui.setWindowTitle("Forget Password")
        self.close()

    def setupUi(self, MainWindow):
        MainWindow.resize(1000, 600)
        self.check_count = 0
        self.ban = False
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(30)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.picture_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.picture_lbl.setGeometry(QtCore.QRect(30, 0, 501, 561))
        self.picture_lbl.setText("")
        self.picture_lbl.setPixmap(QtGui.QPixmap("pictures/logon.jpg"))

        self.loginpage_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.loginpage_lbl.setGeometry(QtCore.QRect(680, 40, 231, 81))
        self.loginpage_lbl.setFont(font)

        self.username_lbl = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username_lbl.setGeometry(QtCore.QRect(590, 200, 361, 31))
        self.username_lbl.setText("")
        self.username_lbl.textChanged.connect(self.username_changed)

        self.error_lbl = QtWidgets.QLabel(
            "You are banned for 60 seconds".title(), parent=self.centralwidget)
        self.error_lbl.setGeometry(QtCore.QRect(590, 170, 361, 31))
        self.error_lbl.setStyleSheet("color:red")
        self.error_lbl.hide()

        self.time = QtCore.QTime.currentTime()

        self.password_lbl = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_lbl.setGeometry(QtCore.QRect(590, 260, 361, 31))
        self.password_lbl.textChanged.connect(self.password_changed)

        self.login_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(590, 354, 361, 31))
        self.login_btn.clicked.connect(self.pressed_login_btn)
        self.login_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #0763e5;
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

        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(570, 420, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.forget_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.forget_btn.setGeometry(QtCore.QRect(590, 470, 361, 31))
        self.forget_btn.clicked.connect(self.forget_password_clicked)
        self.forget_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #0763e5;
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))

        self.menuFile = QtWidgets.QMenu(parent=self.menubar)

        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)

        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(parent=MainWindow)

        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginpage_lbl.setText(_translate("MainWindow", "Login Page"))
        self.username_lbl.setPlaceholderText(
            _translate("MainWindow", "User Name"))
        self.password_lbl.setPlaceholderText(
            _translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.forget_btn.setText(_translate("MainWindow", "Forgot Password"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def pressed_login_btn(self):

        if self.ban:
            self.check_count = 0
            second = QtCore.QTime.currentTime().second() == self.time.second()
            minutes = QtCore.QTime.currentTime().minute() == self.time.minute()
            hour = QtCore.QTime.currentTime().hour() == self.time.hour()
            self.error_lbl.show()
            if hour and minutes and second:
                self.ban = False
        else:
            self.username_lbl.setStyleSheet(" ")
            self.password_lbl.setStyleSheet(" ")
            if self.check_count == 3:
                self.ban = True
                self.time = QtCore.QTime.currentTime().addSecs(60)
            login_check = UserController(self)
            if login_check.login(self.username_lbl, self.password_lbl):
                pass
            else:
                self.username_lbl.setStyleSheet("border: 1px solid red")
                self.password_lbl.setStyleSheet("border: 1px solid red")
                self.check_count += 1

    def forget_password_clicked(self):
        self.open_window_forgetpage()

    def username_changed(self):
        self.username_lbl.setStyleSheet("")

    def password_changed(self):
        self.password_lbl.setStyleSheet("")
