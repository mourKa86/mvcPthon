from PyQt5 import QtWidgets, uic, QtGui, QtCore
class LoginWindowController(QtWidgets.QWidget):
    def __init__(self, viewFactory, uiPath, *args, **kwargs):
        super(LoginWindowController, self).__init__(*args, **kwargs)
        self.viewFactory = viewFactory
        self.uiPath = uiPath

    def initializeWindow(self):
        uic.loadUi(self.uiPath, self)
        self.bindToControls()
        self.show()

    def bindToControls(self):
        self.login_btn.clicked.connect(self.on_login_btn)

    def on_login_btn(self):
        self.viewFactory.mainWindow.initializeWindow()

