import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, uic, QtGui, QtCore


def relpath(path):
    return os.path.join(os.path.dirname(__file__), path)

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.mainView = LoginWindow()
        self.mainView.show()

class LoginWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(LoginWindow, self).__init__(*args, **kwargs)
        uic.loadUi(relpath('view/loginWindow.ui'), self)

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())