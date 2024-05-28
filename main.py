import sys
from PyQt6 import QtWidgets, uic
from Views.signUp import Ui_SignUp
from Views.recordIncome import Ui_RecordIncome
from Views.recordCost import Ui_RecordCost
from Controlers.user_controller import UserController

class sign_up(QtWidgets.QMainWindow, Ui_RecordCost):
    def __init__(self, *args, obj=None, **kwargs):
        super(sign_up, self).__init__(*args, **kwargs)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
sign_up_window = sign_up()
sign_up_window.show()
app.exec()
