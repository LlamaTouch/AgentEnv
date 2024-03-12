from environment import AgentEnv
from random_agent import RandomAgent
import logging
import time

# AgentEnv init params
device_serial = "10.29.212.189:5555"
local_output_path = "/data/jxq/mobile-agent/AgentEnv/captured_data"
instruction_file_path = "docs/instructions/general/all_instruction.csv"
max_steps = 30 # agent max steps for each instruction

# agent_env instance
agent_env =  AgentEnv(device_serial=device_serial, local_output_path=local_output_path, max_steps=max_steps,instruction_fp=instruction_file_path)
agent = RandomAgent()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler(f'{local_output_path}/log/{time.time()}_out.log', 'a'),
                            logging.StreamHandler()])


instruction_length = agent_env.get_instruction_len()
for i in range(instruction_length):
    instruction = agent_env.get_instruction()
    while not agent_env.episode_done():
        # get current state in the envrionment
        state = agent_env.get_state()
        # agent predict action
        action  = agent.get_action(state)
        # push action to agent_env, agent_env execute the action
        status = agent_env.post_action(action=action)
        # get state history
        state_history = agent_env.get_state_history()
        # get action history
        device_size = agent_env.get_device_size()
    # reset the environment
    agent_env.reset_env()








