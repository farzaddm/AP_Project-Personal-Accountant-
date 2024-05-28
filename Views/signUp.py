from PyQt6 import QtCore, QtGui, QtWidgets
from Controlers.user_controller import UserController


class Ui_SignUp(object):
    """ It's a class for seting up the signup. """
    def setupUi(self, MainWindow) -> None:
        """ set up signup page elements. """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lbl_signup_pic = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_signup_pic.setGeometry(QtCore.QRect(320, 60, 661, 491))
        self.lbl_signup_pic.setText("")
        self.lbl_signup_pic.setPixmap(QtGui.QPixmap("pictures/sign_up.png"))
        self.lbl_signup_pic.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_signup_pic.setObjectName("lbl_signup_pic")

        self.lbl_signup = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_signup.setGeometry(QtCore.QRect(10, 10, 281, 41))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)

        self.lbl_signup.setFont(font)
        self.lbl_signup.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_signup.setObjectName("lbl_signup")

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 60, 281, 491))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.le_fname = QtWidgets.QLineEdit(parent=self.widget)
        self.le_fname.setObjectName("le_fname")
        self.verticalLayout.addWidget(self.le_fname)

        self.le_lname = QtWidgets.QLineEdit(parent=self.widget)
        self.le_lname.setObjectName("le_lname")
        self.verticalLayout.addWidget(self.le_lname)

        self.le_phone = QtWidgets.QLineEdit(parent=self.widget)
        self.le_phone.setObjectName("le_phone")
        self.verticalLayout.addWidget(self.le_phone)

        self.le_username = QtWidgets.QLineEdit(parent=self.widget)
        self.le_username.setObjectName("le_username")
        self.verticalLayout.addWidget(self.le_username)

        self.le_password = QtWidgets.QLineEdit(parent=self.widget)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.le_password.setObjectName("le_password")
        self.verticalLayout.addWidget(self.le_password)

        self.le_repeat_password = QtWidgets.QLineEdit(parent=self.widget)
        self.le_repeat_password.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password)
        self.le_repeat_password.setObjectName("le_repeat_password")
        self.verticalLayout.addWidget(self.le_repeat_password)

        self.le_city = QtWidgets.QLineEdit()
        cities = ["Tehran", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Karaj",
                  "Qom", "Ahvaz", "Kermanshah", "Urmia", "Yazd", "Bushehr", "Semnan"]
        completer = QtWidgets.QCompleter(cities)
        self.le_city.setCompleter(completer)
        self.le_city.setObjectName("le_city")
        self.verticalLayout.addWidget(self.le_city)

        self.le_email = QtWidgets.QLineEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le_email.setFont(font)
        self.le_email.setObjectName("le_email")
        self.verticalLayout.addWidget(self.le_email)

        self.le_birthday = QtWidgets.QDateEdit(parent=self.widget)
        self.le_birthday.setCalendarPopup(True)
        self.le_birthday.setDisplayFormat("yyyy-MM-dd")
        self.le_birthday.setObjectName("le_birthday")
        self.verticalLayout.addWidget(self.le_birthday)

        self.le_security_q = QtWidgets.QLineEdit(parent=self.widget)
        self.le_security_q.setText("")
        self.le_security_q.setObjectName("le_security_q")
        self.verticalLayout.addWidget(self.le_security_q)

        self.btn_signup = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        
        self.btn_signup.setFont(font)
        self.btn_signup.setObjectName("btn_signup")
        self.btn_signup.setStyleSheet("""
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
                    }
                """)
        self.btn_signup.clicked.connect(self.submit_btn_clicked)
        self.verticalLayout.addWidget(self.btn_signup)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtGui.QAction(parent=MainWindow)
        self.actionHelp.setObjectName("actionHelp")

        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.controller = UserController(self)


    def retranslateUi(self, MainWindow) -> None:
        """ Puting text to labels and set place holders. """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_signup.setText(_translate("MainWindow", "Sign Up"))
        self.le_fname.setPlaceholderText(
            _translate("MainWindow", "First name"))
        self.le_lname.setPlaceholderText(_translate("MainWindow", "Last name"))
        self.le_phone.setPlaceholderText(_translate("MainWindow", "Phone"))
        self.le_username.setPlaceholderText(
            _translate("MainWindow", "Username"))
        self.le_password.setPlaceholderText(
            _translate("MainWindow", "Password"))
        self.le_repeat_password.setPlaceholderText(
            _translate("MainWindow", "Please repeat password"))
        self.le_city.setPlaceholderText(_translate("MainWindow", "City"))
        self.le_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.le_security_q.setPlaceholderText(_translate(
            "MainWindow", "What\'s your favorite color?"))
        self.btn_signup.setText(_translate("MainWindow", "Submit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))

    def submit_btn_clicked(self) -> None:
        """ Check the validation of inputs and save it to database. """
        self.controller.sign_up()

    def show_error(self, message: str) -> None:
        """make a messagebox to show errors to user.

        Args:
            message (str): It's an error message that when inputs are invalid throw.
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()
