import json
from dataclasses import dataclass, field
from datetime import datetime, timezone

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
    Slot,
)

from core.paths import get_config_path

_EMPTY_INDEX = QModelIndex()

config_path = get_config_path()


@dataclass
class QuarantineItem:
    name: str
    type: str
    location: str
    date: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class QuarantineModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
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

        if role != Qt.ItemDataRole.DisplayRole:
            return

        item = self._items[index.row()]
        values = [
            item.name,
            item.type,
            item.location,
            item.date.isoformat(),
        ]
        return values[index.column()]

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

    @Slot()
    def load(self):
        if not self.file_path.exists():
            return

        try:
            self.beginResetModel()
            with self.file_path.open("r", encoding="utf-8") as f:
                self._items = [
                    QuarantineItem(
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
                "name": item.name,
                "type": item.type,
                "location": item.location,
                "date": item.date.isoformat(),
            }
            for item in self._items
        ]
        with self.file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def addItem(self, item: QuarantineItem):
        row = len(self._items)

        self.beginInsertRows(
            QModelIndex(),
            row,
            row,
        )

        self._items.append(item)
        self.endInsertRows()
        self.save()
