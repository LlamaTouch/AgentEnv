from setup.tasks.Settings import *
from setup.tasks.Clock import *
from setup.tasks.GoogleTask import *
from setup.tasks.GoogleDrive import *
from setup.tasks.Quora import *
from setup.tasks.Zoom import *
from setup.tasks.Trello import *
from setup.tasks.Coursera import *
from setup.tasks.Discord import *
from setup.tasks.Pinterest import * 

_TaskSetUpMap = {
    # settings
    'turn notification dots off' : SettingsTask01,
    'turn off wifi' : SettingsTask02,
    'Set the phone to "Do not disturb".' : SettingsTask03,
    'turn on improve location accuracy' : SettingsTask04,
    'turn on bluetooth scan' : SettingsTask05,
    'turn on airplane mode' : SettingsTask06,
    'toggle show notifications on the lock screen' : SettingsTask07,
    'turn off improve location accuracy' : SettingsTask08,
    # clock
    'turn on the 12-hour format for clock' : ClockTask01,
    # Google Task
    'Open Google Tasks and star "Task2".' : GoogleTask01,
    'Open Google Tasks and mark "Task2" as complete.' : GoogleTask02,
    'Open Google Tasks and delete the list "Test".' : GoogleTask03,
    # Google Drive
    'Upload the latest photo from my device to a new folder named "Selfie2024" on Google Drive app.' : GoogleDriveTask01,
    'Share the "Testbed" spreadsheet on Google Drive by copy link, make sure anyone with the link can view.' : GoogleDriveTask02,
    # Quora
    'In page "Following", check latest posts and click the first one on the Quora app.' : QuoraTask01,
    'Upvote all contents I\'ve bookmarked on the Quora app.' : QuoraTask02,
    'Check the log of latest answer I\'ve bookmarked on Quora app.' : QuoraTask03,
    # Zoom
    'On Zoom, start my scheduled meeting \'regular meeting\' right now.' : ZoomTask01,
    'On Zoom, delete my scheduled meeting \'regular meeting\'.' : ZoomTask02,
    'On Zoom, edit my scheduled meeting \'Weekly group meeting\', set \'Repeat\' to \'Every week\'.' : ZoomTask03,
    'On Zoom, edit my scheduled meeting \'Weekly group meeting\', turn \'Enable waiting room\' on.' : ZoomTask04,
    'On Zoom, turn to page \'Team chat\', bookmark my latest message to myself.' : ZoomTask05,
    'On Zoom, turn to page \'Team chat\', set a reminder for my latest message to myself in 1 hour.' : ZoomTask06,
    # Trello
    'Open the Trello app and add a new list titled "To Do" to the "School" board.' : TrelloTask01,
    'Open the Trello app, add a new card titled "Task 1" to the "To Do" list in the "School" board.' : TrelloTask02,
    'Open the Trello app and archive a list named "To Do" in the "School" board.' : TrelloTask03,
    'Open the Trello app and set a due date for a card in the "School" board.': TrelloTask04,
    # Coursera
    'Download the first video lecture for the \'Algorithms, Part I\' course to watch offline on the Coursera app.' : CourseraTask01,
    'Visit the forums for the \'Algorithms, Part I\' course and go to discussion for Week 1 on Coursera.' : CourseraTask02,
    # Discord
    'Send text \'Hello World\' in text channel \'general\' of agentian\'s server on Discord app.' : DiscordTask01,
    'Create a new private text channel \'Testbed\' in agentian\'s server on Discord app.' : DiscordTask02,
    'Delete voice channel Lobby in agentian\'s server on Discord app.' : DiscordTask03,
    'Upload my latest picture as server icon of agentian\'s server on Discord app.' : DiscordTask04,
    'Join the voice channel \'Gaming\' in agentian\'s server on Discord app.': DiscordTask05,
    'Turn to sever \'homework\' and turn on \'Allow Direct Messages\' on Discord app.': DiscordTask06,
    'Go to Settings of server \'Agent Env\' on Discord app.': DiscordTask07,
    # Pinterest
    'Open Pinterest and open one of your own board.': PinterestTask01,
    'Open Pinterest and search "DIY" in your own board list and open it.': PinterestTask02,


}

def TaskSetUp(device, instruction):
    d = device
    taskSetup= _TaskSetUpMap.get(instruction)

    if taskSetup:
        task = taskSetup(d, instruction)
        task.setup()
    else:
        print(f"Task: {instruction} don`t need to setup.")
        


if __name__ == "__main__":
    TaskSetUp("emulator-5554", "turn notification dots off")