from setup.tasks.BaseTaskSetup import BaseTaskSetup,SetupFailureException
import time
from uiautomator2 import Device

def add_to_cart(d: Device):
    """
    start from the Home page
    add a milk to cart 
    """
    try:
        # go to Home page first
        home = d(resourceId="com.dd.doordash:id/homepage") 
        if not home.wait(timeout=5):
            # restart the app and go to Home page
            d.press("home")   
            d.app_stop("com.dd.doordash")
            time.sleep(2)
            d.app_start("com.dd.doordash", use_monkey=True)
            time.sleep(5)

        if not home.wait(timeout=5):
            raise SetupFailureException("Home page not found")
        home.click()

        # Click on edit text field
        edit_text = d(resourceId="com.dd.doordash:id/edit_text")
        if not edit_text.wait(timeout=5):
            raise SetupFailureException("Edit text field not found")
        edit_text.click()

        # search for coffee
        edit_text2 = d(resourceId="com.dd.doordash:id/edit_text")
        if not edit_text2.wait(timeout=5):
            raise SetupFailureException("Edit text field not found")
        edit_text2.set_text("milk")
        
        # press milk
        milk = d.xpath('//android.widget.TextView[@resource-id="com.dd.doordash:id/title" and @text="milk"]')
        if not milk.wait(timeout=5):
            raise SetupFailureException("milk field not found")
        milk.click()

        # add button
        add_button = d.xpath('(//android.widget.ImageView[@content-desc="Add"])[1]')
        if not add_button.wait(timeout=5):
            raise SetupFailureException("Add button not found")
        add_button.click()

    except Exception as e:
        raise SetupFailureException(f"An error occurred when add a milk to cart: {e}")
    
def save_store(d: Device):
    """
    start from the Home page
    save a coffee store
    """
    try:
        # go to Home page first
        home = d(resourceId="com.dd.doordash:id/homepage") 
        if not home.wait(timeout=5):
            # restart the app and go to Home page
            d.press("home")   
            d.app_stop("com.dd.doordash")
            time.sleep(2)
            d.app_start("com.dd.doordash", use_monkey=True)
            time.sleep(5)

        if not home.wait(timeout=5):
            raise SetupFailureException("Home page not found")
        home.click()

        # Click on edit text field
        edit_text = d(resourceId="com.dd.doordash:id/edit_text")
        if not edit_text.wait(timeout=5):
            raise SetupFailureException("Edit text field not found")
        edit_text.click()

        # search for coffee
        edit_text2 = d(resourceId="com.dd.doordash:id/edit_text")
        if not edit_text2.wait(timeout=5):
            raise SetupFailureException("Edit text field not found")
        edit_text2.set_text("coffee")
        
        # press coffee
        coffee = d.xpath('//android.widget.TextView[@resource-id="com.dd.doordash:id/title" and @text="coffee"]')
        if not coffee.wait(timeout=5):
            raise SetupFailureException("coffee field not found")
        coffee.click()

        # Click on the seventh instance of FrameLayout
        frame_layout = d.xpath('//androidx.recyclerview.widget.RecyclerView[@resource-id="com.dd.doordash:id/results_list"]/android.widget.FrameLayout[1]')
        if not frame_layout.wait(timeout=5):
            raise SetupFailureException("Seventh instance of FrameLayout not found")
        frame_layout.click()

        # Click on 'Save' button by accessibility ID
        save_button = d(description="Save")
        if not save_button.wait(timeout=5):
            raise SetupFailureException("Save button not found")
        save_button.click()

    except Exception as e:
        raise SetupFailureException(f"An error occurred when save a store: {e}")
    	

class DoorDashTask01(BaseTaskSetup):
    '''
    instruction: Clear my cart on DoorDash app.
    setup: make sure there is one item in your cart at least.   
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.dd.doordash", use_monkey=True)
        time.sleep(5)
        
        # add a milk to cart
        add_to_cart(self.d)
	
        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.dd.doordash")


class DoorDashTask02(BaseTaskSetup):
    '''
    instruction: DoorDash, turn to the first one of saved stores, and add the most liked item to my cart.
    setup: make sure there is one store saved at least.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.dd.doordash", use_monkey=True)
        time.sleep(5)
        
        # save a store
        save_store(self.d)

        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.dd.doordash")

    
class DoorDashTask03(BaseTaskSetup):
    '''
    instruction: DoorDash, turn to the first one of saved stores, start a group order and copy its link.
    setup: make sure there is one store saved at least.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.dd.doordash", use_monkey=True)
        time.sleep(5)

        # save a store
        save_store(self.d)

        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.dd.doordash")
