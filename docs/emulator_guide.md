# AgentEnv -- Emulator setup guide

In this document we provide a guide for creating a virtual Android device with Android studio or with the command line.After creating an AVD, you will be able to connect it to an AndroidEnv instance.

## Use Android studio to create AVD
In this way, you can refer to this docs (https://github.com/google-deepmind/android_env/blob/main/docs/emulator_guide.md) in details.

## Only use command line tools to create AVD(for linux)

In this way, you can use the command line tools for setting up the Android SDK and creating an AVD, without Android Studio. This guide provides a step-by-step process for installing the Android SDK and creating an Android Virtual Device (AVD) using command line tools. This approach is useful for those who prefer not to use Android Studio for their Android development setup.

### 1. Install Java if you don`t have
Download and install Java from [here](https://www.oracle.com/java/technologies/downloads/). Make sure you set the JAVA_HOME environment variable.

### 2. Install Android SDK Command line tools
   - Download the [Command line tools](https://developer.android.com/studio) and extract them.
   - Move the extracted `cmdline-tools` directory to a new directory of your choice, for example, `android_sdk`. This new directory will be your Android SDK directory.
   - Inside the extracted `cmdline-tools directory`, create a new subdirectory named `latest`.
   - Move the contents of the original cmdline-tools directory (including the `lib` directory, `bin` directory, `NOTICE.txt` file, and `source.properties` file) to the newly created `latest` directory. Now, you can use the command line tools from this location. 

### 3. Install platform tools

```bash
path_to_your_android_sdk\cmdline-tools\latest\bin\sdkmanager "platform-tools" "platforms;android-31"
```
### 3. Set Up Environment Variables

To easily access SDK tools from any terminal session, you'll need to set up several environment variables. This includes paths to `cmdline-tools`, `platform-tools`, and the `emulator`, as well as specifying the `ANDROID_SDK_ROOT`. Here's an example of how to set these up:

```bash
export PATH=$PATH:path_to_your_android_sdk/cmdline-tools/latest/bin
export PATH=$PATH:path_to_your_android_sdk/platform-tools
export PATH=$PATH:path_to_your_android_sdk/emulator
export ANDROID_SDK_ROOT=path_to_your_android_sdk
```
Add these lines to your shell profile file (e.g., .bashrc, .zshrc, or .bash_profile) to make the changes permanent.

### 4. Download the Android image(API-level 31)
To download Android image API-level 31, execute the following command:
```bash
path_to_your_android_sdk\cmdline-tools\latest\bin\sdkmanager "system-images;android-31;google_apis_playstore;x86_64"
```

### 5. Create an Android Virtual Device(AVD)
To create an AVD which is Pixel 6a with API level 31, execute the following command:
```bash
path_to_your_android_sdk/cmdline-tools/latest/bin/avdmanager create avd -n pixel_6a_api_31 -k "system-images;android-31;google_apis_playstore;x86_64" --device "pixel_6a"
```

### 6. Launch the AVD
   - For the Android GUI:
   ```bash
   emulator -avd pixel_6a_api_31
   ```
   - For headless mode (no Android GUI):
   ```bash
   emulator -avd pixel_6a_api_31 -no-window
   ```

### 7. Test ADB connection
After you launch your AVD, run this command:
```bash
adb devices
```

