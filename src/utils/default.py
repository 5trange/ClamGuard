import tempfile
from pathlib import Path

from utils.paths import get_config_path


runtime_path = Path(tempfile.gettempdir()) / "clamguard"
runtime_path.mkdir(exist_ok=True)

socket_path = runtime_path / "clamguard.sock"

DEFAULT_CLAMD_SETTINGS = f"""
Foreground yes
LocalSocket {socket_path}
"""

DEFAULT_FRESHCLAM_SETTINGS = f"""
DatabaseDirectory {get_config_path() / "db"}
UpdateLogFile /tmp/freshclam.log
DatabaseMirror database.clamav.net
"""
