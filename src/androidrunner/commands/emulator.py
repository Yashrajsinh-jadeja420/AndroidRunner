import subprocess

import typer
from rich.console import Console


console = Console()

app = typer.Typer(
    help="Manage Android emulators."
)


@app.command()
def list():

    """
    List available Android emulators.
    """


    console.rule(
        "[bold cyan]Available Emulators[/bold cyan]"
    )


    result = subprocess.run(
        [
            "emulator",
            "-list-avds"
        ],
        capture_output=True,
        text=True
    )


    if not result.stdout.strip():

        console.print(
            "[yellow]No emulators found.[/yellow]"
        )

        return


    for avd in result.stdout.splitlines():

        console.print(
            f"[green]✓[/green] {avd}"
        )



@app.command()
def start(
    name: str
):

    """
    Start an Android emulator.
    """


    console.rule(
        "[bold cyan]Starting Emulator[/bold cyan]"
    )


    subprocess.Popen(
        [
            "emulator",
            "-avd",
            name
        ]
    )


    console.print(
        f"[green]Starting {name}[/green]"
    )