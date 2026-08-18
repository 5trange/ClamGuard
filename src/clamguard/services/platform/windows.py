import subprocess

from .base import PlatformService


class WindowsService(PlatformService):
    def get_clamav_connection(self):
        return {"type": "tcp", "host": "127.0.0.1", "port": 3310}

    def get_quick_scan_paths(self):
        return ["C:\\Users\\", "C:\\Program Files\\"]

    def start_daemon(self):
        pass

    def get_clamscan_exclude_dirs(self) -> list[str]:
        # Windows doesn't need Linux-specific system dir exclusions
        return []

    def get_subprocess_creation_flags(self) -> int:
        return subprocess.CREATE_NO_WINDOW
