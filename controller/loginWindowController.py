
from PyQt5 import QtWidgets, uic, QtGui, QtCore

class LoginWindowController(QtWidgets.QWidget):
    def __init__(self, viewFactory, emailManager, uiPath, *args, **kwargs):
        super(LoginWindowController, self).__init__(*args, **kwargs)
        self.__emailManager = emailManager
        self.__viewFactory = viewFactory
        self.__uiPath = uiPath

    def initializeWindow(self):
        try:
            uic.loadUi(self.__uiPath, self)
        except Exception as e:
            raise(e)
            return

        self.bindToControls()
        self.show()

    def bindToControls(self):
        self.login_btn.clicked.connect(self.on_login_btn)

    def on_login_btn(self):
        self.__viewFactory.mainWindow.initializeWindow()
        self.__viewFactory.closeWindow(self)

