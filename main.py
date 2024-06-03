import sys
from PyQt6 import QtWidgets, uic
from Views.start_window import Signupandlogin

class MainWindow(QtWidgets.QMainWindow, Signupandlogin):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
sign_up_window = MainWindow()
sign_up_window.setWindowTitle("Login and SignUp")
sign_up_window.show()
app.exec()
