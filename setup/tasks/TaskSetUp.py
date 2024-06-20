import uiautomator2 as u2
from setup.tasks.settings import *

_TaskSetUpMap = {
    'turn notification dots off' : SettingsTask01,
    'turn off wifi' : SettingsTask02,
    'Set the phone to "Do not disturb".' : SettingsTask03,
    'turn on improve location accuracy' : SettingsTask04,
}

def TaskSetUp(device, instruction):
    d = device
    taskSetup= _TaskSetUpMap.get(instruction)

    if taskSetup:
        task = taskSetup(d, instruction)
        task.setup()
    else:
        raise Exception(f"Instruction {instruction} is not supported.")
        


if __name__ == "__main__":
    TaskSetUp("emulator-5554", "turn notification dots off")