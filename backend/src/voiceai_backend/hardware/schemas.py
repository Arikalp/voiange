from pydantic import BaseModel, Field


class GpuDevice(BaseModel):
    index: int
    name: str
    memory_total_mb: int | None = None
    memory_free_mb: int | None = None
    is_cuda: bool = False


class CpuInfo(BaseModel):
    physical_cores: int
    logical_cores: int
    usage_percent: float


class MemoryInfo(BaseModel):
    total_mb: int
    available_mb: int
    usage_percent: float


class GpuReport(BaseModel):
    cuda_available: bool
    devices: list[GpuDevice] = Field(default_factory=list)
    cpu: CpuInfo
    memory: MemoryInfo
