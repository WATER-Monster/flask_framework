import sys
from application import app

def linux_server():
    """Set running in Linux env."""
    app.run(host=app.config.get("HOST"), port=app.config.get("PORT"))


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


if __name__ == '__main__':
    main()