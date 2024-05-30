from PyQt6 import QtCore, QtGui, QtWidgets
from Views.forget_password import *
from Views.firstpage import *
from Controlers.user_controller import UserController

class Ui_Login(object):
    def open_window_forgetpage(self):
        class MainWindow(QtWidgets.QMainWindow,ForgetPassword):
            def __init__(self):
                super().__init__()
                self.setupUi(self)
        self.ui=MainWindow()
        self.ui.show()
        self.ui.setWindowTitle("Forget Passwords")
        self.close()

    def open_window_firstpage(self):
        class MainWindow(QtWidgets.QMainWindow,Ui_Firstpage):
            def __init__(self):
                super().__init__()
                self.setupUi(self)
        self.ui=MainWindow()
        self.ui.show()
        self.ui.setWindowTitle("Welcome to my app")
        self.close()

    def setupUi(self, MainWindow):
        MainWindow.resize(1000, 600)
        self.check_count = 0
        self.ban = False
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(30)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("""
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

        self.error_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_lbl.setGeometry(QtCore.QRect(590, 170, 361, 31))
        self.error_lbl.setStyleSheet("color:red")
        self.error_lbl.hide()

        self.time = QtCore.QTimer()
        self.time_change=QtCore.QTime(0,1,0)
        self.time.timeout.connect(self.update_timer)
        

        self.password_lbl = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_lbl.setGeometry(QtCore.QRect(590, 260, 361, 31))
        self.password_lbl.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_lbl.textChanged.connect(self.password_changed)

        self.login_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(590, 354, 361, 31))
        self.login_btn.clicked.connect(self.pressed_login_btn)
        

        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(570, 420, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.forget_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.forget_btn.setGeometry(QtCore.QRect(590, 470, 361, 31))
        self.forget_btn.clicked.connect(self.forget_password_clicked)


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
            self.error_lbl.show()
            self.time.start(1000)
        else:
            self.check_count += 1
            self.username_lbl.setStyleSheet(" ")
            self.password_lbl.setStyleSheet(" ")
            if self.check_count == 3:
                self.ban = True
                self.pressed_login_btn()
            login_check = UserController(self)
            if login_check.login(self.username_lbl, self.password_lbl):
                self.open_window_firstpage()
            else:
                self.username_lbl.setStyleSheet("border: 1px solid red")
                self.password_lbl.setStyleSheet("border: 1px solid red")

    def update_timer(self):
        self.time_change= self.time_change.addSecs(-1)
        if not self.time_change.toString("hh:mm:ss") == "00:00:00":
            self.error_lbl.setText(f"You Are Banned  for {int(self.time_change.toString("s"))+int(self.time_change.toString("m"))*60} Seconds")
        else:
            self.error_lbl.hide()
        
    def forget_password_clicked(self):
        self.open_window_forgetpage()

    def username_changed(self):
        self.username_lbl.setStyleSheet("")

    def password_changed(self):
        self.password_lbl.setStyleSheet("")
