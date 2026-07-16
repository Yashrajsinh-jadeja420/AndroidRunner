import shutil
import subprocess
import os

from pathlib import Path



def find_adb():

    # Check PATH
    adb = shutil.which("adb")

    if adb:
        return adb


    # Check ANDROID_HOME
    sdk = os.environ.get("ANDROID_HOME")

    if sdk:

        adb = (
            Path(sdk)
            /
            "platform-tools"
            /
            "adb.exe"
        )

        if adb.exists():
            return str(adb)



    # Check ANDROID_SDK_ROOT
    sdk = os.environ.get("ANDROID_SDK_ROOT")

    if sdk:

        adb = (
            Path(sdk)
            /
            "platform-tools"
            /
            "adb.exe"
        )

        if adb.exists():
            return str(adb)



    return None





def get_connected_devices():

    adb = find_adb()

    if not adb:
        return []


    result = subprocess.run(
        [
            adb,
            "devices"
        ],
        capture_output=True,
        text=True
    )


    devices = []


    for line in result.stdout.splitlines():

        if (
            line.strip()
            and
            not line.startswith("List")
        ):

            parts = line.split()

            if len(parts) >= 2 and parts[1] == "device":

                devices.append(parts[0])


    return devices