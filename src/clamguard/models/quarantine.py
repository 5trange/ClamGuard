import json
from dataclasses import dataclass, field
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

from clamguard.core.paths import get_config_path
from clamguard.services.quarantine_service import QuarantineService

config_path = get_config_path()


@dataclass
class QuarantineItem:
    token: str
    name: str
    type: str
    location: str
    date: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class QuarantineModel(QAbstractTableModel):
    TextRole = Qt.ItemDataRole.UserRole + 1
    rowsChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._quarantine_service = QuarantineService()
        self._items: list[QuarantineItem] = []
        self._headers = ["Name", "Type", "Original Location", "Date"]
        self._data_path = config_path / "data"
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
        if not index.isValid():
            return None
        if role not in (Qt.ItemDataRole.DisplayRole, self.TextRole):
            return None

        item = self._items[index.row()]
        col = index.column()

        match col:
            case 0:
                return item.name
            case 1:
                return item.type
            case 2:
                return item.location
            case 3:
                return item.date.strftime("%d %b %Y, %H:%M:%S")
            case _:
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
                self._items = [
                    QuarantineItem(
                        token=item["token"],
                        name=item["name"],
                        type=item["type"],
                        location=item["location"],
                        date=datetime.fromisoformat(item["date"]),
                    )
                    for item in raw_data
                ]
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Failed to load quarantine data: {e}")

        self.endResetModel()
        self.rowsChanged.emit()

    def save(self) -> None:
        data = [
            {
                "token": item.token,
                "name": item.name,
                "type": item.type,
                "location": item.location,
                "date": item.date.isoformat(),
            }
            for item in self._items
        ]
        try:
            with self._file_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except OSError as e:
            print(f"Failed to save quarantine data: {e}")

    @Slot(str, str, str)
    def addItem(self, file_name: str, file_type: str, file_path: str) -> None:
        full_path = Path(file_path) / file_name

        try:
            token = self._quarantine_service.quarantine(str(full_path))
        except Exception as e:
            print(f"Failed to quarantine file: {e}")
            return

        row = len(self._items)
        self.beginInsertRows(QModelIndex(), row, row)
        self._items.append(
            QuarantineItem(
                token=token,
                name=file_name,
                type=file_type,
                location=file_path,
            )
        )
        self.endInsertRows()
        self.rowsChanged.emit()
        self.save()
