from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from voiceai_backend.models.schemas import ModelCreateRequest, ModelRecord, ModelUpdateRequest
from voiceai_backend.storage.json_store import JsonStore


class ModelManager:
    def __init__(self, state_root: Path) -> None:
        self.store = JsonStore(state_root / "models.json", ModelRecord)

    def list_models(self) -> list[ModelRecord]:
        return self.store.read_all()

    def get_model(self, model_id: str) -> ModelRecord | None:
        return next((item for item in self.list_models() if item.id == model_id), None)

    def create_model(self, payload: ModelCreateRequest) -> ModelRecord:
        items = self.list_models()
        now = datetime.now(UTC)
        record = ModelRecord(
            id=f"model_{uuid4().hex[:12]}",
            created_at=now,
            updated_at=now,
            **payload.model_dump(),
        )
        items.append(record)
        self.store.write_all(items)
        return record

    def update_model(self, model_id: str, payload: ModelUpdateRequest) -> ModelRecord | None:
        items = self.list_models()
        updated: ModelRecord | None = None
        next_items: list[ModelRecord] = []
        for item in items:
            if item.id != model_id:
                next_items.append(item)
                continue
            merged = item.model_copy(
                update={**payload.model_dump(exclude_none=True), "updated_at": datetime.now(UTC)}
            )
            updated = merged
            next_items.append(merged)
        self.store.write_all(next_items)
        return updated

    def delete_model(self, model_id: str) -> bool:
        items = self.list_models()
        filtered = [item for item in items if item.id != model_id]
        if len(filtered) == len(items):
            return False
        self.store.write_all(filtered)
        return True
