import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, uic, QtGui, QtCore, QtWebEngineWidgets

from view.viewFactory import ViewFactory
from emailManager import EmailManager

class App(QApplication):
    viewFactory: ViewFactory
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.viewFactory = ViewFactory(EmailManager())
        self.viewFactory.showLoginWindow()


        # self.mainView = LoginWindow()
        # self.loginWindow = uic.loadUi(relpath('view/loginWindow.ui'), None)
        # url = "https://www.google.co.jp"
        # self.mainView.emailWebView.setUrl(QtCore.QUrl(url))
        # self.loginWindow.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())