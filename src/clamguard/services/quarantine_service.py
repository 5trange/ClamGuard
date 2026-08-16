import secrets
import shutil
from pathlib import Path

from clamguard.core.paths import get_config_path

config_path = get_config_path()

class QuarantineService:
    def __init__(self):
        self.quarantine_dir = config_path / "quarantine"
        self.quarantine_dir.mkdir(parents=True, exist_ok=True)

    def quarantine(self, file_raw: str) -> str:
        file_path = Path(file_raw).resolve()

        if not file_path.is_file():
            raise FileNotFoundError(file_path)

        quarantine_name = f"{secrets.token_hex(32)}.quarantine"
        destination = self.quarantine_dir / quarantine_name

        shutil.move(str(file_path), str(destination))

        return quarantine_name
