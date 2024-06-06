from PyQt6 import QtCore, QtGui, QtWidgets
from Controlers.user_controller import UserController
from Views.mode import SetSetyling


class Pics(QtWidgets.QLabel):
    def __init__(self, parent, type, pic, width, height):
        super().__init__(parent=parent)
        pixmap = QtGui.QPixmap(pic)
        if width and height:
            pixmap = pixmap.scaled(width, height, QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                   QtCore.Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(pixmap)


class Ui_Setting(object):

    def __init__(self) -> None:
        self.firstpage = "firstpage"
        self.loginpage = "loginpage"
        self.username = "name"
        self.style = "style"

    def setupUi(self, MainWindow) -> None:
        self.controller = UserController(self)

        self.MainWindow = MainWindow
        self.MainWindow.resize(700, 400)

        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()

        self.username_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.verticalLayout_3.addWidget(self.username_lbl)
        self.pic_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.pic_lbl = Pics(self.centralwidget, "Set Pic", "?", None, None)
        self.verticalLayout_3.addWidget(self.pic_lbl)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_3.addWidget(self.pic_lbl)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.add_pic_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_pic_btn.clicked.connect(self.choosing_pic)

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

        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19.addLayout(self.verticalLayout_7)
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.horizontalLayout_19.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()

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

        self.save_info_btn.clicked.connect(self.update_user)

        self.verticalLayout_4.addWidget(self.save_info_btn)
        self.del_user_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.del_user_btn.clicked.connect(self.delete_user)

        self.del_user_btn.clicked.connect(self.delete_user)

        self.verticalLayout_4.addWidget(self.del_user_btn)
        self.export_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.export_btn.clicked.connect(self.get_backup)

        self.export_btn.clicked.connect(self.get_backup)

        self.verticalLayout_4.addWidget(self.export_btn)
        self.delete_transacation = QtWidgets.QPushButton(
            parent=self.centralwidget)
        self.delete_transacation.clicked.connect(self.clear_user_transacation)
        self.verticalLayout_4.addWidget(self.delete_transacation)
        self.save_mode = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_mode.setText("Save Mode")
        self.save_mode.clicked.connect(self.update_dark_and_light_mode)
        self.verticalLayout_4.addWidget(self.save_mode)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 22))

        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.MainWindow)

        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.is_date_change = False
        self.get_information()
        self.get_user_pic()

    def retranslateUi(self, MainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_lbl.setText(_translate("MainWindow", "username"))
        self.pic_lbl.setText(_translate("MainWindow", "pic"))
        self.add_pic_btn.setText(_translate("MainWindow", "Upload Picture"))
        self.theme_lbl.setText(_translate("MainWindow", "Theme:"))
        self.theme_combo.setItemText(0, _translate("MainWindow", "Dark"))
        self.theme_combo.setItemText(1, _translate("MainWindow", "Light"))
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
        self.le_password.setPlaceholderText(
            _translate("MainWindow", "New password..."))
        self.city_lbl.setText(_translate("MainWindow", "City"))
        self.le_city.setPlaceholderText(
            _translate("MainWindow", "New city..."))
        self.sequrity_q_lbl.setText(_translate(
            "MainWindow", "Security question"))
        self.le_security_q.setPlaceholderText(_translate(
            "MainWindow", "What\'s your favorite color?..."))
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
        self.export_btn.setText(_translate("MainWindow", "Get BackUp"))
        self.delete_transacation.setText(_translate(
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

    def clear_user_transacation(self) -> None:
        self.controller.delete_transacation_from_db(self.username)

    def delete_user(self) -> None:
        self.controller.delete_user(self.username)
        # ? what to do after???

    def get_backup(self) -> None:
        self.controller.export_to_json(self.username)

    def choosing_pic(self) -> None:
        options = QtWidgets.QFileDialog.Option.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select a File", "",
                                                             "All Files (*);;Text Files (*.txt);;Python Files (*.py)",
                                                             options=options)
        self.verticalLayout_3.removeWidget(self.pic_lbl)
        self.pic_lbl.deleteLater()

        self.pic_lbl = Pics(self.centralwidget, "Set Pic",
                            r"{R}".format(R=file_name), 200, 200)
        self.controller.update_user_pic(self.username, file_name)
        self.verticalLayout_3.addWidget(self.pic_lbl)

    def get_user_pic(self) -> None:
        file_name = self.controller.get_pic(self.username)
        self.verticalLayout_3.removeWidget(self.pic_lbl)
        self.pic_lbl.deleteLater()

        self.pic_lbl = Pics(self.centralwidget, "Set Pic",
                            r"{R}".format(R=file_name[0]), 200, 200)
        self.verticalLayout_3.addWidget(self.pic_lbl)

    def update_dark_and_light_mode(self) -> None:
        if self.theme_combo.currentText().lower() == "light":
            self.style.update("#ffffff", "#000000",
                              "#d3d3d3", "#0763e5", "#1AA7EC")
            SetSetyling.light_mode = True
        else:
            self.style.update("#282828", "#d7d7d7",
                              "#202020", "#1A1110", "#202020")
            SetSetyling.light_mode = False
        self.firstpage.close()
        self.loginpage.show()
        self.close()
