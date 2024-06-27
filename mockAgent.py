import logging

class MockAgent:
    def __init__(self):
       self.index = 0
       self.logger = logging.getLogger(self.__class__.__name__) 
       # The action string returned by the Agent must be in the AitW format; 
       # for reference, see docs/AITW_ACTION_FORMAT.md
       self.actions = [
                "action_type: DUAL_POINT, touch_point: [0.1, 0.9], lift_point: [0.1, 0.9], typed_text:",
                "action_type: TYPE, touch_point: [-1.0, -1.0], lift_point: [-1.0, -1.0], typed_text: best rated coffee maker",
                "action_type: DUAL_POINT, touch_point: [0.2, 0.5], lift_point: [0.3, 0.6], typed_text:",
                "action_type: STATUS_TASK_COMPLETE, touch_point: [-1.0, -1.0], lift_point: [-1.0,-1.0], typed_text:",
                
                "action_type: DUAL_POINT, touch_point: [0.1, 0.1], lift_point: [0.1, 0.1], typed_text:",
                "action_type: TYPE, touch_point: [-1.0, -1.0], lift_point: [-1.0, -1.0], typed_text: best rated coffee maker",
                "action_type: DUAL_POINT, touch_point: [0.2, 0.5], lift_point: [0.3, 0.6], typed_text:",
                "action_type: STATUS_TASK_IMPOSSIBLE, touch_point: [-1.0, -1.0], lift_point: [-1.0,-1.0], typed_text:",
                ]
        
    def get_action(self, state):
        screenshot = state["screenshot"] 
        view_hierarchy = state["view_hierarchy"]
        # infer use screenshot and view_hierarchy
        index = self.index
        self.logger.info(f"getting {index}th index action {self.actions[index]}")
        self.index = self.index + 1
        return self.actions[index]