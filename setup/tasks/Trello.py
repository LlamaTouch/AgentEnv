from setup.tasks.BaseTaskSetup import BaseTaskSetup
import time

def create_board(d, board_name="School") -> None:
    """
    start from home page
    """
    # Open the create board or add card menu
    d(description="Open create board or add card menu").click()
    time.sleep(2)
    # Navigate to add a new board
    d(resourceId="com.trello:id/add_board_text").click()
    time.sleep(2)
    # Enter the name of the board
    d(resourceId="com.trello:id/board_name").set_text(board_name)
    time.sleep(2)
    # Click the create board button
    d(resourceId="com.trello:id/create_board_button").click()
    time.sleep(2)
    # back to main page
    d.press("back")
    time.sleep(2)

def check_board_exist(d, board_name="School") -> bool:
    """
    start from home page
    """
    # Check if the board exists
    exists = d(text=board_name).exists()
    return exists

def get_all_listname_in_board(d) -> list:
    """
    start from a broad page
    """
    list_names = []
    max_steps = 30  # Maximum number of swipes

    for _ in range(max_steps):
        # Get all list names on the current screen
        lists = d.xpath('//android.widget.AutoCompleteTextView[@resource-id="com.trello:id/list_name"]')
        for list_item in lists.all():
            name = list_item.get_text()
            if name not in list_names:
                list_names.append(name)
        
        # Check if the end marker exists
        if d.xpath('//android.widget.Button[@resource-id="com.trello:id/add_list_button"]').exists():
            break

        # Swipe left to view more lists, making smaller movements
        d.swipe(800, 500, 700, 500, 0.2) 
        time.sleep(2)  

        # In case no new lists are found in the current swipe, and end marker is not visible, stop to avoid infinite loop
        if not lists.exists():
            break

    return list_names


def check_list_exist(d, board_name="School", list_name="To Do") -> bool:
    pass


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
        
        # make sure there is a "To Do" list in the "School" board
        

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
        pass

class TrelloTask04(BaseTaskSetup):
    '''
    instruction: Open the Trello app and set a due date for a card in the "School" board.
    setup: Make sure there is a board named "School" and a card.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        pass
