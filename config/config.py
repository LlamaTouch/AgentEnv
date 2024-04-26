
class AgentEnvConfig:
    
    """
    Configuration settings for the Agent Environment that defines parameters
    for the Android Virtual Device (AVD) testing environment and associated tasks.
    
    Attributes:
        LOCAL_OUTPUT_PATH (str): Directory path where captured data from the emulator will be stored.
        
        INSTRUCTION_FILE_PATH (str): The file path to a CSV file containing tasks or instructions
            that the agent should execute. This file is expected to list tasks in a structured format,
            which the testing environment utilizes to guide the agent's actions.
        
        AVD_NAME (str): The name identifier for the Android Virtual Device (AVD) used in testing.
            This should match the name of an AVD configured in the Android emulator to ensure proper connection.

        MAX_STEPS (int): The maximum number of steps (actions) that the agent is allowed to take
            for each instruction set in the task file. This limit helps to prevent infinite loops
            and manage test duration.
        
        ADB_CLIENT_BIN_PATH (str): The path to the adb executable. ADB is used for interfacing
            with the Android operating system running on the emulator. This path should be set
            to where adb is installed on the host machine. If you want to use default adb, the parameter is
            set "adb"
        
        EMULATOR_CONTROLLER_AGRS (dict): A dictionary of arguments used to configure the emulator
            controller. These settings include:
            - "snapshot": The name of the emulator snapshot to use for testing, allowing for quick
              resets to a known state.
            - "port": Port number to use for adb connecting to the emulator.
            - "no-window": A boolean string ('true' or 'false') indicating whether the emulator should
              run without opening a GUI window. Useful for running tests in a headless environment.
    """
    LOCAL_OUTPUT_PATH = "captured_data"
    INSTRUCTION_FILE_PATH = "docs/instructions/llamatouch_task_metadata.csv"
    AVD_NAME = "pixel_6a31"
    MAX_STEPS = 30
    ADB_CLIENT_BIN_PATH = "adb"
    EMULATOR_CONTROLLER_AGRS = {
        "snapshot" : "default_boot",
        "port" : "5554",
        "no-window" : "true",  # Change this to "false" to run the emulator without a GUI.
    }

class LogConfig:
    """
    Configuration settings for logging.
    
    Attributes:
        LOGGING_LEVEL (str): Defines the minimum level of events to log; options include DEBUG, INFO, WARNING, ERROR, CRITICAL.
        LOGGING_FORMAT (str): Template string defining the format of log messages.
        LOGGING_DATE_FORMAT (str): Template string defining the format of dates in log messages.
        LOG_FILE_PATH (str): Directory path where log files will be stored.
    """
    LOGGING_LEVEL = "DEBUG"
    LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    LOG_FILE_PATH = "log/"
