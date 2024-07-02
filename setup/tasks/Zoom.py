from setup.tasks.BaseTaskSetup import BaseTaskSetup
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
        meetings_button = d(text="Meetings", instance=1)
        if not meetings_button.exists(timeout=5):
            raise Exception("Meetings button not found on the screen")
        meetings_button.click()
        time.sleep(2)  
        
        # Search for target meeting
        elements = d.xpath('//android.widget.TextView[@resource-id="us.zoom.videomeetings:id/title"]').all()
        for element in elements:
            text = element.text
            if text == meeting_name:
                return True
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

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
        if not meetings_button.exists(timeout=5):
            raise Exception("Meetings button not found on the screen")
        meetings_button.click()

        # Navigate to the Schedule section
        schedule_button = d(text="Schedule")
        if not schedule_button.exists(timeout=5):
            raise Exception("Schedule button not found on the screen")
        schedule_button.click()

        # Input the topic of the meeting
        topic_input = d(resourceId="us.zoom.videomeetings:id/edtTopic")
        if not topic_input.exists(timeout=5):
            raise Exception("Topic input field not found")
        topic_input.set_text(meeting_name)

        # Click the Schedule button
        schedule_button = d(resourceId="us.zoom.videomeetings:id/btnSchedule")
        if not schedule_button.exists(timeout=5):
            raise Exception("Schedule button not found")
        schedule_button.click()

        # Confirm the schedule
        confirm_button = d(resourceId="us.zoom.videomeetings:id/button1")
        if not confirm_button.exists(timeout=10):
            raise Exception("Confirm button not found")
        confirm_button.click()
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the device returns to the Meetings page or main screen
        d.press("back")
        time.sleep(2)
        if d(text="Meeting details").exists():
            d.press("back")

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
        time.sleep(2)
        
        # create regular meeting
        if not check_meeting_exist(self.d, "regular meeting"):
            add_scheduled_meeting(self.d, "regular meeting")

        # stop app
        self.d.press("home")
        time.sleep(2)
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
        time.sleep(2)
        
        # create regular meeting
        if not check_meeting_exist(self.d, "regular meeting"):
            add_scheduled_meeting(self.d, "regular meeting")

        # stop app
        self.d.press("home")
        time.sleep(2)
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
        time.sleep(2)
        
        # create regular meeting
        if not check_meeting_exist(self.d, "Weekly group meeting"):
            add_scheduled_meeting(self.d, "Weekly group meeting")

        # stop app
        self.d.press("home")
        time.sleep(2)
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
        time.sleep(2)
        
        # create regular meeting
        if not check_meeting_exist(self.d, "Weekly group meeting"):
            add_scheduled_meeting(self.d, "Weekly group meeting")

        # stop app
        self.d.press("home")
        time.sleep(2)
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

            # Navigate to "Team Chat"
            team_chat = self.d(text="Team Chat")
            if not team_chat.exists(timeout=5):
                raise Exception("Team Chat button not found")
            team_chat.click()

            # Select yourself to chat with
            self_selector = self.d(className="android.widget.LinearLayout", instance=11)
            if not self_selector.exists(timeout=5):
                raise Exception("Self selector not found")
            self_selector.click()

            # Input the message
            message_field = self.d(resourceId="us.zoom.videomeetings:id/inflatedCommandEditText")
            if not message_field.exists(timeout=5):
                raise Exception("Message input field not found")
            message_field.set_text("hellomessage")

            # Send the message
            send_button = self.d(description="Send")
            if not send_button.exists(timeout=5):
                raise Exception("Send button not found")
            send_button.click()

        finally:
            # Stop the Zoom app
            self.d.press("home")
            time.sleep(2)
            self.d.app_stop("us.zoom.videomeetings")

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

            # Navigate to "Team Chat"
            team_chat = self.d(text="Team Chat")
            if not team_chat.exists(timeout=5):
                raise Exception("Team Chat button not found")
            team_chat.click()

            # Select yourself to chat with
            self_selector = self.d(className="android.widget.LinearLayout", instance=11)
            if not self_selector.exists(timeout=5):
                raise Exception("Self selector not found")
            self_selector.click()

            # Input the message
            message_field = self.d(resourceId="us.zoom.videomeetings:id/inflatedCommandEditText")
            if not message_field.exists(timeout=5):
                raise Exception("Message input field not found")
            message_field.set_text("hellomessage")

            # Send the message
            send_button = self.d(description="Send")
            if not send_button.exists(timeout=5):
                raise Exception("Send button not found")
            send_button.click()

        finally:
            # Stop the Zoom app
            self.d.press("home")
            time.sleep(2)
            self.d.app_stop("us.zoom.videomeetings")

