#!/bin/bash

# Check the number of input parameters
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <android_sdk_root> <android_avd_home> <avd_name>"
    exit 1
fi

# Assign parameters
ANDROID_SDK_ROOT="$1"
ANDROID_AVD_HOME="$2"
AVD_NAME="$3"

# Set file paths
AVD_INI="$ANDROID_AVD_HOME/$AVD_NAME.ini"
HARDWARE_INI="$ANDROID_AVD_HOME/$AVD_NAME.avd/hardware-qemu.ini"
DEFAULTSNAPSHOT_INI="$ANDROID_AVD_HOME/$AVD_NAME.avd/snapshots/default_boot/hardware.ini"

# Update the path in the AVD INI file
sed -i "s|^\(path\s*=\s*\).*|\1$ANDROID_AVD_HOME/$AVD_NAME.avd|" $AVD_INI

# Update the hardware-qemu.ini file
sed -i "s|^\(android.avd.home\s*=\s*\).*|\1$ANDROID_AVD_HOME|" $HARDWARE_INI
sed -i "s|^\(android.sdk.root\s*=\s*\).*|\1$ANDROID_SDK_ROOT|" $HARDWARE_INI

# Update android avd home related paths
sed -i "s|^\(disk.encryptionKeyPartition.path\s*=\s*\).*|\1$ANDROID_AVD_HOME/$AVD_NAME.avd/encryptionkey.img|" $HARDWARE_INI
sed -i "s|^\(disk.dataPartition.path\s*=\s*\).*|\1$ANDROID_AVD_HOME/$AVD_NAME.avd/userdata-qemu.img|" $HARDWARE_INI
sed -i "s|^\(disk.cachePartition.path\s*=\s*\).*|\1$ANDROID_AVD_HOME/$AVD_NAME.avd/cache.img|" $HARDWARE_INI

# Update android-sdk root related paths
sed -i "s|^\(disk.vendorPartition.initPath\s*=\s*\).*|\1$ANDROID_SDK_ROOT/system-images/android-31/google_apis_playstore/x86_64/vendor.img|" $HARDWARE_INI
sed -i "s|^\(disk.systemPartition.initPath\s*=\s*\).*|\1$ANDROID_SDK_ROOT/system-images/android-31/google_apis_playstore/x86_64/system.img|" $HARDWARE_INI
sed -i "s|^\(disk.ramdisk.path\s*=\s*\).*|\1$ANDROID_SDK_ROOT/system-images/android-31/google_apis_playstore/x86_64/ramdisk.img|" $HARDWARE_INI
sed -i "s|^\(kernel.path\s*=\s*\).*|\1$ANDROID_SDK_ROOT/system-images/android-31/google_apis_playstore/x86_64/kernel-ranchu|" $HARDWARE_INI

# Copy contents of hardware-qemu.ini file to default_boot/hardware.ini
cp $HARDWARE_INI $DEFAULTSNAPSHOT_INI

echo "Configuration updated successfully."
