from PyQt6 import QtCore, QtGui, QtWidgets


class Show:
    """Qmessage box to show errors in app.
    """
    def __init__(self, type1, message: str, title: str) -> None:
        self.type = type1
        self.message = message
        self.title = title
        self.show()

    def show(self):
        """Make a QMessageBox.
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(self.type)
        msg.setText(self.message)
        msg.setWindowTitle(self.title)
        msg.exec()
