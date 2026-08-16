import os
import tempfile
from pathlib import Path

from .paths import get_config_path

runtime_path = Path(tempfile.gettempdir()) / "clamguard"
runtime_path.mkdir(exist_ok=True)


if os.name == "nt":
    DEFAULT_CLAMD_SETTINGS = f"""
Foreground yes
TCPSocket 3310
TCPAddr 127.0.0.1
DatabaseDirectory {get_config_path() / "db"}
"""
else:
    socket_path = runtime_path / "clamguard.sock"
    DEFAULT_CLAMD_SETTINGS = f"""
Foreground yes
LocalSocket {socket_path}
DatabaseDirectory {get_config_path() / "db"}
"""

if os.name == "nt":
    DEFAULT_FRESHCLAM_SETTINGS = f"""
DatabaseDirectory {get_config_path() / "db"}
UpdateLogFile C:\\Windows\\Temp\\freshclam.log
DatabaseMirror database.clamav.net
"""
else:
    (get_config_path() / "log").mkdir(parents=True, exist_ok=True)
    DEFAULT_FRESHCLAM_SETTINGS = f"""
DatabaseDirectory {get_config_path() / "db"}
UpdateLogFile {get_config_path() / "log"}/freshclam.log
DatabaseMirror database.clamav.net
"""
