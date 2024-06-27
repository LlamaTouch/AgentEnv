from setup.tasks.BaseTaskSetup import BaseTaskSetup
import time

class ClockTask01(BaseTaskSetup):
    '''
    instruction: turn on the 12-hour format for clock
    setup: make sure clock not in 12-hour format  
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start settings app
        self.d.app_start("com.android.settings", use_monkey=True)
        
        # Scroll to the text="System"
        self.d(scrollable=True).scroll.to(text="System")

        # Click the element with text "System"
        self.d(text="System").click()

        # Click the element with text "Date & time"
        self.d(text="Date & time").click()

        # Get the status of the switch widget
        switch_element = self.d(resourceId="android:id/switch_widget", instance=3)
        is_switch_on = switch_element.info.get('checked')
        # If the switch is on, click it to turn it off
        if is_switch_on:
            switch_element.click()

        # stop the settings app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.android.settings")
