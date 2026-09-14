import logging
import os
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
        freshclam_conf.write_text(
            DEFAULT_FRESHCLAM_SETTINGS,
            encoding="utf-8",
        )


def initialise_config_folder():
    config_dir = get_config_path()
    config_dir.mkdir(parents=True, exist_ok=True)
    write_default_clamav_settings()


def _get_clamav_environment() -> dict[str, str]:
    """
    Create a clean environment for ClamAV subprocesses.

    PyInstaller one-file applications modify LD_LIBRARY_PATH so that
    bundled libraries from /tmp/_MEIxxxx are preferred. This can cause
    ClamAV to load incompatible versions of OpenSSL, PCRE2, etc.

    Restore the original environment before launching ClamAV.
    """
    env = os.environ.copy()

    # PyInstaller stores the original value here before modifying it.
    original_ld_library_path = env.get("LD_LIBRARY_PATH_ORIG")

    if original_ld_library_path is not None:
        env["LD_LIBRARY_PATH"] = original_ld_library_path
    else:
        env.pop("LD_LIBRARY_PATH", None)

    return env


def _start_process(
    command: list[str],
    *,
    capture_output: bool = False,
) -> subprocess.Popen | None:
    """
    Start a ClamAV subprocess with a clean environment.
    """
    try:
        kwargs = {
            "args": command,
            "creationflags": platform_service.get_subprocess_creation_flags(),
            "env": _get_clamav_environment(),
        }

        if capture_output:
            kwargs.update(
                {
                    "stdout": subprocess.PIPE,
                    "stderr": subprocess.STDOUT,
                    "text": True,
                    "bufsize": 1,
                }
            )

        return subprocess.Popen(**kwargs)

    except FileNotFoundError:
        logger.error(
            "ClamAV executable not found in system PATH: %s",
            command[0],
        )
    except PermissionError:
        logger.error(
            "Permission denied when trying to start %s.",
            command[0],
        )
    except OSError as e:
        logger.error(
            "OS error while starting %s: %s",
            command[0],
            e,
        )

    return None


def init_clamd():
    command = [
        "clamd",
        "--config-file",
        str(get_clamd_path()),
    ]

    return _start_process(command)


def init_freshclam():
    command = [
        "freshclam",
        "--config-file",
        str(get_freshclam_path()),
    ]

    return _start_process(
        command,
        capture_output=True,
    )


def scan_file(paths: list[str]) -> subprocess.Popen | None:
    db_path = get_config_path() / "db"
    config_dir_str = str(get_config_path())

    command = [
        "clamscan",
        "-r",
        "--exclude-dir",
        config_dir_str,
        "--database",
        str(db_path),
    ]

    # Dynamically add OS-specific exclude directories.
    for exclude_dir in platform_service.get_clamscan_exclude_dirs():
        command.extend(
            [
                "--exclude-dir",
                exclude_dir,
            ]
        )

    command.extend(paths)

    return _start_process(
        command,
        capture_output=True,
    )
