import subprocess

import typer
from rich.console import Console


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def logs():

    """
    Show live Android device logs.
    """


    console.rule(
        "[bold cyan]Android Logs[/bold cyan]"
    )


    console.print(
        "[green]Starting logcat... Press CTRL+C to stop[/green]"
    )


    try:

        subprocess.run(
            [
                "adb",
                "logcat"
            ]
        )


    except KeyboardInterrupt:

        console.print(
            "\n[yellow]Logs stopped[/yellow]"
        )