from setup.tasks.BaseTaskSetup import BaseTaskSetup
import time

def get_screenshot(d) -> None:
    d.screenshot("/sdcard/screenshot.png")
    time.sleep(2)

def create_sheet(d, sheet_name="Testbed") -> None:
    # create a new sheet
    d(description="Files").click()
    time.sleep(2)
    d(text="My Drive").click()
    time.sleep(2)
    d(description="Create").click()
    time.sleep(2)
    d(description="Google Sheets").click()
    time.sleep(2)
    d.press("back")
    time.sleep(2)
    # rename the sheet
    d(description="More actions for Untitled spreadsheet").click()
    time.sleep(2)
    d(text="Rename").click()
    time.sleep(2)
    d(resourceId="com.google.android.apps.docs:id/edit_text").set_text(sheet_name)
    time.sleep(2)
    d(resourceId="com.google.android.apps.docs:id/positive_button").click()


def check_sheet_exist(d, sheet_name="Testbed") -> bool:
    d(description="Files").click()
    time.sleep(2)
    d(text="My Drive").click()
    time.sleep(2)
    exists = d(className="android.widget.TextView", description=f"{sheet_name}, Google Sheets").exists()
    return exists

class GoogleDriveTask01(BaseTaskSetup):
    '''
    instruction: Upload the latest photo from my device to a new folder named 'Selfie2024' on Google Drive app.
    setup: make sure there is a photo in the device.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)

    def setup(self):
        # start app
        self.d.app_start("com.google.android.apps.docs", use_monkey=True)
        get_screenshot(self.d)
        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.google.android.apps.docs")


class GoogleDriveTask02(BaseTaskSetup):
    '''
    instruction: Share the 'Testbed' spreadsheet on Google Drive by copy link, make sure anyone with the link can view.
    setup: make sure there is 'Testbed' spreadsheet on Google Drive.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)

    def setup(self):
        # start app
        self.d.app_start("com.google.android.apps.docs", use_monkey=True)
        if not check_sheet_exist(self.d):
            create_sheet(self.d)
        else:
            print("Sheet already exists.")
        
        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.google.android.apps.docs")