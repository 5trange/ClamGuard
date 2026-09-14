# This File exist to build the resource data use this file before running the program

import argparse
import os
import platform
import shutil
import stat
import subprocess
import sys
import zipfile

import requests
from tqdm import tqdm

CLAMAV_VERSION = "1.5.4"
CLAMAV_WIN_SUBFOLDER = f"clamav-{CLAMAV_VERSION}.win.x64"
CLAMGUARD_VERSION = "1.3.0"
STAGING_DIR = "dist"
INSTALLER_SCRIPT = "install/setup.iss"
WINDOWS_FILE_URL = (
    f"https://github.com/Cisco-Talos/clamav/releases/download/"
    f"clamav-{CLAMAV_VERSION}/clamav-{CLAMAV_VERSION}.win.x64.zip"
)
LINUX_FILE_URL = (
    f"https://github.com/Cisco-Talos/clamav/releases/download/"
    f"clamav-{CLAMAV_VERSION}/clamav-{CLAMAV_VERSION}.linux.x86_64.deb"
)

APPIMAGETOOL_URL = (
    "https://github.com/AppImage/AppImageKit/releases/download/"
    "continuous/appimagetool-x86_64.AppImage"
)
APPIMAGETOOL_PATH = "build/tools/appimagetool-x86_64.AppImage"


def parse_args():
    parser = argparse.ArgumentParser(description="Manage the ClamGuard project")

    subparsers = parser.add_subparsers(
        dest="command", required=False, help="Available subcommands"
    )
    subparsers.add_parser("build", help="Build the project using PyInstaller")
    subparsers.add_parser(
        "production",
        help="Build the project for production (auto-detects Linux/Windows)",
    )
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
            "--noconsole",
            "--onefile",
            "--name",
            "ClamGuard",
            "--icon",
            "resources/img/clamguard.ico",
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


def build_windows_installer():
    """
    Stage ClamGuard.exe + the extracted ClamAV win.x64 files into one folder,
    then compile setup.iss with Inno Setup to produce the installer exe.
    """
    print("Staging files for installer...")

    exe_path = "build/dist/ClamGuard.exe"
    clamav_src = os.path.join("build/dist/Clamav", CLAMAV_WIN_SUBFOLDER)

    if not os.path.isfile(exe_path):
        print(f"Error: {exe_path} not found. Run build_executable() first.")
        sys.exit(1)
    if not os.path.isdir(clamav_src):
        print(
            f"Error: {clamav_src} not found. Check CLAMAV_WIN_SUBFOLDER matches the zip contents."
        )
        sys.exit(1)

    # Fresh staging folder every time
    if os.path.isdir(STAGING_DIR):
        shutil.rmtree(STAGING_DIR)
    os.makedirs(STAGING_DIR, exist_ok=True)

    shutil.copy2(exe_path, os.path.join(STAGING_DIR, "ClamGuard.exe"))
    shutil.copytree(clamav_src, STAGING_DIR, dirs_exist_ok=True)

    print("Building installer with Inno Setup...")

    iscc = shutil.which("iscc") or shutil.which("ISCC")
    if not iscc:
        default_path = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
        if os.path.isfile(default_path):
            iscc = default_path
        else:
            print(
                "Error: ISCC.exe (Inno Setup compiler) not found on PATH or in the default install location."
            )
            sys.exit(1)

    if not os.path.isfile(INSTALLER_SCRIPT):
        print(f"Error: {INSTALLER_SCRIPT} not found in project root.")
        sys.exit(1)

    try:
        subprocess.run([iscc, INSTALLER_SCRIPT], check=True)
    except subprocess.CalledProcessError as e:
        print("found error when building the installer : ", e)
        sys.exit(1)

    print("Installer built successfully.")


def download_file(url, dest_path=None, label=None):
    """Download a URL to dest_path (or the legacy build/dist/Clamav.<ext> path
    when dest_path is not given, kept for backwards compatibility)."""
    if dest_path is None:
        dest_path = f"build/dist/Clamav.{url.split('64.')[-1]}"

    os.makedirs(os.path.dirname(dest_path) or ".", exist_ok=True)

    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with (
                open(dest_path, "wb") as f,
                tqdm(
                    desc=label or f"Downloading {os.path.basename(dest_path)}",
                    total=int(response.headers.get("content-length", 0)),
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                ) as pbar,
            ):
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    pbar.update(len(chunk))
    except Exception as e:
        print("found exception while downloading : ", e)
        return False
    return True


def build_production():
    system = platform.system()

    if system == "Windows":
        if not download_file(WINDOWS_FILE_URL):
            print("Failed to download the clamav zip")
            sys.exit(1)
        try:
            with zipfile.ZipFile("build/dist/Clamav.zip") as zf:
                zf.extractall("build/dist/Clamav")
        except zipfile.BadZipFile as e:
            print("found error when unzipping : ", e)
            sys.exit(1)
        except Exception as e:
            print("found exception : ", e)
            sys.exit(1)

        build_windows_installer()

    elif system == "Linux":
        if not download_file(LINUX_FILE_URL):
            print("Failed to download the clamav zip")
            sys.exit(1)
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

        build_appimage()

    else:
        print(f"Error: unsupported platform '{system}', nothing to build.")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Linux AppImage
# ---------------------------------------------------------------------------


def ensure_appimagetool():
    """Download appimagetool if it isn't already cached locally."""
    if os.path.isfile(APPIMAGETOOL_PATH) and os.access(APPIMAGETOOL_PATH, os.X_OK):
        return APPIMAGETOOL_PATH

    print("appimagetool not found, downloading...")
    if not download_file(
        APPIMAGETOOL_URL, dest_path=APPIMAGETOOL_PATH, label="Downloading appimagetool"
    ):
        print("Failed to download appimagetool")
        sys.exit(1)

    st = os.stat(APPIMAGETOOL_PATH)
    os.chmod(APPIMAGETOOL_PATH, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    return APPIMAGETOOL_PATH


def build_appimage():
    print("Building AppImage...")

    dist_dir = os.path.abspath("build/dist")
    output_dir = os.path.abspath("build/output")

    appdir = os.path.join(dist_dir, "ClamGuard.AppDir")
    clamguard_bin = os.path.join(dist_dir, "ClamGuard")
    clamav_usr = os.path.join(dist_dir, "usr")

    if not os.path.isfile(clamguard_bin):
        print(f"Error: {clamguard_bin} not found.")
        sys.exit(1)

    if not os.path.isdir(clamav_usr):
        print(f"Error: {clamav_usr} not found.")
        sys.exit(1)

    # Fresh AppDir
    if os.path.isdir(appdir):
        shutil.rmtree(appdir)

    os.makedirs(os.path.join(appdir, "usr", "bin"), exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Copy ClamAV
    shutil.copytree(
        clamav_usr,
        os.path.join(appdir, "usr"),
        dirs_exist_ok=True,
    )

    # Copy ClamGuard executable
    target_bin = os.path.join(
        appdir,
        "usr",
        "bin",
        "ClamGuard",
    )

    shutil.copy2(clamguard_bin, target_bin)
    os.chmod(target_bin, 0o755)

    # Icon
    icon_src = "resources/img/clamguard.png"

    if not os.path.isfile(icon_src):
        print(f"Error: icon not found: {icon_src}")
        sys.exit(1)

    shutil.copy2(
        icon_src,
        os.path.join(appdir, "clamguard.png"),
    )

    # Desktop file
    desktop_src = "install/clamguard.desktop"

    if not os.path.isfile(desktop_src):
        print(f"Error: desktop file not found: {desktop_src}")
        sys.exit(1)

    shutil.copy2(
        desktop_src,
        os.path.join(appdir, "clamguard.desktop"),
    )

    # AppRun
    apprun_path = os.path.join(appdir, "AppRun")

    with open(apprun_path, "w") as f:
        f.write(
            "#!/bin/bash\n"
            'HERE="$(dirname "$(readlink -f "${0}")")"\n'
            "\n"
            'export PATH="${HERE}/usr/bin:${PATH}"\n'
            "\n"
            "# Use software rendering for maximum compatibility\n"
            'export QT_QUICK_BACKEND="${QT_QUICK_BACKEND:-software}"\n'
            "\n"
            'exec "${HERE}/usr/bin/ClamGuard" "$@"\n'
        )

    os.chmod(apprun_path, 0o755)

    # Output
    appimage_name = (
        f"ClamGuard-{CLAMGUARD_VERSION}-x86_64.AppImage"
    )

    built_path = os.path.join(
        dist_dir,
        appimage_name,
    )

    final_path = os.path.join(
        output_dir,
        appimage_name,
    )

    # Remove old build
    if os.path.isfile(built_path):
        os.remove(built_path)

    if os.path.isfile(final_path):
        os.remove(final_path)

    appimagetool = ensure_appimagetool()

    print("\nAppDir contents:")
    for root, dirs, files in os.walk(appdir):
        for file in files:
            print(os.path.join(root, file))

    print("\nRunning appimagetool...")

    try:
        subprocess.run(
            [
                os.path.abspath(appimagetool),
                appdir,
                built_path,
            ],
            check=True,
        )

    except subprocess.CalledProcessError as e:
        print("\nError when building the AppImage")
        print(f"Return code: {e.returncode}")
        print(f"Command: {e.cmd}")
        sys.exit(1)

    if not os.path.isfile(built_path):
        print(
            f"Error: appimagetool completed successfully but "
            f"output was not found: {built_path}"
        )
        sys.exit(1)

    shutil.move(
        built_path,
        final_path,
    )

    print(f"\nAppImage built successfully: {final_path}")


def clean_build():
    print("Cleaning build artifacts...")
    targets = ["ClamGuard.spec", "build", "dist"]
    for target in targets:
        if os.path.isdir(target):
            shutil.rmtree(target, ignore_errors=True)
        elif os.path.isfile(target):
            os.remove(target)


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
