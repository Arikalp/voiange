from __future__ import annotations

import asyncio
from pathlib import Path

from voiceai_backend.config.settings import settings
from voiceai_backend.core.enums import ArtifactType, JobType
from voiceai_backend.core.schemas import Artifact, JobRecord
from voiceai_backend.jobs.runner import JobRunner
from voiceai_backend.pipelines.inference.schemas import InferenceRequest


class InferenceManager:
    def __init__(self, runner: JobRunner) -> None:
        self.runner = runner

    def start_inference(self, payload: InferenceRequest) -> JobRecord:
        return self.runner.submit(JobType.inference, payload.model_dump(), self._execute)

    async def _execute(self, job_id: str, payload: dict) -> list[Artifact]:
        for step, percent in [
            ("audio_loading", 18),
            ("voice_conversion", 63),
            ("post_processing", 92),
        ]:
            self.runner.update_progress(job_id, percent, step, f"{step.replace('_', ' ').title()} in progress")
            await asyncio.sleep(settings.inference_step_delay_seconds)

        output_dir = Path(payload["output_dir"])
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "converted.wav"
        output_path.write_text("placeholder inference audio artifact", encoding="utf-8")
        return [
            self.runner.artifact(
                name="converted.wav",
                kind=ArtifactType.inference_output,
                path=str(output_path),
                metadata={"model_id": payload["model_id"], "pitch_shift": payload["pitch_shift"]},
            )
        ]
