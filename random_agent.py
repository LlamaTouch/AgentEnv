import random
import time
import logging

class RandomAgent:
    def __init__(self):
       self.index = 0
       self.logger = logging.getLogger(self.__class__.__name__) 
    #    self.actions = [
    #             "action_type: dual_point, touch_point: [0.1, 0.9], lift_point: [0.1, 0.9], typed_text:",
    #             "action_type: dual_point, touch_point: [0.2, 0.5], lift_point: [0.3, 0.6], typed_text:",
    #             "action_type: STATUS_TASK_COMPLETE, touch_point: [-1.0, -1.0], lift_point: [-1.0,-1.0], typed_text:",
    #             "action_type: dual_point, touch_point: [0.1, 0.1], lift_point: [0.1, 0.1], typed_text:",
    #             "action_type: type, touch_point: [-1.0, -1.0], lift_point: [-1.0, -1.0], typed_text: best rated coffee maker",
    #             "action_type: dual_point, touch_point: [0.2, 0.5], lift_point: [0.3, 0.6], typed_text:",
    #             "action_type: STATUS_TASK_COMPLETE, touch_point: [-1.0, -1.0], lift_point: [-1.0,-1.0], typed_text:",
    #             ]
       self.actions = [
                "action_type: type, touch_point: [0.8, 0.5], lift_point: [0.2, 0.5], typed_text: ",
                "action_type: STATUS_TASK_COMPLETE, touch_point: [-1.0, -1.0], lift_point: [-1.0,-1.0], typed_text:",
                "action_type: dual_point, touch_point: [0.5, 0.2], lift_point: [0.5, 0.8], typed_text: ",
                "action_type: STATUS_TASK_COMPLETE, touch_point: [-1.0, -1.0], lift_point: [-1.0,-1.0], typed_text:",
                ]
        

    # return action according to the screenshot
    def get_action(self, screenshot):
        # random agent
        # action example
        # action_type: type, touch_point: [-1.0, -1.0], lift_point: [-1.0, -1.0], typed_text: ”best rated coffee maker”
        # time.sleep(5)
        index = self.index
        self.logger.info(f"getting {index}th index action {self.actions[index]}")
        self.index = self.index + 1
        return self.actions[index]