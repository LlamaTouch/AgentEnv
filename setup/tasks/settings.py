from setup.tasks.BaseTaskSetup import BaseTaskSetup
import time

'''
This file contains the settings Apps`s tasks setup
'''

class SettingsTask01(BaseTaskSetup):
    '''
    instruction: turn notification dots off
    setup: make sure the notification dots are on
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)

    def setup(self):
        '''
        Use UI Automation method to complete the setup work
        '''
        # start settings app
        self.d.app_start("com.android.settings", use_monkey=True)

        # Click the element with text "Notifications"
        self.d(text="Notifications").click()

        # Scroll until the specified element is visible
        self.d(scrollable=True).scroll.to(resourceId="android:id/switch_widget", instance=2)

        # Get the status of the switch widget
        switch_element = self.d(resourceId="android:id/switch_widget", instance=2)
        is_switch_on = switch_element.info.get('checked')

        # If the switch is off, click it to turn it on
        if not is_switch_on:
            switch_element.click()

        # stop the settings app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.android.settings")
        
class SettingsTask02(BaseTaskSetup):
    '''
    instruction: turn off wifi
    setup: make sure the wifi are on
    '''

    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        '''
        Use UI Automation method to complete the setup work
        '''
        # start settings app
        self.d.app_start("com.android.settings", use_monkey=True)

        # Click the element with text "Network & internet"
        self.d(text="Network & internet").click()

        # Click on "Internet"
        self.d(text="Internet").click()

        # Click the element with text "Wi-Fi"
        self.d(text="Wi-Fi").click()

        # Get the status of the switch widget
        switch_element = self.d(resourceId="android:id/switch_widget")
        is_switch_on = switch_element.info.get('checked')

        # If the switch is off, click it to turn it on
        if not is_switch_on:
            switch_element.click()

        # stop the settings app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.android.settings")

class SettingsTask03(BaseTaskSetup):
    '''
    instruction: Set the phone to "Do not disturb".
    setup: make sure the phone is not in "Do not disturb" mode.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        '''
        Use UI Automation method to complete the setup work
        '''
        # start settings app
        self.d.app_start("com.android.settings", use_monkey=True)

        # Click the element with text "Sound"
        self.d(text="Sound & vibration").click()

        # Click the element with text "Do not disturb"
        self.d(text="Do Not Disturb").click()

        # Get the status of the "Do not disturb"
        turn_off_element = self.d(resourceId="com.android.settings:id/zen_mode_settings_turn_off_button").exists()
        
        # If the "Do not disturb" is on, click it to turn it off
        if turn_off_element:
            self.d(resourceId="com.android.settings:id/zen_mode_settings_turn_off_button").click()
    
        # stop the settings app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.android.settings")

class SettingsTask04(BaseTaskSetup):
    '''
    instruction: turn on improve location accuracy
    setup: make sure improve location accuracy is off
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        '''
        Use UI Automation method to complete the setup work
        '''
        # start settings app
        self.d.app_start("com.android.settings", use_monkey=True)

        # Click the element with text "Location"
        self.d(scrollable=True).scroll.to(text="Location", instance=2)
        self.d(text="Location").click() 

        # click Location Services
        self.d(scrollable=True).scroll.to(text="Location services", instance=2)
        self.d(text="Location services").click()

        # Click the element with text "Google Location Accuracy"
        self.d(text="Google Location Accuracy").click()

        # Get the status of the switch widget
        switch_element = self.d(resourceId="android:id/switch_widget")
        is_switch_on = switch_element.info.get('checked')

        # If the switch is on, click it to turn it off
        if  is_switch_on:
            switch_element.click()
        
        # stop the settings app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.android.settings")

    