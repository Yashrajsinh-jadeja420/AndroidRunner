import typer
from importlib.metadata import version, PackageNotFoundError

from androidrunner.commands.run import app as run_app
from androidrunner.commands.doctor import app as doctor_app
from androidrunner.commands.build import app as build_app
from androidrunner.commands.install import app as install_app
from androidrunner.commands.launch import app as launch_app
from androidrunner.commands.detect import app as detect_app
from androidrunner.commands.info import app as info_app
from androidrunner.commands.init import app as init_app
from androidrunner.commands.config import app as config_app
from androidrunner.commands.logs import app as logs_app
from androidrunner.commands.devices import app as devices_app
from androidrunner.commands.clean import app as clean_app
from androidrunner.commands.release import app as release_app
from androidrunner.commands.emulator import app as emulator_app



def get_version():

    try:
        return version("androidrunner")

    except PackageNotFoundError:
        return "0.1.0-alpha"



app = typer.Typer(
    help="AndroidRunner CLI - Build, install and manage Android applications from terminal.",
    invoke_without_command=True
)



@app.callback(invoke_without_command=True)
def main(
    version_flag: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show AndroidRunner version."
    )
):

    if version_flag:

        typer.echo(
            f"AndroidRunner {get_version()}"
        )

        raise typer.Exit()



app.add_typer(
    run_app,
    name="run",
    help="Complete workflow: build APK, install it on device, and launch the app."
)


app.add_typer(
    doctor_app,
    name="doctor",
    help="Check Android development environment: Java, SDK, Build Tools, ADB and devices."
)


app.add_typer(
    build_app,
    name="build",
    help="Build the Android project and generate a debug APK."
)


app.add_typer(
    install_app,
    name="install",
    help="Install the generated APK on a connected Android device using ADB."
)


app.add_typer(
    launch_app,
    name="launch",
    help="Detect the app package and launch the installed Android application."
)


app.add_typer(
    detect_app,
    name="detect",
    help="Detect Android project structure and configuration."
)


app.add_typer(
    info_app,
    name="info",
    help="Show Android project information."
)


app.add_typer(
    init_app,
    name="init",
    help="Create AndroidRunner configuration."
)


app.add_typer(
    config_app,
    name="config",
    help="Show AndroidRunner configuration."
)


app.add_typer(
    logs_app,
    name="logs",
    help="Show live Android device logs."
)


app.add_typer(
    devices_app,
    name="devices",
    help="Show connected Android devices."
)


app.add_typer(
    clean_app,
    name="clean",
    help="Clean Android project build files."
)


app.add_typer(
    release_app,
    name="release",
    help="Build Android release APK."
)


app.add_typer(
    emulator_app,
    name="emulator",
    help="Manage Android emulators."
)



if __name__ == "__main__":
    app()