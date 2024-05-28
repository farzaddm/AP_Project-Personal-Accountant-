# Form implementation generated from reading ui file 'mainwindow4.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(5, 10, 821, 561))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(r"pictures\lock.PNG"))
        self.background.setObjectName("background")
        self.forget_l = QtWidgets.QLabel(parent=self.centralwidget)
        self.forget_l.setGeometry(QtCore.QRect(350, 260, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(25)
        self.forget_l.setFont(font)
        self.forget_l.setObjectName("forget_l")
        self.password_l = QtWidgets.QLabel(parent=self.centralwidget)
        self.password_l.setGeometry(QtCore.QRect(330, 290, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(25)
        self.password_l.setFont(font)
        self.password_l.setObjectName("password_l")
        self.question_l = QtWidgets.QLabel(parent=self.centralwidget)
        self.question_l.setGeometry(QtCore.QRect(280, 370, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(15)
        self.question_l.setFont(font)
        self.question_l.setObjectName("question_l")
        self.LineEdit_l = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LineEdit_l.setGeometry(QtCore.QRect(255, 410, 291, 31))
        self.LineEdit_l.setObjectName("LineEdit_l")
        self.next_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(290, 470, 231, 31))
        self.next_btn.setObjectName("pushButton")
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
        self.forget_l.setText(_translate("MainWindow", "Forget"))
        self.password_l.setText(_translate("MainWindow", "Password"))
        self.question_l.setText(_translate("MainWindow", "What is your favorite color ? "))
        self.next_btn.setText(_translate("MainWindow", "Next ->"))
