import sys
import os


from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, uic, QtGui, QtCore, QtWebEngineWidgets

from view.viewFactory import ViewFactory
from emailManager import EmailManager


def relpath(path):
    return os.path.join(os.path.dirname(__file__), path)

class App(QApplication):
    viewFactory: ViewFactory
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.viewFactory = ViewFactory(EmailManager())
        self.viewFactory.showLoginWindow()

        # self.mainView = LoginWindow()
        # self.mainView.show()

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(LoginWindow, self).__init__(*args, **kwargs)
        uic.loadUi(relpath('view/mainWindow.ui'), self)



        url = "https://www.google.co.jp"
        self.emailWebView.setUrl(QtCore.QUrl(url))

if __name__ == '__main__':

    app = App(sys.argv)
    sys.exit(app.exec_())