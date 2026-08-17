#!/usr/bin/env python3

import os
import site
import sys


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path:
        return os.path.basename(os.path.normpath(venv_path))
    return os.path.basename(os.path.normpath(sys.prefix))


def get_site_packages_path() -> str:
    try:
        paths = site.getsitepackages()
        if paths:
            return paths[0]
    except AttributeError:
        pass
    return os.path.join(sys.prefix, "site-packages")


def show_outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows\n")
    print("Then run this program again.")


def show_inside_construct() -> None:
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}")
    print(f"Environment Path: {venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(get_site_packages_path())


def main() -> None:
    if is_virtual_env():
        show_inside_construct()
    else:
        show_outside_matrix()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(1)
    except Exception as error:
        print(f"Unexpected error while entering the construct: {error}")
        sys.exit(1)
