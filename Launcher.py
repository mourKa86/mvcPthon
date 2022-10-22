import sys
from PyQt5.QtWidgets import QApplication

from view.viewFactory import  ViewFactory

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.viewFactory = ViewFactory()
        self.viewFactory.loginWindow.initializeWindow()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())