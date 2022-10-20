import PyQt5.QtDesigner
from controller.baseController import BaseController

from PyQt5 import QtWidgets
class LoginWindowController(BaseController):

    UIloader = None
    def __init__(self, emailManager, viewFactory, uiName ):
        BaseController.__init__(self, emailManager, viewFactory, uiName)
        self.viewFactory = viewFactory

        # here is the problem self.UIloader is not yet created
        # self.login_btn.clicked.connect(self.on_login_btn_clicked())

    def setWindow(self, UIloader):
        self.UIloader = UIloader
        self.UIloaderUIloader.login_btn.clicked.connect(self.on_login_btn_clicked)

    def on_login_btn_clicked(self):
        print("clicked")
        self.viewFactory.showMainWindow()



