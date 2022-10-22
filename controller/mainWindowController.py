from PyQt5 import QtWidgets, uic, QtGui, QtCore, QtWebEngineWidgets


class MainWindowController(QtWidgets.QMainWindow):

    def __init__(self, viewFactory, emailManager, uiPath, *args, **kwargs):
        super(MainWindowController, self).__init__(*args, **kwargs)
        self.__emailManager = emailManager
        self.__viewFactory = viewFactory
        self.__uiPath = uiPath

    def initializeWindow(self):
        try:
            uic.loadUi(self.__uiPath, self)
        except Exception as e:
            raise(e)
            return

        self.bindToWidgets()
        self.initializeWidgets()
        self.show()

    def bindToWidgets(self):
        self.actionOptions.triggered.connect(self.on_actionOptions_menuBtn)

    def initializeWidgets(self):
        url = "https://www.google.co.jp"
        self.emailWebView.setUrl(QtCore.QUrl(url))

    def on_actionOptions_menuBtn(self):
        self.__viewFactory.optionWindow.initializeWindow()





