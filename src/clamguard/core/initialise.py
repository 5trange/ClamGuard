import os
import subprocess

from .default import DEFAULT_CLAMD_SETTINGS, DEFAULT_FRESHCLAM_SETTINGS
from .paths import get_clamd_path, get_config_path, get_freshclam_path


def write_default_clamav_settings():
    main_config_path = get_config_path()
    config_path = main_config_path / "config"
    config_path.mkdir(exist_ok=True)
    db_path = main_config_path / "db"
    db_path.mkdir(exist_ok=True)

    if not (config_path / "clamd.conf").exists():
        (config_path / "clamd.conf").write_text(
            DEFAULT_CLAMD_SETTINGS, encoding="utf-8"
        )

    if not (config_path / "freshclam.conf").exists():
        (config_path / "freshclam.conf").write_text(
            DEFAULT_FRESHCLAM_SETTINGS, encoding="utf-8"
        )


def initialise_config_folder():
    config_dir = get_config_path()
    config_dir.mkdir(parents=True, exist_ok=True)
    write_default_clamav_settings()


def init_clamd():
    try:
        if os.name == "nt":
            clamd_process = subprocess.Popen(
                ["clamd", "--config-file", get_clamd_path()],
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
        else:
            clamd_process = subprocess.Popen(
                ["clamd", "--config-file", get_clamd_path()]
            )
        return clamd_process
    except FileNotFoundError:
        print("Debug: clamd not found")
        return None
    except PermissionError:
        print("Debug: Permission denied")
        return None
    except OSError:
        print("Debug: OSError")
        return None


def init_freshclam():
    try:
        command = [
            "freshclam",
            "--config-file",
            str(get_freshclam_path()),
        ]
        if os.name == "nt":

            freshclam_process = subprocess.Popen(
                command,
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            print(command)
        else:
            freshclam_process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
        return freshclam_process
    except FileNotFoundError:
        print("Debug: freshclam not found")
        return None
    except PermissionError:
        print("Debug: Permission denied")
        return None
    except OSError:
        print("Debug: OSError")
        return None


def scan_file(path: list[str]) -> subprocess.Popen | None:
    try:

        db_path = get_config_path() / "db"

        if os.name == "nt":
            result = subprocess.Popen(
                ["clamscan", "-r", "--exclude-dir", str(get_config_path()), "--database", db_path, *path],
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
        else:
            result = subprocess.Popen(
                ["clamscan", "-r", "--exclude-dir", str(get_config_path()), "--database", db_path, *path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
        return result

    except FileNotFoundError:
        print("clamscan not found")
        return None

    except PermissionError:
        print("Permission denied")
        return None

    except OSError as e:
        print(f"OS error: {e}")
        return None
