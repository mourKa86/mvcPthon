import os

from controller.loginWindowController import LoginWindowController
from controller.mainWindowController import MainWindowController
from controller.optionsWindowController import OptionsWindowController

from view.colorTheme import ColorTheme
from view.fontSize import FontSize

def relpath(path):
    path = os.path.join(os.path.dirname(__file__), path)
    return path

class ViewFactory:
    __colorTheme = ColorTheme.DEFAULT
    __fontSize = FontSize.MEDIUM
    def __init__(self, emailManager):
        self.__emailManager = emailManager
        uiPath = relpath('loginWindow.ui')
        self.loginWindow = LoginWindowController(self, emailManager, uiPath)

        uiPath = relpath('mainWindow.ui')
        self.mainWindow = MainWindowController(self, emailManager, uiPath)

        uiPath = relpath('optionsWindow.ui')
        self.optionWindow = OptionsWindowController(self, emailManager, uiPath)

    def closeWindow(self, window):
        window.close()

    def getColorTheme(self):
        return self.__colorTheme.name
    def getFontSize(self):
        return self.__fontSize.value

    def setColorTheme(self, value):
        self.__colorTheme = value
    def setFontSize(self, value):
        self.__fontSize = value