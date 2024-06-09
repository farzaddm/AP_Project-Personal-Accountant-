from PyQt6 import QtCore, QtGui, QtWidgets
from Views.forget_password import *
from Views.first_page import *
from Controlers.user_controller import UserController
from Views.mode import SetSetyling

class Ui_Login(object):
    def open_window_forgetpage(self):
        class MainWindow(QtWidgets.QMainWindow, ForgetPassword):
            def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.style=SetSetyling(self)

        self.ui = MainWindow()
        self.ui.login = self
        self.ui.show()
        self.ui.setWindowTitle("Forget Passwords")
        self.hide()

    def open_window_firstpage(self, username):
        class Ui_Firstpage_Login(QtWidgets.QMainWindow, Ui_Firstpage):
            def __init__(self):
                super().__init__()
                self.username = username
                self.setupUi(self)
                self.style=SetSetyling(self)
  
        self.ui = Ui_Firstpage_Login()
        self.ui.login_page=self
        self.ui.show()
        self.ui.setWindowTitle("Welcome to my app")
        self.hide()

    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        self.MainWindow.resize(1000, 600)
        self.check_count = 0
        self.ban = False

        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(30)

        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)
        self.centralwidget.setStyleSheet("""
                    QPushButton {
                        background-color: #0763e5;
                        color: #ffffff;
                        border-radius: 15px;
                        border: 2px #1AA7EC;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color:#1AA7EC ;
                    }
                    QPushButton:pressed {
                        background-color: #1AA7EC;
                    }""")

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
        self.time_change = QtCore.QTime(0, 1, 0)
        self.time.timeout.connect(self.update_timer)

        self.password_le = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_le.setGeometry(QtCore.QRect(590, 260, 361, 31))
        self.password_le.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_le.textChanged.connect(self.password_changed)

        self.password_check_box = QtWidgets.QCheckBox(
            parent=self.centralwidget, text="Show Password")
        self.password_check_box.setGeometry(QtCore.QRect(590, 300, 361, 31))
        self.password_check_box.stateChanged.connect(
            self.change_view_of_password)

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

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))

        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)

        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.MainWindow)

        self.MainWindow.setStatusBar(self.statusbar)

        self.actionExit = QtGui.QAction(parent=self.MainWindow)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginpage_lbl.setText(_translate("MainWindow", "Login Page"))
        self.username_lbl.setPlaceholderText(
            _translate("MainWindow", "User Name"))
        self.password_le.setPlaceholderText(
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
            self.password_le.setStyleSheet(" ")
            if self.check_count == 3:
                self.ban = True

            controller = UserController(self)

            if controller.login(self.username_lbl.text(), self.password_le.text()):
                username = self.username_lbl.text()
                self.check_count=0
                self.open_window_firstpage(username)
            else:
                self.username_lbl.setStyleSheet("border: 1px solid red")
                self.password_le.setStyleSheet("border: 1px solid red")

    def update_timer(self) -> None:
        self.time_change = self.time_change.addSecs(-1)
        if not self.time_change.toString("hh:mm:ss") == "00:00:00":
            self.error_lbl.setText(f"You Are Banned  for {int(self.time_change.toString('s'))+int(self.time_change.toString('m'))*60} Seconds")

        else:
            self.time_change = QtCore.QTime(0, 1, 0)
            self.ban = False
            self.error_lbl.hide()

    def forget_password_clicked(self):
        self.open_window_forgetpage()

    def username_changed(self):

        self.username_lbl.setStyleSheet("")

    def password_changed(self):
        self.password_le.setStyleSheet("")

    def change_view_of_password(self, state):
        if state == 2:
            self.password_le.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.password_le.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
