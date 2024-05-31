from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView


class Ui_Search(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(624, 471)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.group_lbl = QtWidgets.QLabel(parent=self.centralwidget)

        self.verticalLayout.addWidget(self.group_lbl)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()

        self.chb_description = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_4.addWidget(self.chb_description)
        self.chb_category = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_4.addWidget(self.chb_category)
        self.chb_source = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.horizontalLayout_4.addWidget(self.chb_source)
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
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_search = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_search.clicked.connect(self.btn_search_clicked)

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

        self.verticalLayout.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 22))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.group_lbl.setText(_translate(
            "MainWindow", "Choose group (Optional):"))
        self.chb_description.setText(_translate("MainWindow", "Descripption"))
        self.chb_category.setText(_translate("MainWindow", "Category"))
        self.chb_source.setText(_translate("MainWindow", "Source"))
        self.le_min_amount.setPlaceholderText(
            _translate("MainWindow", "Min amount"))
        self.le_max_amount.setPlaceholderText(
            _translate("MainWindow", "Max amount"))
        self.chb_income.setText(_translate("MainWindow", "Income"))
        self.chb_expense.setText(_translate("MainWindow", "Expense"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Type"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionhelp.setText(_translate("MainWindow", "help"))


    def btn_search_clicked(self):
        pass