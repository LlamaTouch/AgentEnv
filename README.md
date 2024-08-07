# AgentEnv

This repository is designed to provide an environment for an agent model to communicate with an Android device or emulator. AgentEnv serves as a bridge between the agent model and the Android device or emulator. It interprets the agent's output actions (in [AITW format](docs/AITW_ACTION_FORMAT.md)) and maps them to corresponding actions on the Android device or emulator. Additionally, AgentEnv returns the state of the Android device or emulator to the agent model, including screenshots, view hierarchy and so on.The process of communication between the agent model and the Android device or emulator is recorded by the AgentEnv.

# Dependencies
## Emulator Preparation
1. download the android emulator package from this [OneDrive Link](https://bupteducn-my.sharepoint.com/:u:/g/personal/jxq_bupt_edu_cn/EZxapI07mqNMvy68qFEe-n4BuVhJ75fz9racU94ixW4oog?e=5Jc1Wv).
2. Follow [Android Emulator Transfer Guide](docs/Emulator_transfer.md) to properly load the Android Emulator.

## Emvironmnet Setup for LlamaTouch
1. Prepare a **new** Google account and sign in it on google play first.This **new** Google account is used to ensure the experimental environment.
2. start the emulator that you have created with the following command:
```bash
    emulator -avd pixel_6a_api31
```
3. If you can`t access the google play store directly, you maybe need to add a proxy accorrding to [this guide](https://blog.csdn.net/smallbabylong/article/details/132257659)
4. login apps in the emulator:
    - **script login**: This login script is designed to sign in to apps that only require Google account for authentication.
        ```bash
        python setup/login/login_apps.py --device_serial <device_serial>
        ```

    - **Manually login**: Apps that require manual login need users to manually register and log in. For more information, please refer to [login_tips](docs/login_tips.md).

    - **Free of login**: Apps that are free of login do not require registration or account login. However, you need to configure certain permissions within the app.For more information, please refer to [login_tips](docs/login_tips.md).

5. quit the emulator and save to the default snapshot.

# Run AgentEnv
## Setup
1. **Clone the Repository and Navigate to the Project Directory**:
   ```bash
   git clone https://github.com/LlamaTouch/AgentEnv
   cd AgentEnv
   ```

2. **Create a Conda Environment**:
   ```bash
   conda create -n AgentEnv python=3.9
   ```
3. **Activate the Conda Environment**:
   ```bash
   conda activate AgentEnv
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Before using AgentEnv, ensure you customize the [config.py file](config/config.py) with the settings specific to your previously configured Android Virtual Device (AVD).

## Integrate your Agent model with AgentEnv
The `MockAgent2AgentEnv.py` script serves as a detailed example of how to use AgentEnv with your own Agent model. It demonstrates all the interfaces provided by AgentEnv, showcasing how to interact with these APIs to facilitate communication between your Agent model and an Android device or emulator.

You can directly run the following command to use a MockAgent to experience how AgentEnv works.
```bash
python MockAgent2AgentEnv.py
```
## Try AgentEnv with AutoDroid

You can easily reproduce experiments in Llamatouch using the AutoDroid Agent model within the AgentEnv environment by referring to this [repository](https://github.com/LlamaTouch/AutoDroid/blob/main/README_AgentEnv.md).
