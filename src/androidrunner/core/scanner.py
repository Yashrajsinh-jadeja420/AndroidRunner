from pathlib import Path
import re


class AndroidProject:

    def __init__(self, root):

        self.root = root
        self.name = root.name
        self.modules = []
        self.package = None
        self.apk = None
        self.gradle = None



def read_text(path):

    try:
        return path.read_text(
            encoding="utf-8"
        )

    except Exception:
        return ""



def scan_project():

    root = Path.cwd()

    project = AndroidProject(root)


    # Gradle Wrapper

    if (root / "gradlew.bat").exists():

        project.gradle = root / "gradlew.bat"

    elif (root / "gradlew").exists():

        project.gradle = root / "gradlew"



    # Modules

    settings = root / "settings.gradle"

    if settings.exists():

        text = read_text(settings)

        project.modules = re.findall(
            r'include\s*\(?[\'"]:(.*?)[\'"]\)?',
            text
        )



    # Package Detection

    manifest = (
        root /
        "app" /
        "src" /
        "main" /
        "AndroidManifest.xml"
    )


    if manifest.exists():

        text = read_text(manifest)

        match = re.search(
            r'package="([^"]+)"',
            text
        )

        if match:

            project.package = match.group(1)



    # Gradle fallback

    if not project.package:

        gradle_files = [

            root /
            "app" /
            "build.gradle",

            root /
            "app" /
            "build.gradle.kts"

        ]


        for gradle_file in gradle_files:


            text = read_text(
                gradle_file
            )


            namespace = re.search(
                r'namespace\s+[\'"]([^\'"]+)[\'"]',
                text
            )


            application_id = re.search(
                r'applicationId\s+[\'"]([^\'"]+)[\'"]',
                text
            )


            if namespace:

                project.package = namespace.group(1)
                break


            if application_id:

                project.package = application_id.group(1)
                break



    # APK Detection

    apks = list(
        root.glob(
            "**/build/outputs/apk/**/*.apk"
        )
    )


    if apks:

        project.apk = apks[0]


    return project