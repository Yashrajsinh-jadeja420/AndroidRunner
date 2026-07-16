from pathlib import Path
import json


CONFIG_FILE = ".adr.json"


def load_config():

    path = Path.cwd() / CONFIG_FILE


    if not path.exists():

        return {}


    try:

        return json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )


    except Exception:

        return {}



def get_variant():

    config = load_config()

    return config.get(
        "variant",
        "debug"
    )



def get_module():

    config = load_config()

    return config.get(
        "module",
        "app"
    )