import time
from uiautomator2 import Device
from setup.tasks.BaseTaskSetup import BaseTaskSetup,SetupFailureException

	
# //android.widget.Button[@resource-id="com.crunchyroll.crunchyroid:id/empty_cta_primary_button"]
def check_crunchylist_exist(d: Device, list_name: str="weekly list"):
    """
    start from Home page
    func: check if the crunchylist named list_name exists
    """
    try:
        # Click on 'My Lists'
        my_lists_button = d(description="My Lists")
        if not my_lists_button.wait(timeout=5):
            raise SetupFailureException("My Lists button not found")
        my_lists_button.click()

        # Click on 'Crunchylists'
        crunchylist = d.xpath('//android.widget.TextView[@resource-id="com.crunchyroll.crunchyroid:id/tab_text" and @text="СRUNCHYLISTS"]')
        if not crunchylist.wait(timeout=5):
            raise SetupFailureException("Crunchylist not found")

        lists = d.xpath('//androidx.recyclerview.widget.RecyclerView[@resource-id="com.crunchyroll.crunchyroid:id/crunchylists_recycler_view"]\
                        /android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')
        
        if not list.wait(timeout=5):
            return False
        
        list_names = []
        for list in lists.all():
            list_names.append(list.info.get("text").strip())
        
        if list_name in list_names:
            return True
        
        return False

    except Exception as e:
        raise SetupFailureException(f"An error occurred when create crunchylist: {e}")

def create_crunchylist(d: Device, list_name: str="weekly list"):
    """
    start from Home page
    func: create a crunchylist named list_name
    """
    try:
        # Click on 'My Lists'
        my_lists_button = d(description="My Lists")
        if not my_lists_button.wait(timeout=5):
            raise SetupFailureException("My Lists button not found")
        my_lists_button.click()

        # Click on 'Crunchylists'
        crunchylist = d.xpath('//android.widget.TextView[@resource-id="com.crunchyroll.crunchyroid:id/tab_text" and @text="СRUNCHYLISTS"]')
        if not crunchylist.wait(timeout=5):
            raise SetupFailureException("Crunchylist not found")
        
        # Click on create list button
        create_list_button = d(text="CREATE NEW LIST")
        if not create_list_button.wait(timeout=5):
            raise SetupFailureException("Create list button not found")
        create_list_button.click()

        # Input for new list name
        list_name_input = d(resourceId="com.crunchyroll.crunchyroid:id/crunchylist_list_name_input")
        if not list_name_input.wait(timeout=5):
            raise SetupFailureException("List name input not found")
        list_name_input.set_text(list_name)

        # Click to confirm creating the list
        create_list_confirm_button = d(resourceId="com.crunchyroll.crunchyroid:id/crunchylists_cta_button")
        if not create_list_confirm_button.wait(timeout=5):
            raise SetupFailureException("Confirm create list button not found")
        create_list_confirm_button.click()

        # Click 'Navigate up' to go back
        navigate_up_button = d(description="Navigate up")
        if not navigate_up_button.wait(timeout=5):
            raise SetupFailureException("Navigate up button not found")
        navigate_up_button.click()

    except Exception as e:
        raise SetupFailureException(f"An error occurred when create crunchylist: {e}")

class CrunchyrollTask01(BaseTaskSetup):
    '''
    instruction: Find and add the anime series 'Attack on Titan' to my crunchylist 'weekly list' on the Crunchyroll app.
    setup: make sure there is a crunchylist named 'weekly list' in the crunchyroll app
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.crunchyroll.crunchyroid", use_monkey=True)
        time.sleep(10)
	    
        if not check_crunchylist_exist(self.d, "weekly list"):
            create_crunchylist(self.d, "weekly list")

        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.crunchyroll.crunchyroid")