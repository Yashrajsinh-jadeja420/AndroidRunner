import typer
from rich.console import Console

from androidrunner.commands.build import build
from androidrunner.commands.install import install
from androidrunner.commands.launch import launch

from androidrunner.core.scanner import scan_project
from androidrunner.core.project import is_android_project


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def run():

    """
    Build, install and launch Android application.
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
            "[yellow]Run adr run inside an Android project folder.[/yellow]"
        )

        raise typer.Exit(1)



    console.rule(
        "[bold cyan]AndroidRunner Run[/bold cyan]"
    )


    console.print(
        "[cyan]1/3 Building APK[/cyan]"
    )

    build()



    console.print(
        "[cyan]2/3 Installing APK[/cyan]"
    )

    install()



    console.print(
        "[cyan]3/3 Launching App[/cyan]"
    )

    launch()



    console.print(
        "\n[green]Application started successfully.[/green]"
    )