from setup.tasks.BaseTaskSetup import BaseTaskSetup, SetupFailureException
import time
from uiautomator2 import Device
# Quora app version: 3.2.27

def follow_recommended_space(d: Device):
    '''
    Quora app start app at home page defaultly.
    start from the home page, follow the first recommended space and there are no spaces followed yet.
    '''
    try:
        # Navigate to the following page
        follow_page = d.xpath('(//android.widget.RelativeLayout[@resource-id="com.quora.android:id/badge_wrapper"])[2]')
        if not follow_page.wait(5):
            raise SetupFailureException("Following page not found.")
        follow_page.click()
        
        # check if the "Spaces you might like" text view exists if exists it means have not follow any space
        text_view = d.xpath('//android.widget.TextView[@text="Spaces you might like"]')
        if not text_view.wait(10):
            return
        
        # follow the fist recommended space
        space = d.xpath('//android.webkit.WebView[@text="Following"]/android.view.View/android.view.View/android.view.View/android.view.View[1]')
        if not space.wait(5):
            raise SetupFailureException('Specified view does not exist."')
        space.click()
            
        # Follow the space
        follow_btn = d.xpath('//android.widget.Button[@text="Follow"]')
        if not follow_btn.wait(5):
            raise SetupFailureException("Follow button not found.")
        follow_btn.click()
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise SetupFailureException("An error occurred while follow recommended sapce.") 

def bookmark_post(d: Device):
    '''
    Quora app start app at home page defaultly.
    start from home page and bookmark a post.(my following page the first post or follow a space first and then bookmark a post in that space)
    '''
    try:
        # make sure follow at least one space
        follow_recommended_space(d)
        
        # restart the app
        d.press("home")
        time.sleep(5)
        d.app_stop("com.quora.android")
        time.sleep(5)
        d.app_start("com.quora.android")
        
        # Navigate to the following page
        follow_page = d.xpath('(//android.widget.RelativeLayout[@resource-id="com.quora.android:id/badge_wrapper"])[2]')
        if not follow_page.wait(5):
            raise SetupFailureException("Following page not found.")
        follow_page.click()

        # check if the "Spaces you might like" text view exists if exists it means have not follow any space
        text_view = d.xpath('//android.widget.TextView[@text="Spaces you might like"]')
        if text_view.wait(10):
            raise SetupFailureException("don't follow any space yet.")
        
        # go to first post
        post = d.xpath('//android.webkit.WebView[@text="Following"]/android.view.View/android.view.View/android.view.View/android.view.View[2]')
        if not post.wait(10):
            raise SetupFailureException("First post not found.")
        post.click()

        # bookmark the post
        # Attempt to click the 'More' button and bookmark the post
        more_button = d(text="More")
        if not more_button.wait(5):
            raise SetupFailureException("More button not found.")
        more_button.click()

        bookmark_button = d(text="Bookmark")
        if not bookmark_button.wait(5):
            raise SetupFailureException("Bookmark option not found.")
        bookmark_button.click()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise SetupFailureException("An error occurred while bookmark first post.")
    
class QuoraTask01(BaseTaskSetup):
    '''
    instruction: In page 'Following', check latest posts and click the first one on the Quora app.
    setup: Make sure follow at least one topic, user, or question on Quora.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # Start the Quora app
        self.d.app_start("com.quora.android")
        time.sleep(5)
        
        # if not follow any space, follow the first recommended space
        follow_recommended_space(self.d)

        # Stop the app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.quora.android")

class QuoraTask02(BaseTaskSetup):
    '''
    instruction: Upvote all contents I've bookmarked on the Quora app.
    setup: make sure there is at least one bookmarked post.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
      
    def setup(self):
        # Start the Quora app
        self.d.app_start("com.quora.android")
        time.sleep(5)

        # bookmark a post
        bookmark_post(self.d)
    
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.quora.android")

class QuoraTask03(BaseTaskSetup):
    '''
    instruction: Check the log of latest answer I've bookmarked on Quora app.
    setup: make sure there is at least one bookmarked answer.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # Start the Quora app
        self.d.app_start("com.quora.android")
        time.sleep(5)

        # bookmark a post
        bookmark_post(self.d)
    
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.quora.android")



