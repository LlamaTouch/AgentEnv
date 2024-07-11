from BaseApp import BaseApp
import logging
import time

# 1
class Google_Tasks(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting Google_tasks...")
        self.d.app_start('com.google.android.apps.tasks', use_monkey=True)
        time.sleep(10)
        self.logger.info("Google_tasks started successfully.")
    
    def close(self):
        self.logger.info("Closing Google_tasks...")
        self.d.app_stop('com.google.android.apps.tasks')
        time.sleep(10)
        self.logger.info("Google_tasks closed successfully.")

    def login(self):
        self.start()
        self.close()
# 1
class YT_Music(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting YT_Music...")
        self.d.app_start('com.google.android.apps.youtube.music', use_monkey=True)
        time.sleep(10)
        self.logger.info("YT_Music started successfully.")
        
    def close(self):
        self.logger.info("Closing YT_Music...")
        self.d.app_stop('com.google.android.apps.youtube.music')
        time.sleep(10)
        self.logger.info("YT_Music closed successfully.")

    def login(self):
        self.start()
        self.close()
# 1   
class Google_Podcast(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def start(self):
        self.logger.info("Starting Google_Podcast...")
        self.d.app_start('com.google.android.apps.podcasts', use_monkey=True)
        time.sleep(10)
        self.logger.info("Google_Podcast started successfully.")
    
    def close(self):
        self.logger.info("Closing Google_Podcast...")
        self.d.app_stop('com.google.android.apps.podcasts')
        time.sleep(10)
        self.logger.info("Google_Podcast closed successfully.")

    def login(self):
        self.start()
        self.close()
# 1
class Google_Play_Books(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting Google_Play_Books...")
        self.d.app_start('com.google.android.apps.books', use_monkey=True)
        time.sleep(10)
        self.logger.info("Google_Play_Books started successfully.")
    
    def close(self):
        self.logger.info("Closing Google_Play_Books...")
        self.d.app_stop('com.google.android.apps.books')
        time.sleep(10)
        self.logger.info("Google_Play_Books closed successfully.")

    def login(self):
        self.start()
        self.close()
# 1
class Google_Drive(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting Google_Drive...")
        self.d.app_start('com.google.android.apps.docs', use_monkey=True)
        time.sleep(10)
        self.logger.info("Google_Drive started successfully.")
    
    def close(self):
        self.logger.info("Closing Google_Drive...")
        self.d.app_stop('com.google.android.apps.docs')
        time.sleep(10)
        self.logger.info("Google_Drive closed successfully.")

    def login(self):
        self.start()
        self.close()
# 1
class Google_Keep(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting Google_Keep...")
        self.d.app_start('com.google.android.keep', use_monkey=True)
        time.sleep(10)
        self.logger.info("Google_Keep started successfully.")
    
    def close(self):
        self.logger.info("Closing Google_Keep...")
        self.d.app_stop('com.google.android.keep')
        time.sleep(10)
        self.logger.info("Google_Keep closed successfully.")

    def login(self):
        self.start()
        self.close()
# 1
class Google_News(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting Google_News...")
        self.d.app_start('com.google.android.apps.magazines', use_monkey=True)
        time.sleep(10)
        self.logger.info("Google_News started successfully.")
    
    def close(self):
        self.logger.info("Closing Google_News...")
        self.d.app_stop('com.google.android.apps.magazines')
        time.sleep(10)
        self.logger.info("Google_News closed successfully.")

    def login(self):
        self.start()
        self.close()
# 1
class Youtube(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def start(self):
        self.logger.info("Starting Youtube...")
        self.d.app_start('com.google.android.youtube', use_monkey=True)
        time.sleep(10)
        self.logger.info("Youtube started successfully.")
    
    def close(self):
        self.logger.info("Closing Youtube...")
        self.d.app_stop('com.google.android.youtube')
        time.sleep(10)
        self.logger.info("Youtube closed successfully.")
    
    def login(self):
        self.start()
        self.close()    
# 1
class Pinterest(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting Pinterest...")
        self.d.app_start('com.pinterest', use_monkey=True)
        time.sleep(10)
        self.logger.info("Pinterest started successfully.")
    
    def close(self):
        self.logger.info("Closing Pinterest...")
        self.d.app_stop('com.pinterest')
        time.sleep(10)
        self.logger.info("Pinterest closed successfully.")

    def login(self):
        self.start()
        element = self.d.xpath('//android.widget.Button[@resource-id="com.google.android.gms:id/continue_button"]')
        if element.exists:
            element.click()
            time.sleep(10)
        else:
            element = self.d.xpath('//android.widget.Button[@resource-id="com.pinterest:id/gplus"]')
            if element.exists:
                self.d.xpath('//android.widget.Button[@resource-id="com.pinterest:id/gplus"]').click()
                time.sleep(10)
                self.d.xpath('(//android.widget.LinearLayout\
                            [@resource-id="com.google.android.gms:id/container"])[1]/android.widget.LinearLayout').click()
                time.sleep(10)
        # pre setting
        # setting birthday
        current_year = time.strftime('%Y', time.localtime())
        element = self.d.xpath(f'//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{current_year}"]')
        start_x, start_y, end_y = 0, 0, 0
        if element.exists:
            bounds = element.info['bounds']
            start_x = (bounds['left'] + bounds['right']) // 2
            start_y = bounds['top'] 
            end_y = bounds['bottom'] + (bounds['bottom'] - bounds['top']) * 2
        for i in range(10):
            self.d.swipe(start_x, start_y, start_x, end_y, 0.5)
            time.sleep(2)
        # click continue
        self.d.xpath('//android.widget.Button[@resource-id="android:id/button1"]').click()
        time.sleep(10)
        self.d.xpath('//android.widget.Button[@resource-id="com.pinterest:id/fragment_signup_step_button"]').click()
        time.sleep(10)  
        # set gender
        self.d.xpath('//android.widget.Button[@content-desc="Male"]').click()
        time.sleep(10)
        self.d.xpath('//android.widget.Button[@resource-id="com.pinterest:id/country_next_button"]').click()
        time.sleep(10)
        # choose first five interests
        for i in range(5):
            self.d.xpath(f'(//android.widget.ImageView[@content-desc="X"])[{i+1}]').click()
            time.sleep(2)
        self.d.xpath('//android.widget.Button[@resource-id="com.pinterest:id/nux_interest_next_button"]').click()
        time.sleep(10)
        self.close()
# 1
class Reddit(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting Reddit...")
        self.d.app_start('com.reddit.frontpage', use_monkey=True)
        time.sleep(10)
        self.logger.info("Reddit started successfully.")

    def close(self):
        self.logger.info("Closing Reddit...")
        self.d.app_stop('com.reddit.frontpage')
        time.sleep(10)
        self.logger.info("Reddit closed successfully.")

    def login(self):
        self.start()
        element = self.d.xpath('//android.widget.Button\
                               [@resource-id="com.google.android.gms:id/continue_button"]')
        if element.exists:
            element.click()
            time.sleep(5)
        else:   
            self.d.xpath('//android.widget.Button[@content-desc="Continue with Google"]').click()
            time.sleep(5)
            self.d.xpath('(//android.widget.LinearLayout\
                        [@resource-id="com.google.android.gms:id/container"])[1]/android.widget.LinearLayout').click()
            print("1111")
            time.sleep(10)
        # create account and init 
        # appium不能获取此界面，猜测的xpath
        element = self.d.xpath('//*[@text="Continue creating account"]')
        if element.exists:
            element.click()
        else:
            self.d.xpath('//*[@content-desc="Continue creating account"]').click()
        time.sleep(10)
        # restart app and skip some setting
        self.close()
        time.sleep(10)
        self.start()
        time.sleep(10)
        self.close()
# 1
class Coursera(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting Coursera...")
        self.d.app_start('org.coursera.android', use_monkey=True)
        time.sleep(10)
        self.logger.info("Coursera started successfully.")

    def close(self):
        self.logger.info("Closing Coursera...")
        self.d.app_stop('org.coursera.android')
        time.sleep(10)
        self.logger.info("Coursera closed successfully.")

    def login(self):
        self.start()
        time.sleep(10)
        element = self.d.xpath('//android.widget.Button\
                               [@resource-id="com.google.android.gms:id/continue_button"]')
        if element.exists:
            element.click()
        else:
            self.d.xpath('//android.widget.TextView[@text="Google"]').click()
            time.sleep(10)
            self.d.xpath('(//android.widget.LinearLayout[@resource-id="com.google.android.gms:id/container"])[1]\
                         /android.widget.LinearLayout').click()
        time.sleep(10)
        # click Got it button
        self.d.xpath('//android.widget.Button').click()
        time.sleep(10)
        self.close()
# 1
class Spotify(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        self.logger.info("Starting Spotify...")
        self.d.app_start('com.spotify.music', use_monkey=True)
        time.sleep(10)
        self.logger.info("Spotify started successfully.")

    def close(self):
        self.logger.info("Closing Spotify...")
        self.d.app_stop('com.spotify.music')
        time.sleep(10)
        self.logger.info("Spotify closed successfully.")

    def login(self):
        # appium can`t use
        self.start()
        self.d.xpath('//android.widget.Button[@text="Continue with Google"]').click()
        time.sleep(10)
        self.d.xpath('(//android.widget.LinearLayout\
                        [@resource-id="com.google.android.gms:id/container"])[1]/android.widget.LinearLayout').click()
        time.sleep(10)

        # birthday setting
        element = self.d.xpath('//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="2014"]')
        if element.exists:
            bounds = element.info['bounds']
            start_x = (bounds['left'] + bounds['right']) // 2
            start_y = bounds['top']
            end_y = bounds['bottom']

        for i in range(10):
            self.d.swipe(start_x, start_y, start_x, end_y, 0.5)
            time.sleep(2)

        self.d.xpath('//android.widget.Button[@text="Next"]').click()
        time.sleep(10)
        # 不确定对不对
        element = self.d.xpath('//*[@content-desc="Prefer not to say"]')
        if element.exists:
            element.click()
        else:
            self.d.xpath('//*[@text="Prefer not to say"]').click()
        time.sleep(10)
        self.d.xpath('//android.widget.TextView\
                     [@text="I agree to the Spotify Terms of Use and Privacy Policy."]').click()
        time.sleep(10)
        self.d.xpath('//android.widget.Button[@text="Create account"]').click()
        time.sleep(10)
        # random choose artist
        for i in range(3):
            self.d.xpath(f'(//android.widget.ImageView[@resource-id="com.spotify.music:id/image"])[{i+1}]').click()
            time.sleep(2)
        self.d.xpath('//android.widget.Button[@text="Done"]').click()
        time.sleep(10)
        self.close()
# 1
class Gmail(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def start(self):
        self.logger.info("Starting Gmail...")
        self.d.app_start('com.google.android.gm', use_monkey=True)
        time.sleep(10)
        self.logger.info("Gmail started successfully.")
    
    def close(self):
        self.logger.info("Closing Gmail...")
        self.d.app_stop('com.google.android.gm')
        time.sleep(10)
        self.logger.info("Gmail closed successfully.")

    def login(self):
        self.start()
        self.d.xpath('//android.widget.TextView\
                     [@resource-id="com.google.android.gm:id/welcome_tour_got_it"]').click()
        time.sleep(10)
        self.d.xpath('//android.widget.TextView[@resource-id="com.google.android.gm:id/action_done"]').click()
        time.sleep(10)
        self.close()

class CBS_Sports(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def start(self):
        self.logger.info("Starting CBS_Sports...")
        self.d.app_start('com.handmark.sportcaster', use_monkey=True)
        time.sleep(10)
        self.logger.info("CBS_Sports started successfully.")
    
    def close(self):
        self.logger.info("Closing CBS_Sports...")
        self.d.app_stop('com.handmark.sportcaster')
        time.sleep(10)
        self.logger.info("CBS_Sports closed successfully.")

    def login(self):
        self.start()
        self.close()

class Google_Keep_Notes(BaseApp):
    def __init__(self, device, app_name):
        super().__init__(device, app_name)
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def start(self):
        self.logger.info("Starting Google_Keep_Notes...")
        self.d.app_start('com.google.android.keep', use_monkey=True)
        time.sleep(10)
        self.logger.info("Google_Keep_Notes started successfully.")
    
    def close(self):
        self.logger.info("Closing Google_Keep_Notes...")
        self.d.app_stop('com.google.android.keep')
        time.sleep(10)
        self.logger.info("Google_Keep_Notes closed successfully.")

    def login(self):
        self.start()
        self.close()
