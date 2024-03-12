# AgentEnv -- Emulator setup guide

In this document we provide a guide for creating a virtual Android device with Android studio or with the command line.After creating an AVD, you will be able to connect it to an AndroidEnv instance.

## use Android studio
In this way, you can refer to this docs (https://github.com/google-deepmind/android_env/blob/main/docs/emulator_guide.md)in details.

## only use command line tools

In this way, you can use the command line tools for setting up the Android SDK and creating an AVD, without Android Studio. This guide provides a step-by-step process for installing the Android SDK and creating an Android Virtual Device (AVD) using command line tools. This approach is useful for those who prefer not to use Android Studio for their Android development setup.


### 1. Download Command Line Tools

1. Visit the **Android Studio download page**: [Android Studio](https://developer.android.com/studio).
2. Scroll down to the **"Command line tools only"** section.
3. Download the package appropriate for your operating system (Windows, Mac, or Linux).

### 2. Extract and Install SDK Command Line Tools

1. Extract the downloaded package to your preferred directory, e.g., `~/android-sdk` on Linux/Mac or `C:\Android\sdk` on Windows.

2. Set Up Environment Variables

To easily access SDK tools from any terminal session, you'll need to set up several environment variables. This includes paths to `cmdline-tools`, `platform-tools`, and the `emulator`, as well as specifying the `ANDROID_SDK_ROOT`. Here's an example of how to set these up:

```bash
export PATH=$PATH:~/android-sdk/cmdline-tools/latest/bin
export PATH=$PATH:~/android-sdk/platform-tools
export PATH=$PATH:~/android-sdk/emulator
export ANDROID_SDK_ROOT=~/android-sdk
```
Add these lines to your shell profile file (e.g., .bashrc, .zshrc, or .bash_profile) to make the changes permanent.

### 3. Install SDK Components Using sdkmanager

1. Open a command line or terminal.
2. Use the `sdkmanager --list` command to view available SDK packages.
3. Install the SDK platform(s) and system images you need. For example, to install the latest Android platform and system image:

   ```bash
   sdkmanager "platforms;android-30" "system-images;android-30;default;x86_64"
   ```

   Replace `android-30` with the version of Android you wish to install.

4. Install `platform-tools` (contains ADB and other tools) and `emulator`:

   ```bash
   sdkmanager "platform-tools" "emulator"
   ```

5. **install build-tools**, specify the version you need:

   ```bash
   sdkmanager "build-tools;30.0.3"
   ```

   Replace `30.0.3` with the version of the build-tools you require.

## 4. Creating an AVD

1. List available system images using `avdmanager`:

   ```bash
   avdmanager list system-images
   ```

2. Create an AVD specifying the name, device ID, system image, and other options. For example, to create an AVD named "MyAVD" using an API level 30 default x86_64 image:

   ```bash
   avdmanager create avd -n MyAVD -k "system-images;android-30;default;x86_64"
   ```

   You may specify a device type with `--device` or use `--force` to overwrite an existing AVD with the same name.

## 5. Launching the AVD

1. Start the AVD using the `emulator` command:

   ```bash
   emulator -avd MyAVD
   ```

This will launch the AVD you've created. The first launch might take some time.

For more details and advanced options, please refer to the official documentation: [Android Developers](https://developer.android.com/studio/command-line). Note that commands and steps may vary depending on your system configuration and the Android version you are setting up.
