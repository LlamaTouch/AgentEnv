import time
from setup.tasks.BaseTaskSetup import BaseTaskSetup, SetupFailureException

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
        try:
            # Start the settings app
            self.d.app_start("com.android.settings", use_monkey=True)
            time.sleep(2)
        
            # Wait and click the element with text "Notifications"
            notifications_element = self.d(text="Notifications")
            if not notifications_element.wait(timeout=5):
                raise SetupFailureException("Notifications option not found.")
            notifications_element.click()

            # Scroll until the specified element is visible
            switch_element = self.d(scrollable=True).scroll.to(resourceId="android:id/switch_widget", instance=2)
            if not switch_element:
                raise SetupFailureException("Switch widget not found.")
            
            # Get the status of the switch widget
            switch_instance = self.d(resourceId="android:id/switch_widget", instance=2)
            if not switch_instance.wait(timeout=5):
                raise SetupFailureException("Switch widget instance not found.")
            is_switch_on = switch_instance.info.get('checked')

            # If the switch is off, click it to turn it on
            if not is_switch_on:
                switch_instance.click()
                print("Switch turned on.")

            self.d.press("home")
            time.sleep(2)
            self.d.app_stop("com.android.settings")

        except Exception as e:
            raise SetupFailureException(f"Unable to configure the environment properly:{e}")
        
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
        try:
            # Start settings app with monkey tool
            self.d.app_start("com.android.settings", use_monkey=True)
            time.sleep(2)

            # Click the element with text "Network & internet"
            if not self.d(text="Network & internet").wait(timeout=5):
                raise SetupFailureException("Network & internet option not found.")
            self.d(text="Network & internet").click()

            # Click on "Internet"
            if not self.d(text="Internet").wait(timeout=5):
                raise SetupFailureException("Internet option not found.")
            self.d(text="Internet").click()

            # Click the element with text "Wi-Fi"
            if not self.d(text="Wi-Fi").wait(timeout=5):
                raise SetupFailureException("Wi-Fi option not found.")
            self.d(text="Wi-Fi").click()

            # Get the status of the switch widget
            switch_element = self.d(resourceId="android:id/switch_widget")
            if not switch_element.wait(timeout=5):
                raise SetupFailureException("Switch widget not found.")
            is_switch_on = switch_element.info.get('checked')

            # If the switch is off, click it to turn it on
            if not is_switch_on:
                switch_element.click()
                print("Wi-Fi switch turned on.")

            # Stop the settings app
            self.d.press("home")
            time.sleep(2)  # Pause to ensure the home operation completes
            self.d.app_stop("com.android.settings")

        except Exception as e:
            print(f"Error during setup: {e}")
            raise SetupFailureException("Unable to configure the environment properly")

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
        try:
            # Start the settings app
            self.d.app_start("com.android.settings", use_monkey=True)
            time.sleep(2)

            # Click the element with text "Sound & vibration"
            if not self.d(text="Sound & vibration").wait(timeout=5):
                raise SetupFailureException("Sound & vibration option not found.")
            self.d(text="Sound & vibration").click()

            # Click the element with text "Do Not Disturb"
            if not self.d(text="Do Not Disturb").wait(timeout=5):
                raise SetupFailureException("Do Not Disturb option not found.")
            self.d(text="Do Not Disturb").click()

            # Check the status of the "Do not disturb" button
            if self.d(resourceId="com.android.settings:id/zen_mode_settings_turn_off_button").wait(timeout=5):
                # If the "Do not disturb" is on, click it to turn it off
                self.d(resourceId="com.android.settings:id/zen_mode_settings_turn_off_button").click()

            # Stop the settings app
            self.d.press("home")
            time.sleep(2)  # Allow time for the operation to complete
            self.d.app_stop("com.android.settings")

        except Exception as e:
            print(f"Error during setup: {e}")
            raise SetupFailureException("Unable to configure the environment properly")

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
        try:
            # Start the settings app with monkey tool
            self.d.app_start("com.android.settings", use_monkey=True)
            time.sleep(2)

            # Scroll and click the element with text "Location"
            if not self.d(scrollable=True).scroll.to(text="Location"):
                raise SetupFailureException("Location option not found.")
            self.d(text="Location").click()


            # Scroll and click Location Services:
            location_service_ele = self.d(text="Location services")
            if not location_service_ele.wait(timeout=5):
                self.d(scrollable=True).scroll.to(text="Location services")
            
            if not location_service_ele.exists:
                raise SetupFailureException("Location services not found.")
            self.d(text="Location services").click()

            # Click the element with text "Google Location Accuracy"
            if not self.d(text="Google Location Accuracy").wait(timeout=5):
                raise SetupFailureException("Google Location Accuracy option not found.")
            self.d(text="Google Location Accuracy").click()

            # Get the status of the switch widget
            if not self.d(resourceId="android:id/switch_widget").wait(timeout=5):
                raise SetupFailureException("Switch widget not found.")
            switch_element = self.d(resourceId="android:id/switch_widget")
            is_switch_on = switch_element.info.get('checked')

            # If the switch is on, click it to turn it off
            if is_switch_on:
                switch_element.click()
                print("Switch turned off.")

            # Stop the settings app
            self.d.press("home")
            time.sleep(2)  # Pause to ensure the home operation completes
            self.d.app_stop("com.android.settings")
            print("Settings app stopped and returned to home screen.")

        except Exception as e:
            print(f"Error during setup: {e}")
            raise SetupFailureException("Unable to configure the environment properly")
             
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
        try:
            # Start the settings app with monkey tool
            self.d.app_start("com.android.settings", use_monkey=True)
            time.sleep(2)

            # Click the element with text "Connected devices"
            if not self.d(text="Connected devices").wait(timeout=5):
                raise SetupFailureException("Connected devices option not found.")
            self.d(text="Connected devices").click()

            # Click the element with text "Connection preferences"
            if not self.d(text="Connection preferences").wait(timeout=5):
                raise SetupFailureException("Connection preferences option not found.")
            self.d(text="Connection preferences").click()

            # Click the element with text "Bluetooth"
            if not self.d(text="Bluetooth").wait(timeout=5):
                raise SetupFailureException("Bluetooth option not found.")
            self.d(text="Bluetooth").click()

            # Get the status of the switch widget
            if not self.d(resourceId="android:id/switch_widget").wait(timeout=5):
                raise SetupFailureException("Switch widget not found.")
            switch_element = self.d(resourceId="android:id/switch_widget")
            is_switch_on = switch_element.info.get('checked')

            # If the switch is on, click it to turn it off
            if is_switch_on:
                switch_element.click()

            # Stop the settings app
            self.d.press("home")
            time.sleep(2)  # Pause to ensure the home operation completes
            self.d.app_stop("com.android.settings")

        except Exception as e:
            print(f"Error during setup: {e}")
            raise SetupFailureException("Unable to configure the environment properly")

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
        try:
            # Start the settings app with monkey tool
            self.d.app_start("com.android.settings", use_monkey=True)
            time.sleep(2)
            # Click the element with text "Network & internet"
            if not self.d(text="Network & internet").wait(timeout=5):
                raise SetupFailureException("Network & internet option not found.")
            self.d(text="Network & internet").click()

            # Get the status of the switch widget
            if not self.d(resourceId="android:id/switch_widget").wait(timeout=5):
                raise SetupFailureException("Switch widget not found.")
            switch_element = self.d(resourceId="android:id/switch_widget")
            is_switch_on = switch_element.info.get('checked')

            # If the switch is on, click it to turn it off
            if is_switch_on:
                switch_element.click()
                print("Network & internet switch turned off.")

            # Stop the settings app
            self.d.press("home")
            time.sleep(2)  # Allow time for the operation to complete
            self.d.app_stop("com.android.settings")

        except Exception as e:
            print(f"Error during setup: {e}")
            raise SetupFailureException("Unable to configure the environment properly")

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
        try:
            # Start the settings app with monkey tool
            self.d.app_start("com.android.settings", use_monkey=True)
            time.sleep(2)

            # Click the element with text "Notifications"
            if not self.d(text="Notifications").wait(timeout=5):
                raise SetupFailureException("Notifications option not found.")
            self.d(text="Notifications").click()

            # Click the element with text "Notifications on lock screen"
            if not self.d(text="Notifications on lock screen").wait(timeout=5):
                raise SetupFailureException("Notifications on lock screen option not found.")
            self.d(text="Notifications on lock screen").click()

            # Click the element with text "Show conversations, default, and silent"
            if not self.d(text="Show conversations, default, and silent").wait(timeout=5):
                raise SetupFailureException("Show conversations, default, and silent option not found.")
            self.d(text="Show conversations, default, and silent").click()
            
            # Stop the settings app
            self.d.press("home")
            time.sleep(2)  # Allow time for the home operation to complete
            self.d.app_stop("com.android.settings")

        except Exception as e:
            print(f"Error during setup: {e}")
            raise SetupFailureException("Unable to configure the environment properly")

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
        try:
            # Start the settings app with monkey tool
            self.d.app_start("com.android.settings", use_monkey=True)
            time.sleep(2)
            
            # Scroll until the "Location" option is visible and click it
            location_ele = self.d(text="Location")
            if not location_ele.wait(timeout=5):
                self.d(scrollable=True).scroll.to(text="Location")
            if not location_ele.exists:
                raise SetupFailureException("Location option not found.")
            location_ele.click()

            # Click the element with text "Location services"
            if not self.d(text="Location services").wait(timeout=5):
                raise SetupFailureException("Location services option not found.")
            self.d(text="Location services").click()

            # Click the element with text "Google Location Accuracy"
            if not self.d(text="Google Location Accuracy").wait(timeout=5):
                raise SetupFailureException("Google Location Accuracy option not found.")
            self.d(text="Google Location Accuracy").click()

            # Get the status of the switch widget
            if not self.d(resourceId="android:id/switch_widget").wait(timeout=5):
                raise SetupFailureException("Switch widget not found.")
            switch_element = self.d(resourceId="android:id/switch_widget")
            is_switch_on = switch_element.info.get('checked')

            # If the switch is off, click it to turn it on
            if not is_switch_on:
                switch_element.click()
                print("Google Location Accuracy switch turned on.")

            # Stop the settings app
            self.d.press("home")
            time.sleep(2)  # Pause to ensure the home operation completes
            self.d.app_stop("com.android.settings")

        except Exception as e:
            print(f"Error during setup: {e}")
            raise SetupFailureException("Unable to configure the environment properly")