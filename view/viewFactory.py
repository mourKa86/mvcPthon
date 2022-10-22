import os

from controller.loginWindowController import LoginWindowController
from controller.mainWindowController import MainWindowController

def relpath(path):
    path = os.path.join(os.path.dirname(__file__), path)
    return path

class ViewFactory:
    def __init__(self, emailManager):
        self.__emailManager = emailManager
        uiPath = relpath('loginWindow.ui')
        self.loginWindow = LoginWindowController(self, emailManager, uiPath)

        uiPath = relpath('mainWindow.ui')
        self.mainWindow = MainWindowController(self, emailManager, uiPath)

