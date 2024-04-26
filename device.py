import logging
import re
import os
import json
from utils.adb import ADB
from utils.droidbot_app import DroidBotAppConn


class ScreenshotException(Exception):
    pass


class Device(object):

    def __init__(self, device_serial,adb_clt_path="adb"):
        """
        Initialize a device connection with the bare minimum requirements.
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.serial = device_serial
        self.adb = ADB(device=self,adb_clt_path=adb_clt_path)
        self.display_info = None

        self.droidbot_app = DroidBotAppConn(device=self,adb_clt_path=adb_clt_path)

        self.sdk_version = None
        self.release_version = None

    def connect(self):
        """
        Connect to the device. Set up the DroidBot app and Minicap.
        """
        self.adb.connect()
        self.logger.info("ADB connected successfully.")
        print("ADB connected successfully.")
        self.droidbot_app.set_up()
        self.logger.info("DroidBotAppConn set up successfully.")
        print("DroidBotAppConn set up successfully.")
        self.droidbot_app.connect()
        self.logger.info("DroidBotAppConn connected successfully.") 
        print("DroidBotAppConn connected successfully.")



    def disconnect(self):
        """
        Disconnect from the device.
        """
        self.droidbot_app.disconnect()

        self.adb.disconnect()


    def get_views(self):
        """
        Retrieve the current views from the DroidBot app.
        """
        if not hasattr(self, 'droidbot_app'):
            self.logger.error("DroidBotAppConn is not set up properly.")
            return None

        try:
            views = self.droidbot_app.get_views()
            if views:
                # print(views)
                return views
            else:
                self.logger.warning("Failed to get views from DroidBotAppConn.")
                return None
        except AttributeError as e:
            self.logger.error(f"An error occurred: {str(e)}")
            return None
        
    def get_service_names(self):
        """
        get current running services
        :return: list of services
        """
        services = []
        dat = self.adb.shell('dumpsys activity services')
        lines = dat.splitlines()
        service_re = re.compile('^.+ServiceRecord{.+ ([A-Za-z0-9_.]+)/([A-Za-z0-9_.]+)')

        for line in lines:
            m = service_re.search(line)
            if m:
                package = m.group(1)
                service = m.group(2)
                services.append("%s/%s" % (package, service))
        return services
    
    def push_file(self, local_file, remote_dir="/sdcard/"):
        """
        push file/directory to target_dir
        :param local_file: path to file/directory in host machine
        :param remote_dir: path to target directory in device
        :return:
        """
        if not os.path.exists(local_file):
            self.logger.warning("push_file file does not exist: %s" % local_file)
        self.adb.run_cmd(["push", local_file, remote_dir])

    def pull_file(self, remote_file, local_file):
        self.adb.run_cmd(["pull", remote_file, local_file])

    def get_sdk_version(self):
        """
        Get version of current SDK
        """
        if self.sdk_version is None:
            self.sdk_version = self.adb.get_sdk_version()
        return self.sdk_version

    def get_release_version(self):
        """
        Get version of current SDK
        """
        if self.release_version is None:
            self.release_version = self.adb.get_release_version()
        return self.release_version

    def get_display_info(self, refresh=True):
        """
        get device display information, including width, height, and density
        :param refresh: if set to True, refresh the display info instead of using the old values
        :return: dict, display_info
        """
        if self.display_info is None or refresh:
            self.display_info = self.adb.get_display_info()
        return self.display_info

    def get_width(self, refresh=False):
        display_info = self.get_display_info(refresh=refresh)
        width = 0
        if "width" in display_info:
            width = display_info["width"]
        elif not refresh:
            width = self.get_width(refresh=True)
        else:
            self.logger.warning("get_width: width not in display_info")
        return width

    def get_height(self, refresh=False):
        display_info = self.get_display_info(refresh=refresh)
        height = 0
        if "height" in display_info:
            height = display_info["height"]
        elif not refresh:
            height = self.get_width(refresh=True)
        else:
            self.logger.warning("get_height: height not in display_info")
        return height

    def get_top_activity_name(self):
        """
        Get current activity
        """
        r = self.adb.shell("dumpsys activity activities")
        activity_line_re = re.compile(r'\*\s*Hist\s*#\d+:\s*ActivityRecord\{[^ ]+\s*[^ ]+\s*([^ ]+)\s*t(\d+)}')
        m = activity_line_re.search(r)
        if m:
            return m.group(1)
        self.logger.warning("Unable to get top activity name.")
        return None
    
    def get_brand(self):
        """
        Get device brand
        """
        return self.adb.shell("getprop ro.product.brand")
    
    def get_size(self):
        adb_command = "wm size"
        result = self.adb.shell(adb_command)
        if result != "ERROR":
            return map(int, result.split(": ")[1].split("x"))
        return 0, 0
    
    def take_screenshot(self,local_fp):
        """"
        return image data
        """
        times = 0
        success = False
        remote_fp = f"/sdcard/{local_fp.split('/')[-1]}"
        while not success and times < 20:
            try:
                # self.adb.run_cmd(f"exec-out screencap -p > {local_fp}")
                self.adb.run_cmd(f"shell screencap -p {remote_fp}")
                self.adb.run_cmd(f"pull {remote_fp} {local_fp}")
                # check if the file exists, if so, set success to True to exit the loop
                if os.path.exists(local_fp):
                    success = True
                    self.adb.run_cmd(f"shell rm {remote_fp}")
            except Exception as e:
                self.logger.info(f"try {times + 1} fail: {e}")

            times += 1

        if not success:
            # if failed after 20 times, raise a custom exception
            raise ScreenshotException(f"20 times failed to get screenshot and save to {local_fp}")

        return local_fp
    
    def dumpsy_device_state(self,file_path):
        """
        function: dumpsys device state to a json file
        """
        state = dict()
        state["wifi_mode"] = self.adb.shell("dumpsys wifi | grep 'Wi-Fi is'")
        state["zen_mode"]  =self.adb.shell("settings get global zen_mode")
        state["location_mode"] = self.adb.shell("settings get secure location_mode")
        state["bluetooth_mode"] = self.adb.shell("dumpsys bluetooth_manager | grep 'state: '")
        state["airplane_mode"] = self.adb.shell("settings get global airplane_mode_on")

        with open(file_path,"w") as f:
            json.dump([state], f, indent=4)

        
        
    


    

