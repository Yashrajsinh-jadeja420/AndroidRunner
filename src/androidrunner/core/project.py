from pathlib import Path


def is_android_project(path=None):

    if path is None:
        path = Path.cwd()

    required = [
        "gradlew",
        "gradlew.bat",
        "settings.gradle",
        "settings.gradle.kts",
    ]

    has_gradle = any(
        (path / file).exists()
        for file in required[:2]
    )

    has_settings = any(
        (path / file).exists()
        for file in required[2:]
    )

    has_app = (
        path / "app"
    ).exists()


    return (
        has_gradle
        and has_settings
        and has_app
    )