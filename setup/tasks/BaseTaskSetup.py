from abc import ABC, abstractmethod
from uiautomator2 import Device


class BaseTaskSetup(ABC):
    def __init__(self, device: Device, instruction: str):
        self.d = device
        self.instruction = instruction

    @abstractmethod
    def setup(self):
        '''
        Use UI Automation method to complete the setup work
        '''
        pass
