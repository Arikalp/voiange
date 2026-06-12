from __future__ import annotations

from pathlib import Path

from voiceai_backend.core.schemas import JobRecord
from voiceai_backend.storage.json_store import JsonStore


class JobStore:
    def __init__(self, state_root: Path) -> None:
        self.store = JsonStore(state_root / "jobs.json", JobRecord)

    def list_jobs(self) -> list[JobRecord]:
        return self.store.read_all()

    def get_job(self, job_id: str) -> JobRecord | None:
        return next((item for item in self.list_jobs() if item.id == job_id), None)

    def upsert_job(self, record: JobRecord) -> JobRecord:
        items = self.list_jobs()
        replaced = False
        next_items: list[JobRecord] = []
        for item in items:
            if item.id == record.id:
                next_items.append(record)
                replaced = True
            else:
                next_items.append(item)
        if not replaced:
            next_items.append(record)
        self.store.write_all(next_items)
        return record
