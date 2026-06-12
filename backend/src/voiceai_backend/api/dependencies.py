from dataclasses import dataclass

from fastapi import Request

from voiceai_backend.datasets.manager import DatasetManager
from voiceai_backend.hardware.manager import HardwareManager
from voiceai_backend.jobs.runner import JobRunner
from voiceai_backend.models.manager import ModelManager
from voiceai_backend.pipelines.audio.manager import AudioProcessingManager
from voiceai_backend.pipelines.inference.manager import InferenceManager
from voiceai_backend.pipelines.training.manager import TrainingManager


@dataclass
class ServiceContainer:
    hardware_manager: HardwareManager
    model_manager: ModelManager
    dataset_manager: DatasetManager
    training_manager: TrainingManager
    inference_manager: InferenceManager
    audio_processing_manager: AudioProcessingManager
    job_runner: JobRunner


def get_services(request: Request) -> ServiceContainer:
    return request.app.state.services
