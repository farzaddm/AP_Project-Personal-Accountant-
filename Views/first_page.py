from PyQt6 import QtCore, QtGui, QtWidgets
from Views.record_income import *
from Views.record_cost import *
from Views.category import Ui_Category
from Views.search import Ui_Search
from Views.reporting import Ui_Reporting
from Views.setting import Ui_Setting
from Views.mode import SetSetyling
from Views.font import Font_detail
from Utils.show import Show


class Buttons(QtWidgets.QPushButton):
    def __init__(self, parent, text):
        super().__init__(parent=parent)
        self.setText(text)


class Pics(QtWidgets.QLabel):
    def __init__(self, parent, type, pic):
        super().__init__(parent=parent)
        self.setPixmap(QtGui.QPixmap(pic))


class Ui_Firstpage(object):
    def __init__(self) -> None:
        self.username = "name"
        self.style = "style"
        self.login_page = "loginpage"
        self.font=Font_detail()

    def setupUi(self, MainWindow) -> None:
        self.MainWindow = MainWindow
        self.MainWindow.resize(1000, 600)
        pics = [r"pictures/recordincome.PNG", r"pictures/costregistration.PNG", r"pictures/category.PNG", r"pictures/search.PNG",
                r"pictures/reporting.PNG", r"pictures/setting.PNG", r"pictures/exit.PNG"]
        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)

        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(27 * self.font.font_size)

        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 100, 691, 428))

        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.usernmae_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.usernmae_lbl.setText(f"Username:{self.username}😊")
        self.usernmae_lbl.setGeometry(20, 5, 200+len(self.username)*5, 50)
        username_font = QtGui.QFont()
        username_font.setPointSize(12* self.font.font_size)
        self.usernmae_lbl.setFont(username_font)

        self.costregistration_lbl = Pics(
            parent=self.centralwidget, type="Cost Registration", pic=pics[0])
        self.verticalLayout.addWidget(self.costregistration_lbl)

        self.recordincome_btn = Buttons(
            parent=self.centralwidget, text="Record income")
        self.verticalLayout.addWidget(self.recordincome_btn)

        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()

        self.recordincome_lbl = Pics(
            parent=self.centralwidget, type="Record income", pic=pics[1])
        self.recordincome_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.recordincome_btn.clicked.connect(self.btn_recordincome_clicked)
        self.verticalLayout_2.addWidget(self.recordincome_lbl)

        self.costregistration_btn = Buttons(
            parent=self.centralwidget, text="Cost registration")
        self.costregistration_btn.clicked.connect(self.btn_recordcost_clicked)
        self.verticalLayout_2.addWidget(self.costregistration_btn)

        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()

        self.catgory_lbl = Pics(parent=self.centralwidget,
                                type="Category", pic=pics[2])
        self.catgory_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_3.addWidget(self.catgory_lbl)

        self.category_btn = Buttons(parent=self.centralwidget, text="Category")
        self.category_btn.clicked.connect(self.btn_category_clicked)
        self.verticalLayout_3.addWidget(self.category_btn)

        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 3, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()

        self.search_lbl = Pics(parent=self.centralwidget,
                               type="Search", pic=pics[3])
        self.search_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_4.addWidget(self.search_lbl)

        self.search_btn = Buttons(parent=self.centralwidget, text="Search")
        self.search_btn.clicked.connect(self.btn_search_clicked)
        self.verticalLayout_4.addWidget(self.search_btn)

        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 5, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()

        self.reporting_lbl = Pics(
            parent=self.centralwidget, type="Reporting", pic=pics[4])
        self.reporting_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_5.addWidget(self.reporting_lbl)

        self.reporting_btn = Buttons(
            parent=self.centralwidget, text="Reporting")
        self.reporting_btn.clicked.connect(self.btn_reporting_clicked)
        self.verticalLayout_5.addWidget(self.reporting_btn)

        self.gridLayout_3.addLayout(self.verticalLayout_5, 1, 0, 1, 2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()

        self.setting_lbl = Pics(parent=self.centralwidget,
                                type="Setting", pic=pics[5])
        self.setting_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_6.addWidget(self.setting_lbl)

        self.setting_btn = Buttons(parent=self.centralwidget, text="Setting")
        self.setting_btn.clicked.connect(self.btn_setting_clicked)
        self.verticalLayout_6.addWidget(self.setting_btn)

        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 2, 1, 2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()

        self.exit_lbl = Pics(parent=self.centralwidget,
                             type="Exit", pic=pics[6])
        self.exit_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_7.addWidget(self.exit_lbl)

        self.exit_btn = Buttons(parent=self.centralwidget, text="Exit")
        self.exit_btn.clicked.connect(self.close_window_by_exit)
        self.verticalLayout_7.addWidget(self.exit_btn)

        self.gridLayout_3.addLayout(self.verticalLayout_7, 1, 4, 1, 2)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 20, 151, 81))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.MainWindow)
        self.MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def btn_recordincome_clicked(self) -> None:
        self.open_window_incomepage(self.username)

    def btn_recordcost_clicked(self) -> None:
        self.open_window_costpage(self.username)

    def btn_category_clicked(self) -> None:
        self.open_window_categorypage(self.username)

    def btn_search_clicked(self) -> None:
        self.open_window_searchpage(self.username)

    def btn_reporting_clicked(self) -> None:
        self.open_window_reportingpage(self.username)

    def btn_setting_clicked(self) -> None:
        self.open_window_setting(self.username)

    def open_window_searchpage(self, username: str) -> None:
        class Ui_Search_FirstPage(QtWidgets.QMainWindow, Ui_Search):
            def __init__(self):
                super().__init__()

                self.username = username
                self.setupUi(self)
                self.style = SetSetyling(self)
        self.ui = Ui_Search_FirstPage()
        self.ui.show()
        self.ui.setWindowTitle("Search Page")

    def open_window_incomepage(self, username: str) -> None:
        class Ui_Income_FirstPage(QtWidgets.QMainWindow, Ui_RecordIncome):
            def __init__(self):
                super().__init__()

                self.username = username
                self.setupUi(self)
                self.style = SetSetyling(self)
        self.ui = Ui_Income_FirstPage()
        self.ui.show()
        self.ui.setWindowTitle("Income Page")

    def open_window_costpage(self, username: str) -> None:
        class Ui_Cost_FirstPage(QtWidgets.QMainWindow, Ui_RecordCost):
            def __init__(self):
                super().__init__()

                self.username = username
                self.setupUi(self)
                self.style = SetSetyling(self)
        self.ui = Ui_Cost_FirstPage()
        self.ui.show()
        self.ui.setWindowTitle("Cost Page")

    def open_window_categorypage(self, username: str) -> None:
        class Ui_Category_Login(QtWidgets.QMainWindow, Ui_Category):
            def __init__(self):
                super().__init__()

                self.username = username
                self.setupUi(self)
                self.style = SetSetyling(self)
        self.ui = Ui_Category_Login()
        self.ui.show()
        self.ui.setWindowTitle("Category Page")

    def open_window_reportingpage(self, username: str) -> None:
        class Ui_Report_Login(QtWidgets.QMainWindow, Ui_Reporting):
            def __init__(self):
                super().__init__()

                self.username = username
                self.setupUi(self)
                self.style = SetSetyling(self)
        self.ui = Ui_Report_Login()
        self.ui.show()
        self.ui.setWindowTitle("Reporting Page")

    def open_window_setting(self, username: str) -> None:
        class Ui_Setting_Login(QtWidgets.QMainWindow, Ui_Setting):
            def __init__(self):
                super().__init__()
                self.username = username
                self.setupUi(self)
                self.style = SetSetyling(self)
        self.ui = Ui_Setting_Login()
        self.ui.firstpage = self
        self.ui.loginpage = self.login_page
        self.ui.show()
        self.ui.setWindowTitle("Setting")

    def close_window_by_exit(self):
        Show(QtWidgets.QMessageBox.Icon.Information,
             "The App Will Close Soon ...", "Exist")
        self.close()
