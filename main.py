import sys
from PyQt6 import QtWidgets, uic
from Views.sign_up import Ui_SignUp
from Views.record_income import Ui_RecordIncome
from Views.record_cost import Ui_RecordCost
from Controlers.user_controller import UserController
from Views.start_window import *
class MainWindow(QtWidgets.QMainWindow, Signupandlogin):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
sign_up_window = MainWindow()
sign_up_window.setWindowTitle("Login and SignUp")
sign_up_window.show()
app.exec()
