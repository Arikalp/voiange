from datetime import datetime

from pydantic import BaseModel, Field

from voiceai_backend.core.enums import ModelType


class ModelCreateRequest(BaseModel):
    name: str
    model_type: ModelType
    source: str
    local_path: str
    description: str | None = None
    tags: list[str] = Field(default_factory=list)


class ModelUpdateRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    tags: list[str] | None = None


class ModelRecord(BaseModel):
    id: str
    name: str
    model_type: ModelType
    source: str
    local_path: str
    description: str | None = None
    tags: list[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime
