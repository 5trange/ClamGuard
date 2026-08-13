import json
from dataclasses import dataclass, field
from datetime import datetime, timezone

from PySide6.QtCore import (
    QAbstractTableModel,
    QByteArray,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
    Slot,
)

from core.paths import get_config_path
from services.quarantine_service import QuarantineService

_EMPTY_INDEX = QModelIndex()

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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.quarantine_service = QuarantineService()
        self._items: list[QuarantineItem] = []
        self._headers = [
            "Name",
            "Type",
            "Original Location",
            "Date",
        ]
        self.data_path = config_path / "data"
        self.data_path.mkdir(parents=True, exist_ok=True)
        self.file_path = self.data_path / "records.json"

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = _EMPTY_INDEX):
        return len(self._items)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = _EMPTY_INDEX):
        return len(self._headers)

    def data(
        self,
        index: QModelIndex | QPersistentModelIndex,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):

        if not index.isValid():
            return None

        if role != Qt.ItemDataRole.DisplayRole and role != self.TextRole:
            return

        item = self._items[index.row()]
        values = [
            item.name,
            item.type,
            item.location,
            item.date.isoformat(),
        ]

        if role in (Qt.ItemDataRole.DisplayRole, self.TextRole):
            return values[index.column()]

        return None

    def headerData(
        self,
        section,
        orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

        return section + 1

    def roleNames(self):
        return {
            self.TextRole: QByteArray(b"text"),
        }

    @Slot()
    def load(self):
        if not self.file_path.exists():
            return

        try:
            self.beginResetModel()
            with self.file_path.open("r", encoding="utf-8") as f:
                self._items = [
                    QuarantineItem(
                        token=item["token"],
                        name=item["name"],
                        type=item["type"],
                        location=item["location"],
                        date=datetime.fromisoformat(item["date"]),
                    )
                    for item in json.loads(f.read())
                ]
            self.endResetModel()
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Failed to load quarantine data: {e}")
            self._items = []

    def save(self):
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
        with self.file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def addItem(self, file_name: str, file_type: str, file_path: str):
        row = len(self._items)

        self.beginInsertRows(
            QModelIndex(),
            row,
            row,
        )

        try:
            token = self.quarantine_service.quarantine(file_path + "/" + file_name)
        except Exception as e:
            print(f"Failed to quarantine file: {e}")
            return

        self._items.append(
            QuarantineItem(
                token=token,
                name=file_name,
                type=file_type,
                location=file_path,
            )
        )
        self.endInsertRows()
        self.save()
