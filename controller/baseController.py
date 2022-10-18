from abc import ABC, abstractmethod
from emailManager import EmailManager
from view.viewFactory import ViewFactory

class BaseController(ABC):

    __emailManager:EmailManager
    __viewFactor:ViewFactory
    __uiName:str

    def __init__(self,emailManager, viewFactory, uiName):
        self.__emailManager = emailManager
        self.__viewFactor = viewFactory
        self.__uiName = uiName
