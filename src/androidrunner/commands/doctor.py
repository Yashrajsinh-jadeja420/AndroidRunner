import shutil

import typer
from rich.console import Console

from androidrunner.android.sdk import find_sdk, find_build_tools
from androidrunner.android.adb import find_adb, get_connected_devices

console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def doctor():
    """Check Android development environment."""

    console.rule("[bold cyan]AndroidRunner Doctor[/bold cyan]")

    # Java
    java = shutil.which("java")

    if java:
        console.print("[green]✓ Java[/green]")
        console.print(f"   {java}")
    else:
        console.print("[red]✗ Java not found[/red]")

    # Android SDK
    sdk = find_sdk()

    if sdk:
        console.print("[green]✓ Android SDK[/green]")
        console.print(f"   {sdk}")
    else:
        console.print("[red]✗ Android SDK not found[/red]")

        # Build Tools
    build_tools = find_build_tools()

    if build_tools:
        console.print("[green]✓ Build Tools[/green]")
        console.print(f"   {build_tools.name}")
    else:
        console.print("[red]✗ Build Tools not found[/red]")

    # ADB
    adb = find_adb()

    if adb:
        console.print("[green]✓ ADB[/green]")
        console.print(f"   {adb}")
    else:
        console.print("[red]✗ ADB not found[/red]")

	    # Connected Devices
    devices = get_connected_devices()

    if devices:
        console.print("[green]✓ Connected Device(s)[/green]")

        for device in devices:
            console.print(f"   {device}")
    else:
        console.print("[yellow]! No Android devices connected[/yellow]")