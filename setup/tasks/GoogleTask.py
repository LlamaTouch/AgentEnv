from setup.tasks.BaseTaskSetup import BaseTaskSetup
import time
from uiautomator2 import Device
from uiautomator2.xpath import XPathSelector

def check_task_exist(d: Device, task_name: str="Task2") -> bool:
    '''
    Check if the task exists in the Google Task list.
    '''
    # Locate the parent HorizontalScrollView
    parent = d.xpath('//android.widget.HorizontalScrollView[@resource-id="com.google.android.apps.tasks:id/tabs"]')
    # Find all LinearLayout elements, excluding those with content-desc "New list"
    elements: XPathSelector = parent.child(className="android.widget.LinearLayout")
   
    for element in elements:
        # Get the content-desc attribute of the element
        ui_object = element.get()  # 转换为UiObject
        content_desc = ui_object.info.get('contentDescription', "")  
        
        # Check if the element does not have a content-desc "New list"
        if content_desc != "New list":
            # Perform the click action
            element.click()
            time.sleep(2)  # Wait for 2 seconds

            # Check if there is an element with text 'Task2'
            if d(text=task_name).exists():
                print(f"Found the element with text '{task_name}'")
                return True
            else:
                print(f"Did not find the element with text '{task_name}'")
                return False
            
def create_task(d: Device, task_name: str = "Task2") -> None:
    """
    Creates a task named 'task_name' in Google Tasks.
    Assumes the function starts from the main page of the Google Tasks app.
    """
    try:
        # Navigate to "My Tasks"
        my_tasks = d(text="My Tasks")
        if not my_tasks.exists(timeout=5):
            raise Exception("My Tasks button not found.")
        my_tasks.click()

        # Click on "Create new task"
        create_new_task = d(description="Create new task")
        if not create_new_task.exists(timeout=5):
            raise Exception("Create new task button not found.")
        create_new_task.click()

        # Enter the task name
        task_name_field = d(resourceId="com.google.android.apps.tasks:id/add_task_title")
        if not task_name_field.exists(timeout=5):
            raise Exception("Task name input field not found.")
        task_name_field.set_text(task_name)

        # Click the "Done" button to save the task
        done_button = d(resourceId="com.google.android.apps.tasks:id/add_task_done")
        if not done_button.exists(timeout=5):
            raise Exception("Done button not found.")
        done_button.click()

    except Exception as e:
        print(f"An error occurred while creating the task: {e}")

def check_list_exist(d: Device, list_name: str="Test") -> bool:
    '''
    check if the list exists in the Google Task list.
    '''
    # Locate the parent HorizontalScrollView
    parent = d.xpath('//android.widget.HorizontalScrollView[@resource-id="com.google.android.apps.tasks:id/tabs"]')

    # Find all LinearLayout elements, excluding those with content-desc "New list"
    elements = parent.child(className="android.widget.LinearLayout")

    for element in elements:
        # Check if the element has a content-desc "New list"
        ui_object = element.get()  # 转换为UiObject
        content_desc = ui_object.info.get('contentDescription', "")  
        if content_desc != list_name:
            return True
    
    return False

def create_list(d: Device, list_name: str = "Test") -> None:
    """
    Creates a new task list named 'list_name' in Google Tasks.
    Assumes the function starts from the main page where the 'New list' button is visible.
    """
    try:
        # Click on "New list"
        new_list_button = d(description="New list")
        if not new_list_button.exists(timeout=5):
            raise Exception("New list button not found.")
        new_list_button.click()

        # Enter the list name
        list_title_field = d(resourceId="com.google.android.apps.tasks:id/edit_list_title")
        if not list_title_field.exists(timeout=5):
            raise Exception("List title input field not found.")
        list_title_field.set_text(list_name)

        # Click the "Done" button to save the new list
        done_button = d(resourceId="com.google.android.apps.tasks:id/done_button")
        if not done_button.exists(timeout=5):
            raise Exception("Done button not found.")
        done_button.click()

    except Exception as e:
        print(f"An error occurred while creating the list: {e}")

class GoogleTask01(BaseTaskSetup):
    '''
    instruction: Open Google Tasks and star "Task2".
    setup: make sure there is a Task named "Task2".
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # Start the Google Tasks app
        self.d.app_start("com.google.android.apps.tasks")
        time.sleep(2)
        # Check if the task exists in the Google Task list
        if not check_task_exist(self.d):
            # If the task does not exist, create the task
            create_task(self.d)
        
        # Stop the Google Tasks app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.google.android.apps.tasks")

class GoogleTask02(BaseTaskSetup):
    '''
    instruction: Open Google Tasks and mark "Task2" as complete.
    setup: make sure there is a Task named "Task2".
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # Start the Google Tasks app
        self.d.app_start("com.google.android.apps.tasks")
        time.sleep(2)
        # Check if the task exists in the Google Task list
        if not check_task_exist(self.d):
            # If the task does not exist, create the task
            create_task(self.d)
        
        # Stop the Google Tasks app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.google.android.apps.tasks")

class GoogleTask03(BaseTaskSetup):
    '''
    instruction: Open Google Tasks and delete the list "Test".
    setup: make sure there is a list named "Test".
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # Start the Google Tasks app
        self.d.app_start("com.google.android.apps.tasks")
        time.sleep(2)
        # Check if the list exists in the Google Task list
        if check_list_exist(self.d):
            # If the list exists, delete the list
            create_list(self.d)
        
        # Stop the Google Tasks app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.google.android.apps.tasks")


