import tempfile
from pathlib import Path

from .base import PlatformService


class LinuxService(PlatformService):
    def get_clamav_connection(self):

        runtime_path = Path(tempfile.gettempdir()) / "clamguard" / "clamguard.sock"
        return {"type": "socket", "path": str(runtime_path)}

    def get_quick_scan_paths(self):
        return ["/home/", "/var/www/"]

    def start_daemon(self):
        pass

    def get_clamscan_exclude_dirs(self) -> list[str]:
        # Prevent clamscan from hanging on virtual filesystems
        return [
            "^/proc", "^/sys", "^/dev", "^/run", "^/snap", "^/tmp"
        ]

    def get_subprocess_creation_flags(self) -> int:
        return 0
