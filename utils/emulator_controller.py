import subprocess
import logging
import time

class EmulatorController:
    def __init__(self,avd_name,device_serial,params):
        self.avd_name = avd_name
        self.device_serial = device_serial
        self.params = params
        self.logger = logging.getLogger(self.__class__.__name__)
        self.state = "off"


    def load_emulator_with_snapshot(self,snapshot_name="default_boot"):
        """
        start the emulator and load the specified snapshot.

        Args:
        snapshot_name (str): the name of snapshot。
        """
        # cmd = ["emulator", "-avd", self.avd_name, "-snapshot", snapshot_name, "-no-snapshot-save"]
        cmd = ["emulator", "-avd", self.avd_name,"-no-snapshot-save"]
        for key, value in self.params.items():
            if key == "no-window":
                if value == "true":
                    cmd.append(f"-{key}")
            else:
                cmd.append(f"-{key}")
                cmd.append(f"{value}")

        self.logger.info(f"cmd: {cmd}")
        try:
            self.logger.info(f"Loading emulator '{self.avd_name}' with snapshot '{snapshot_name}'.")
            subprocess.Popen(cmd)
            self.state = "on"
        except Exception as e:
            self.logger.error(f"Error loading emulator with snapshot: {e}")

    def exit_emulator(self):
        """
        exit the current running emulator instance.
        """
        try:
            self.logger.info(f"Exiting emulator '{self.avd_name}'.")
            subprocess.run(["adb", "-s", f"{self.device_serial}", "emu", "kill"], check=True)
            self.state = "off"
        except Exception as e:
            self.logger.error(f"Error exiting emulator: {e}")

    def reload_snapshot(self, snapshot_name="default_boot"):
        """
        reload the specified snapshot.

        Args:
        snapshot_name (str): the name of snapshot。
        """
        if self.state == "on":
            # first exit the emulator
            self.exit_emulator()
            time.sleep(20)
            # restart the emulator with the specified snapshot
            self.load_emulator_with_snapshot(snapshot_name)
        else:
            self.load_emulator_with_snapshot(snapshot_name)
