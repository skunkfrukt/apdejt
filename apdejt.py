import pathlib
import pip
from pip import _internal as pip_internal


def upgrade():
    if hasattr(pip, "main"):
        main_cmd = pip.main
    else:
        main_cmd = pip_internal.main

    reqs_txt = pathlib.Path(__file__).parent.absolute() / "requirements.txt"
    main_cmd(["install", "-r", str(reqs_txt)])


if __name__ == "__main__":
    upgrade()
