from setup.tasks.BaseTaskSetup import BaseTaskSetup, SetupFailureException
import time
from uiautomator2 import Device
# Google Tasks app version: 2024.06.10.644692922.1-release

def check_task_exist(d: Device, task_name: str="Task2") -> bool:
    '''
    Check if the task exists in the Google Task list.
    '''
    all_task_names = []
    # Find all task list elements
    task_lists = d.xpath('//android.widget.HorizontalScrollView[@resource-id="com.google.android.apps.tasks:id/tabs"]\
                     /android.widget.LinearLayout/android.widget.LinearLayout').all()
    
    # record all task names by traversing all task lists
    for task_list in task_lists:
        task_list_name = task_list.info.get('contentDescription', "").strip()
        if task_list_name != "New list":
            # enter the task list
            task_list.click()
            time.sleep(2)
            task_names = d.xpath('//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.apps.tasks:id/tasks_list"]\
                                 /android.widget.FrameLayout').all()
            
            # record name
            for task in task_names:
                task = d.xpath(f"{task.get_xpath()}/android.widget.FrameLayout")
                name = task.info.get('contentDescription', "").strip()
                if name != "":
                    all_task_names.append(name)
    
    if task_name in all_task_names:
        print(f"{task_name} already exists")
        return True
    
    print(f"{task_name} not exists")
    return False

def create_task(d: Device, task_name: str = "Task2") -> None:
    """
    Creates a task named 'task_name' in Google Tasks.
    Assumes the function starts from the main page of the Google Tasks app.
    """
    try:
        # Navigate to "My Tasks"
        my_tasks = d(text="My Tasks")
        if not my_tasks.wait(timeout=5):
            raise SetupFailureException("My Tasks button not found.")
        my_tasks.click()

        # Click on "Create new task"
        create_new_task = d(description="Create new task")
        if not create_new_task.wait(timeout=5):
            raise SetupFailureException("Create new task button not found.")
        create_new_task.click()

        # Enter the task name
        task_name_field = d(resourceId="com.google.android.apps.tasks:id/add_task_title")
        if not task_name_field.wait(timeout=5):
            raise SetupFailureException("Task name input field not found.")
        task_name_field.set_text(task_name)

        # Click the "Done" button to save the task
        done_button = d(resourceId="com.google.android.apps.tasks:id/add_task_done")
        if not done_button.wait(timeout=5):
            raise SetupFailureException("Done button not found.")
        done_button.click()

    except Exception as e:
        raise SetupFailureException(f"Failed to create the task.:{e}")

def check_list_exist(d: Device, list_name: str="Test") -> bool:
    '''
    check if the list exists in the Google Task list.
    '''
    # Find all task list elements
    task_lists = d.xpath('//android.widget.HorizontalScrollView[@resource-id="com.google.android.apps.tasks:id/tabs"]\
                     /android.widget.LinearLayout/android.widget.LinearLayout').all()

    for task_list in task_lists:
        content_desc = task_list.info.get('contentDescription', "").strip()
        if content_desc == list_name:
            print(f"Found the element with text '{list_name}'")
            return True
    
    print(f"Did not find the element with text '{list_name}'")
    return False

def create_list(d: Device, list_name: str = "Test") -> None:
    """
    Creates a new task list named 'list_name' in Google Tasks.
    Assumes the function starts from the main page where the 'New list' button is visible.
    """
    try:
        # Click on "New list"
        new_list_button = d(description="New list")
        if not new_list_button.wait(timeout=5):
            raise SetupFailureException("New list button not found.")
        new_list_button.click()

        # Enter the list name
        list_title_field = d(resourceId="com.google.android.apps.tasks:id/edit_list_title")
        if not list_title_field.wait(timeout=5):
            raise SetupFailureException("List title input field not found.")
        list_title_field.set_text(list_name)

        # Click the "Done" button to save the new list
        done_button = d(resourceId="com.google.android.apps.tasks:id/done_button")
        if not done_button.wait(timeout=5):
            raise SetupFailureException("Done button not found.")
        done_button.click()

    except Exception as e:
        raise SetupFailureException(f"Failed to create the list.:{e}")

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
        if not check_list_exist(self.d):
            # If the list not exists, create the list
            create_list(self.d)
        
        # Stop the Google Tasks app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.google.android.apps.tasks")


