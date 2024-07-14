from typing import Any, Dict, Iterator
import os
from device import Device
import time
import logging
import pandas as pd

from utils.parse_action import parse_action_string, parse_action
from utils.emulator_controller import EmulatorController
from setup.tasks.TaskSetUp import TaskSetUp
from utils.transxml2vh import xml_string_to_json

class AgentEnv:
    def __init__(self, avd_name = None, emulator_controller_args=None,\
                 max_steps=30,local_output_path="captured_data",instruction_fp="docs/instructions/llamatouch_task_metadata.csv") -> None:
        
        self.device_serial = f"emulator-{emulator_controller_args['port']}"
        self.logger = logging.getLogger(self.__class__.__name__)
        self.local_output_path = local_output_path
        os.makedirs(self.local_output_path, exist_ok=True)
        self.device = Device(device_serial=self.device_serial)
        self.emulator_controller = EmulatorController(avd_name=avd_name,device_serial=self.device_serial,params=emulator_controller_args)
        
        self.instructions = pd.read_csv(instruction_fp, sep='\t')
        self.instruction_generator = self._generate_instruction()
        self.max_steps = max_steps

        self.current_action = "None|None|None"
        self.state_history = []
        self.episode_end = False
        self.current_steps = 0
    
    def _generate_instruction(self) -> Iterator[tuple[str, str]]:
        for _, row in self.instructions.iterrows():
            yield row['description'], os.path.join(self.local_output_path, str(row['episode']))

    def _setup_directories(self, base_path, subdirectories) -> list[str]:
        paths = []
        for subdir in subdirectories:
            dir_path = os.path.join(base_path, f'captured_data/{subdir}')
            os.makedirs(dir_path, exist_ok=True)
            paths.append(dir_path)
        return paths
    
    def _execute_action(self, action_type, action_para) -> bool:
        status = None
        w, h = self.device.get_screen_size()
        if action_type == "CLICK":
            status = self.device.click(action_para[0] * w, action_para[1] * h)
        elif action_type == "SWIPE":
            status = self.device.swipe(action_para[0] * w, action_para[1] * h, action_para[2] * w, action_para[3] * h)
        elif action_type == "TYPE":
            # have already processed special characters
            status = self.device.input_text(action_para)
        elif action_type == "PRESS_ENTER":
            status = self.device.enter()
        elif action_type == "PRESS_BACK":
            status = self.device.back()
        elif action_type == "PRESS_HOME":
            status = self.device.home()
        return status

    def _trans_action_format(self,action_type, action_para) -> Any:

        width, height = self.get_device_size()
        if action_type == "CLICK":
            return f"{action_type}|{str(action_para)}|NULL|{width}|{height}"
        elif action_type == "SWIPE":
            return f"{action_type}|{str(action_para[:2])}|{str(action_para[2:])}|{width}|{height}"
        elif action_type == "TYPE":
            # action_para.replace("\ ", " ")
            return f"{action_type}|{action_para}|NULL|{width}|{height}"
        elif action_type == "PRESS_BACK":
            return f"{action_type}|NULL|NULL|{width}|{height}"
        elif action_type == "PRESS_HOME":
            return f"{action_type}|NULL|NULL|{width}|{height}"
        elif action_type == "PRESS_ENTER":
            return f"{action_type}|NULL|NULL|{width}|{height}"
        elif action_type == "STATUS_TASK_COMPLETE":
            return f"{action_type}|NULL|NULL|{width}|{height}"
        elif action_type == "STATUS_TASK_IMPOSSIBLE":
            return f"{action_type}|NULL|NULL|{width}|{height}"
        else:
            raise ValueError("action_type not supported")
    
    def _backtohome(self) -> None:
        self.device.home()
    
    def set_up(self) -> None:
        self.logger.info("loading emulator...")
        self.emulator_controller.load_emulator_with_snapshot()
        time.sleep(30) # waiting for emulator to start
        self.logger.info("connecting to device...")
        self.device.connect()
        self._backtohome()
        time.sleep(2)
        self.logger.info("AgentEnv setup over!")
    
    def get_state(self) -> Dict[Any, str]:
        """
        Get the current state of the device
        """
        # save view hierarchy, screenshot, top activity name and agent action in local
        
        screenshot_dir_path, activity_dir_path, vh_dir_path, vh_json_dir_path = self._setup_directories(\
                  self.task_output_path, ['screenshot', 'activity', 'xml', 'vh'])

        self.logger.info("getting the agent env state...")
        
        view_hierarchy = self.device.get_viewhierachy()
        view_hierarchy_json = xml_string_to_json(view_hierarchy)
        activity_name = self.device.get_top_activity_name()
        screenshot = self.device.get_screenshot()
        
        tag = self.current_steps
        view_hierarchy_path = os.path.join(vh_dir_path, f"{tag}.xml")
        view_hierarchy_json_path = os.path.join(vh_json_dir_path, f"{tag}.vh")
        activity_path = os.path.join(activity_dir_path, f"{tag}.activity")
        screenshot_path = os.path.join(screenshot_dir_path, f"{tag}.png")

        with open(view_hierarchy_path, "w") as vh_file:
            vh_file.write(view_hierarchy)
        
        with open(activity_path, "w") as activity_file:
            activity_file.write(activity_name)
        
        screenshot.save(screenshot_path)

        self.logger.info(f"View hierarchy saved to: {view_hierarchy_path}")
        self.logger.info(f"Activity saved to {activity_path}")
        self.logger.info(f"Screenshot saved to: {screenshot_path}")
        
        state = {
            "screenshot": screenshot, # Pillow.Image
            "screenshot_path": screenshot_path, # str
            "view_hierarchy": view_hierarchy, # str
            "view_hierarchy_path": view_hierarchy_path, # str
            "view_hierarchy_json": view_hierarchy_json, # json
            "view_hierarchy_json_path": view_hierarchy_json_path # json
            # view_hierarchy_json example
            # [
            # {'bounds': [[0, 0], [0, 0]], 'checkable': False, 'checked': False, 'children': [1, 30, 48], 'class': None, 'clickable': False, 
            # 'content_description': None, 'editable': False, 'enabled': True, 'focusable': False, 'focused': False, 'is_password': False, 'long_clickable': False, 'package': '', 
            # 'parent': -1, 'resource_id': None, 'scrollable': False, 'selected': False, 'size': '1080*2400', 'temp_id': 0, 'text': None, 'visible': True, 'child_count': 3}, 

            # {'bounds': [[0, 0], [1080, 2400]], 'checkable': False, 'checked': False, 'children': [2], 'class': 'android.widget.FrameLayout', 'clickable': False, 'content_description': '', 
            # 'editable': False, 'enabled': True, 'focusable': False, 'focused': False, 'is_password': False, 'long_clickable': False, 'package': 'com.google.android.apps.nexuslauncher', 
            # 'parent': 0, 'resource_id': '', 'scrollable': False, 'selected': False, 'size': '1080*2400', 'temp_id': 1, 'text': '', 'visible': True, 'child_count': 1}

            # ...
            # ]
            # 
        }

        self.state_history.append(state)
        return state
    
    def get_state_history(self) -> list[dict[Any, str]]:
        self.logger.info("getting the agent env state_history...")
        return self.state_history
    
    def post_action(self, action: str) -> bool: 
        # action example
        # action_type: type, touch_point: [-1.0, -1.0], lift_point: [-1.0, -1.0], typed_text: ”best rated coffee maker”
        """Takes a step in the environment."""
        action_dict = parse_action_string(action)
        action_type, action_para = parse_action(action_dict)
        self.current_action = self._trans_action_format(action_type, action_para)
        operator_state = self._execute_action(action_type, action_para)

        # save the action
        tag = self.current_steps
        action_dir_path = self._setup_directories(self.task_output_path, ['action'])[0]
        action_path = os.path.join(action_dir_path, f"{tag}.action")
        with open(action_path, "w") as action_file:
            action_file.write(self.current_action)
        
        self.logger.info("execute action: " + self.current_action)
        self.current_steps += 1
        self.logger.info(f"current steps: {self.current_steps},action type: {action_type}")

        if self.current_steps >= self.max_steps or action_type == "STATUS_TASK_COMPLETE" or action_type == "STATUS_TASK_IMPOSSIBLE":
            self.episode_end = True
            self.logger.info("episode end")
            # record installed packages after each episode
            self.ep_installed_apps = self.device.get_installed_apps()
            ep_installed_dir = self._setup_directories(self.task_output_path, ['installed_apps'])[0]
            self.ep_installed_fp = os.path.join(ep_installed_dir, "installed_apps.txt")

            if self.ep_installed_apps:
                with open(self.ep_installed_fp, 'w') as file:
                    for item in self.ep_installed_apps:
                        file.write(f"{item}\n")
            else:
                with open(self.ep_installed_fp, 'w') as file:
                    file.write("")

        time.sleep(5)
        self.logger.info("action executed successfully")
        return operator_state
    
    def get_device_size(self) -> tuple[int, int]:
        # return width, height
        width, height = self.device.get_screen_size()
        self.logger.info(f"getting device size {width}, {height}")
        return width, height

    def get_instruction(self) -> str:
        try:
            instruction, path = next(self.instruction_generator)

            self.task_output_path = path
            return instruction
        except StopIteration:
            self.logger.warning("All instructions have been fetched.")  
            return None
  
    def reset_env(self):
        
        self.logger.info("resetting agent env...")
        self.current_action = "None|None|None"
        self.state_history = []
        self.episode_end = False
        self.current_steps = 0
        self.device.disconnect()
        time.sleep(5)
        self.emulator_controller.reload_snapshot()
        time.sleep(30)
        self.device.connect()
        time.sleep(5)
        self.logger.info("agent env reset successfully!")

    def episode_done(self) -> bool:
        return self.episode_end
    
    def tear_down(self) -> None:
        self.device.disconnect()
        time.sleep(5)
        self.emulator_controller.exit_emulator()
        self.logger.info(f"tear down the agent env...")
    
    def setup_task(self, instruction: str) -> None:
        self.logger.info(f"setting up the task: {instruction}")
        TaskSetUp(self.device.u2d, instruction)


