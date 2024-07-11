from abc import ABC, abstractmethod

class BaseApp(ABC):
    def __init__(self, device, app_name):
        self.d = device
        self.app_name = app_name


    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def close(self):
        pass
    

