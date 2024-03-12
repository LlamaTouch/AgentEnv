# AgentEnv

This repository contains the source code for the State-Capture project, which is based on the [droidbot](https://github.com/honeynet/droidbot) and designed to provide environment for agent model to conmunacate with an android device or emulator.AgentEnv is a tool to bridge agent model and real android device or android emulator.AgentEnv can parse agent output_action(AITW format) and map the action into android device or emulator action.In the meantime, AgentEnv can return android device or emulator state to agent model,such as screenshot, xml, view hiearachy


## Getting Started

### Prerequisites

Before you can use this tool, ensure you have the following installed:

- Python 3.x
- ADB (Android Debug Bridge)
- A real Android device or an avd connected to your machine via adb.

### Installation

1. Clone the repository to your local machine:

   ```sh
   git clone 
   ```

2. Navigate to the cloned repository:

   ```sh
   cd AgentEnv/
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

### create an avd
Before running the environment, you will need access to an emulated Android device. For instructions on creating a virtual Android device, see the [Emulator guide](docs/emulator_guide.md).

### Usage


1. **TASK SET**.Use [instruction files](docs/instructions) as your tasks set, or you can build your own tasks set according to this [instruction file](docs/instructions/general/all_instruction.csv)

2. **Preinstalled Apps**.if you use our [tasks set](docs/instructions), you should preinstall [these apps](docs/app_package/app_package.csv) in your android device.These apps need to be involved in the process of executing our tasks set by the agent.

3. **Initialize AgentEnv instance**.To initialize an instance of `AgentEnv`, you need to configure several parameters that define the environment's behavior and its interaction with devices. Below is a detailed explanation of the parameters involved in the initialization process:

- `device_serial`: This parameter specifies the serial number of the device that the agent will connect to. It can be an IP address (for devices connected over a network) or a USB-connected device's serial number. For example, the device connected over a network with the IP address `10.29.212.189` on port `5555`.

    ```python
    device_serial = "10.29.212.189:5555"
    ```
   you can get device_serial via command:
   ```bash
   adb devices -l 
   ```

- `local_output_path`: This defines the path on the local filesystem where the agent will store captured data during its operation. It's important that this directory exists and is writable by the agent. In the given example, captured data will be stored in `captured_data`.

    ```python
    local_output_path = "captured_data"
    ```

- `instruction_file_path`: This parameter points to a CSV file containing a list of instructions that the agent will execute. Each instruction should be detailed enough for the agent to perform specific actions. The example uses a general instruction set located at `docs/instructions/general/all_instruction.csv`.

    ```python
    instruction_file_path = "docs/instructions/general/all_instruction.csv"
    ```

- `max_steps`: This defines the maximum number of steps the agent is allowed to take for each instruction. It serves as a control mechanism to prevent the agent from executing indefinitely.For example, the maximum steps are set to `30`.

    ```python
    max_steps = 30 
    ```

To initialize the `AgentEnv`, you would typically use these parameters to create a new instance, ensuring that the environment is set up with the specific device, data storage location, instruction set, and operation constraints defined by these parameters.For example:
   ```python 
   agent_env =  AgentEnv(device_serial=device_serial, local_output_path=local_output_path, max_steps=max_steps,instruction_fp=instruction_file_path)
   ```

4. **Integrate your Agent into AgentEnv**.The test_environment.py file is a demo example to show how to use AgentEnv in your own Agent models.


