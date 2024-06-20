# AitW ACTION FORMAT

In this document, we will explain the format of the actions that the agent can take in the environment. In AgentEnv, we adopt the action space definition from [AitW](https://arxiv.org/abs/2307.10088). If you are using AgentEnv, you need to ensure that your agent passes the action string in the following format to AgentEnv:

## action string format
```
"action_type: <action_type>, touch_point: [<point_x>, <point_y>], lift_point: [<point_x>, <point_y>], typed_text: <typed_text>"
```

### 1.Keywords
The keywords are `action_type`, `touch_point`, `lift_point`, and `typed_text`. For detailed explanations of these four keywords, please refer to the original document [here](https://github.com/google-research/google-research/tree/master/android_in_the_wild#action-space).

### 2.Parameters
The parameters are `<action_type>`, `<point_x>`, `<point_y>`, and `<typed_text>`:

- `<action_type>` is a string that represents the type of the current action. It can be one of the following:
  
  | action_type          |
  |----------------------|
  | TYPE                 |
  | DUAL_POINT           |
  | PRESS_BACK           |
  | PRESS_HOME           |
  | PRESS_ENTER          |
  | STATUS_TASK_COMPLETE |
  | STATUS_TASK_COMPLETE |

- `<point_x>` and `<point_y>` are decimal numbers between 0 and 1 that represent the percentage coordinates for the corresponding position in a DUAL_POINT action.

- `<typed_text>` is a string that represents the text to be inputted for the TYPE action.

