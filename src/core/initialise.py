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
        if os.name == "nt":
            freshclam_process = subprocess.Popen(
                ["freshclam", "--config-file", get_freshclam_path()],
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        else:
            freshclam_process = subprocess.Popen(
                ["freshclam", "--config-file", get_freshclam_path()],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
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
