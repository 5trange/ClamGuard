import logging
import subprocess

from clamguard.services.platform import platform_service

from .default import DEFAULT_CLAMD_SETTINGS, DEFAULT_FRESHCLAM_SETTINGS
from .paths import get_clamd_path, get_config_path, get_freshclam_path

logger = logging.getLogger(__name__)


def write_default_clamav_settings():
    main_config_path = get_config_path()
    config_path = main_config_path / "config"
    config_path.mkdir(parents=True, exist_ok=True)

    db_path = main_config_path / "db"
    db_path.mkdir(parents=True, exist_ok=True)

    clamd_conf = config_path / "clamd.conf"
    if not clamd_conf.exists():
        clamd_conf.write_text(DEFAULT_CLAMD_SETTINGS, encoding="utf-8")

    freshclam_conf = config_path / "freshclam.conf"
    if not freshclam_conf.exists():
        freshclam_conf.write_text(DEFAULT_FRESHCLAM_SETTINGS, encoding="utf-8")


def initialise_config_folder():
    config_dir = get_config_path()
    config_dir.mkdir(parents=True, exist_ok=True)
    write_default_clamav_settings()


def init_clamd():
    try:
        clamd_process = subprocess.Popen(
            ["clamd", "--config-file", str(get_clamd_path())],
            creationflags=platform_service.get_subprocess_creation_flags(),
        )
        return clamd_process
    except FileNotFoundError:
        logger.error("clamd executable not found in system PATH.")
        return None
    except PermissionError:
        logger.error("Permission denied when trying to start clamd.")
        return None
    except OSError as e:
        logger.error(f"OS error while starting clamd: {e}")
        return None


def init_freshclam():
    try:
        command = [
            "freshclam",
            "--config-file",
            str(get_freshclam_path()),
        ]
        freshclam_process = subprocess.Popen(
            command,
            creationflags=platform_service.get_subprocess_creation_flags(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        return freshclam_process
    except FileNotFoundError:
        logger.error("freshclam executable not found in system PATH.")
        return None
    except PermissionError:
        logger.error("Permission denied when trying to start freshclam.")
        return None
    except OSError as e:
        logger.error(f"OS error while starting freshclam: {e}")
        return None


def scan_file(paths: list[str]) -> subprocess.Popen | None:
    try:
        db_path = get_config_path() / "db"
        config_dir_str = str(get_config_path())

        # Base command
        command = [
            "clamscan",
            "-r",
            "--exclude-dir",
            config_dir_str,
            "--database",
            str(db_path),
        ]

        # Dynamically add OS-specific exclude directories
        for exclude_dir in platform_service.get_clamscan_exclude_dirs():
            command.extend(["--exclude-dir", exclude_dir])

        command.extend(paths)

        result = subprocess.Popen(
            args=command,
            creationflags=platform_service.get_subprocess_creation_flags(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        return result

    except FileNotFoundError:
        logger.error("clamscan executable not found in system PATH.")
        return None
    except PermissionError:
        logger.error("Permission denied when trying to run clamscan.")
        return None
    except OSError as e:
        logger.error(f"OS error while running clamscan: {e}")
        return None
