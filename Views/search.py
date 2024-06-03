from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView, QSizePolicy
from Controlers.transaction_controllet import TransactionController


class Ui_Search(object):
    # def __init__(self):
    #     self.username="name"
    def setupUi(self, MainWindow):
        MainWindow.resize(650, 571)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("""
        QLineEdit{
            border:none;
            border-radius: 8px;
        }
        QPushButton{
            border=none;
            border-radius:8px;
            background-color: #0763e5;
            color:white;
        }
        QPushButton:hover {
                        background-color:#1AA7EC ;
        }
        QPushButton:pressed {
            background-color: #1AA7EC;
        }
        """)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.le_search = QtWidgets.QLineEdit(parent=self.centralwidget)

        self.verticalLayout.addWidget(self.le_search)
        self.time_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.verticalLayout.addWidget(self.time_lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.chb_daily = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout.addWidget(self.chb_daily)
        self.chb_monthly = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout.addWidget(self.chb_monthly)
        self.chb_yearly = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout.addWidget(self.chb_yearly)
        self.chb_no_choice_time = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout.addWidget(self.chb_no_choice_time)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.type_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.verticalLayout.addWidget(self.type_lbl)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()

        self.chb_cheque = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_5.addWidget(self.chb_cheque)
        self.chb_cash = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_5.addWidget(self.chb_cash)
        self.chb_digital_c = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_5.addWidget(self.chb_digital_c)
        
        self.chb_no_choice_price_type = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.horizontalLayout_5.addWidget(self.chb_no_choice_price_type)
        
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.group_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.verticalLayout.addWidget(self.group_lbl)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()

        self.chb_description = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_4.addWidget(self.chb_description)
        self.chb_category = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_4.addWidget(self.chb_category)
        
        self.chb_no_choice_info = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.horizontalLayout_4.addWidget(self.chb_no_choice_info)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.le_min_amount = QtWidgets.QLineEdit(parent=self.centralwidget)

        self.horizontalLayout_3.addWidget(self.le_min_amount)
        self.le_max_amount = QtWidgets.QLineEdit(parent=self.centralwidget)

        self.horizontalLayout_3.addWidget(self.le_max_amount)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        self.chb_income = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_2.addWidget(self.chb_income)
        self.chb_expense = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_2.addWidget(self.chb_expense)
        
        self.chb_no_choice_type = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.horizontalLayout_2.addWidget(self.chb_no_choice_type)
        
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_search = QtWidgets.QPushButton(parent=self.centralwidget)

        self.verticalLayout.addWidget(self.btn_search)
        self.table = QtWidgets.QTableWidget(parent=self.centralwidget)

        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setCascadingSectionResizes(False)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addWidget(self.table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 22))

        self.menuFile = QtWidgets.QMenu(parent=self.menubar)

        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)

        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtGui.QAction(parent=MainWindow)

        self.actionhelp = QtGui.QAction(parent=MainWindow)

        self.menuFile.addAction(self.actionexit)
        self.menuHelp.addAction(self.actionhelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.btn_search.clicked.connect(self.btn_search_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.time_group = QtWidgets.QButtonGroup()
        self.time_group.addButton(self.chb_daily)
        self.time_group.addButton(self.chb_monthly)
        self.time_group.addButton(self.chb_yearly)
        self.time_group.addButton(self.chb_no_choice_time)

        self.info_group = QtWidgets.QButtonGroup()
        self.info_group.addButton(self.chb_description)
        self.info_group.addButton(self.chb_category)
        self.info_group.addButton(self.chb_no_choice_info)
        

        self.type_group = QtWidgets.QButtonGroup()
        self.type_group.addButton(self.chb_income)
        self.type_group.addButton(self.chb_expense)
        self.type_group.addButton(self.chb_no_choice_type)
        

        self.price_group = QtWidgets.QButtonGroup()
        self.price_group.addButton(self.chb_cheque)
        self.price_group.addButton(self.chb_cash)
        self.price_group.addButton(self.chb_digital_c)
        self.price_group.addButton(self.chb_no_choice_price_type)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.le_search.setPlaceholderText(
            _translate("MainWindow", "Search..."))
        self.time_lbl.setText(_translate(
            "MainWindow", "Time filter (Optional):"))
        self.chb_daily.setText(_translate("MainWindow", "Daily"))
        self.chb_monthly.setText(_translate("MainWindow", "Monthly"))
        self.chb_yearly.setText(_translate("MainWindow", "Yearly"))
        self.chb_no_choice_time.setText(_translate("MainWindow", "No Choice"))
        self.chb_no_choice_info.setText(_translate("MainWindow", "No Choice"))
        self.chb_no_choice_type.setText(_translate("MainWindow", "No Choice"))
        self.chb_no_choice_price_type.setText(_translate("MainWindow", "No Choice"))
        
        self.group_lbl.setText(_translate(
            "MainWindow", "Choose group (Optional):"))
        self.chb_description.setText(_translate("MainWindow", "Descripption"))
        self.chb_category.setText(_translate("MainWindow", "Source"))
        self.type_lbl.setText(_translate(
            "MainWindow", "type of price (Optional):"))
        self.chb_cheque.setText(_translate("MainWindow", "Cheque"))
        self.chb_cash.setText(_translate("MainWindow", "Cash"))
        self.chb_digital_c.setText(_translate(
            "MainWindow", "Digital currencies"))
        self.le_min_amount.setPlaceholderText(
            _translate("MainWindow", "Min amount"))
        self.le_max_amount.setPlaceholderText(
            _translate("MainWindow", "Max amount"))
        self.chb_income.setText(_translate("MainWindow", "Income"))
        self.chb_expense.setText(_translate("MainWindow", "Cost"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Type"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Source"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Description"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Type of price"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionhelp.setText(_translate("MainWindow", "help"))

    def btn_search_clicked(self):
        self.table.setRowCount(0)
        self.controller = TransactionController(self)
        search_text = self.le_search.text().capitalize()

        filter_search = {
            "type": "",
            "group": "",
            "time": "",
            "min_amount": "",
            "max_amount": "",
            "type_price": ""
        }

        if self.chb_daily.isChecked():
            filter_search["time"] = "daily"
        elif self.chb_monthly.isChecked():
            filter_search["time"] = "monthly"
        elif self.chb_yearly.isChecked():
            filter_search["time"] = "yearly"

        if self.chb_description.isChecked():
            filter_search["group"] = "description"
        elif self.chb_category.isChecked():
            filter_search["group"] = "source_of_price"

        if self.chb_digital_c.isChecked():
            filter_search["type_price"] = "Digital currencies"
        elif self.chb_cash.isChecked():
            filter_search["type_price"] = "Cash"
        elif self.chb_cheque.isChecked():
            filter_search["type_price"] = "Cheque"

        if self.chb_income.isChecked():
            filter_search["type"] = "income"
        elif self.chb_expense.isChecked():
            filter_search["type"] = "cost"

        if self.le_max_amount.text():
            if self.le_max_amount.text().isnumeric():
                filter_search["max_amount"] = self.le_max_amount.text()
            else:
                self.show_error("The max has to be integer")
                return
        if self.le_min_amount.text():
            if self.le_min_amount.text().isnumeric():
                filter_search["min_amount"] = self.le_min_amount.text()
            else:
                self.show_error("The min has to be integer")
                return

        data = self.controller.search(search_text, filter_search, self.username)
        if data:
            self.add_row_to_table(data)
        else:
            self.show_error("There was not any result.")

    def add_row_to_table(self, data: list) -> None:
        self.table.setRowCount(len(data))

        for row_id, row_data in enumerate(data):
            for item_id, item in enumerate(row_data[1:]):
                self.table.setItem(
                    row_id, item_id, QtWidgets.QTableWidgetItem(str(item)))

    def show_error(self, message: str) -> None:
        """make a messagebox to show errors to user.

        Args:
            message (str): It's an error message that when inputs are invalid throw.
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()
