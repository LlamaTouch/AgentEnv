import time
from uiautomator2 import Device
from setup.tasks.BaseTaskSetup import BaseTaskSetup,SetupFailureException


def is_nba_in_favourite(d: Device):
    """
    start from the More page
    func: check if NBA is in my favourite team
    """

    favourite = d(text="Favorites")
    if not favourite.wait(timeout=5):
        return False
     
    sports = []
    list_views = d.xpath('//androidx.recyclerview.widget.RecyclerView[@resource-id="com.espn.score_center:id/sports_list"]/android.view.ViewGroup/android.widget.TextView')
    if not list_views.wait(timeout=5):
        raise SetupFailureException("List views not found")
    
    list_view = list_views.all()
    for view in list_view:
        sport = view.info.get("contentDescription").strip()
        if sport == "NBA":
            nba_id = len(sports)
        if sport == "ALL SPORTS":
            all_sports_id = len(sports)
        sports.append(sport)
    
    # if nba is in favorite
    if nba_id < all_sports_id:
        return True
    
    return False
    
def add_nba_to_favourite(d: Device):
    """
    start from the More page
    func: add NBA to my favourite team and back to the More page
    """
    try:
        # Click on 'NBA'
        nba_button = d(text="NBA")
        if not nba_button.wait(timeout=5):
            raise SetupFailureException("NBA button not found")
        nba_button.click()

        # Click on favorite button
        favorite_button = d(resourceId="button.favorite")
        if not favorite_button.wait(timeout=5):
            raise SetupFailureException("Favorite button not found")
        favorite_button.click()

        # Click back button
        back_button = d(description="back.button")
        if not back_button.wait(timeout=5):
            raise SetupFailureException("Back button not found")
        back_button.click()

        time.sleep(2)
        # swipe to the top
        d(scrollable=True).scroll.vert.toBeginning()

    except Exception as e:
        raise SetupFailureException(f"An error occurred when add NBA to my favourite team.: {e}")


def is_lakers_in_my_nba(d: Device):
    """
    start from more page
    Check if the Lakers are already added to my favorite NBA teams.
    """

    favourite_team_names = d.xpath('//android.widget.TextView[@resource-id="com.espn.score_center:id/team_name')

    if not favourite_team_names.wait(timeout=5):
        return False
    
    team_names = []
    for team_name in favourite_team_names.all():
        team_names.append(team_name.info.get("text").strip())
    
    if "LAL" in team_names: 
        return True
    
    return False



def add_lakers_to_my_nba(d: Device):
    """
    start from the More page
    Add the Lakers to my favorite NBA teams
    """
    try:    
        # Click on edit button
        edit_button = d(resourceId="com.espn.score_center:id/xEditButton")
        if not edit_button.wait(timeout=5):
            raise SetupFailureException("Edit button not found")
        edit_button.click()

        # Click on 'ADD TEAMS'
        add_teams_button = d(text="ADD TEAMS")
        if not add_teams_button.wait(timeout=5):
            raise SetupFailureException("ADD TEAMS button not found")
        add_teams_button.click()

        # Click on the first instance of 'NBA'
        first_nba_button = d.xpath('//android.widget.TextView[@resource-id="com.espn.score_center:id/league_name" and @text="NBA"]')
        if not first_nba_button.wait(timeout=5):
            raise SetupFailureException("NBA button not found")
        first_nba_button.click()

        # Click on 'Lakers' team
        lakers_button = d(description="Lakers")
        if not lakers_button.wait(timeout=5):
            raise SetupFailureException("Lakers button not found")
        lakers_button.click()

        # Click 'Finish and Close'
        finish_and_close_button = d(description="Finish and Close")
        if not finish_and_close_button.wait(timeout=5):
            raise SetupFailureException("Finish and Close button not found")
        finish_and_close_button.click()
    
    except Exception as e:
        raise SetupFailureException(f"An error occurred when add Lakers to my favourite NBA team.: {e}")
    
def add_Lakers_to_favourite(d: Device):
    """
    start from the Home page
    func: First, navigate to the 'more' interface. Check if 'favorite' contains the Lakers, and if not, add the Lakers to 'favorite'.
    """
    try:
        # Click on 'More'
        more_button = d(text="More")
        if not more_button.wait(timeout=5):
            raise SetupFailureException("More button not found")
        more_button.click()

        if not is_nba_in_favourite(d):
            add_nba_to_favourite(d)

        if not is_lakers_in_my_nba(d):
            add_lakers_to_my_nba(d)

    except Exception as e:
        raise SetupFailureException(f"An error occurred when add Lakers to my favourite team.: {e}")

class ESPNTask01(BaseTaskSetup):
    '''
    instruction: Open ESPN, remove nba Lakers from your favourite team.
    setup: make sure Lakers is in your favourite team.
    '''
    def __init__(self, device, instruction):
        super().__init__(device, instruction)
    
    def setup(self):
        # start app
        self.d.app_start("com.dd.doordash", use_monkey=True)
        time.sleep(10)
	    
        # add Lakers to favourite
        add_Lakers_to_favourite(self.d)

        # stop app
        self.d.press("home")
        time.sleep(2)
        self.d.app_stop("com.dd.doordash")