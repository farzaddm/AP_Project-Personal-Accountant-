from PyQt6 import QtCore, QtGui, QtWidgets
from Controlers.transaction_controllet import TransactionController


class Ui_Category(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(316, 146)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.category_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.category_lbl.setFont(font)
        self.category_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.category_lbl)
        
        self.le_category = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.verticalLayout.addWidget(self.le_category)
        
        self.add_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_btn.clicked.connect(self.add_btn_clicked)
        self.verticalLayout.addWidget(self.add_btn)
        # self.add_btn.setStyleSheet("""
        #     QPushButton {
        #         background-color: #0763e5;
        #         color: #ffffff;
        #         font-size: 12px;
        #     }
        #     QPushButton:hover {
        #         background-color:#1AA7EC ;
        #     }
        #     QPushButton:pressed {
        #         background-color: #1AA7EC;
        #     }
        # """)

        
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 22))

        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)

        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtGui.QAction(parent=MainWindow)
        self.actionhelp = QtGui.QAction(parent=MainWindow)

        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionexit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionhelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.controller = TransactionController(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add category"))
        self.category_lbl.setText(_translate("MainWindow", "Add Category"))
        self.le_category.setPlaceholderText(
            _translate("MainWindow", "Enter category name"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionhelp.setText(_translate("MainWindow", "help"))
    
    def add_btn_clicked(self) -> None:
        if self.le_category.text():
            self.controller.add_category(self.le_category.text())
        else:
            self.show_error("Please write name of your category")
            
    def show_error(self, message: str) -> None:
        """make a messagebox to show errors to user.

        Args:
            message (str): It's an error message that when inputs are invalid throw.
        """
        
        self.le_category.setStyleSheet("border: 1px solid red")
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()
