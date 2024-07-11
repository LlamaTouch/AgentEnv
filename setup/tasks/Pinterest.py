from setup.tasks.BaseTaskSetup import BaseTaskSetup, SetupFailureException
import time
from uiautomator2 import Device
# Pinterest app version: 12.14.0


def create_board(d: Device, board_name: str = "DIY") -> None:
    """
    start from the home page of Pinterest app
    """
    try:
        # Navigate to 'Saved' tab
        saved_tab = d(description="Saved, Tab")
        if not saved_tab.wait(timeout=5):
            raise SetupFailureException("Saved tab not found")
        saved_tab.click()

        # Navigate to 'Boards'
        boards_button = d(text="Boards")
        if not boards_button.wait(timeout=5):
            raise SetupFailureException("Boards button not found")
        boards_button.click()

        # Click the button with the specified resource ID '+'
        icon_button = d(resourceId="com.pinterest:id/icon_button")
        if not icon_button.wait(timeout=5):
            raise SetupFailureException("Icon button not found")
        icon_button.click()
        
        # choose 'Board' after clicking '+'
        board_button = d(text="Board")
        if not board_button.wait(timeout=5):
            raise SetupFailureException("Board button not found")
        board_button.click()

        # Enter the board name
        board_name_input = d(resourceId="com.pinterest:id/edit_text")
        if not board_name_input.wait(timeout=5):
            raise SetupFailureException("Board name input not found")
        board_name_input.set_text(board_name)

        # Click the 'Next' button
        create_board_confirm_button = d(text="Next")
        if not create_board_confirm_button.wait(timeout=5):
            raise SetupFailureException("Create board confirm button not found")
        create_board_confirm_button.click()
        
        # Click the 'Done' button
        create_board_confirm_button = d(text="Done")
        if not create_board_confirm_button.wait(timeout=5):
            raise SetupFailureException("Create board confirm button not found")
        create_board_confirm_button.click()

    except Exception as e:
        raise SetupFailureException(f"An error occurred when create board: {e}")


def check_exist_board(d: Device, board_name: str = "DIY") -> bool:
    """
    start from the home page of Pinterest app
    """
    try:
        # Navigate to 'Saved' tab
        saved_tab = d(description="Saved, Tab")
        if not saved_tab.wait(timeout=5):
            raise SetupFailureException("Saved tab not found")
        saved_tab.click()

        # Navigate to 'Boards'
        boards_button = d(text="Boards")
        if not boards_button.wait(timeout=5):
            raise SetupFailureException("Boards button not found")
        boards_button.click()
        
        board_list = []
        boards = d.xpath('//androidx.recyclerview.widget.RecyclerView[@resource-id="com.pinterest:id/recycler_adapter_view"]')\
            .child('.//android.view.ViewGroup').all()
        
        for board in boards:
            name = board.info.get("contentDescription")
            if name:
                board_list.append(name)
        
        if board_name in board_list:
            print(f"{board_name} already exists.")
            return True
        print(f"{board_name} not exists.")
        return False

    except Exception as e:
        raise SetupFailureException(f"An error occurred when check exist board!:{e}")


class PinterestTask01(BaseTaskSetup):
    '''
    instruction: Open Pinterest and open one of your own board.
    setup: make sure there is a board in your own board list.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.pinterest", use_monkey=True)
        time.sleep(2)
        
        if not check_exist_board(self.d, "DIY"):
            create_board(self.d, "DIY")

        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.pinterest")


class PinterestTask02(BaseTaskSetup):
    '''
    instruction: Open Pinterest and search "DIY" in your own board list and open it.
    setup: make sure there is a board named "DIY" in your own board list.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.pinterest", use_monkey=True)
        time.sleep(2)
        
        if not check_exist_board(self.d, "DIY"):
            create_board(self.d, "DIY")

        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.pinterest")