from view.viewFactory import ViewFactory
from PyQt5 import QtWidgets, uic, QtGui, QtCore, QtWebEngineWidgets


class MainWindowController(QtWidgets.QMainWindow):
    __emailManager: EmailManager
    __viewFactory: ViewFactory
    __uiPath: str
    def __init__(self, emailManager, viewFactory, uiPath, *args, **kwargs):
        super(MainWindowController, self).__init__(*args, **kwargs)
        self.__viewFactory = viewFactory
        self.__uiPath = uiPath

    def initializeWindow(self):
        uic.loadUi(self.__uiPath, self)
        self.bindToControls()
        self.show()

    def bindToControls(self):
        url = "https://www.google.co.jp"
        self.emailWebView.setUrl(QtCore.QUrl(url))

