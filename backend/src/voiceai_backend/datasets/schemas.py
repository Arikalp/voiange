from datetime import datetime

from pydantic import BaseModel, Field


class DatasetClip(BaseModel):
    id: str
    file_name: str
    duration_seconds: float | None = None
    transcript: str | None = None


class DatasetCreateRequest(BaseModel):
    name: str
    location: str
    description: str | None = None
    tags: list[str] = Field(default_factory=list)


class DatasetUpdateRequest(BaseModel):
    description: str | None = None
    tags: list[str] | None = None


class DatasetRecord(BaseModel):
    id: str
    name: str
    location: str
    description: str | None = None
    tags: list[str] = Field(default_factory=list)
    clips: list[DatasetClip] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime
