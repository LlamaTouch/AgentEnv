from setup.tasks.BaseTaskSetup import BaseTaskSetup
import time
from uiautomator2 import Device

def create_board(d: Device, board_name: str="School") -> None:
    """
    start from home page
    end at home page
    """
    try:
        # Open the "Create board or add card" menu
        open_menu = d(description="Open create board or add card menu")
        if not open_menu.exists(timeout=5):
            raise Exception("The menu to create board or add card cannot be opened.")
        open_menu.click()

        # Navigate to add a new board
        add_board_option = d(resourceId="com.trello:id/add_board_text")
        if not add_board_option.exists(timeout=5):
            raise Exception("The option to add a new board is not available.")
        add_board_option.click()

        # Enter the name of the board
        board_name_field = d(resourceId="com.trello:id/board_name")
        if not board_name_field.exists(timeout=5):
            raise Exception("The field to enter the board name does not exist.")
        board_name_field.set_text(board_name)

        # Click the create board button
        create_board_button = d(resourceId="com.trello:id/create_board_button")
        if not create_board_button.exists(timeout=5):
            raise Exception("The button to create the board is not available.")
        create_board_button.click()

        # Navigate back to the home page
        d.press("back")
        
    except Exception as e:
        print(f"An error occurred while creating the board: {e}")

def check_board_exist(d: Device, board_name: str="School") -> bool:
    """
    start from home page
    end at home page
    """
    # Check if the board exists
    exists = d(text=board_name).exists()
    return exists

def get_all_listname_in_board(d: Device) -> list:
    """
    start from a broad page
    end at a board page
    """
    list_names = []
    max_steps = 30  # Maximum number of swipes

    for _ in range(max_steps):
        # Get all list names on the current screen
        lists = d.xpath('//android.widget.AutoCompleteTextView[@resource-id="com.trello:id/list_name"]')
        for list_item in lists.all():
            name = list_item.text
            if name not in list_names:
                list_names.append(name)
        
        # Check if the end marker exists
        if d.xpath('//android.widget.Button[@resource-id="com.trello:id/add_list_button"]').exists():
            break

        # Swipe left to view more lists, making smaller movements
        d.swipe(800, 500, 700, 500, 0.5) 
        time.sleep(2)  

        # In case no new lists are found in the current swipe, and end marker is not visible, stop to avoid infinite loop
        if not lists.exists():
            break

    return list_names

def check_list_exist(d: Device, list_name: str="To Do") -> bool:
    """
    start from board page
    end at board page
    func: check if the list exists in a board
    """
    list_names = get_all_listname_in_board(d)
    if list_name in list_names:
        return True
    return False

def create_list(d: Device, list_name: str="To Do") -> None:
    """
    start from board page
    end at board page
    """
    try:
        # Swipe to find the "Add list" button
        max_steps = 30  # Maximum number of swipes
        found = False
        for _ in range(max_steps):
            if d.xpath('//android.widget.Button[@resource-id="com.trello:id/add_list_button"]').exists():
                print("Add list button found")
                found = True
                break
            d.swipe(800, 500, 700, 500, 0.5)  # Swipe left to view more lists

        if not found:
            raise Exception("Add list button not found after maximum swipes.")

        # Click the "Add list" button
        d.xpath('//android.widget.Button[@resource-id="com.trello:id/add_list_button"]').click()

        # Enter the name of the list
        list_name_field = d(resourceId="com.trello:id/list_name_edit_text")
        if not list_name_field.exists(timeout=5):
            raise Exception("List name input field does not exist.")
        list_name_field.set_text(list_name)

        # Click the "Save" button
        save_button = d(description="Save")
        if not save_button.exists(timeout=5):
            raise Exception("The 'Save' button does not exist.")
        save_button.click()
        
    except Exception as e:
        print(f"An error occurred while creating the list: {e}")

def create_card(d: Device,card_name: str="task") -> None:
    """
    start from board page after a list is created
    end at board page
    """
    try:
        # Check if the "Add card" button exists
        add_card_button = d(description="Add card")
        if not add_card_button.exists(timeout=5):
            raise Exception("The 'Add card' button does not exist. please check if a list is created.")

        # Click the "Add card" button
        add_card_button.click()

        # Enter the name of the card
        card_name_field = d(resourceId="com.trello:id/card_name_edit_text")
        if not card_name_field.exists(timeout=5):
            raise Exception("Card name input field does not exist.")
        card_name_field.set_text(card_name)

        # Click the "Save" button
        save_button = d(description="Save")
        if not save_button.exists(timeout=5):
            raise Exception("The 'Save' button does not exist.")
        save_button.click()
        
    except Exception as e:
        print(f"An error occurred while creating the card: {e}")

class TrelloTask01(BaseTaskSetup):
    '''
    instruction: Open the Trello app and add a new list titled "To Do" to the "School" board.
    setup: Make sure there is a board named "School".
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.trello", use_monkey=True)
        time.sleep(2)

        # make sure there is a "School" board
        if not check_board_exist(self.d, "School"):
            create_board(self.d, "School")

        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.trello")

class TrelloTask02(BaseTaskSetup):
    '''
    instruction: Open the Trello app, add a new card titled "Task 1" to the "To Do" list in the "School" board.
    setup: Make sure there is a board named "School" and a list named "To Do" in the board.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.trello", use_monkey=True)
        time.sleep(2)

        # make sure there is a "School" board
        if not check_board_exist(self.d, "School"):
            create_board(self.d, "School")
        
        # go to the board page
        self.d(text="School").click()

        # make sure there is a "To Do" list in the "School" board
        if not check_list_exist(self.d, "To Do"):
            create_list(self.d, "To Do")
        
        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.trello")

class TrelloTask03(BaseTaskSetup):
    '''
    instruction: Open the Trello app and archive a list named "To Do" in the "School" board.
    setup: Make sure there is a board named "School" and a list named "To Do".
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.trello", use_monkey=True)
        time.sleep(2)

        # make sure there is a "School" board
        if not check_board_exist(self.d, "School"):
            create_board(self.d, "School")
        
        # go to the board page
        self.d(text="School").click()

        # make sure there is a "To Do" list in the "School" board
        if not check_list_exist(self.d, "To Do"):
            create_list(self.d, "To Do")
        
        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.trello")

class TrelloTask04(BaseTaskSetup):
    '''
    instruction: Open the Trello app and set a due date for a card in the "School" board.
    setup: Make sure there is a board named "School" and and a list and then a card in the list.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.trello", use_monkey=True)
        time.sleep(2)

        # make sure there is a "School" board
        if not check_board_exist(self.d, "School"):
            create_board(self.d, "School")
        
        # go to the board page
        self.d(text="School").click()

        # create a "To Do" list in the "School" board
        create_list(self.d, "test")

        # create a card in the "To Do" list
        create_card(self.d,"task")
        
        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.trello")

