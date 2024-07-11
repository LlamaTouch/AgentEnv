# Emulator Transfer

This document guides you through the process of setting up a pre-installed app on an Android Virtual Device (AVD) on your **Linux** or **WSL2** machine. It should be noted that if you are using WSL2, you need to manually enable systemd. You can refer to [here](https://github.com/microsoft/WSL/issues/7149).

The AVD is specifically configured with the following properties:

- **Name**: The AVD is named `pixel_6a_api31`, which is a user-defined identifier for the virtual device.
- **System Image**: It uses the Android 31 system image that includes Google APIs and the Play Store, providing a realistic environment for app testing and development.
- **Architecture**: The system image is based on the x86_64 architecture, optimized for performance in an emulation environment.
- **Device Profile**: The virtual device mimics the specifications of a Google Pixel 6a, ensuring that the app's behavior and layout can be tested on a specific device profile.

## Setting up the Android SDK

### 1. Install Java (if not already installed)
Download and install Java (Java 17 recommended) from [here](https://www.oracle.com/java/technologies/downloads/). Ensure you set the `JAVA_HOME` environment variable.

### 2. Install Android SDK Command Line Tools
   - Download the [Command Line Tools](https://developer.android.com/studio) and extract them.
   - Move the extracted `cmdline-tools` directory to a directory named `android_sdk`, which will serve as your Android SDK directory.
   - Inside the `cmdline-tools` directory, create a subdirectory named `latest`.
   - Move all contents of the original `cmdline-tools` directory into the `latest` directory. This setup allows the use of the command line tools from this location.

### 3. Install Platform Tools
```bash
path_to_your_android_sdk/cmdline-tools/latest/bin/sdkmanager "platform-tools" "platforms;android-31"
```

### 4. Download the Android Image (API-level 31)
To download the Android image for API-level 31, use the following command:
```bash
path_to_your_android_sdk/cmdline-tools/latest/bin/sdkmanager "system-images;android-31;google_apis_playstore;x86_64"
```

### 5. Install Build Tools
Ensure you have the appropriate version of the build tools installed. Here, we use version 31.0.0, which is compatible with the system image specified. Verify compatibility if you plan to use a different system image.
```bash
path_to_your_android_sdk/cmdline-tools/latest/bin/sdkmanager "build-tools;31.0.0"
```

### 6. Set Up Environment Variables
Establish environment variables to facilitate easy access to SDK tools from any terminal session:
```bash
export ANDROID_SDK_ROOT=path_to_your_android_sdk
export PATH=$PATH:$ANDROID_SDK_ROOT/cmdline-tools/latest/bin
export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools
export PATH=$PATH:$ANDROID_SDK_ROOT/emulator
```
Incorporate these lines into your shell profile file (e.g., `.bashrc`, `.zshrc`, or `.bash_profile`) to make the setup permanent.

## Importing the AVD

### 1. Set Up the Environment Variables
Ensure that the environment variables are set up correctly by running the following command:
```bash
export ANDROID_AVD_HOME=<your_android_avd_home>
```

### 2. Extract the AVD file to your ANDROID_AVD_HOME, in linux it usually located at `~/.android/avd`:
```bash
tar -xzvf pixel_6a_api31.tar.gz -C $ANDROID_AVD_HOME
```

### 3. Verify the AVD:
```bash
avdmanager list avd
```
You can also delete the AVD
```bash
avdmanager delete avd -n pixel_6a_api31
```

### 4. Execute the initialization script to adjust necessary parameters:
```bash
bash init.sh $ANDROID_SDK_ROOT $ANDROID_AVD_HOME pixel_6a_api31
```

### 5. Cold Boot the AVD:
Sometimes it requires adding the current user to the KVM group, just follow the quiding information and run the evaluator commandagain after setting up.

To avoid logging out and back, run the following command:
```bash
newgrp kvm
```
Start the emulator without loading a snapshot:
```bash
emulator -avd pixel_6a_api31 -no-snapshot-load
```
Note that starting the emulator in this way requires a display device. However, some Linux servers are headless, so in these cases, you will need to use a tool that supports the X11 forwarding protocol, like MobaXterm on Windows, to forward the display.
