from setup.tasks.BaseTaskSetup import BaseTaskSetup, SetupFailureException
import time
from uiautomator2 import Device

def save_news_article(d: Device):
    '''
    start from home page and save the first news article.
    '''
    try:
        # Click on 'Refresh' button by accessibility ID
        refresh_button = d(description="Refresh")
        if not refresh_button.wait(timeout=5):
            raise SetupFailureException("Refresh button not found")
        refresh_button.click()

        # Click on the first news article
        linear_layout = d.xpath('//androidx.recyclerview.widget.RecyclerView[@resource-id="com.particlenews.newsbreak:id/list"]/android.widget.LinearLayout[2]')
        if not linear_layout.wait(timeout=5):
            raise SetupFailureException("first news article not found")
        linear_layout.click()

        # Click save button
        action_button = d(resourceId="com.particlenews.newsbreak:id/toolbar_action_btn")
        if not action_button.wait(timeout=5):
            raise SetupFailureException("save button not found")
        action_button.click()

    except Exception as e:
        raise SetupFailureException(f"An error occurred while saving news article.:{e}")

class NewsBreakTask01(BaseTaskSetup):
    '''
    instruction: Open my latest saved news acticle on NewsBreak app and check comments.
    setup: Make sure there is at least one saved news article.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # Start the Quora app
        self.d.app_start("com.particlenews.newsbreak")
        time.sleep(5)
        
        # save a news article
        save_news_article(self.d)

        # Stop the app
        self.d.press("home")
        time.sleep(5)
        self.d.app_stop("com.particlenews.newsbreak")