import subprocess

import typer
from rich.console import Console
from rich.table import Table


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def devices():

    """
    Show connected Android devices.
    """


    console.rule(
        "[bold cyan]Android Devices[/bold cyan]"
    )


    try:

        result = subprocess.run(
            [
                "adb",
                "devices"
            ],
            capture_output=True,
            text=True
        )


    except FileNotFoundError:

        console.print(
            "[red]ADB not found.[/red]"
        )

        raise typer.Exit(1)



    lines = result.stdout.splitlines()


    table = Table()


    table.add_column("Device")
    table.add_column("Status")


    count = 0


    for line in lines[1:]:

        if line.strip():

            parts = line.split()


            if len(parts) >= 2:

                table.add_row(
                    parts[0],
                    parts[1]
                )

                count += 1



    if count == 0:

        console.print(
            "[yellow]No devices connected.[/yellow]"
        )

    else:

        console.print(table)

        console.print(
            f"\n[green]{count} device(s) connected[/green]"
        )