from PyQt6 import QtCore, QtGui, QtWidgets
from Controlers.transaction_controllet import TransactionController
from Utils.show import Show
from Views.font import Font_detail


class Ui_RecordIncome(object):
    def __init__(self):
        self.username = "name"
        self.style = "style"
        self.font=Font_detail()

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.resize(310, 448)
        self.MainWindow.setMinimumSize(QtCore.QSize(300, 448))
        self.MainWindow.setMaximumSize(QtCore.QSize(300, 448))
        self.controller = TransactionController(self)
        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)

        self.le_Income = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.le_Income.setGeometry(QtCore.QRect(10, 30, 271, 31))

        self.le_discription = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.le_discription.setGeometry(QtCore.QRect(10, 260, 271, 81))
        self.le_discription.setMaxLength(100)

        self.sumbit_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sumbit_btn.setGeometry(QtCore.QRect(10, 370, 271, 31))
        self.sumbit_btn.clicked.connect(self.btn_submit_clicked)

        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 350, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setGeometry(QtCore.QRect(10, 90, 271, 31))
        self.dateEdit.setCalendarPopup(True)

        self.date_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.date_lbl.setGeometry(QtCore.QRect(10, 70, 122, 17))

        self.combo_source = QtWidgets.QComboBox(parent=self.centralwidget)
        self.combo_source.setGeometry(QtCore.QRect(10, 150, 271, 31))
        self.source_of_income_update()
        self.combo_source.setCurrentIndex(-1)

        self.source_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.source_lbl.setGeometry(QtCore.QRect(10, 130, 122, 17))

        self.type_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.type_lbl.setGeometry(QtCore.QRect(10, 190, 108, 17))

        self.combo_incom_type = QtWidgets.QComboBox(parent=self.centralwidget)
        self.combo_incom_type.setGeometry(QtCore.QRect(10, 210, 271, 31))
        self.combo_incom_type.setAutoFillBackground(False)
        self.combo_incom_type.setDuplicatesEnabled(False)
        self.combo_incom_type.addItem("")
        self.combo_incom_type.addItem("")
        self.combo_incom_type.addItem("")
        self.combo_incom_type.setCurrentIndex(-1)

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)

        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.MainWindow)

        self.MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtGui.QAction(parent=self.MainWindow)
        self.actionhelp = QtGui.QAction(parent=self.MainWindow)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionexit)
        self.menuHelp.addAction(self.actionhelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("RecordIncome", "RecordIncome"))
        self.le_Income.setPlaceholderText(_translate("MainWindow", "Income"))
        self.le_discription.setPlaceholderText(
            _translate("MainWindow", "Description"))
        self.sumbit_btn.setText(_translate("MainWindow", "Submit"))
        self.date_lbl.setText(_translate("MainWindow", "Date of income:"))
        self.source_lbl.setText(_translate("MainWindow", "Source of income:"))
        self.type_lbl.setText(_translate("MainWindow", "Type of income:"))
        self.combo_incom_type.setItemText(0, _translate("MainWindow", "Cash"))
        self.combo_incom_type.setItemText(
            1, _translate("MainWindow", "Cheque"))
        self.combo_incom_type.setItemText(
            2, _translate("MainWindow", "Digital currencies"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionhelp.setText(_translate("MainWindow", "help"))

    def btn_submit_clicked(self):
        result = self.controller.record_income()
        if result != None:
            Show(QtWidgets.QMessageBox.Icon.Information,
                 "Your Income Has Added", "Income Added")
            QtCore.QTimer.singleShot(1000, self.hide)

    def source_of_income_update(self):
        try:
            source_of_income = self.controller.get_source_of_price(
                self.username)
            for sources in source_of_income:
                self.combo_source.addItem(sources[0])
        except:
            Show(QtWidgets.QMessageBox.Icon.Critical,
                 "Category Not Exists", "category error")
