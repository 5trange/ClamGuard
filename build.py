# This File exist to build the resource data use this file before running the program

import subprocess
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Manage the ClamGuard project")

    subparsers = parser.add_subparsers(dest="command", required=True, help="Available subcommands")
    build_parser = subparsers.add_parser("build", help="Build the project using PyInstaller")
    build_parser.add_argument("--no-resources", action="store_true", help="Skip resources building step")

    return parser.parse_args()


def build_resources():
    process = subprocess.Popen(
        [
            "uv",
            "run",
            "pyside6-rcc",
            "./resources/resources.qrc",
            "-o",
            "./src/core/resources_rc.py",
        ]
    )
    return_code = process.wait()
    if return_code != 0:
        print("Error : Running the pyside6-rcc command")

def build_executable():
    process = subprocess.Popen(
        [
            "uv",
            "run",
            "pyinstaller",
            "src/main.py",
            "--onefile",
            "--name",
            "ClamGuard",
            "--icon",
            "resources/icon.ico",
            "--distpath",
            "dist/"
        ]
    )
    return_code = process.wait()
    if return_code != 0:
        print("Error : Running the pyinstaller command")

def main():
    args = parse_args()
    if not args.no_resources:
        build_resources()
    if args.command == "build":
        build_executable()

if __name__ == "__main__":
    main()
