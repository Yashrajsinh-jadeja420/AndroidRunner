import subprocess

import typer
from rich.console import Console

from androidrunner.core.scanner import scan_project
from androidrunner.android.adb import find_adb
from androidrunner.core.project import is_android_project


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def launch():

    """
    Launch installed Android application.
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

        raise typer.Exit(1)



    if not project.package:

        console.print(
            "[red]Package name not detected.[/red]"
        )

        raise typer.Exit(1)



    adb = find_adb()


    if not adb:

        console.print(
            "[red]ADB not found.[/red]"
        )

        raise typer.Exit(1)



    console.rule(
        "[bold cyan]Launching APK[/bold cyan]"
    )


    console.print(
        f"[cyan]Package:[/cyan] {project.package}"
    )


    result = subprocess.run(
        [
            str(adb),
            "shell",
            "monkey",
            "-p",
            project.package,
            "1"
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
            "[red]Launch failed[/red]"
        )

        if result.stderr:

            console.print(
                result.stderr
            )

        raise typer.Exit(1)



    console.print(
        "[green]Application started successfully.[/green]"
    )