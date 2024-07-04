from setup.tasks.BaseTaskSetup import BaseTaskSetup, SetupFailureException
import time

class ClockTask01(BaseTaskSetup):
    '''
    instruction: turn on the 12-hour format for clock
    setup: make sure clock not in 12-hour format  
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        try:
            # start settings app
            self.d.app_start("com.android.settings", use_monkey=True)
            
            # Scroll to the text="System"
            system_ele = self.d(text="System")
            if not system_ele.wait(timeout=5.0):
                self.d(scrollable=True).scroll.to(text="System")
            
            if not system_ele.exists:
                raise SetupFailureException("System not found")
            # Click the element with text "System"
            self.d(text="System").click()

            if not self.d(text="Date & time").wait(timeout=5.0):
                raise SetupFailureException("Date & time not found")
            # Click the element with text "Date & time"
            self.d(text="Date & time").click()

            # Get the status of the switch widget
            switch_element = self.d(resourceId="android:id/switch_widget", instance=3)
            if not switch_element.wait(timeout=5.0):
                raise SetupFailureException("Switch widget not found")
            is_switch_on = switch_element.info.get('checked')
            
            # If the switch is on, click it to turn it off
            if is_switch_on:
                switch_element.click()

            # stop the settings app
            self.d.press("home")
            time.sleep(2)
            self.d.app_stop("com.android.settings")
        except Exception as e:
            print(f"Error during setup: {e}")
            raise SetupFailureException("Unable to configure the environment properly")
