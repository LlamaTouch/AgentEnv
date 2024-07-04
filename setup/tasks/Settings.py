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
        time.sleep(2)
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
        # 执行下面的代码的时候，似乎会点击一下开关组件
        switch_element = self.d(resourceId="android:id/switch_widget")
        is_switch_on = switch_element.info.get('checked')
        # If the switch is off, click it to turn it on
        if not is_switch_on:
            switch_element.click()

        # stop the settings app
        self.d.press("home")
        time.sleep(2)
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
        time.sleep(2)
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
        time.sleep(2)
        self.d.app_stop("com.android.settings")

class SettingsTask05(BaseTaskSetup):
    '''
    instruction: turn on bluetooth scan
    setup: make sure bluetooth scan is off
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        '''
        Use UI Automation method to complete the setup work
        '''
        # start settings app
        self.d.app_start("com.android.settings", use_monkey=True)

        # Click the element with text "Connected devices"
        self.d(text="Connected devices").click()

        # Click the element with text "Connection preferences"
        self.d(text="Connection preferences").click()

        # Click the element with text "Bluetooth"
        self.d(text="Bluetooth").click()

        # Get the status of the switch widget
        switch_element = self.d(resourceId="android:id/switch_widget")
        is_switch_on = switch_element.info.get('checked')

        # If the switch is on, click it to turn it off
        if  is_switch_on:
            switch_element.click()
        
        # stop the settings app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.android.settings")

class SettingsTask06(BaseTaskSetup):
    '''
    instruction: turn on airplane mode
    setup: make sure airplane mode is off
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

        # Get the status of the switch widget
        switch_element = self.d(resourceId="android:id/switch_widget")
        is_switch_on = switch_element.info.get('checked')

        # If the switch is on, click it to turn it off
        if  is_switch_on:
            switch_element.click()
        
        # stop the settings app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.android.settings")

class SettingsTask07(BaseTaskSetup):
    '''
    instruction: toggle show notifications on the lock screen
    setup: make sure show notifications on the lock screen 
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

        # Click the element with text "Notifications on lock screen"
        self.d(text="Notifications on lock screen").click()

        # Click the element with text "Show conversations, default, and silent"
        self.d(text="Show conversations, default, and silent").click()
        
        # stop the settings app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.android.settings")

class SettingsTask08(BaseTaskSetup):
    '''
    instruction: turn off improve location accuracy
    setup: make sure improve location accuracy is on
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        '''
        Use UI Automation method to complete the setup work
        '''
        # start settings app
        self.d.app_start("com.android.settings", use_monkey=True)

        # Scroll until the switch widget for Google Location Accuracy is visible
        self.d(scrollable=True).scroll.to(text="Location")

        # Click the element with text "Location"
        self.d(text="Location").click()

        # Click the element with text "Location services"
        self.d(text="Location services").click()

        # Click the element with text "Google Location Accuracy"
        self.d(text="Google Location Accuracy").click()

        # Get the status of the switch widget
        switch_element = self.d(resourceId="android:id/switch_widget")
        is_switch_on = switch_element.info.get('checked')

        # If the switch is off, click it to turn it on
        if not is_switch_on:
            switch_element.click()

        # stop the settings app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.android.settings")
