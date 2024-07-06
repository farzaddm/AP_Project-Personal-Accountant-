from PyQt6 import QtCore, QtGui, QtWidgets
from Controlers import user_controller
from Utils.show import Show
import asyncio
from Utils import contact_us
from Views.font import Font_detail

class Ui_ContactUs(object):
    def __init__(self):
        self.username="name"
        self.style="style"
        self.font=Font_detail()

    def setupUi(self, MainWindow):

        self.MainWindow=MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(490, 620)
        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")


        self.contactus_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(19 * self.font.font_size)
        self.contactus_lbl.setFont(font)
        self.contactus_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.contactus_lbl.setObjectName("contactus_lbl")
        self.verticalLayout.addWidget(self.contactus_lbl)


        self.justwrite_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7 * self.font.font_size)
        self.justwrite_lbl.setFont(font)
        self.justwrite_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.justwrite_lbl.setObjectName("justwrite_lbl")
        self.verticalLayout.addWidget(self.justwrite_lbl)


        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("QFrame { border: 1px solid black; }")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")


        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")


        self.firstname_lbl = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10 * self.font.font_size)
        self.firstname_lbl.setFont(font)
        self.firstname_lbl.setObjectName("firstname_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.firstname_lbl)

        self.firstname_le = QtWidgets.QLineEdit(parent=self.frame)
        self.firstname_le.setObjectName("firstname_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.firstname_le)


        self.lastname_lbl = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10 * self.font.font_size)
        self.lastname_lbl.setFont(font)
        self.lastname_lbl.setObjectName("lastname_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lastname_lbl)

        self.lastname_le = QtWidgets.QLineEdit(parent=self.frame)
        self.lastname_le.setObjectName("lastname_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lastname_le)


        self.email_lbl = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10 * self.font.font_size)
        self.email_lbl.setFont(font)
        self.email_lbl.setObjectName("email_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.email_lbl)

        self.email_le = QtWidgets.QLineEdit(parent=self.frame)
        self.email_le.setObjectName("email_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.email_le)


        self.phonenumber_lbl = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10 * self.font.font_size)
        self.phonenumber_lbl.setFont(font)
        self.phonenumber_lbl.setObjectName("phonenumber_lbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.phonenumber_lbl)

        self.phonenumber_le = QtWidgets.QLineEdit(parent=self.frame)
        self.phonenumber_le.setObjectName("phonenumber_le")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.phonenumber_le)


        self.message_lbl = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10 * self.font.font_size)
        self.message_lbl.setFont(font)
        self.message_lbl.setObjectName("message_lbl")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.message_lbl)

        self.message_te = QtWidgets.QTextEdit(parent=self.frame)
        self.message_te.setObjectName("message_te")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.message_te)


        self.send_btn = QtWidgets.QPushButton(parent=self.frame)
        self.send_btn.clicked.connect(self.clicked_send_btn)
        self.send_btn.setObjectName("send_btn")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.send_btn)

        self.verticalLayout.addWidget(self.frame)
        self.MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(parent=self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 25))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(parent=self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.MainWindow)
        self.controller=user_controller.UserController(self)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.contactus_lbl.setText(_translate("MainWindow", "Contact Us"))
        self.firstname_lbl.setText(_translate("MainWindow", "FirstName"))
        self.lastname_lbl.setText(_translate("MainWindow", "LastName"))
        self.email_lbl.setText(_translate("MainWindow", "Email"))
        self.phonenumber_lbl.setText(_translate("MainWindow", "PhoneNumber"))
        self.message_lbl.setText(_translate("MainWindow", "Message"))
        self.send_btn.setText(_translate("MainWindow", "Send Message"))
        self.justwrite_lbl.setText(_translate("MainWindow", "Just Write Us Message"))
    
    def clicked_send_btn(self):
        check=self.controller.contact_us()
        if check:
            message=f"""Hello {self.firstname_le.text()},{self.lastname_le.text()} with Email:{self.email_le.text()} and PhoneNumber:{self.phonenumber_le.text()} sent you message:{self.message_te.toPlainText()}"""
            asyncio.run(contact_us.send_message(message))
            # print(f"""Hello {self.firstname_le.text()} {self.lastname_le.text()}
            #     with Email:{self.email_le.text()} and PhoneNumber:{self.phonenumber_le.text()} sent you message:{self.message_te.toPlainText()}""")
            # self.controller.send_email(message=f"""Hello {self.firstname_le.text()},{self.lastname_le.text()} with Email:{self.email_le.text()} and PhoneNumber:{self.phonenumber_le.text()} sent you message:{self.message_te.toPlainText()}""")
            # Show(QtWidgets.QMessageBox.Icon.Information,"Your Email has Sent","Email Sent")
