import subprocess

import typer
from rich.console import Console

from androidrunner.core.scanner import scan_project
from androidrunner.core.config import (
    get_module,
)


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def release():

    """
    Build Android release APK.
    """


    project = scan_project()


    if not project.gradle:

        console.print(
            "[red]Gradle wrapper not found.[/red]"
        )

        raise typer.Exit(1)


    module = get_module()


    task = (
        f":{module}:assembleRelease"
    )


    console.rule(
        "[bold cyan]Building Release APK[/bold cyan]"
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
            "[red]Release build failed[/red]"
        )

        raise typer.Exit(1)


    console.print(
        "[green]RELEASE BUILD SUCCESSFUL[/green]"
    )