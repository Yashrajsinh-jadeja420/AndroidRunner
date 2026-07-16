from pathlib import Path
import re

import typer
from rich.console import Console

console = Console()

app = typer.Typer()


def read_text(path):

    try:
        return path.read_text(
            encoding="utf-8"
        )

    except Exception:
        return ""


@app.callback(invoke_without_command=True)
def detect():

    """
    Detect Android project information.
    """

    root = Path.cwd()

    console.rule(
        "[bold cyan]Android Project Detection[/bold cyan]"
    )


    # Project Information

    console.print(
        f"[cyan]Project:[/cyan] {root.name}"
    )

    console.print(
        f"[cyan]Path:[/cyan] {root}"
    )


    # Gradle Wrapper

    gradle = (
        root / "gradlew.bat"
        if (root / "gradlew.bat").exists()
        else root / "gradlew"
    )


    if gradle.exists():

        console.print(
            "[green]✓[/green] Gradle Wrapper"
        )

    else:

        console.print(
            "[red]✗[/red] Gradle Wrapper missing"
        )


    # Gradle Settings / Modules

    settings = root / "settings.gradle"


    if settings.exists():

        console.print(
            "[green]✓[/green] Gradle Settings"
        )


        text = read_text(
            settings
        )


        modules = re.findall(
            r'include\s*\(?[\'"]:(.*?)[\'"]\)?',
            text
        )


        if modules:

            console.print(
                f"[cyan]Modules:[/cyan] {modules}"
            )


    else:

        console.print(
            "[red]✗[/red] settings.gradle missing"
        )


    # Android Manifest

    manifest = (
        root
        / "app"
        / "src"
        / "main"
        / "AndroidManifest.xml"
    )


    package_found = False


    if manifest.exists():

        console.print(
            "[green]✓[/green] Android Manifest"
        )


        manifest_text = read_text(
            manifest
        )


        package = re.search(
            r'package="([^"]+)"',
            manifest_text
        )


        if package:

            console.print(
                f"[cyan]Package:[/cyan] {package.group(1)}"
            )

            package_found = True



    # Fallback Application ID

    if not package_found:


        build_file = (
            root
            / "app"
            / "build.gradle"
        )


        build_text = read_text(
            build_file
        )


        application_id = re.search(
            r'applicationId\s+"([^"]+)"',
            build_text
        )


        if application_id:

            console.print(
                f"[cyan]Application ID:[/cyan] {application_id.group(1)}"
            )



    # App Module

    app_module = root / "app"


    if app_module.exists():

        console.print(
            "[green]✓[/green] App Module"
        )

    else:

        console.print(
            "[red]✗[/red] App Module missing"
        )


    console.print(
        "\n[green]Detection complete.[/green]"
    )