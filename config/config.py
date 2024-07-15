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
        
        EMULATOR_CONTROLLER_AGRS (dict): A dictionary of arguments used to configure the emulator
            controller. These settings include:
            - "snapshot": The name of the emulator snapshot to use for testing, allowing for quick
              resets to a known state.
            - "port": Port number to use for adb connecting to the emulator.
            - "no-window": A boolean string ('true' or 'false') indicating whether the emulator should
              run without opening a GUI window. Useful for running tests in a headless environment.
    """
    LOCAL_OUTPUT_PATH = "captured_data"
    # INSTRUCTION_FILE_PATH = "docs/instructions/llamatouch_task_metadata.csv"
    INSTRUCTION_FILE_PATH = "docs/instructions/setup_test.tsv"
    AVD_NAME = "pixel_6a_api31"
    MAX_STEPS = 30
    EMULATOR_CONTROLLER_AGRS = {
        "snapshot" : "default_boot",
        "port" : "5554",
        "no-window" : "true",  # Change this to "true" to run the emulator without GUI.
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
