# This File exist to build the resource data use this file before running the program

import zipfile
import argparse
import os
import platform
import shutil
import stat
import subprocess
import sys

import requests
from tqdm import tqdm

CLAMAV_VERSION = "1.5.4"
CLAMAV_WIN_SUBFOLDER = f'clamav-{CLAMAV_VERSION}.win.x64'
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
        print(f"Error: {clamav_src} not found. Check CLAMAV_WIN_SUBFOLDER matches the zip contents.")
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
            print("Error: ISCC.exe (Inno Setup compiler) not found on PATH or in the default install location.")
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
        else:
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
    """
    Assemble build/dist/ClamGuard.AppDir out of:
      - build/dist/ClamGuard          (PyInstaller onefile binary)
      - build/dist/usr                (extracted ClamAV data.tar.gz tree)
    and package it into an AppImage using appimagetool, moved into build/output/.
    """
    print("Building AppImage...")

    dist_dir = "build/dist"
    output_dir = "build/output"

    appdir = os.path.join(dist_dir, "ClamGuard.AppDir")
    clamguard_bin = os.path.join(dist_dir, "ClamGuard")
    clamav_usr = os.path.join(dist_dir, "usr")

    if not os.path.isfile(clamguard_bin):
        print(f"Error: {clamguard_bin} not found. Run build_executable() first.")
        return
    if not os.path.isdir(clamav_usr):
        print(f"Error: {clamav_usr} not found. Extract data.tar.gz first.")
        return

    # Fresh AppDir every time
    if os.path.isdir(appdir):
        shutil.rmtree(appdir)
    os.makedirs(os.path.join(appdir, "usr", "bin"), exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # 1. Merge extracted ClamAV tree into AppDir/usr
    shutil.copytree(clamav_usr, os.path.join(appdir, "usr"), dirs_exist_ok=True)

    # 2. Put the ClamGuard binary into AppDir/usr/bin
    shutil.copy2(clamguard_bin, os.path.join(appdir, "usr", "bin", "ClamGuard"))
    os.chmod(os.path.join(appdir, "usr", "bin", "ClamGuard"), 0o755)

    # 3. Icon — appimagetool REQUIRES a valid icon file matching the
    # .desktop file's Icon= key, or it fails validation (confusingly
    # reported as "Desktop file not found, aborting"). AppImage only
    # accepts png/svg/xpm per the freedesktop icon spec, so a .ico source
    # gets converted to png.
    icon_src_candidates = [
        "resources/icon.png",
        "resources/icon.svg",
        "resources/img/clamguard.png",
        "resources/img/clamguard.ico",
    ]
    icon_found = False
    for candidate in icon_src_candidates:
        if not os.path.isfile(candidate):
            continue
        ext = os.path.splitext(candidate)[1].lower()
        if ext in (".png", ".svg"):
            shutil.copy2(candidate, os.path.join(appdir, f"clamguard{ext}"))
            icon_found = True
            break
    if not icon_found:
        print(
            f"Error: no icon found. Checked {', '.join(icon_src_candidates)}. "
            "appimagetool requires a root icon — add one before packaging."
        )
        return

    # 4. .desktop file (required at AppDir root). Using the one already
    # maintained at the project root instead of generating one here.
    desktop_src = "install/clamguard.desktop"
    if not os.path.isfile(desktop_src):
        print(
            f"Error: {desktop_src} not found in project root. "
            "appimagetool requires a .desktop file at the AppDir root."
        )
        return
    shutil.copy2(desktop_src, os.path.join(appdir, "clamguard.desktop"))

    # 5. AppRun launcher — sets LD_LIBRARY_PATH so bundled ClamAV libs resolve
    apprun_path = os.path.join(appdir, "AppRun")
    with open(apprun_path, "w") as f:
        f.write(
            "#!/bin/bash\n"
            'HERE="$(dirname "$(readlink -f "${0}")")"\n'
            'export LD_LIBRARY_PATH="${HERE}/usr/lib:${LD_LIBRARY_PATH}"\n'
            'export PATH="${HERE}/usr/bin:${PATH}"\n'
            'exec "${HERE}/usr/bin/ClamGuard" "$@"\n'
        )
    os.chmod(apprun_path, 0o755)

    # 6. Package with appimagetool
    os.makedirs("dist", exist_ok=True)
    appimage_name = f"dist/ClamGuard-{CLAMGUARD_VERSION}-x86_64.AppImage"
    final_path = os.path.abspath(os.path.join("dist", appimage_name))

    appimagetool = ensure_appimagetool()
    try:
        subprocess.run(
            [os.path.abspath(appimagetool), os.path.abspath(appdir), final_path],
            cwd=dist_dir,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print("found error when building the AppImage : ", e)
        return

    print(f"AppImage built: {final_path}")

    # 7. Move the built AppImage from build/dist/ into build/output/
    built_path = os.path.join(dist_dir, appimage_name)
    final_path = os.path.join(output_dir, appimage_name)
    shutil.move(built_path, final_path)

    print(f"AppImage built: {final_path}")


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
