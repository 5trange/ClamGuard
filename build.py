# This File exist to build the resource data use this file before running the program

import argparse
import subprocess
import platform
import sys

import requests
from tqdm import tqdm

CLAMAV_VERSION = "1.5.4"
WINDOWS_FILE_URL = (
    f"https://github.com/Cisco-Talos/clamav/releases/download/"
    f"clamav-{CLAMAV_VERSION}/clamav-{CLAMAV_VERSION}.win.x64.zip"
)
LINUX_FILE_URL = (
    f"https://github.com/Cisco-Talos/clamav/releases/download/"
    f"clamav-{CLAMAV_VERSION}/clamav-{CLAMAV_VERSION}.linux.x86_64.deb"
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
            "./src/clamguard/resources_rc.py",
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
            "src/clamguard/__main__.py",
            "--onefile",
            "--name",
            "ClamGuard",
            "--icon",
            "resources/icon.ico",
            "--paths",
            "src",
            "--distpath",
            "build/dist/",
            "--workpath",
            "build/temp",
        ]
    )
    return_code = process.wait()
    if return_code != 0:
        print("Error : Running the pyinstaller command")

def download_file(url):
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(f"build/dist/Clamav.{url.split('64.')[-1]}", "wb") as f, tqdm(
                desc=f"Downloading Clamav.{url.split('64.')[-1]}",
                total=int(response.headers.get("content-length", 0)),
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) as pbar:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    pbar.update(len(chunk))
    except:
        return False
    return True


def build_production():
    if platform.system() == "Windows":
        if(not download_file(WINDOWS_FILE_URL)):
            print("Failed to download the clamav zip")
            sys.exit(1)
        else:
            try:
                subprocess.run(
                    ["Expand-Archive", "-Path", "build/dist/Clamav.zip", "-DestinationPath", "build/dist/Clamav"],
                    check=True
                )
            except subprocess.CalledProcessError as e:
                print("found error when unzippping : ", e)
            except Exception as e:
                print("found exception : ", e)

    elif platform.system() == "Linux":
        if(not download_file(LINUX_FILE_URL)):
            print("Failed to download the clamav zip")
            sys.exit(1)
        else:
            try:
                subprocess.run(
                    ["ar", "x", "Clamav.deb"],
                    cwd="build/dist/",
                    check=True,
                )
                subprocess.run(
                    ["tar", "-xf", "data.tar.gz"],
                    cwd="build/dist/",
                    check=True,
                )
            except subprocess.CalledProcessError as e:
                print("found error when unzippping : ", e)
            except Exception as e:
                print("found exception : ", e)


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
        build_executable()
        build_production()

    elif args.command == "clean":
        clean_build()


if __name__ == "__main__":
    main()
