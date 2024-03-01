# AgentEnv

This repository contains the source code for the State-Capture project, which is based on the [droidbot](https://github.com/honeynet/droidbot) and designed to provide environment for agent model to conmunacate with an android device or emulator.AgentEnv is a tool to bridge agent model and real android device or android emulator.AgentEnv can parse agent output_action(AITW format) and map the action into android device or emulator action.In the meantime, AgentEnv can return android device or emulator state to agent model,such as screenshot, xml, view hiearachy


## Getting Started

### Prerequisites

Before you can use this tool, ensure you have the following installed:

- Python 3.x
- ADB (Android Debug Bridge)
- An Android device connected to your machine via USB with USB debugging enabled.

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

### Usage

1. Connect to your device by usb or adb.

2. test_environment is an example to show how to use AgentEnv and its interface in your own agent


