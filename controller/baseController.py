from abc import ABC, abstractmethod
from emailManager import EmailManager


class BaseController(ABC):

    __emailManager:EmailManager
    __uiName:str

    def __init__(self, emailManager, viewFactory, uiName):
        self.__emailManager = emailManager
        self.__viewFactor = viewFactory
        self.__uiName = uiName

    def getUIName(self):
        return self.__uiName