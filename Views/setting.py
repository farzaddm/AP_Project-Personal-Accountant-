from PyQt6 import QtCore, QtGui, QtWidgets
from Controlers.user_controller import UserController


class Ui_Setting(object):
    def setupUi(self, MainWindow):
        self.controller = UserController(self)

        MainWindow.resize(764, 503)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()

        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()

        self.verticalLayout_7 = QtWidgets.QVBoxLayout()

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()

        self.username_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.verticalLayout_3.addWidget(self.username_lbl)
        self.pic_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.pic_lbl.setMinimumSize(QtCore.QSize(150, 150))
        self.pic_lbl.setMaximumSize(QtCore.QSize(150, 150))
        self.pic_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.pic_lbl)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.add_pic_btn = QtWidgets.QPushButton(parent=self.centralwidget)

        self.verticalLayout.addWidget(self.add_pic_btn)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.theme_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout.addWidget(self.theme_lbl)
        self.theme_combo = QtWidgets.QComboBox(parent=self.centralwidget)

        self.theme_combo.addItem("")
        self.theme_combo.addItem("")
        self.horizontalLayout.addWidget(self.theme_combo)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()

        self.menu_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout_18.addWidget(self.menu_lbl)
        self.menu_combo = QtWidgets.QComboBox(parent=self.centralwidget)

        self.horizontalLayout_18.addWidget(self.menu_combo)
        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19.addLayout(self.verticalLayout_7)
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.horizontalLayout_19.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()

        # self.horizontalLayout_6 = QtWidgets.QHBoxLayout()

        # self.username_lbl_4 = QtWidgets.QLabel(parent=self.centralwidget)

        # self.horizontalLayout_6.addWidget(self.username_lbl_4)
        # self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        # self.id_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        # self.horizontalLayout_2.addWidget(self.id_lbl)
        # self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.email_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout_3.addWidget(self.email_lbl)
        self.le_email = QtWidgets.QLineEdit(parent=self.centralwidget)

        self.horizontalLayout_3.addWidget(self.le_email)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()

        self.phone_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout_4.addWidget(self.phone_lbl)
        self.le_phone = QtWidgets.QLineEdit(parent=self.centralwidget)

        self.horizontalLayout_4.addWidget(self.le_phone)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()

        self.firstname_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout_7.addWidget(self.firstname_lbl)
        self.le_fname = QtWidgets.QLineEdit(parent=self.centralwidget)

        self.horizontalLayout_7.addWidget(self.le_fname)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()

        self.lastname_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout_9.addWidget(self.lastname_lbl)
        self.le_lname = QtWidgets.QLineEdit(parent=self.centralwidget)

        self.horizontalLayout_9.addWidget(self.le_lname)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()

        self.password_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout_10.addWidget(self.password_lbl)
        self.le_password = QtWidgets.QLineEdit(parent=self.centralwidget)

        self.horizontalLayout_10.addWidget(self.le_password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()

        self.city_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout_11.addWidget(self.city_lbl)
        self.le_city = QtWidgets.QLineEdit(parent=self.centralwidget)

    # -------
        cities = ["Tehran", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Karaj",
                  "Qom", "Ahvaz", "Kermanshah", "Urmia", "Yazd", "Bushehr", "Semnan"]
        completer = QtWidgets.QCompleter(cities)
        self.le_city.setCompleter(completer)

        self.horizontalLayout_11.addWidget(self.le_city)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()

        self.sequrity_q_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout_12.addWidget(self.sequrity_q_lbl)
        self.le_security_q = QtWidgets.QLineEdit(parent=self.centralwidget)

        self.horizontalLayout_12.addWidget(self.le_security_q)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()

        self.birthday_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.horizontalLayout_13.addWidget(self.birthday_lbl)
        self.le_birthday = QtWidgets.QDateTimeEdit(parent=self.centralwidget)
        self.le_birthday.setMaximumDate(QtCore.QDate(2005, 12, 31))
        self.le_birthday.setMinimumDate(QtCore.QDate(1920, 9, 14))
        self.le_birthday.setCalendarPopup(True)
        self.le_birthday.dateTimeChanged.connect(self.date_change)

        self.horizontalLayout_13.addWidget(self.le_birthday)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_19.addLayout(self.verticalLayout_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        self.line_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()

        self.save_info_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_info_btn.clicked.connect(self.update_user)

        self.verticalLayout_4.addWidget(self.save_info_btn)
        self.del_user_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.del_user_btn.clicked.connect(self.delete_user)

        self.verticalLayout_4.addWidget(self.del_user_btn)
        self.export_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.export_btn.clicked.connect(self.export_to_csv)

        self.verticalLayout_4.addWidget(self.export_btn)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)

        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 22))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.is_date_change = False
        self.get_information()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_lbl.setText(_translate("MainWindow", "username"))
        self.pic_lbl.setText(_translate("MainWindow", "pic"))
        self.add_pic_btn.setText(_translate("MainWindow", "Upload Picture"))
        self.theme_lbl.setText(_translate("MainWindow", "Theme:"))
        self.theme_combo.setItemText(0, _translate("MainWindow", "Dark"))
        self.theme_combo.setItemText(1, _translate("MainWindow", "Light"))
        self.menu_lbl.setText(_translate("MainWindow", "Menu Position:"))
        # self.username_lbl_4.setText(_translate("MainWindow", "username"))
        # self.id_lbl.setText(_translate("MainWindow", "id"))
        self.email_lbl.setText(_translate("MainWindow", "Email"))
        self.le_email.setPlaceholderText(
            _translate("MainWindow", "New email..."))
        self.phone_lbl.setText(_translate("MainWindow", "Phone"))
        self.le_phone.setPlaceholderText(
            _translate("MainWindow", "New phone number..."))
        self.firstname_lbl.setText(_translate("MainWindow", "First name"))
        self.le_fname.setPlaceholderText(
            _translate("MainWindow", "New first name..."))
        self.lastname_lbl.setText(_translate("MainWindow", "Last name"))
        self.le_lname.setPlaceholderText(
            _translate("MainWindow", "New last name..."))
        self.password_lbl.setText(_translate("MainWindow", "Password"))
        self.le_password.setPlaceholderText(
            _translate("MainWindow", "New password..."))
        self.city_lbl.setText(_translate("MainWindow", "City"))
        self.le_city.setPlaceholderText(
            _translate("MainWindow", "New city..."))
        self.sequrity_q_lbl.setText(_translate(
            "MainWindow", "Security question"))
        self.le_security_q.setPlaceholderText(_translate(
            "MainWindow", "What\'s your favorite color?..."))
        self.birthday_lbl.setText(_translate("MainWindow", "Birthday"))
        self.le_birthday.setDisplayFormat(
            _translate("MainWindow", "yyyy-MM-dd"))
        self.save_info_btn.setText(_translate("MainWindow", "Save Changes"))
        self.del_user_btn.setText(_translate("MainWindow", "Delete User"))
        self.export_btn.setText(_translate("MainWindow", "Export to CSV"))
        self.pushButton_3.setText(_translate(
            "MainWindow", "Clear Transactions"))

    def get_information(self) -> None:
        info = self.controller.get_information(self.username)
        self.username_lbl.setText(info[0])
        self.firstname_lbl.setText(info[1])
        self.lastname_lbl.setText(info[2])
        self.email_lbl.setText(info[3])
        self.password_lbl.setText(info[4])
        self.phone_lbl.setText(info[5])
        self.city_lbl.setText(info[6])
        self.birthday_lbl.setText(info[7])
        self.sequrity_q_lbl.setText(info[8])
    
    def date_change(self) -> None:
        self.is_date_change = True
        
    def update_user(self) -> None:
        changes = {}
        if self.le_email.text():
            changes["email"] = self.le_email.text()
            self.le_email.setText("")
            
        if self.le_phone.text():
            changes["phone"] = self.le_phone.text()
            self.le_phone.setText("")
            
        if self.le_fname.text():
            changes["first_name"] = self.le_fname.text()
            self.le_fname.setText("")
            
        if self.le_lname.text():
            changes["last_name"] = self.le_lname.text()
            self.le_lname.setText("")
            
        if self.le_password.text():
            changes["password"] = self.le_password.text()
            self.le_password.setText("")
            
        if self.le_city.text():
            changes["city"] = self.le_city.text()
            self.le_city.setText("")
            
        if self.le_security_q.text():
            changes["security_q"] = self.le_security_q.text()
            self.le_security_q.setText("")
            
        if self.is_date_change:
            changes["birthday"] = self.le_birthday.text()
            

        self.controller.update_user(changes, self.username)
        self.get_information()

    def delete_user(self) -> None:
        self.controller.delete_user(self.username)
        #? what to do after???
    
    def export_to_csv(self) -> None:
        self.controller.export_to_csv(self.username)
        
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
