import subprocess

import typer
from rich.console import Console

from androidrunner.core.project import is_android_project
from androidrunner.core.scanner import scan_project
from androidrunner.core.config import (
    get_variant,
    get_module
)


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def build():

    """
    Build the current Android project.
    """


    project = scan_project()


    # Check Android project
    if not is_android_project(project.root):

        console.print(
            "[red]❌ Not an Android project[/red]"
        )

        console.print(
            f"[yellow]Current folder:[/yellow] {project.root}"
        )

        console.print(
            "[yellow]Run this command inside an Android project folder.[/yellow]"
        )

        raise typer.Exit(1)



    if not project.gradle:

        console.print(
            "[red]Gradle wrapper not found.[/red]"
        )

        raise typer.Exit(1)



    module = get_module()
    variant = get_variant()


    task = (
        f":{module}:assemble"
        f"{variant.capitalize()}"
    )


    console.rule(
        "[bold cyan]Building APK[/bold cyan]"
    )


    console.print(
        f"[cyan]Task:[/cyan] {task}"
    )


    result = subprocess.run(
        [
            str(project.gradle),
            task
        ],
        cwd=project.root,
        shell=True
    )


    if result.returncode != 0:

        console.print(
            "[red]Build failed[/red]"
        )

        raise typer.Exit(1)


    console.print(
        "[green]BUILD SUCCESSFUL[/green]"
    )