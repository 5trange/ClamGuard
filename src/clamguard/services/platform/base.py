from abc import ABC, abstractmethod


class PlatformService(ABC):
    @abstractmethod
    def get_clamav_connection(self) -> dict:
        pass

    @abstractmethod
    def get_quick_scan_paths(self) -> list[str]:
        pass

    @abstractmethod
    def start_daemon(self) -> bool:
        pass

    @abstractmethod
    def get_clamscan_exclude_dirs(self) -> list[str]:
        pass

    @abstractmethod
    def get_subprocess_creation_flags(self) -> int:
        pass
