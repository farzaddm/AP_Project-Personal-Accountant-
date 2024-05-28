import sys
from PyQt6 import QtWidgets, uic
from Views.signUp import Ui_SignUp
from Views.recordIncome import Ui_RecordIncome
from Views.recordCost import Ui_RecordCost
from Controlers.user_controller import UserController
from Views.SignuporLogin import *
class MainWindow(QtWidgets.QMainWindow, Signupandlogin):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
sign_up_window = MainWindow()
sign_up_window.setWindowTitle("Login and SignUp")
sign_up_window.show()
app.exec()
