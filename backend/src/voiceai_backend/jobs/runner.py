from __future__ import annotations

import asyncio
from datetime import UTC, datetime
from pathlib import Path
from typing import Awaitable, Callable
from uuid import uuid4

from voiceai_backend.core.enums import ArtifactType, JobStatus, JobType
from voiceai_backend.core.schemas import Artifact, JobProgress, JobRecord
from voiceai_backend.jobs.store import JobStore
from voiceai_backend.logging.setup import get_logger

logger = get_logger(__name__)

JobHandler = Callable[[str, dict], Awaitable[list[Artifact]]]


class JobRunner:
    def __init__(self, state_root: Path, artifacts_root: Path) -> None:
        self.store = JobStore(state_root)
        self.artifacts_root = artifacts_root
        self.tasks: dict[str, asyncio.Task[None]] = {}

    def list_jobs(self) -> list[JobRecord]:
        return self.store.list_jobs()

    def get_job(self, job_id: str) -> JobRecord | None:
        return self.store.get_job(job_id)

    def submit(self, job_type: JobType, payload: dict, handler: JobHandler) -> JobRecord:
        now = datetime.now(UTC)
        record = JobRecord(
            id=f"job_{uuid4().hex[:12]}",
            job_type=job_type,
            status=JobStatus.queued,
            progress=JobProgress(percent=0, stage="queued", message="Job accepted"),
            payload=payload,
            artifacts=[],
            created_at=now,
            updated_at=now,
        )
        self.store.upsert_job(record)
        self.tasks[record.id] = asyncio.create_task(self._run_job(record.id, handler))
        return record

    async def _run_job(self, job_id: str, handler: JobHandler) -> None:
        record = self.store.get_job(job_id)
        if not record:
            return
        try:
            logger.info("Starting job %s", job_id)
            running = record.model_copy(
                update={
                    "status": JobStatus.running,
                    "progress": JobProgress(percent=5, stage="starting", message="Job started"),
                    "updated_at": datetime.now(UTC),
                }
            )
            self.store.upsert_job(running)
            artifacts = await handler(job_id, running.payload)
            completed = running.model_copy(
                update={
                    "status": JobStatus.completed,
                    "progress": JobProgress(percent=100, stage="completed", message="Job completed"),
                    "artifacts": artifacts,
                    "updated_at": datetime.now(UTC),
                }
            )
            self.store.upsert_job(completed)
            logger.info("Completed job %s", job_id)
        except asyncio.CancelledError:
            cancelled = record.model_copy(
                update={
                    "status": JobStatus.cancelled,
                    "progress": JobProgress(percent=0, stage="cancelled", message="Job cancelled"),
                    "updated_at": datetime.now(UTC),
                }
            )
            self.store.upsert_job(cancelled)
            logger.warning("Cancelled job %s", job_id)
            raise
        except Exception as exc:
            logger.exception("Job %s failed", job_id)
            failed = record.model_copy(
                update={
                    "status": JobStatus.failed,
                    "progress": JobProgress(percent=record.progress.percent, stage="failed", message="Job failed"),
                    "error": str(exc),
                    "updated_at": datetime.now(UTC),
                }
            )
            self.store.upsert_job(failed)
        finally:
            self.tasks.pop(job_id, None)

    def update_progress(self, job_id: str, percent: float, stage: str, message: str) -> None:
        record = self.store.get_job(job_id)
        if not record:
            return
        updated = record.model_copy(
            update={
                "progress": JobProgress(percent=percent, stage=stage, message=message),
                "updated_at": datetime.now(UTC),
            }
        )
        self.store.upsert_job(updated)

    def artifact(self, name: str, kind: ArtifactType, path: str, metadata: dict | None = None) -> Artifact:
        return Artifact(
            id=f"artifact_{uuid4().hex[:12]}",
            name=name,
            kind=kind,
            path=path,
            metadata=metadata or {},
        )
