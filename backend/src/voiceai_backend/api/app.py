from contextlib import asynccontextmanager

from fastapi import FastAPI

from voiceai_backend.api.dependencies import ServiceContainer
from voiceai_backend.api.routes import router
from voiceai_backend.config.settings import settings
from voiceai_backend.datasets.manager import DatasetManager
from voiceai_backend.hardware.manager import HardwareManager
from voiceai_backend.jobs.runner import JobRunner
from voiceai_backend.logging.setup import configure_logging
from voiceai_backend.models.manager import ModelManager
from voiceai_backend.pipelines.audio.manager import AudioProcessingManager
from voiceai_backend.pipelines.inference.manager import InferenceManager
from voiceai_backend.pipelines.training.manager import TrainingManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    settings.state_root.mkdir(parents=True, exist_ok=True)
    settings.artifacts_root.mkdir(parents=True, exist_ok=True)

    runner = JobRunner(settings.state_root, settings.artifacts_root)
    app.state.services = ServiceContainer(
        hardware_manager=HardwareManager(),
        model_manager=ModelManager(settings.state_root),
        dataset_manager=DatasetManager(settings.state_root),
        training_manager=TrainingManager(runner),
        inference_manager=InferenceManager(runner),
        audio_processing_manager=AudioProcessingManager(runner),
        job_runner=runner,
    )
    yield


app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)
app.include_router(router, prefix=settings.api_prefix, tags=["voiceai"])
