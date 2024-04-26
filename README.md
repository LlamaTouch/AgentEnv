# AgentEnv

This repository contains part of the source code for the [DroidBot project](https://github.com/honeynet/droidbot) and is designed to provide an environment for an agent model to communicate with an Android device or emulator. AgentEnv serves as a bridge between the agent model and the Android device or emulator. It interprets the agent's output actions (in AITW format) and maps them to corresponding actions on the Android device or emulator. Additionally, AgentEnv returns the state of the Android device or emulator to the agent model, including screenshots, XML, and view hierarchy, and records  the agent's actions and the state of environment.

# Dependencies
## Python
- Python 3.9
- `pip install -r requirements.txt`

## Emulator Installation
Follow [Android Emulator Installation Guide](docs/emulator_guide.md) to prepare the Android Emulator.If you want to use AgentEnv for Llamatouch,you should create AVD with API-level=31 and device=pixel_6a.

## Emvironmnet Setup for LlamaTouch
1. Prepare a **new** Google account and sign in it on google play first.
2. Install and login apps:
    - Install
        - for our dataset involved Apps intallation: `python setup/intall_apps.py`
    - Login
        - use script login part of Apps: `python setup/login_apps.py`.This login script is designed to sign in to apps that only require Google account for authentication.
        - manually login other Apps: For apps that require manual login, please refer to this [table](setup/login/app_login.csv).

# Run AgentEnv

## Configuration
Before using AgentEnv, ensure you customize the [config.py file](config/config.py) with the settings specific to your previously configured Android Virtual Device (AVD) and Android Debug Bridge (ADB).

## Integrate your Agent model with AgentEnv
The `Agent2AgentEnv.py` script serves as a detailed example of how to use AgentEnv under your own Agent model. It demonstrates all the interfaces provided by AgentEnv, showcasing how to interact with these APIs to facilitate communication between your Agent model and an Android device or emulator.

