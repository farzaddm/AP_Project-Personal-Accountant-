

from PyQt6 import QtWidgets, uic

from SignuporLogin import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):

        super().__init__()

        self.setupUi(self)

app = QtWidgets.QApplication([])

window = MainWindow()



window.show()


app.exec()