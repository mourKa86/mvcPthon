from abc import ABC, abstractmethod
from emailManager import EmailManager


class BaseController(ABC):

    _emailManager:EmailManager
    _uiName:str

    def __init__(self, emailManager, viewFactory, uiName):
        self._emailManager = emailManager
        self._viewFactory = viewFactory
        self._uiName = uiName

    def getUIName(self):
        return self._uiName