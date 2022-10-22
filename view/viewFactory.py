import os

from controller.loginWindowController import LoginWindowController
from controller.mainWindowController import MainWindowController

def relpath(path):
    path = os.path.join(os.path.dirname(__file__), path)
    return path

class ViewFactory:
    def __init__(self):
        uiPath = relpath('loginWindow.ui')
        self.loginWindow = LoginWindowController(self, uiPath)

        uiPath = relpath('mainWindow.ui')
        self.mainWindow = MainWindowController(self, uiPath)

