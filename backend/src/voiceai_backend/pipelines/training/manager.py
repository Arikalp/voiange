from __future__ import annotations

import asyncio
from pathlib import Path

from voiceai_backend.config.settings import settings
from voiceai_backend.core.enums import ArtifactType, JobType
from voiceai_backend.core.schemas import Artifact, JobRecord
from voiceai_backend.jobs.runner import JobRunner
from voiceai_backend.pipelines.training.schemas import TrainingRequest


class TrainingManager:
    def __init__(self, runner: JobRunner) -> None:
        self.runner = runner

    def start_training(self, payload: TrainingRequest) -> JobRecord:
        return self.runner.submit(JobType.training, payload.model_dump(), self._execute)

    async def _execute(self, job_id: str, payload: dict) -> list[Artifact]:
        for step, percent in [
            ("dataset_validation", 15),
            ("feature_extraction", 45),
            ("training", 82),
            ("checkpoint_finalization", 95),
        ]:
            self.runner.update_progress(job_id, percent, step, f"{step.replace('_', ' ').title()} in progress")
            await asyncio.sleep(settings.training_step_delay_seconds)

        output_dir = Path(payload["output_dir"])
        output_dir.mkdir(parents=True, exist_ok=True)
        file_path = output_dir / f"{payload['model_name']}.pth"
        file_path.write_text("placeholder trained model artifact", encoding="utf-8")
        return [
            self.runner.artifact(
                name=payload["model_name"],
                kind=ArtifactType.trained_model,
                path=str(file_path),
                metadata={"epochs": payload["epochs"], "batch_size": payload["batch_size"]},
            )
        ]
