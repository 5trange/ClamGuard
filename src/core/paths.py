from pathlib import Path

from platformdirs import user_config_dir


def get_config_path() -> Path:
    return Path(user_config_dir("Clamguard"))


def get_clamd_path() -> Path:
    return Path(user_config_dir("Clamguard")) / "config/clamd.conf"


def get_freshclam_path() -> Path:
    return Path(user_config_dir("Clamguard")) / "config/freshclam.conf"
