from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from voiceai_backend.core.enums import ArtifactType, JobStatus, JobType, ModelType


class HealthResponse(BaseModel):
    status: str
    app_name: str
    environment: str


class TimestampedModel(BaseModel):
    created_at: datetime
    updated_at: datetime


class ErrorResponse(BaseModel):
    detail: str


class Artifact(BaseModel):
    id: str
    name: str
    kind: ArtifactType
    path: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class JobProgress(BaseModel):
    percent: float = Field(ge=0, le=100)
    stage: str
    message: str


class JobRecord(TimestampedModel):
    id: str
    job_type: JobType
    status: JobStatus
    progress: JobProgress
    payload: dict[str, Any] = Field(default_factory=dict)
    artifacts: list[Artifact] = Field(default_factory=list)
    error: str | None = None
