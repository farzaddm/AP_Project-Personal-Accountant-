from PyQt6 import QtCore, QtGui, QtWidgets

class OpeningWindow:
    def __init__(self,current_page,next_page,title):
        class MainWindow(QtWidgets.QMainWindow,next_page):
            def __init__(self):
                super().__init__()
                self.setupUi(self)

        self.ui=MainWindow()
        self.ui.show()
        self.ui.setWindowTitle(title)
        current_page.close()