import os
import tempfile
from pathlib import Path

from .paths import get_config_path

# Ensure runtime directory exists (used for Linux socket)
runtime_path = Path(tempfile.gettempdir()) / "clamguard"
runtime_path.mkdir(exist_ok=True)

config_path = get_config_path()
db_path = config_path / "db"

if os.name == "nt":
    clamd_network = "TCPSocket 3310\nTCPAddr 127.0.0.1"
    freshclam_log = "UpdateLogFile C:\\Windows\\Temp\\freshclam.log"
    socket_path = None  # Not used on Windows
else:
    socket_path = runtime_path / "clamguard.sock"
    clamd_network = f"LocalSocket {socket_path}"

    log_path = config_path / "log"
    log_path.mkdir(parents=True, exist_ok=True)
    freshclam_log = f"UpdateLogFile {log_path / 'freshclam.log'}"

DEFAULT_CLAMD_SETTINGS = f"""Foreground yes
{clamd_network}
DatabaseDirectory {db_path}
"""

DEFAULT_FRESHCLAM_SETTINGS = f"""DatabaseDirectory {db_path}
{freshclam_log}
DatabaseMirror database.clamav.net
"""
