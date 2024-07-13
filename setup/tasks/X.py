import time
from uiautomator2 import Device
from setup.tasks.BaseTaskSetup import BaseTaskSetup,SetupFailureException
from setup.tasks.GoogleDrive import get_screenshot

class XTask01(BaseTaskSetup):
    '''
    instruction: Upload my avatar on X app using my latest picture on device.
    setup: make sure there is one picture in device at least.   
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # take a screenshot and save it to the device
        get_screenshot(self.d)