import logging
import time
from environment import AgentEnv
from mockAgent import MockAgent
from config.config import AgentEnvConfig, LogConfig 

# Setup logging using configuration settings
log_file_name = f"{LogConfig.LOG_FILE_PATH}/{time.time()}_out.log"
logging.basicConfig(level=getattr(logging, LogConfig.LOGGING_LEVEL),
                    format=LogConfig.LOGGING_FORMAT,
                    datefmt=LogConfig.LOGGING_DATE_FORMAT,
                    handlers=[logging.FileHandler(log_file_name, 'a'),
                              logging.StreamHandler()])

# Initialize the Agent environment with configuration settings
agent_env = AgentEnv(
    avd_name=AgentEnvConfig.AVD_NAME,
    emulator_controller_args=AgentEnvConfig.EMULATOR_CONTROLLER_AGRS,
    adb_clt_path=AgentEnvConfig.ADB_CLIENT_BIN_PATH,
    max_steps=AgentEnvConfig.MAX_STEPS,
    local_output_path=AgentEnvConfig.LOCAL_OUTPUT_PATH,
    instruction_fp=AgentEnvConfig.INSTRUCTION_FILE_PATH,
)
agent_env.set_up()
agent = MockAgent()

# Main loop
while True:
    '''
    In this loop,you can get all interface that AgentEnv provice for agent to interact with.    
    '''
    instruction = agent_env.get_instruction()
    if instruction is None:
        break
    logging.info(f"Current instruction: {instruction}")
    agent_env.setup_task(instruction)
    
    while not agent_env.episode_done():
        state = agent_env.get_state()
        action = agent.get_action(state)
        status = agent_env.post_action(action=action)
        state_history = agent_env.get_state_history()
        device_size = agent_env.get_device_size()
    agent_env.get_state() # get the final state
    agent_env.reset_env()

agent_env.tear_down()
