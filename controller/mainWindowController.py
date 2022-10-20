from controller.baseController import BaseController
class MainWindowController(BaseController):
    def __init__(self, emailManager, viewFactory, uiName):
        BaseController.__init__(self, emailManager, viewFactory, uiName)