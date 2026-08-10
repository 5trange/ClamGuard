from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
)

_EMPTY_INDEX = QModelIndex()

class QuarantineModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._items = []
        self._headers = [
            "File",
            "Location",
            "Status",
        ]

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = _EMPTY_INDEX):
        return len(self._items)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = _EMPTY_INDEX):
        return len(self._headers)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.ItemDataRole.DisplayRole):

        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            item = self._items[index.row()]
            return item[index.column()]

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

    def add_item(self, file, location, status):
        row = len(self._items)

        self.beginInsertRows(
            QModelIndex(),
            row,
            row,
        )

        self._items.append([
            file,
            location,
            status,
        ])

        self.endInsertRows()
