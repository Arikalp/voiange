from __future__ import annotations

import asyncio
from pathlib import Path

from voiceai_backend.config.settings import settings
from voiceai_backend.core.enums import ArtifactType, JobType
from voiceai_backend.core.schemas import Artifact, JobRecord
from voiceai_backend.jobs.runner import JobRunner
from voiceai_backend.pipelines.audio.schemas import AudioProcessingRequest


class AudioProcessingManager:
    def __init__(self, runner: JobRunner) -> None:
        self.runner = runner

    def start_processing(self, payload: AudioProcessingRequest) -> JobRecord:
        return self.runner.submit(JobType.audio_processing, payload.model_dump(), self._execute)

    async def _execute(self, job_id: str, payload: dict) -> list[Artifact]:
        operations: list[str] = payload["operations"]
        total = max(len(operations), 1)
        for index, operation in enumerate(operations, start=1):
            percent = round(index / total * 90, 2)
            self.runner.update_progress(job_id, percent, operation, f"Applying {operation}")
            await asyncio.sleep(settings.audio_step_delay_seconds)

        output_dir = Path(payload["output_dir"])
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"processed.{payload['export_format']}"
        output_path.write_text("placeholder processed audio artifact", encoding="utf-8")
        return [
            self.runner.artifact(
                name=output_path.name,
                kind=ArtifactType.audio_output,
                path=str(output_path),
                metadata={"operations": operations},
            )
        ]
