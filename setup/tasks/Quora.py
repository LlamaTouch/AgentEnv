from setup.tasks.BaseTaskSetup import BaseTaskSetup
import time


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
        time.sleep(2)
        
        # Navigate to the following page
        try:
            self.d.xpath('//android.widget.RelativeLayout[@resource-id="com.quora.android:id/badge_wrapper"])[2]').click()
            time.sleep(2)
            text_view = self.d.xpath('//android.widget.TextView[@text="Spaces you might like"]')
            
            if text_view.wait():
                # Navigate to the first recommended space
                view = text_view.child('.//android.view.View[1]')
                
                # Check if the space exists
                if view.exists():
                    # Enter the first recommended space
                    view.click()
                    time.sleep(5)
                    
                    # Follow the space
                    follow_btn = self.d.xpath('//android.widget.Button[@text="Follow"]')
                    if follow_btn.wait():
                        follow_btn.click()
                    else:
                        print("Follow button not found.")
                else:
                    print("Specified view does not exist.")
            else:
                print("Specified TextView 'Spaces you might like' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
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
        time.sleep(2)
        
        # Navigate to the following page
        try:
            # Access the badge wrapper to navigate to the intended section
            navigation_path = '//android.widget.RelativeLayout[@resource-id="com.quora.android:id/badge_wrapper"])[2]'
            self.d.xpath(navigation_path).click()
            time.sleep(2)
            
            # Wait for the "Spaces you might like" text view to appear
            text_view = self.d.xpath('//android.widget.TextView[@text="Spaces you might like"]')
            if text_view.wait():
                # Navigate to the first recommended space
                view = text_view.child('.//android.view.View[1]')
                if view.exists():
                    view.click()
                    time.sleep(5)
                    
                    # Attempt to go to the first post
                    post = self.d.xpath('//android.webkit.WebView[@text="Quora"]/android.view.View/android.view.View[5]')
                    if post.wait():
                        post.click()
                        time.sleep(5)
                        
                        # Attempt to click the 'More' button and bookmark the post
                        if self.d(text="More").exists():
                            self.d(text="More").click()
                            time.sleep(2)
                            if self.d(text="Bookmark").exists():
                                self.d(text="Bookmark").click()
                            else:
                                print("Bookmark option not found.")
                        else:
                            print("More button not found.")
                    else:
                        print("First post not found.")
                else:
                    print("Specified view does not exist.")
            else:
                print("Specified TextView 'Spaces you might like' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            # Ensure the app is stopped even if an error occurs
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
        time.sleep(2)
        
        # Navigate to the following page
        try:
            # Access the badge wrapper to navigate to the intended section
            navigation_path = '//android.widget.RelativeLayout[@resource-id="com.quora.android:id/badge_wrapper"])[2]'
            self.d.xpath(navigation_path).click()
            time.sleep(2)
            
            # Wait for the "Spaces you might like" text view to appear
            text_view = self.d.xpath('//android.widget.TextView[@text="Spaces you might like"]')
            if text_view.wait():
                # Navigate to the first recommended space
                view = text_view.child('.//android.view.View[1]')
                if view.exists():
                    view.click()
                    time.sleep(5)
                    
                    # Attempt to go to the first post
                    post = self.d.xpath('//android.webkit.WebView[@text="Quora"]/android.view.View/android.view.View[5]')
                    if post.wait():
                        post.click()
                        time.sleep(5)
                        
                        # Attempt to click the 'More' button and bookmark the post
                        if self.d(text="More").exists():
                            self.d(text="More").click()
                            time.sleep(2)
                            if self.d(text="Bookmark").exists():
                                self.d(text="Bookmark").click()
                            else:
                                print("Bookmark option not found.")
                        else:
                            print("More button not found.")
                    else:
                        print("First post not found.")
                else:
                    print("Specified view does not exist.")
            else:
                print("Specified TextView 'Spaces you might like' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            # Ensure the app is stopped even if an error occurs
            self.d.press("home")
            time.sleep(2)
            self.d.app_stop("com.quora.android")


