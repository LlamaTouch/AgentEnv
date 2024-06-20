from abc import ABC, abstractmethod


class BaseTaskSetup(ABC):
    def __init__(self, device, instruction):
        self.d = device
        self.instruction = instruction

    @abstractmethod
    def setup(self):
        '''
        Use UI Automation method to complete the setup work
        '''
        pass
