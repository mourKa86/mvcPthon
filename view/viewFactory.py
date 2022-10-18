from emailManager import EmailManager

class ViewFactory:
    __emailManager: EmailManager

    def __init__(self, emailManager):
        self.__emailManager = emailManager


    def showLoginWindow(self):
        print("show login window")