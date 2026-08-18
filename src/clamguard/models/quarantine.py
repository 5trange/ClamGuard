import json
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from PySide6.QtCore import (
    Property,
    QAbstractTableModel,
    QByteArray,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
    Signal,
    Slot,
)

from clamguard.services.quarantine_service import QuarantineService

logger = logging.getLogger(__name__)


@dataclass
class QuarantineItem:
    name: str
    file_type: str
    original_location: str
    quarantine_location: str
    date: datetime


class QuarantineModel(QAbstractTableModel):
    TextRole = Qt.ItemDataRole.UserRole + 1
    rowsChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._quarantine_service = QuarantineService()
        self._items: list[QuarantineItem] = []
        self._headers = ["Name", "Type", "Original Location", "Date"]

        from clamguard.core.paths import get_config_path

        self._data_path = get_config_path() / "data"
        self._data_path.mkdir(parents=True, exist_ok=True)
        self._file_path = self._data_path / "records.json"

        self.load()

    def rowCount(
        self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()
    ) -> int:
        if parent.isValid():
            return 0
        return len(self._items)

    def columnCount(
        self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()
    ) -> int:
        if parent.isValid():
            return 0
        return len(self._headers)

    def data(
        self,
        index: QModelIndex | QPersistentModelIndex,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> str | None:
        if not index.isValid() or role not in (
            Qt.ItemDataRole.DisplayRole,
            self.TextRole,
        ):
            return None

        item = self._items[index.row()]
        col = index.column()

        if col == 0:
            return item.name
        if col == 1:
            return item.file_type
        if col == 2:
            return item.original_location
        if col == 3:
            now = datetime.now(timezone.utc)
            delta = now - item.date

            if delta.days > 365:
                return item.date.strftime("%d %b %Y")
            elif delta.days > 0:
                return f"{delta.days}d ago"
            elif delta.seconds > 3600:
                return f"{delta.seconds // 3600}h ago"
            elif delta.seconds > 60:
                return f"{delta.seconds // 60}m ago"
            else:
                return "Just now"

        return None

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> str | int | None:
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        return section + 1

    def roleNames(self) -> dict[int, QByteArray]:
        return {self.TextRole: QByteArray(b"text")}

    @Property(int, notify=rowsChanged)
    def count(self) -> int:
        return self.rowCount()

    @Slot()
    def load(self) -> None:
        self.beginResetModel()
        self._items = []

        if self._file_path.exists():
            try:
                with self._file_path.open("r", encoding="utf-8") as f:
                    raw_data = json.load(f)

                self._items = []
                for item in raw_data:
                    original_location = item.get(
                        "original_location", item.get("location", "")
                    )
                    quarantine_location = item.get("quarantine_location", "")

                    if not quarantine_location and original_location:
                        quarantine_location = str(
                            self._quarantine_service.quarantine_dir
                            / f"{item.get('token', 'unknown')}.quarantine"
                        )

                    self._items.append(
                        QuarantineItem(
                            name=item["name"],
                            file_type=item.get(
                                "type", item.get("file_type", "Unknown")
                            ),
                            original_location=original_location,
                            quarantine_location=quarantine_location,
                            date=datetime.fromisoformat(item["date"])
                            if "date" in item
                            else datetime.now(timezone.utc),
                        )
                    )
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Failed to load quarantine data: {e}")
                self._items = []

        self.endResetModel()
        self.rowsChanged.emit()

    def save(self) -> None:
        data = [
            {
                "name": item.name,
                "type": item.file_type,
                "original_location": item.original_location,
                "quarantine_location": item.quarantine_location,
                "date": item.date.isoformat(),
            }
            for item in self._items
        ]
        try:
            with self._file_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except OSError as e:
            logger.error(f"Failed to save quarantine data: {e}")

    @Slot(str, str, str)
    def addItem(self, file_name: str, file_type: str, original_file_path: str) -> None:
        """
        Adds a detected file to the quarantine model and moves it.
        NOTE: original_file_path is ALREADY the full path (e.g., 'C:/virus/malware.exe').
        """
        new_quarantine_path = self._quarantine_service.quarantine(original_file_path)

        if not new_quarantine_path:
            logger.error(f"Failed to quarantine file: {original_file_path}")
            return

        row = len(self._items)
        self.beginInsertRows(QModelIndex(), row, row)

        self._items.append(
            QuarantineItem(
                name=file_name,
                file_type=file_type,
                original_location=original_file_path,
                quarantine_location=str(new_quarantine_path),
                date=datetime.now(timezone.utc),
            )
        )

        self.endInsertRows()
        self.rowsChanged.emit()
        self.save()

    @Slot(int, result=bool)
    def restoreItem(self, row: int) -> bool:
        """Restores a file from quarantine and removes it from the model."""
        if 0 <= row < len(self._items):
            item = self._items[row]
            success = self._quarantine_service.restore(
                Path(item.quarantine_location), Path(item.original_location)
            )
            if success:
                self._removeRow(row)
            return success
        return False

    @Slot(int, result=bool)
    def deleteItem(self, row: int) -> bool:
        """Permanently deletes a quarantined file and removes it from the model."""
        if 0 <= row < len(self._items):
            item = self._items[row]
            success = self._quarantine_service.delete(Path(item.quarantine_location))
            if success:
                self._removeRow(row)
            return success
        return False

    def _removeRow(self, row: int):
        """Internal helper to cleanly remove a row from the model."""
        self.beginRemoveRows(QModelIndex(), row, row)
        self._items.pop(row)
        self.endRemoveRows()
        self.rowsChanged.emit()
        self.save()
