#!/usr/bin/env python

import os
import subprocess
import sys
import shutil


def is_poetry_installed_and_version_ok():
    poetry_path = shutil.which("poetry")
    if not poetry_path:
        return False
    try:
        result = subprocess.run(
            ["poetry", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        version_str = result.stdout.strip().split()[-1]
        print(f"Found Poetry version: {version_str}")
        major, minor, *_ = map(int, version_str.split("."))
        return (major, minor) >= (2, 0)
    except Exception:
        return False


def install_or_upgrade_poetry():
    print("Poetry not found or version < 2.0.0. Installing/Upgrading Poetry...")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
        check=True
    )
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "poetry>=2.0.0"],
        check=True
    )
    print("Poetry installed/upgraded successfully.")

def setup_dev_environment():
    """Install dev environment with Poetry and pre-commit hooks."""

    try:
        # Initialize git repository if not already initialized
        if not os.path.exists(".git"):
            subprocess.run(["git", "init"], check=True)
            print("Git repository initialized.")

        if not is_poetry_installed_and_version_ok():
            install_or_upgrade_poetry()

        # Set-up Poetry
        subprocess.run(["poetry", "install", "--with", "dev,test,docs"], check=True)

        # Set-up pre-commit hooks
        subprocess.run(["poetry", "run", "pre-commit", "install"], check=True)

    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        print("You must manually set up the development environment")


if __name__ == "__main__":
    setup_dev_environment()
