from setup.tasks.BaseTaskSetup import BaseTaskSetup,SetupFailureException,SetupFailureException
import time
from uiautomator2 import Device

def check_meeting_exist(d: Device, meeting_name: str=None) -> bool:
    """
    func: check the meeting is exist or not. 
    """
    if meeting_name is None:
        raise ValueError("Meeting name must be provided")

    try:
        # Go to Meetings page
        meetings_button = d(text="Meetings")
        if not meetings_button.wait(timeout=5):
            raise SetupFailureException("Meetings button not found on the screen")
        meetings_button.click()
        time.sleep(5)  
        
        # Search for target meeting
        elements = d.xpath('//android.widget.TextView[@resource-id="us.zoom.videomeetings:id/txtTopic"]').all()
        for element in elements:
            text = element.info.get("text")
            if text == meeting_name:
                return True
       
        return False

    except Exception as e:
        raise SetupFailureException(f"An error occurred while checking meeting existence.:{e}")

def add_scheduled_meeting(d: Device, meeting_name: str = None) -> None:
    """
    Adds a scheduled meeting named 'meeting_name'.
    Raises ValueError if no meeting name is provided.
    Assumes starting from the main page of the app.
    """
    if meeting_name is None:
        raise ValueError("Meeting name must be provided")

    try:
        # Go to Meetings page
        meetings_button = d(text="Meetings", instance=1)
        if not meetings_button.wait(timeout=5):
            raise SetupFailureException("Meetings button not found on the screen")
        meetings_button.click()

        # Navigate to the Schedule section
        schedule_button = d(text="Schedule")
        if not schedule_button.wait(timeout=5):
            raise SetupFailureException("Schedule button not found on the screen")
        schedule_button.click()

        # Input the topic of the meeting
        topic_input = d(resourceId="us.zoom.videomeetings:id/edtTopic")
        if not topic_input.wait(timeout=5):
            raise SetupFailureException("Topic input field not found")
        topic_input.set_text(meeting_name)

        # Click the Schedule button
        schedule_button = d(resourceId="us.zoom.videomeetings:id/btnSchedule")
        if not schedule_button.wait(timeout=5):
            raise SetupFailureException("Schedule button not found")
        schedule_button.click()

        # Confirm the schedule
        confirm_button = d(resourceId="us.zoom.videomeetings:id/button1")
        if not confirm_button.wait(timeout=10):
            raise SetupFailureException("Confirm button not found")
        confirm_button.click()

        # Ensure the device returns to the Meetings page or main screen
        d.press("back")
        time.sleep(5)
        if d(text="Meeting details").exists():
            d.press("back")
    
    except Exception as e:
        raise SetupFailureException(f"Failed to add scheduled meeting:{e}")


class ZoomTask01(BaseTaskSetup):
    '''
    instruction: On Zoom, start my scheduled meeting 'regular meeting' right now.
    setup: Make sure there is a scheduled meeting 'regular meeting'.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("us.zoom.videomeetings", use_monkey=True)
        time.sleep(10)
        
        # create regular meeting
        if not check_meeting_exist(self.d, "regular meeting"):
            add_scheduled_meeting(self.d, "regular meeting")

        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("us.zoom.videomeetings")

class ZoomTask02(BaseTaskSetup):
    '''
    instruction: On Zoom, delete my scheduled meeting 'regular meeting'.
    setup: make sure there is a scheduled meeting 'regular meeting'.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("us.zoom.videomeetings", use_monkey=True)
        time.sleep(10)
        
        # create regular meeting
        if not check_meeting_exist(self.d, "regular meeting"):
            add_scheduled_meeting(self.d, "regular meeting")

        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("us.zoom.videomeetings")

class ZoomTask03(BaseTaskSetup):
    '''
    instruction: On Zoom, edit my scheduled meeting 'Weekly group meeting', set 'Repeat' to 'Every week'.
    setup: Make sure there is a scheduled meeting 'Weekly group meeting'.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("us.zoom.videomeetings", use_monkey=True)
        time.sleep(10)
        
        # create regular meeting
        if not check_meeting_exist(self.d, "Weekly group meeting"):
            add_scheduled_meeting(self.d, "Weekly group meeting")

        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("us.zoom.videomeetings")

class ZoomTask04(BaseTaskSetup):
    '''
    instruction: On Zoom, edit my scheduled meeting 'Weekly group meeting', turn 'Enable waiting room' on.
    setup: Make sure there is a scheduled meeting 'Weekly group meeting'.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("us.zoom.videomeetings", use_monkey=True)
        time.sleep(10)
        
        # create regular meeting
        if not check_meeting_exist(self.d, "Weekly group meeting"):
            add_scheduled_meeting(self.d, "Weekly group meeting")

        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("us.zoom.videomeetings")

class ZoomTask05(BaseTaskSetup):
    '''
    instruction: On Zoom, turn to page 'Team chat', bookmark my latest message to myself.
    setup: Make sure there is a message from myself in the chat.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        try:
            # Start the Zoom app
            self.d.app_start("us.zoom.videomeetings", use_monkey=True)
            time.sleep(10)
            # Navigate to "Team Chat"
            team_chat = self.d(text="Team Chat")
            if not team_chat.wait(timeout=5):
                raise SetupFailureException("Team Chat button not found")
            team_chat.click()

            # Select yourself to chat with
            self_selector = self.d.xpath('(//android.widget.ImageView[@resource-id="us.zoom.videomeetings:id/imgAvator"])[2]')
            if not self_selector.wait(timeout=10):
                raise SetupFailureException("Self selector not found")
            self_selector.click()
            
            # Input the message
            message_field = self.d(resourceId="us.zoom.videomeetings:id/inflatedCommandEditText")
            if not message_field.wait(timeout=5):
                raise SetupFailureException("Message input field not found")
            message_field.set_text("hellomessage")

            # Send the message
            send_button = self.d(description="Send")
            if not send_button.wait(timeout=5):
                raise SetupFailureException("Send button not found")
            send_button.click()

            # Stop the Zoom app
            self.d.press("home")
            time.sleep(2)
            self.d.app_stop("us.zoom.videomeetings")
        
        except Exception as e:
            raise SetupFailureException(f"An error occurred while sending message.:{e}")

class ZoomTask06(BaseTaskSetup):
    '''
    instruction: On Zoom, turn to page 'Team chat', set a reminder for my latest message to myself in 1 hour.
    setup: Make sure there is a message from myself in the chat.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        try:
            # Start the Zoom app
            self.d.app_start("us.zoom.videomeetings", use_monkey=True)
            time.sleep(10)

            # Navigate to "Team Chat"
            team_chat = self.d(text="Team Chat")
            if not team_chat.wait(timeout=5):
                raise SetupFailureException("Team Chat button not found")
            team_chat.click()

            # Select yourself to chat with
            self_selector = self.d.xpath('(//android.widget.ImageView[@resource-id="us.zoom.videomeetings:id/imgAvator"])[2]')
            if not self_selector.wait(timeout=10):
                raise SetupFailureException("Self selector not found")
            self_selector.click()

            # Input the message
            message_field = self.d(resourceId="us.zoom.videomeetings:id/inflatedCommandEditText")
            if not message_field.wait(timeout=5):
                raise SetupFailureException("Message input field not found")
            message_field.set_text("hellomessage")

            # Send the message
            send_button = self.d(description="Send")
            if not send_button.wait(timeout=5):
                raise SetupFailureException("Send button not found")
            send_button.click()

            # Stop the Zoom app
            self.d.press("home")
            time.sleep(5)
            self.d.app_stop("us.zoom.videomeetings")
        
        except Exception as e:
            raise SetupFailureException(f"An error occurred while sending message.:{e}")

