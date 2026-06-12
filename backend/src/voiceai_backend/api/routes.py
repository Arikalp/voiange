from fastapi import APIRouter, Depends, HTTPException, status

from voiceai_backend.api.dependencies import ServiceContainer, get_services
from voiceai_backend.config.settings import settings
from voiceai_backend.core.schemas import ErrorResponse, HealthResponse, JobRecord
from voiceai_backend.datasets.schemas import DatasetCreateRequest, DatasetRecord, DatasetUpdateRequest
from voiceai_backend.hardware.schemas import GpuReport
from voiceai_backend.models.schemas import ModelCreateRequest, ModelRecord, ModelUpdateRequest
from voiceai_backend.pipelines.audio.schemas import AudioProcessingRequest
from voiceai_backend.pipelines.inference.schemas import InferenceRequest
from voiceai_backend.pipelines.training.schemas import TrainingRequest

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def healthcheck() -> HealthResponse:
    return HealthResponse(status="ok", app_name=settings.app_name, environment=settings.environment)


@router.get("/gpu", response_model=GpuReport)
def get_gpu_report(services: ServiceContainer = Depends(get_services)) -> GpuReport:
    return services.hardware_manager.get_report()


@router.get("/models", response_model=list[ModelRecord])
def list_models(services: ServiceContainer = Depends(get_services)) -> list[ModelRecord]:
    return services.model_manager.list_models()


@router.post("/models", response_model=ModelRecord, status_code=status.HTTP_201_CREATED)
def create_model(
    payload: ModelCreateRequest, services: ServiceContainer = Depends(get_services)
) -> ModelRecord:
    return services.model_manager.create_model(payload)


@router.patch("/models/{model_id}", response_model=ModelRecord, responses={404: {"model": ErrorResponse}})
def update_model(
    model_id: str, payload: ModelUpdateRequest, services: ServiceContainer = Depends(get_services)
) -> ModelRecord:
    record = services.model_manager.update_model(model_id, payload)
    if not record:
        raise HTTPException(status_code=404, detail="Model not found")
    return record


@router.delete("/models/{model_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_model(model_id: str, services: ServiceContainer = Depends(get_services)) -> None:
    if not services.model_manager.delete_model(model_id):
        raise HTTPException(status_code=404, detail="Model not found")


@router.get("/datasets", response_model=list[DatasetRecord])
def list_datasets(services: ServiceContainer = Depends(get_services)) -> list[DatasetRecord]:
    return services.dataset_manager.list_datasets()


@router.post("/datasets", response_model=DatasetRecord, status_code=status.HTTP_201_CREATED)
def create_dataset(
    payload: DatasetCreateRequest, services: ServiceContainer = Depends(get_services)
) -> DatasetRecord:
    return services.dataset_manager.create_dataset(payload)


@router.patch(
    "/datasets/{dataset_id}", response_model=DatasetRecord, responses={404: {"model": ErrorResponse}}
)
def update_dataset(
    dataset_id: str, payload: DatasetUpdateRequest, services: ServiceContainer = Depends(get_services)
) -> DatasetRecord:
    record = services.dataset_manager.update_dataset(dataset_id, payload)
    if not record:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return record


@router.delete("/datasets/{dataset_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dataset(dataset_id: str, services: ServiceContainer = Depends(get_services)) -> None:
    if not services.dataset_manager.delete_dataset(dataset_id):
        raise HTTPException(status_code=404, detail="Dataset not found")


@router.post("/training/jobs", response_model=JobRecord, status_code=status.HTTP_202_ACCEPTED)
def create_training_job(
    payload: TrainingRequest, services: ServiceContainer = Depends(get_services)
) -> JobRecord:
    return services.training_manager.start_training(payload)


@router.post("/inference/jobs", response_model=JobRecord, status_code=status.HTTP_202_ACCEPTED)
def create_inference_job(
    payload: InferenceRequest, services: ServiceContainer = Depends(get_services)
) -> JobRecord:
    return services.inference_manager.start_inference(payload)


@router.post("/audio/jobs", response_model=JobRecord, status_code=status.HTTP_202_ACCEPTED)
def create_audio_job(
    payload: AudioProcessingRequest, services: ServiceContainer = Depends(get_services)
) -> JobRecord:
    return services.audio_processing_manager.start_processing(payload)


@router.get("/jobs", response_model=list[JobRecord])
def list_jobs(services: ServiceContainer = Depends(get_services)) -> list[JobRecord]:
    return services.job_runner.list_jobs()


@router.get("/jobs/{job_id}", response_model=JobRecord, responses={404: {"model": ErrorResponse}})
def get_job(job_id: str, services: ServiceContainer = Depends(get_services)) -> JobRecord:
    record = services.job_runner.get_job(job_id)
    if not record:
        raise HTTPException(status_code=404, detail="Job not found")
    return record
