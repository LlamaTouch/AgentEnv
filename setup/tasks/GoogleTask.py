from setup.tasks.BaseTaskSetup import BaseTaskSetup
import time

def check_task_exist(d, task_name="Task2") -> bool:
    '''
    Check if the task exists in the Google Task list.
    '''
    # Locate the parent HorizontalScrollView
    parent = d.xpath('//android.widget.HorizontalScrollView[@resource-id="com.google.android.apps.tasks:id/tabs"]')

    # Find all LinearLayout elements, excluding those with content-desc "New list"
    elements = parent.child(className="android.widget.LinearLayout")

    for element in elements:
        # Check if the element has a content-desc "New list"
        if element.attrib.get('content-desc') != "New list":
            # Perform the click action
            element.click()
            time.sleep(2)  # Wait for 2 seconds

            # Check if there is an element with text 'Task2'
            if d(text=task_name).exists:
                print(f"Found the element with text '{task_name}'")
                return True
            else:
                print(f"Did not find the element with text '{task_name}'")
                return False

def create_task(d, task_name="Task2") -> None:
    '''
    Create a task in the Google Task list.
    '''
    # Click on "My Tasks"
    d(text="My Tasks").click()
    time.sleep(2)
    
    # Click on "Create new task" (using content description)
    d(description="Create new task").click()
    time.sleep(2)
    
    # Enter the task name "Task2"
    d(resourceId="com.google.android.apps.tasks:id/add_task_title").set_text(f"{task_name}")
    time.sleep(2)
    
    # Click the "Done" button to save the task
    d(resourceId="com.google.android.apps.tasks:id/add_task_done").click()
    time.sleep(2)

def check_list_exist(d, list_name="Test") -> bool:
    '''
    check if the list exists in the Google Task list.
    '''
    # Locate the parent HorizontalScrollView
    parent = d.xpath('//android.widget.HorizontalScrollView[@resource-id="com.google.android.apps.tasks:id/tabs"]')

    # Find all LinearLayout elements, excluding those with content-desc "New list"
    elements = parent.child(className="android.widget.LinearLayout")

    for element in elements:
        # Check if the element has a content-desc "New list"
        if element.attrib.get('content-desc') != list_name:
            return True
    
    return False

def create_list(d, list_name="Test") -> None:
    '''
    Create a task list in the Google Task list.
    '''
    # Click on "New list" using its Accessibility ID, which maps to content description in uiautomator2
    d(description="New list").click()
    time.sleep(2)
    
    # Find the input field for the list title and enter "Test"
    d(resourceId="com.google.android.apps.tasks:id/edit_list_title").set_text(f"{list_name}")
    time.sleep(2)
    
    # Click the "Done" button to save the new list
    d(resourceId="com.google.android.apps.tasks:id/done_button").click()
    time.sleep(2)

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


