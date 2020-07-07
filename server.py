import sys
import os
from application import app

def linux_server():
    """Set running in Linux env."""
    dirname = app.config.get("ROOT_DIR")
    os.system("bash %s/start.sh %s" % (dirname, API_LOG_DIRNAME))


def windows_server():
    """Set running in Windows env."""
    app.run(host=app.config.get("HOST"), port=app.config.get("PORT"))


def main():
    windows = sys.platform.startswith("win")

    if windows:
        try:
            windows_server()
        except Exception as error:
            pass
    else:
        linux_server()

