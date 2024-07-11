import time
from uiautomator2 import Device
from setup.tasks.BaseTaskSetup import BaseTaskSetup, SetupFailureException
from setup.tasks.GoogleDrive import get_screenshot
# Discord app version: 235.28 - Stable
# test on 236.20 - Stable

def check_popup(d: Device, popup_text: str="Check it out") -> bool:
    """
    Check if a popup with the specified text is present on the screen. If the popup is found, press check button and press back.
    """
    popup = d(text=popup_text)
    if popup.wait(timeout=5):
        popup.click()
        time.sleep(2) 
        d.press("back")
        time.sleep(2)

def check_server_exist(d: Device, server_name: str="agentian's server") -> bool:
    """
    start from the home page of discord app
    """
    try:
        # Navigate to the Home page
        home_button = d(text="Home")
        if not home_button.wait(timeout=5):
            raise SetupFailureException("Home button not found.")
        home_button.click()
        
        time.sleep(5)
        # Navigate to the server list
        server_list = []
        # Find all the server nodes
        server_btns = d.xpath('//android.widget.AbsListView[@content-desc="Servers"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').all()
        if not server_btns:
            print(f"Server list not found.")
            return []
        for server_button in server_btns:
            if server_button:
                server_name_desc = server_button.info.get("contentDescription").strip()
                server_list.append(server_name_desc)

        # Check if the specified server name exists in the list
        if server_name in server_list:
            return True
        return False

    except Exception as e:
        raise SetupFailureException(f"An error occurred while checking server existence.:{e}")

def create_server(d: Device, server_name: str="agentian's server") -> None:
    """
    start from the home page of discord app
    """
    try:
        # Navigate to the Home page
        home_button = d(text="Home")
        if not home_button.wait(timeout=5):
            raise SetupFailureException("Home button not found.")
        home_button.click()

        # Navigate to Add a Server
        add_server_button = d(description="Add a Server")
        if not add_server_button.wait(timeout=5):
            raise SetupFailureException("Add a Server button not found.")
        add_server_button.click()

        # Select "Create My Own"
        create_own_button = d(text="Create My Own")
        if not create_own_button.wait(timeout=5):
            raise SetupFailureException("Create My Own option not found.")
        create_own_button.click()

        # Choose "For me and my friends"
        for_me_and_friends_button = d(description="For me and my friends")
        if not for_me_and_friends_button.wait(timeout=5):
            raise SetupFailureException("For me and my friends option not found.")
        for_me_and_friends_button.click()

        # Input server name
        server_name_field = d(className="android.widget.EditText")
        if not server_name_field.wait(timeout=5):
            raise SetupFailureException("Server name edit text field not found.")
        server_name_field.clear_text()
        server_name_field.set_text(server_name)

        # Create server
        create_server_button = d(description="Create Server")
        if not create_server_button.wait(timeout=5):
            raise SetupFailureException("Create Server button not found.")
        create_server_button.click()

        # Skip next step
        skip_button = d(description="Skip")
        if not skip_button.wait(timeout=5):
            raise SetupFailureException("Skip button not found.")
        skip_button.click()

    except Exception as e:
        raise SetupFailureException(f"An error occurred while creating server.:{e}")
    
def is_home_page(d: Device) -> bool:
    try:
        # Check if the home button exists
        home_button = d(text="Home")
        return home_button.wait(timeout=5)
    except Exception as e:
        raise SetupFailureException(f"An error occurred while checking if the home page.:{e}")

def check_voice_channel_exist(d: Device, channel_name: str="lobby") -> bool:    
    """
    start from the server page of the Discord app.
    """    
    target_channel = d.xpath(f'//android.widget.TextView[@text="{channel_name}"]').wait(timeout=5)
    if target_channel:
        return True
    
    return False

def create_voice_channel(d: Device, server_name: str="agentian`s server",channel_name: str="lobby") -> None:
    """
    Start from the server page of the Discord app.
    """
    try:
        # Navigate to 'agentian`s server'
        server = d(text=server_name)
        if not server.wait(timeout=5):
            raise SetupFailureException(f"Server {server_name} not found")
        server.click()

        # Click on 'Create Channel'
        create_channel_button = d(text="Create Channel")
        if not create_channel_button.wait(timeout=5):
            raise SetupFailureException("Create Channel button not found")
        create_channel_button.click()

        # Enter channel name
        edit_text = d(className="android.widget.EditText")
        if not edit_text.wait(timeout=5):
            raise SetupFailureException("Text input for channel name not found")
        edit_text.set_text(channel_name)


        # Select the channel type (assuming it's voice channel for this example)
        voice_channel_option = d(description="Voice, Hang out together with voice, video, and screen share")
        if not voice_channel_option.wait(timeout=5):
            raise SetupFailureException("Voice channel option not found")
        voice_channel_option.click()

        # Click 'Create' to finalize channel creation
        create_button = d(description="Create")
        if not create_button.wait(timeout=5):
            raise  SetupFailureException("Create button not found")
        create_button.click()

    except Exception as e:
        raise SetupFailureException(f"An error occurred while creating voice channel.{e}")


class DiscordTask01(BaseTaskSetup):
    '''
    instruction: Send text 'Hello World' in text channel 'general' of agentian's server on Discord app.
    setup: make sure there is a server named 'agentian' and a text channel named 'general' in it.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.discord", use_monkey=True)
        time.sleep(5)

        # check popup
        check_popup(self.d)
        
        # if not in home page, go back to home page
        if not is_home_page(self.d):
            self.d.press("back")
            time.sleep(2)
        
        # check if the server exists,if not create one
        if not check_server_exist(self.d, "agentian's server"):
            create_server(self.d, "agentian's server")
        
        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.discord")

class DiscordTask02(BaseTaskSetup):
    '''
    instruction: Create a new private text channel 'Testbed' in agentian's server on Discord app.
    setup: make sure there is a server named 'agentian' and a text channel named 'general' in it.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.discord", use_monkey=True)
        time.sleep(5)

        # check popup
        check_popup(self.d) 

        # if not in home page, go back to home page
        if not is_home_page(self.d):
            self.d.press("back")
            time.sleep(2)
        
        # check if the server exists,if not create one
        if not check_server_exist(self.d, "agentian's server"):
            create_server(self.d, "agentian's server")
        
        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.discord")

class DiscordTask03(BaseTaskSetup):
    '''
    instruction: Delete voice channel Lobby in agentian's server on Discord app.
    setup: make sure there is a server named 'agentian' and a voice channel named 'Lobby' in it.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.discord", use_monkey=True)
        time.sleep(5)
        
        # check popup
        check_popup(self.d)

        # if not in home page, go back to home page
        if not is_home_page(self.d):
            self.d.press("back")
            time.sleep(2)
        
        # check if the server exists,if not create one
        if not check_server_exist(self.d, "agentian's server"):
            create_server(self.d, "agentian's server")

        # go to the agentian's server 
        # a little wired, the server name is 'agentian's server' but the content description is '  agentian`s server'
        server = self.d(description="  agentian's server" , className="android.widget.Button")
        if not server.wait(timeout=5):
            raise SetupFailureException("agentian's server not found")
        server.click()
        # necceary to wait for the server page to load
        time.sleep(2)

        # if already in the agentian's server, go back to the home page
        if not is_home_page(self.d):
            self.d.press("back")
            time.sleep(2)

        # check if the 'lobby' voice channel exists,if not create one
        if not check_voice_channel_exist(self.d, "lobby"):
            create_voice_channel(self.d, "agentian's server", "lobby")

        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.discord")

class DiscordTask04(BaseTaskSetup):
    '''
    instruction: Upload my latest picture as server icon of agentian's server on Discord app.
    setup: make sure there is a server named 'agentian' and a picture in the device.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.discord", use_monkey=True)
        time.sleep(5)                
        
        # check popup
        check_popup(self.d)

        # when there is a server, Discord app will directly go to the server page
        # if not in home page, go back to home page
        if not is_home_page(self.d):
            self.d.press("back")
            time.sleep(2)

        # take a screenshot and save in this device
        get_screenshot(self.d)

        # check if the server exists,if not create one
        if not check_server_exist(self.d, "agentian's server"):
            create_server(self.d, "agentian's server")
        
        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.discord")

class DiscordTask05(BaseTaskSetup):
    '''
    instruction: Join the voice channel 'Gaming' in agentian's server on Discord app.
    setup: make sure there is a server named 'agentian'.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.discord", use_monkey=True)
        time.sleep(5)

        # check popup
        check_popup(self.d)

        # if not in home page, go back to home page
        if not is_home_page(self.d):
            self.d.press("back")
            time.sleep(2)
        
        # check if the server exists,if not create one
        if not check_server_exist(self.d, "agentian's server"):
            create_server(self.d, "agentian's server")

        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.discord")

class DiscordTask06(BaseTaskSetup):
    '''
    instruction: Turn to sever 'homework' and turn on 'Allow Direct Messages' on Discord app.
    setup: make sure there is a server named 'homework'.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.discord", use_monkey=True)
        time.sleep(5)

        # check popup
        check_popup(self.d)

        # if not in home page, go back to home page
        if not is_home_page(self.d):
            self.d.press("back")
            time.sleep(2)
        
        # check if the server exists,if not create one
        if not check_server_exist(self.d, "homework"):
            create_server(self.d, "homework")

        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.discord")
    
class DiscordTask07(BaseTaskSetup):
    '''
    instruction: Go to Settings of server 'Agent Env' on Discord app.
    setup: make sure there is a server named 'Agent Env'.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.discord", use_monkey=True)
        time.sleep(5)

        # check popup
        check_popup(self.d)

        # if not in home page, go back to home page
        if not is_home_page(self.d):
            self.d.press("back")
            time.sleep(2)
        
        # check if the server exists,if not create one
        if not check_server_exist(self.d, "Agent Env"):
            create_server(self.d, "Agent Env")
    
        # stop app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.discord")