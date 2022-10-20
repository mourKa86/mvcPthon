from emailManager import EmailManager
from controller.baseController import BaseController
from controller.loginWindowController import LoginWindowController
from controller.mainWindowController import MainWindowController

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication

import os
from PyQt5 import uic

def relpath(path):
    return os.path.join(os.path.dirname(__file__), path)

class ViewFactory:

    __emailManager: EmailManager
    __App: QApplication

    def __init__(self, emailManager):
        self.__emailManager = emailManager

    def __initializeStage(self, baseController: BaseController):
        try:
            self.UIloader = uic.loadUi(relpath(baseController.getUIName()), None)

        except IOError as e:
            raise(e)
            return

        self.UIloader.show()

    def showLoginWindow(self):
        print("show login window")
        controller = LoginWindowController(self.__emailManager, self, "loginWindow.ui")
        self.__initializeStage(controller)
        controller.setWindow(self.UIloader)


    def showMainWindow(self):
        print("show Main window")
        controller = MainWindowController(self.__emailManager, self, "mainWindow.ui")
        self.__initializeStage(controller)






