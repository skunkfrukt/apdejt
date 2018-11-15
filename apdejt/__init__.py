"""A simple function that uses pip to install the dependencies of an application."""
__version__ = "1.0.0"

import pathlib
import pip
from pip import _internal as pip_internal


def install_dependencies(path):
    """
    Use pip to install the packages in a requirements.txt file.
    - If the path given as input to the function is itself the path to
      a file named requirements.txt, that file is used.
    - If the path given is a directory, the function expects to find
      requirements.txt in that directory.
    - If the path is a file other than requirements.txt, the function
      expects to find requirements.txt in the same directory.
    """
    if hasattr(pip, "main"):
        pip_command = pip.main
    else:
        pip_command = pip_internal.main

    pathlib_path = pathlib.Path(path)

    if pathlib_path.is_dir():
        reqs_txt = pathlib_path / "requirements.txt"
    elif pathlib_path.is_file():
        if pathlib_path.name == "requirements.txt":
            reqs_txt = pathlib_path
        else:
            reqs_txt = pathlib_path.parent.absolute() / "requirements.txt"

    pip_command(["install", "-r", str(reqs_txt)])
