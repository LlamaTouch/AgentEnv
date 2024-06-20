import logging
from typing import List
import time
import uiautomator2 as u2
import subprocess

class Device(object):

    def __init__(self, device_serial: str) -> None:
        """
        Initialize a device connection with the bare minimum requirements.
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.serial = device_serial
        self.width, self.height = None, None

    def _activate_uiautomator2(self) -> None:
        try:
            # 初始化uiautomator2
            self.logger.info("Initializing uiautomator2...")
            subprocess.check_call(["python", "-m", "uiautomator2", "init"])
            time.sleep(5)

            # # 设置atx-agent的权限
            # self.logger.info("Setting permissions for atx-agent...")
            # self.device.adb.run_cmd(["shell", "chmod", "755", "/data/local/tmp/atx-agent"])
            
            # # 启动atx-agent服务
            # self.logger.info("Starting atx-agent server...")
            # self.device.adb.run_cmd(["shell", "/data/local/tmp/atx-agent", "server", "-d"])
            # print("atx-agent activated successfully.")

        except subprocess.CalledProcessError as e:
            print("Failed to initialize uiautomator2 with error:", e)
        # except Exception as e:
        #     print("An error occurred:", e)

    def connect(self) -> None:
        """
        Connect to the device. Set up the DroidBot app and Minicap.
        """
        self._activate_uiautomator2()
        time.sleep(5)
        self.u2d = u2.connect(self.serial)
        self.logger.info("Connected to device.")
        # self.adb.connect()
        # self.logger.info("ADB connected successfully.")
        # print("ADB connected successfully.")
        # self.droidbot_app.set_up()
        # self.logger.info("DroidBotAppConn set up successfully.")
        # print("DroidBotAppConn set up successfully.")
        # self.droidbot_app.connect()
        # self.logger.info("DroidBotAppConn connected successfully.") 
        # print("DroidBotAppConn connected successfully.")

    def disconnect(self) -> None:
        """
        Disconnect from the device.
        """
        self.u2d.stop_uiautomator()
        self.logger.info("Disconnected from device.")

    def get_viewhierachy(self) -> None:
        viewhierachy = self.u2d.dump_hierarchy(compressed=False, pretty=False, max_depth=50)
        return viewhierachy
    
    def get_screenshot(self) -> None:
        screenshot = self.u2d.screenshot()
        return screenshot
    
    def get_screen_size(self) -> tuple[int, int]:
        if self.width is None or self.height is None:
            self.width, self.height = self.u2d.window_size()
        return self.width, self.height
    
    def get_top_activity_name(self) -> str:
        current = self.u2d.app_current()
        return current['activity']
    
    def get_installed_apps(self) -> List[str]:
        return self.u2d.app_list()    

    def click(self, x: int, y: int):
        status = self.u2d.click(x, y)
        return status
        
    def swipe(self, x1: int, y1: int, x2: int, y2: int, duration=0.5):
        status = self.u2d.swipe(x1, y1, x2, y2, duration)
        return status

    def input_text(self, text: str):
        encoded = text
        status = self.u2d.send_keys(encoded)
        return status
    
    def enter(self):
        status = self.u2d.press("enter")
        return status
    
    def home(self):
        status = self.u2d.press("home")
        return status
    
    def back(self):
        status = self.u2d.press("back")
        return status


        
        
    


    

