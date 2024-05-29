from PyQt6 import QtCore, QtGui, QtWidgets


class ForgetPassword(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("hello")
        MainWindow.resize(800, 600)
        
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(25)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.background = QtWidgets.QLabel(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(5, 10, 821, 561))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("pictures/lock.PNG"))

        self.forget_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.forget_lbl.setGeometry(QtCore.QRect(350, 260, 121, 51))
        self.forget_lbl.setFont(font)
        
        self.password_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.password_lbl.setGeometry(QtCore.QRect(330, 290, 171, 51))
        self.password_lbl.setFont(font)
        self.question_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        
        font.setPointSize(15)
        self.question_lbl.setGeometry(QtCore.QRect(280, 370, 291, 41))
        self.question_lbl.setFont(font)
        
        self.LineEdit_l = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LineEdit_l.setGeometry(QtCore.QRect(255, 410, 291, 31))
        
        self.next_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(290, 470, 231, 31))
        self.next_btn.setStyleSheet("""
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.forget_lbl.setText(_translate("MainWindow", "Forget"))
        self.password_lbl.setText(_translate("MainWindow", "Password"))
        self.question_lbl.setText(_translate("MainWindow", "What is your favorite color ? "))
        self.next_btn.setText(_translate("MainWindow", "Next ->"))
