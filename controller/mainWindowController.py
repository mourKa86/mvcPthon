from PyQt5 import QtWidgets, uic, QtGui, QtCore, QtWebEngineWidgets

class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self, viewFactory, emailManager, uiPath, *args, **kwargs):
        super(MainWindowController, self).__init__(*args, **kwargs)
        self.__emailManager = emailManager
        self.__viewFactory = viewFactory
        self.__uiPath = uiPath

    def initializeWindow(self):
        uic.loadUi(self.__uiPath, self)
        self.bindToControls()
        self.show()

    def bindToControls(self):
        url = "https://www.google.co.jp"
        self.emailWebView.setUrl(QtCore.QUrl(url))

