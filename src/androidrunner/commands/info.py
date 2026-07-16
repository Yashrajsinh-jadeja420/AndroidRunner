from pathlib import Path
import subprocess

import typer
from rich.console import Console

console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def info():

    """
    Show Android project information.
    """

    root = Path.cwd()

    console.rule(
        "[bold cyan]AndroidRunner Project Info[/bold cyan]"
    )


    console.print(
        f"[cyan]Project:[/cyan] {root.name}"
    )


    console.print(
        f"[cyan]Path:[/cyan] {root}"
    )


    # Module

    if (root / "app").exists():

        console.print(
            "[cyan]Module:[/cyan] app"
        )


    # Device

    result = subprocess.run(
        [
            "adb",
            "devices"
        ],
        capture_output=True,
        text=True
    )


    if "device" in result.stdout:

        console.print(
            "[green]Device: Connected[/green]"
        )

    else:

        console.print(
            "[red]Device: Not Connected[/red]"
        )


    # APK

    apk = (
        root /
        "app" /
        "build" /
        "outputs" /
        "apk" /
        "debug" /
        "app-debug.apk"
    )


    if apk.exists():

        console.print(
            "[green]APK: app-debug.apk found[/green]"
        )

    else:

        console.print(
            "[yellow]APK: Not built yet[/yellow]"
        )


    console.print(
        "\n[green]Information complete.[/green]"
    )