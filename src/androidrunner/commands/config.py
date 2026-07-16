import typer

from rich.console import Console

from androidrunner.core.config import load_config


console = Console()

app = typer.Typer()


@app.callback(invoke_without_command=True)
def config():

    """
    Show AndroidRunner configuration.
    """


    data = load_config()


    console.rule(
        "[bold cyan]AndroidRunner Configuration[/bold cyan]"
    )


    if not data:

        console.print(
            "[yellow]No .adr.json found.[/yellow]"
        )

        console.print(
            "Run: adr init"
        )

        raise typer.Exit()


    console.print(
        f"[cyan]Project:[/cyan] {data.get('project','Unknown')}"
    )

    console.print(
        f"[cyan]Module:[/cyan] {data.get('module','app')}"
    )

    console.print(
        f"[cyan]Variant:[/cyan] {data.get('variant','debug')}"
    )

    console.print(
        f"[cyan]Device:[/cyan] {data.get('device','Not selected')}"
    )