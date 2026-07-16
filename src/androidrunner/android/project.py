from pathlib import Path


def find_project_root(start: Path) -> Path | None:
    """
    Search upward until an Android Gradle project is found.
    """

    current = start.resolve()

    while True:

        if (
            (current / "gradlew").exists()
            and (
                (current / "settings.gradle").exists()
                or (current / "settings.gradle.kts").exists()
            )
        ):
            return current

        if current.parent == current:
            return None

        current = current.parent