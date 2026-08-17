import sys
from pathlib import Path

from platformdirs import user_config_dir


def get_config_path() -> Path:
    return Path(user_config_dir("Clamguard"))


def get_clamd_path() -> Path:
    return Path(user_config_dir("Clamguard")) / "config/clamd.conf"


def get_freshclam_path() -> Path:
    return Path(user_config_dir("Clamguard")) / "config/freshclam.conf"


def get_quick_scan_path() -> list[Path]:
    home = Path.home()
    paths = [
        home / "Downloads",
        home / "Desktop",
        home / "Documents",
    ]

    if sys.platform == "win32":
        paths.append(Path.home() / "AppData" / "Local" / "Temp")
    else:
        paths.append(Path.home() / ".config")
        paths.append(Path.home() / ".local")
        paths.append(Path.home() / ".cache")

    return [path for path in paths if path.exists()]


def get_full_scan_path() -> list[Path]:
    paths = []
    if sys.platform == "win32":
        import ctypes

        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for i in range(26):
            if bitmask & (1 << i):
                drive = Path(f"{chr(65 + i)}:\\")
                paths.append(drive)
    else:
        paths.append(Path("/"))

    return [path for path in paths if path.exists()]
