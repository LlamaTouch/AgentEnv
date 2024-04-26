import numpy as np
from typing import Dict
import logging
from typing import Any, Dict

# Adapted from AITW
_SWIPE_DISTANCE_THRESHOLD = 0.04
def is_tap_action(normalized_start_yx, normalized_end_yx):

    distance = np.linalg.norm(
    np.array(normalized_start_yx) - np.array(normalized_end_yx))
    return distance <= _SWIPE_DISTANCE_THRESHOLD


# Splitting the action string into key-value pairs
def parse_action_string(action_str):

    logging.info(f"parsing action string: {action_str}")

    action_str = action_str.lower()
    action_dict = {}
    elements = action_str.split(", ")

    # Buffer for accumulating parts of a split list
    temp = ""

    for element in elements:
        # Check if the element is part of a split list
        if temp:
            temp += ", " + element
            if element.endswith(']'):
                # If the end of the list is found, process the whole item
                key, value = temp.split(": ", 1)
                action_dict[key] = eval(value)  # Convert string list to actual list
                temp = ""  # Reset the buffer
        elif element.count('[') != element.count(']'):
            # If the list is split, start accumulating
            temp = element
        else:
            # Process a normal item
            key, value = element.split(":", 1)
            # 去除空格
            key = key.strip()
            value = value.strip()
            if value.startswith('[') and value.endswith(']'):
                value = eval(value)  # Convert string list to actual list
            action_dict[key] = value

    return action_dict

def parse_action(action: Dict[str,str]):
    # action_type: type or dual_point or status_task_complete or back or home...
    # action_type: type, touch_point: [-1.0, -1.0], lift_point: [-1.0, -1.0], typed_text: "best rated coffee maker"
    action_type = action["action_type"]
    action_type = action_type.upper()

    if action_type == "TYPE":
        # # 每个空格前要加上转义字符
        # action_para = action["typed_text"].replace(" ", "\ ")
        action_para = action["typed_text"]
    elif action_type == "DUAL_POINT":
        if is_tap_action(action["touch_point"], action["lift_point"]):
            action_type = "CLICK"
            action_para = action["touch_point"]
        else:
            action_type = "SWIPE"
            point1 = action["touch_point"]
            point2 = action["lift_point"]
            action_para = point1 + point2
    elif action_type == "STATUS_TASK_COMPLETE":
        action_para = None
    elif action_type == "STATUS_TASK_IMPOSSIBLE":
        action_para = None
    elif action_type == "PRESS_BACK":
        action_para = None
    elif action_type == "PRESS_HOME":
        action_para = None
    elif action_type == "PRESS_ENTER":
        action_para = None
    else:
        raise ValueError("action_type not supported")
    return action_type, action_para



