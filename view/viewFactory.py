from emailManager import EmailManager
from controller.baseController import BaseController
from controller.loginWindowController import LoginWindowController
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



    def showLoginWindow(self):
        print("show login window")
        controller = LoginWindowController(self.__emailManager, self, "loginWindow.ui")
        try:
            self.UIloader = uic.loadUi(relpath(controller.getUIName()), None)
        except IOError as e:
            raise(e)
            return

        self.UIloader.show()






