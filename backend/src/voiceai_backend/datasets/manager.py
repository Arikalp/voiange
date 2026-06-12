from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from voiceai_backend.datasets.schemas import DatasetCreateRequest, DatasetRecord, DatasetUpdateRequest
from voiceai_backend.storage.json_store import JsonStore


class DatasetManager:
    def __init__(self, state_root: Path) -> None:
        self.store = JsonStore(state_root / "datasets.json", DatasetRecord)

    def list_datasets(self) -> list[DatasetRecord]:
        return self.store.read_all()

    def get_dataset(self, dataset_id: str) -> DatasetRecord | None:
        return next((item for item in self.list_datasets() if item.id == dataset_id), None)

    def create_dataset(self, payload: DatasetCreateRequest) -> DatasetRecord:
        items = self.list_datasets()
        now = datetime.now(UTC)
        record = DatasetRecord(
            id=f"dataset_{uuid4().hex[:12]}",
            created_at=now,
            updated_at=now,
            **payload.model_dump(),
        )
        items.append(record)
        self.store.write_all(items)
        return record

    def update_dataset(self, dataset_id: str, payload: DatasetUpdateRequest) -> DatasetRecord | None:
        items = self.list_datasets()
        updated: DatasetRecord | None = None
        next_items: list[DatasetRecord] = []
        for item in items:
            if item.id != dataset_id:
                next_items.append(item)
                continue
            merged = item.model_copy(
                update={**payload.model_dump(exclude_none=True), "updated_at": datetime.now(UTC)}
            )
            updated = merged
            next_items.append(merged)
        self.store.write_all(next_items)
        return updated

    def delete_dataset(self, dataset_id: str) -> bool:
        items = self.list_datasets()
        filtered = [item for item in items if item.id != dataset_id]
        if len(filtered) == len(items):
            return False
        self.store.write_all(filtered)
        return True
