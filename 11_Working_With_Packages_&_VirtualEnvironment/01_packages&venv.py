"""A safe, hands-on tour of packages and virtual environments.

This script uses only Python's standard library, so it can run before installing
any third-party package. It shows how to inspect the current interpreter and
where packages are loaded from, plus the commands to create an environment.
"""

import importlib.util
import sys
from pathlib import Path


def main():
    print("=" * 68)
    print("PYTHON PACKAGES AND VIRTUAL ENVIRONMENTS: A HANDS-ON TOUR")
    print("=" * 68)

    # 1. The interpreter running this file.
    print("\n1. CURRENT PYTHON")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Interpreter path: {sys.executable}")

    # 2. Virtual environments expose their location through sys.prefix.
    # When an environment is active, sys.prefix generally points into it.
    print("\n2. ENVIRONMENT INFORMATION")
    print(f"Environment prefix: {sys.prefix}")
    print(f"Base Python prefix: {sys.base_prefix}")
    in_venv = sys.prefix != sys.base_prefix
    print(f"Running in a virtual environment? {in_venv}")

    # 3. A module comes with Python; a third-party distribution is installed.
    print("\n3. MODULE AVAILABILITY")
    print(f"Standard library module 'json' is available: {importlib.util.find_spec('json') is not None}")
    print(f"Optional package 'rich' is installed: {importlib.util.find_spec('rich') is not None}")
    print("The tour does not require rich; it only checks whether it is installed.")

    # 4. Show the conventional project layout.
    print("\n4. PROJECT LAYOUT")
    example_project = Path("study_project")
    print(example_project / ".venv")
    print(example_project / "main.py")
    print(example_project / "requirements.txt")

    # 5. Print the core commands as examples. These are not executed by the script.
    print("\n5. TYPICAL COMMANDS")
    commands = [
        "python -m venv .venv",
        "source .venv/bin/activate  # macOS/Linux",
        r".venv\Scripts\Activate.ps1  # Windows PowerShell",
        "python -m pip install package-name",
        "python -m pip install -r requirements.txt",
        "deactivate",
    ]
    for command in commands:
        print(command)

    print("\n" + "=" * 68)
    print("TOUR COMPLETE — the Markdown guide explains each command and when to use it.")
    print("=" * 68)


if __name__ == "__main__":
    main()
