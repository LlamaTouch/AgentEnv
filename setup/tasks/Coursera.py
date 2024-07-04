from setup.tasks.BaseTaskSetup import BaseTaskSetup,SetupFailureException
from uiautomator2 import Device
import time

def enroll_course(d: Device, course_name: str = "Algorithms, Part I"):
    """
    Start from the default 'Learn' page of the Coursera app.
    Func: Searches for a course named 'course_name' and proceeds through the enrollment process.
    Raises an exception if any of the UI elements required for the process are not found.
    """
    try:
        # Click the "Search" button
        search_button = d(description="Search")
        if not search_button.exists(timeout=5):
            raise SetupFailureException("Search button not found.")
        search_button.click()

        # Click and type in the search input field
        search_input = d(className="android.widget.EditText")
        if not search_input.exists(timeout=5):
            raise SetupFailureException("Search input field not found.")
        search_input.click()
        search_input.set_text(course_name)
        d.press("enter")

        # wait for search results to load
        time.sleep(5)

        # Click the first course in the search results
        first_course = d(className="android.view.View", instance=6)
        if not first_course.exists(timeout=5):
            raise SetupFailureException("First course in search results not found.")
        first_course.click()

        # Navigate through the enrollment options
        see_options = d(text="See enrollment options")
        if not see_options.exists(timeout=5):
            raise SetupFailureException("Enrollment options button not found.")
        see_options.click()

        enroll_button = d(className="android.widget.Button", instance=0)
        if not enroll_button.exists(timeout=5):
            raise SetupFailureException("Enroll button not found.")
        enroll_button.click()
        
        # this process be required only for the first course enrollment
        try:
            # Check terms and conditions
            terms_checkbox = d(className="android.widget.CheckBox", instance=3)
            if terms_checkbox.exists(timeout=5):
                terms_checkbox.click()

            # Commit to goals
            commit_button = d(text="I Commit to My Goals")
            if commit_button.exists(timeout=5):
                commit_button.click()

        except Exception as e:
            print(f"not first course enrollment: {e}")
        
    except SetupFailureException as e:
        print(f"An error occurred during the enrollment process: {e}")
        raise SetupFailureException("Unable to enroll in the course.")
    
def check_course_enrolled(d: Device, course_name: str ="Algorithms, Part I") -> bool:
    '''
    start from the default page of Coursera app: learn page
    '''
    # Click the "Learn" button
    d(description="Learn").click()
    course = d(text=course_name)
    if course.exists(timeout=5):
        return True
    
    return False

class CourseraTask01(BaseTaskSetup):
    '''
    instruction: Download the first video lecture for the 'Algorithms, Part I' course to watch offline on the Coursera app.
    setup: make enrollment to the course 'Algorithms, Part I' on Coursera app.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("org.coursera.android", use_monkey=True)
        time.sleep(2)

        # make enrollment to the course 'Algorithms, Part I'
        if not check_course_enrolled(self.d,"Algorithms, Part I"):
            enroll_course(self.d,"Algorithms, Part I")
            
        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("org.coursera.android")

class CourseraTask02(BaseTaskSetup):
    '''
    instruction: Visit the forums for the 'Algorithms, Part I' course and go to discussion for Week 1 on Coursera.
    setup: make enrollment to the course 'Algorithms, Part I' on Coursera app.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("org.coursera.android", use_monkey=True)
        time.sleep(2)

        # make enrollment to the course 'Algorithms, Part I'
        if not check_course_enrolled(self.d,"Algorithms, Part I"):
            enroll_course(self.d,"Algorithms, Part I")
            
        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("org.coursera.android")