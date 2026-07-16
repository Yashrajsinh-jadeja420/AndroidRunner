import subprocess

import typer
from rich.console import Console

from androidrunner.core.scanner import scan_project
from androidrunner.android.adb import find_adb
from androidrunner.core.project import is_android_project


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def install():

    """
    Install generated APK to connected Android device.
    """


    project = scan_project()


    # Validate Android project
    if not is_android_project(project.root):

        console.print(
            "[red]❌ Not an Android project[/red]"
        )

        console.print(
            f"[yellow]Current folder:[/yellow] {project.root}"
        )

        console.print(
            "[yellow]Run adr install inside an Android project folder.[/yellow]"
        )

        raise typer.Exit(1)



    if not project.apk:

        console.print(
            "[red]APK not found. Run adr build first.[/red]"
        )

        raise typer.Exit(1)



    adb = find_adb()


    if not adb:

        console.print(
            "[red]ADB not found.[/red]"
        )

        raise typer.Exit(1)



    console.rule(
        "[bold cyan]Installing APK[/bold cyan]"
    )



    result = subprocess.run(
        [
            str(adb),
            "install",
            "-r",
            str(project.apk)
        ],
        capture_output=True,
        text=True
    )



    if result.stdout:

        console.print(
            result.stdout
        )


    if result.returncode != 0:

        console.print(
            "[red]Installation failed[/red]"
        )

        if result.stderr:

            console.print(
                result.stderr
            )

        raise typer.Exit(1)



    console.print(
        "[green]APK Installed Successfully[/green]"
    )