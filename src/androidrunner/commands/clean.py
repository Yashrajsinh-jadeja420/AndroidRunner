import subprocess

import typer
from rich.console import Console

from androidrunner.core.scanner import scan_project


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def clean():

    """
    Clean Android project build files.
    """

    project = scan_project()


    if not project.gradle:

        console.print(
            "[red]Gradle wrapper not found.[/red]"
        )

        raise typer.Exit(1)


    console.rule(
        "[bold cyan]Cleaning Project[/bold cyan]"
    )


    result = subprocess.run(
        [
            str(project.gradle),
            "clean"
        ],
        cwd=project.root,
        shell=True
    )


    if result.returncode != 0:

        console.print(
            "[red]Clean failed[/red]"
        )

        raise typer.Exit(1)


    console.print(
        "[green]Clean completed successfully[/green]"
    )