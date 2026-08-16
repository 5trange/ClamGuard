# This File exist to build the resource data use this file before running the program

import argparse
from operator import sub
import subprocess

import requests
from tqdm import tqdm

CLAMAV_VERSION = "1.5.4"
WINDOWS_FILE_URL = (
    f"https://github.com/Cisco-Talos/clamav/releases/download/"
    f"clamav-{CLAMAV_VERSION}/clamav-{CLAMAV_VERSION}.win.x64.zip"
)


def parse_args():
    parser = argparse.ArgumentParser(description="Manage the ClamGuard project")

    subparsers = parser.add_subparsers(
        dest="command", required=False, help="Available subcommands"
    )
    subparsers.add_parser("build", help="Build the project using PyInstaller")
    subparsers.add_parser("production", help="Build the project for production")
    subparsers.add_parser("clean", help="Clean the build artifacts")
    parser.add_argument(
        "--no-resources", action="store_true", help="Skip resources building step"
    )

    return parser.parse_args()


def build_resources():
    print("Building resources...")
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
    print("Building executable...")
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
            "build/dist/",
            "--workpath",
            "build/temp",
        ]
    )
    return_code = process.wait()
    if return_code != 0:
        print("Error : Running the pyinstaller command")


def build_production():
    with requests.get(WINDOWS_FILE_URL, stream=True) as response:
        response.raise_for_status()
        with open("build/dist/Clamav.zip", "wb") as f, tqdm(
            desc="Downloading Clamav.zip",
            total=int(response.headers.get("content-length", 0)),
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                pbar.update(len(chunk))


def clean_build():
    print("Cleaning build artifacts...")
    subprocess.run(["rm", "-rf", "ClamGuard.spec", "build/", "dist/"], check=False)


def main():
    args = parse_args()
    if not getattr(args, "no_resources", None):
        build_resources()

    if args.command == "build":
        build_executable()

    elif args.command == "production":
        build_production()

    elif args.command == "clean":
        clean_build()


if __name__ == "__main__":
    main()
