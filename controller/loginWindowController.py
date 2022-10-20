import PyQt5.QtDesigner
from controller.baseController import BaseController

from PyQt5 import QtWidgets
class LoginWindowController(BaseController):

    login_btn: QtWidgets.QPushButton
    def __init__(self, emailManager, viewFactory, uiName ):
        BaseController.__init__(self, emailManager, viewFactory, uiName)
        self.viewFactory = viewFactory

        # self.login_btn.clicked.connect(self.on_login_btn_clicked())

    @PyQt5.QtWidgets.QPushButton.clicked
    def on_login_btn_clicked(self):
        print("clicked")
        self.viewFactory.showMainWindow()


