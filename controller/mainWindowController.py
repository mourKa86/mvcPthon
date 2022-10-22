from PyQt5 import QtWidgets, uic, QtGui, QtCore
class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self, viewFactory, uiPath, *args, **kwargs):
        super(MainWindowController, self).__init__(*args, **kwargs)
        self.viewFactory = viewFactory
        self.uiPath = uiPath

    def initializeWindow(self):
        uic.loadUi(self.uiPath, self)
        self.show()