from pathlib import Path
import json

import typer
from rich.console import Console

from androidrunner.core.scanner import scan_project


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def init():

    """
    Create AndroidRunner project configuration.
    """


    project = scan_project()


    config_file = (
        project.root /
        ".adr.json"
    )


    if config_file.exists():

        console.print(
            "[yellow].adr.json already exists[/yellow]"
        )

        raise typer.Exit()



    config = {

        "project": project.name,

        "module": (
            project.modules[0]
            if project.modules
            else "app"
        ),

        "variant": "debug",

        "device": None

    }


    config_file.write_text(
        json.dumps(
            config,
            indent=4
        ),
        encoding="utf-8"
    )


    console.print(
        "[green]Created .adr.json successfully[/green]"
    )