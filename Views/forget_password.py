from PyQt6 import QtCore, QtGui, QtWidgets
from Controlers.user_controller import UserController
from Views.first_page import Ui_Firstpage
from Views.font import Font_detail

class ForgetPassword(object):
    def __init__(self):
        self.user_password=""
        self.username_save=""
        self.style="style"
        self.font=Font_detail()
        self.login = "login"
        
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        self.MainWindow.resize(334, 400)

        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)

        self.forget_l = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(25 * self.font.font_size)
        self.forget_l.setFont(font)
        self.forget_l.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2.addWidget(self.forget_l)

        self.background = QtWidgets.QLabel(parent=self.centralwidget)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("pictures/lock.PNG"))
        self.background.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2.addWidget(self.background)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        
        self.username_le = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username_le.setPlaceholderText("Username")
        self.verticalLayout.addWidget(self.username_le)


        self.question_le = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.question_le.setPlaceholderText("What is your favorite color ? ")
        self.verticalLayout.addWidget(self.question_le)


        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.clicked.connect(self.next_clicked)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 25))
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.MainWindow)
        self.MainWindow.setStatusBar(self.statusbar)

        self.controller = UserController(self)
        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.forget_l.setText(_translate("MainWindow", "Forget Password"))
        self.pushButton.setText(_translate("MainWindow", "Next ->"))
    
    def next_clicked(self):
        if self.controller.forget_password(self.username_le.text(),self.question_le.text().lower()):
            self.username_save=self.username_le.text()
            user_email=self.controller.get_email(self.username_le.text())
            self.user_password=self.controller.send_email(email=user_email)
            self.question_le.hide()
            self.username_le.setText("")
            self.username_le.setObjectName("password")
            self.username_le.setPlaceholderText("Password")
            self.pushButton.setText("Check Password")
            self.pushButton.clicked.connect(lambda: self.check_password(self.username_le.text()))
            
    def check_password(self,password):
        if password == self.user_password:
            user_password=self.controller.get_password(self.username_save)
            self.show_information(f"Your Password is {user_password}")
            self.close()
            self.login.show()
            
            
    def show_information(self, message: str) -> None:
        """make a messagebox to show errors to user.

        Args:
            message (str): It's an error message that when inputs are invalid throw.
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()
            

            


