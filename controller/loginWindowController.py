from view.viewFactory import ViewFactory
from PyQt5 import QtWidgets, uic, QtGui, QtCore


class LoginWindowController(QtWidgets.QWidget):
    __emailManager: EmailManager
    __viewFactory: ViewFactory
    __uiPath: str
    def __init__(self, emailManager, viewFactory, uiPath, *args, **kwargs):
        super(LoginWindowController, self).__init__(*args, **kwargs)
        self.__emailManager = emailManager
        self.__viewFactory = viewFactory
        self.__uiPath = uiPath

    def initializeWindow(self):
        uic.loadUi(self.__uiPath, self)
        self.bindToControls()
        self.show()

    def bindToControls(self):
        self.login_btn.clicked.connect(self.on_login_btn)

    def on_login_btn(self):
        self.__viewFactory.mainWindow.initializeWindow()

