from typing import Any, Dict
import os
import numpy as np
from device import Device
import time
import json
from datetime import datetime
import logging
from PIL import Image
import pandas as pd

from trans_vh_to_xml import vh_to_xml
from parse_action import parse_action_string, parse_action


class AgentEnv:
    def __init__(self, device_serial=None, local_output_path=None, max_steps=30,instruction_fp="/data/jxq/all_instruction.csv") -> None:
        
        self.logger = logging.getLogger(self.__class__.__name__)
        self.local_output_path = local_output_path
        
        # 如果未按顺序先调用get_instruction再调用AgentEnv，那么task_output_path默认值
        self.task_output_path = local_output_path
        self.device = Device(device_serial=device_serial)
        self.device.connect()
        self.logger.info("AgentEnv device connected!")
        self.max_steps = max_steps

        self.instu_idx = 0
        self.current_action = "None|None|None"
        self.state_history = []
        self.episode_end = False
        self.current_steps = 0
        self.current_instruction = None
        self.instruction_ls = []
        self.ep_id_ls = []

        data = pd.read_csv(instruction_fp)
        for index, row in data.iterrows():
            self.instruction_ls.append(str(row["instruction"]))
            self.ep_id_ls.append(str(row["episode_id"]))

        self.logger.info("waiting for minicap and adb to start...")
        # 留一个minicap和adb的启动时间
        time.sleep(5)

    def get_state(self) -> Dict[Any, str]:
        """
        Get the current state of the device
        """

        # save view hierarchy, screenshot, top activity name and agent action in local

        tag = self.current_steps
        screenshot_dir_path = os.path.join(self.task_output_path, 'captured_data/screenshot')
        os.makedirs(screenshot_dir_path, exist_ok=True)
        vh_dir_path = os.path.join(self.task_output_path, 'captured_data/view_hierarchy')
        os.makedirs(vh_dir_path, exist_ok=True)
        activity_dir_path = os.path.join(self.task_output_path, 'captured_data/activity')
        os.makedirs(activity_dir_path, exist_ok=True)
        action_dir_path = os.path.join(self.task_output_path, 'captured_data/action')
        os.makedirs(action_dir_path, exist_ok=True)
        xml_dir_path = os.path.join(self.task_output_path, 'captured_data/xml')
        os.makedirs(xml_dir_path, exist_ok=True)

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
        
        # 将screenshots转换成np.array
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
    
    def _execute_action(self, action_type, action_para) -> bool:
        status = None
        w = self.device.get_width()
        h = self.device.get_height()
        if action_type == "CLICK":
            status = self.device.adb.click(action_para[0] * w, action_para[1] * h)
        elif action_type == "SWIPE":
            status = self.device.adb.swipe(action_para[0] * w, action_para[1] * h, action_para[2] * w, action_para[3] * h)
        elif action_type == "TYPE":
            # 已经处理了特殊字符
            status = self.device.adb.input_text(action_para)
        elif action_type == "PRESS_ENTER":
            status = self.device.adb.enter()
        elif action_type == "PRESS_BACK":
            status = self.device.adb.back()
        elif action_type == "PRESS_HOME":
            status = self.device.adb.home()
        return status
    
    def _trans_action_format(self, action_type, action_para) -> Any:

        width, height = self.get_device_size()
        if action_type == "CLICK":
            return f"{action_type}|{str(action_para)}|NULL|{width}|{height}"
        elif action_type == "SWIPE":
            return f"{action_type}|{str(action_para[:2])}|{str(action_para[2:])}|{width}|{height}"
        elif action_type == "TYPE":
            # # 为了能输入空格，每个空格前要加上转义字符，记录的时候换回来
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

        self.logger.info(f"current steps: {self.current_steps}")
        self.logger.info(f"action type: {action_type}")

        if self.current_steps >= self.max_steps or action_type == "STATUS_TASK_COMPLETE" or action_type == "STATUS_TASK_IMPOSSIBLE":
            self.episode_end = True
            self.logger.info("episode end")
           
            # record installed packages after each episode
            self.ep_installed_apps = list(self.device.adb.get_installed_apps().keys())
            ep_installed_dir = os.path.join(self.task_output_path, 'captured_data/installed_apps')
            os.makedirs(ep_installed_dir, exist_ok=True)
            self.ep_installed_fp = os.path.join(ep_installed_dir, "installed_apps.txt")
            if self.ep_installed_apps:
                with open(self.ep_installed_fp, 'w') as file:
                    for item in self.ep_installed_apps:
                        file.write(f"{item}\n")
            else:
                with open(self.ep_installed_fp, 'w') as file:
                    file.write("")
                                
            # uninstall droidbot after each episode
            if self.instu_idx == len(self.instruction_ls):
                self.device.disconnect()
                droidbot_package_name = "io.github.ylimit.droidbotapp"
                self.device.adb.uninstall_app(droidbot_package_name)
            
            # save the last action
            tag = self.current_steps
            action_dir_path = os.path.join(self.task_output_path, 'captured_data/action')
            os.makedirs(action_dir_path, exist_ok=True)
            action_path = os.path.join(action_dir_path, f"{tag-1}.action")
            with open(action_path, "w") as action_file:
                action_file.write(self.current_action)

        
        # wait for the action to be executed
        time.sleep(10)
        self.logger.info("action executed successfully")
        return operator_state
    
    def get_device_size(self):
        # return width, height
        self.logger.info(f"getting device size {self.device.get_width()}, {self.device.get_height()}")
        return self.device.get_width(), self.device.get_height()
    
    def get_instruction_len(self):
        # return the length of instruction list
        self.logger.info("getting instruction length")
        return len(self.instruction_ls)
    
    def get_instruction(self):
        # return index and instruction
        if self.instu_idx < len(self.instruction_ls):

            instruction = self.instruction_ls[self.instu_idx]
            self.current_instruction = instruction
            self.logger.info(f"getting instruction: {instruction}")
            # 
            self.task_output_path = os.path.join(self.local_output_path, self.ep_id_ls[self.instu_idx])
            os.makedirs(self.task_output_path, exist_ok=True)
            self.logger.info(f"getting {self.instu_idx}th instruction :{instruction}")
            self.instu_idx += 1
            return instruction
        else:
            self.logger.info("have already got all instructions")
            return None 
  
    def reset_env(self):
        self.logger.info("resetting agent env...")

        # self.instu_idx = 0
        self.current_action = "None|None|None"
        self.state_history = []
        self.episode_end = False
        self.current_steps = 0
        
        # return to home
        self.device.adb.home()
        time.sleep(1)
        self.device.adb.home()
        # self.app_packages = list(self.device.adb.get_installed_apps().keys())

        self.logger.info("agent env reset successfully!")

    def episode_done(self) -> bool:
        return self.episode_end
    
            
if __name__ == "__main__":
    print("hello world")



