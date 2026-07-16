import os
from pathlib import Path


def find_sdk() -> Path | None:
    """
    Find the Android SDK.
    """

    candidates = [
        os.environ.get("ANDROID_HOME"),
        os.environ.get("ANDROID_SDK_ROOT"),
        Path.home() / "AppData/Local/Android/Sdk",
    ]

    for sdk in candidates:
        if sdk:
            path = Path(sdk)
            if path.exists():
                return path

    return None


def find_build_tools() -> Path | None:
    """
    Find the newest installed Android Build Tools.
    """

    sdk = find_sdk()

    if sdk is None:
        return None

    build_tools = sdk / "build-tools"

    if not build_tools.exists():
        return None

    versions = [d for d in build_tools.iterdir() if d.is_dir()]

    if not versions:
        return None

    return sorted(versions)[-1]