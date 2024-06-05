from PyQt6 import QtCore, QtGui, QtWidgets


class Show:
    def __init__(self,type1,message,title):
        self.type=type1
        self.message=message
        self.title=title
        self.show()
    def show(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(self.type)
        msg.setText(self.message)
        msg.setWindowTitle(self.title)
        msg.exec()



