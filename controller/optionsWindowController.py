from PyQt5 import QtWidgets, uic, QtGui, QtCore, QtWebEngineWidgets
from view.colorTheme import ColorTheme
import view.colorTheme
from view.fontSize import FontSize

class OptionsWindowController(QtWidgets.QWidget):

    def __init__(self, viewFactory, emailManager, uiPath, *args, **kwargs):
        super(OptionsWindowController, self).__init__(*args, **kwargs)
        self.__emailManager = emailManager
        self.__viewFactory = viewFactory
        self.__uiPath = uiPath

    def initializeWindow(self):
        try:
            uic.loadUi(self.__uiPath, self)
        except Exception as e:
            raise(e)
            return

        self.bindToControls()
        self.initializeWidgets()
        self.show()

    def bindToControls(self):
        pass

    def initializeWidgets(self):
        self.setupThemePicker()
        self.setupSizePicker()

    def setupThemePicker(self):
        names = [member.name for member in ColorTheme]
        self.theme_combo.addItems(names)

    def setupSizePicker(self):
        #self.fontSize_slider
        self.fontSize_slider.setMinimum(0)
        names = [str(member.name) for member in FontSize]
        self.fontSize_slider.setMaximum(len(names)-1)
        self.fontSize_slider.setValue(self.__viewFactory.getFontSize())
