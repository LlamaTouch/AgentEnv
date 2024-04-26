from typing import Any, Dict
import os
import numpy as np
from device import Device
import time
import json
import logging
from PIL import Image
import pandas as pd

from utils.trans_vh_to_xml import vh_to_xml
from utils.parse_action import parse_action_string, parse_action
from utils.emulator_controller import EmulatorController

class AgentEnv:
    def __init__(self, avd_name = None, emulator_controller_args=None,\
                 adb_clt_path="adb",max_steps=30,local_output_path="captured_data",instruction_fp="docs/instructions/llamatouch_task_metadata.csv") -> None:
        
        self.adb_clt_path = adb_clt_path
        self.device_serial = f"emulator-{emulator_controller_args['port']}"
        self.logger = logging.getLogger(self.__class__.__name__)
        self.local_output_path = local_output_path
        self.device = Device(device_serial=self.device_serial,adb_clt_path=self.adb_clt_path)
        self.emulator_controller = EmulatorController(avd_name=avd_name,device_serial=self.device_serial,params=emulator_controller_args)
        
        self.instructions = pd.read_csv(instruction_fp)
        self.instruction_generator = self._generate_instruction()
        self.max_steps = max_steps

        self.current_action = "None|None|None"
        self.state_history = []
        self.episode_end = False
        self.current_steps = 0
    
    def _activate_droidbot(self):
        # swipe slightly to activiate droidbot
        width = self.device.get_width()
        height = self.device.get_height()
        x0,y0,x1,y1 = 0.5,0.5,0.4,0.5
        self.device.adb.swipe(x0 * width, y0 * height, x1 * width, y1 * height)

    def _generate_instruction(self):
        for _, row in self.instructions.iterrows():
            yield row['description'], os.path.join(self.local_output_path, str(row['episode']))

    def _setup_directories(self, base_path, subdirectories):
        paths = []
        for subdir in subdirectories:
            dir_path = os.path.join(base_path, f'captured_data/{subdir}')
            os.makedirs(dir_path, exist_ok=True)
            paths.append(dir_path)
        return paths
    
    def _execute_action(self, action_type, action_para) -> bool:
        status = None
        w = self.device.get_width()
        h = self.device.get_height()
        if action_type == "CLICK":
            status = self.device.adb.click(action_para[0] * w, action_para[1] * h)
        elif action_type == "SWIPE":
            status = self.device.adb.swipe(action_para[0] * w, action_para[1] * h, action_para[2] * w, action_para[3] * h)
        elif action_type == "TYPE":
            # have already processed special characters
            status = self.device.adb.input_text(action_para)
        elif action_type == "PRESS_ENTER":
            status = self.device.adb.enter()
        elif action_type == "PRESS_BACK":
            status = self.device.adb.back()
        elif action_type == "PRESS_HOME":
            status = self.device.adb.home()
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
    
    def set_up(self) -> None:
        self.logger.info("loading emulator...")
        self.emulator_controller.load_emulator_with_snapshot()
        time.sleep(100) # waiting for emulator to start
        self.logger.info("connecting to device...")
        self.device.connect()
        time.sleep(5)
        # activate droidbot
        self._activate_droidbot()
        self.logger.info("AgentEnv setup over!")

    def get_state(self) -> Dict[Any, str]:
        """
        Get the current state of the device
        """
        # save view hierarchy, screenshot, top activity name and agent action in local
        tag = self.current_steps
        screenshot_dir_path, vh_dir_path, activity_dir_path,\
              action_dir_path, xml_dir_path = self._setup_directories(\
                  self.task_output_path, ['screenshot', 'view_hierarchy', 'activity', 'action', 'xml'])

        self.logger.info("getting the agent env state...")

        view_hierarchy = self.device.get_views()
        top_activity_name = self.device.get_top_activity_name()
        xml = vh_to_xml(view_hierarchy)

        xml_path = os.path.join(xml_dir_path, f"{tag}.xml")
        with open(xml_path, "w") as xml_file:
            xml_file.write(xml)

        vh_path = os.path.join(vh_dir_path, f"{tag}.json")
        with open(vh_path, "w") as vh_file:
            json.dump(view_hierarchy, vh_file)
        
        activity_path = os.path.join(activity_dir_path, f"{tag}.activity")
        with open(activity_path, "w") as activity_file:
            activity_file.write(top_activity_name)
        
        action_path = os.path.join(action_dir_path, f"{tag-1}.action")
        with open(action_path, "w") as action_file:
            action_file.write(self.current_action)

        screenshot_path = self.device.take_screenshot(os.path.join(screenshot_dir_path, f"{tag}.png"))

        self.logger.info(f"Screenshot saved to: {screenshot_path}")
        self.logger.info(f"View hierarchy saved to: {vh_path}")
        self.logger.info(f"Activity saved to {activity_path}")
        self.logger.info(f"Action saved to {action_path}")
        
        # tranform screenshots into np.array type
        screenshot = Image.open(screenshot_path)
        screenshot = np.array(screenshot)


        state = {
            "view_hierarchy": view_hierarchy, # str
            "view_hierarchy_path": vh_path, # str
            "screenshot": screenshot, # np.array
            "screenshot_path": screenshot_path, # str
            "xml_path": xml_path, # str
            "xml": xml, # str
            # "top_activity_name": top_activity_name,
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
        
        self.logger.info("execute action: " + self.current_action)
        self.current_steps += 1

        self.logger.info(f"current steps: {self.current_steps},action type: {action_type}")

        if self.current_steps >= self.max_steps or action_type == "STATUS_TASK_COMPLETE" or action_type == "STATUS_TASK_IMPOSSIBLE":
            self.episode_end = True
            self.logger.info("episode end")
           
            # record installed packages after each episode
            self.ep_installed_apps = list(self.device.adb.get_installed_apps().keys())
            ep_installed_dir = self._setup_directories(self.task_output_path, ['installed_apps'])[0]
            self.ep_installed_fp = os.path.join(ep_installed_dir, "installed_apps.txt")

            if self.ep_installed_apps:
                with open(self.ep_installed_fp, 'w') as file:
                    for item in self.ep_installed_apps:
                        file.write(f"{item}\n")
            else:
                with open(self.ep_installed_fp, 'w') as file:
                    file.write("")
            # save the last action
            tag = self.current_steps
            action_dir_path = self._setup_directories(self.task_output_path, ['action'])[0]
            action_path = os.path.join(action_dir_path, f"{tag-1}.action")
            with open(action_path, "w") as action_file:
                action_file.write(self.current_action)

        time.sleep(5)
        self.logger.info("action executed successfully")
        return operator_state
    
    def get_device_size(self):
        # return width, height
        self.logger.info(f"getting device size {self.device.get_width()}, {self.device.get_height()}")
        return self.device.get_width(), self.device.get_height()

    def get_instruction(self):
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
        time.sleep(50)
        self.device.connect()
        time.sleep(5)
        self._activate_droidbot()
        self.logger.info("agent env reset successfully!")

    def episode_done(self) -> bool:
        return self.episode_end
    
    def tear_down(self) -> None:
        self.device.disconnect()
        time.sleep(5)
        self.emulator_controller.exit_emulator()
        self.logger.info(f"tear down the agent env...")




