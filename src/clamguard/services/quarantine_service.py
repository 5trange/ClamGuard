import logging
import secrets
import shutil
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


class QuarantineService:
    def __init__(self):
        # Evaluate config path at instantiation, not module load time
        from clamguard.core.paths import get_config_path

        self.quarantine_dir: Path = get_config_path() / "quarantine"
        self.quarantine_dir.mkdir(parents=True, exist_ok=True)

    def quarantine(self, file_raw: str) -> Optional[Path]:
        """
        Moves a file to the quarantine directory.
        Returns the new Path of the quarantined file, or None if it failed.
        """
        file_path = Path(file_raw).resolve()

        if not file_path.is_file():
            logger.error(f"Cannot quarantine: File not found at {file_path}")
            return None

        # 16 bytes = 32 hex characters. Plenty for uniqueness, keeps filenames shorter.
        quarantine_name = f"{secrets.token_hex(16)}.quarantine"
        destination = self.quarantine_dir / quarantine_name

        try:
            # shutil.move handles cross-device moves automatically
            shutil.move(str(file_path), str(destination))
            logger.info(f"Quarantined {file_path} to {destination}")
            return destination
        except PermissionError:
            logger.error(f"Permission denied when trying to quarantine {file_path}")
            return None
        except OSError as e:
            logger.error(f"OS error while quarantining {file_path}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error quarantining {file_path}: {e}")
            return None

    def restore(self, quarantine_path: Path, original_path: Path) -> bool:
        """Restores a file from quarantine to its original location."""
        if not quarantine_path.is_file():
            logger.error(
                f"Cannot restore: Quarantined file not found at {quarantine_path}"
            )
            return False

        try:
            # Ensure the original directory still exists
            original_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(quarantine_path), str(original_path))
            logger.info(f"Restored {quarantine_path} to {original_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to restore {quarantine_path}: {e}")
            return False

    def delete(self, quarantine_path: Path) -> bool:
        """Permanently deletes a quarantined file."""
        if not quarantine_path.is_file():
            logger.error(
                f"Cannot delete: Quarantined file not found at {quarantine_path}"
            )
            return False

        try:
            quarantine_path.unlink()
            logger.info(f"Permanently deleted {quarantine_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete {quarantine_path}: {e}")
            return False
