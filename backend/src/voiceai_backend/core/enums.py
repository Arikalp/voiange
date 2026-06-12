from enum import Enum


class JobType(str, Enum):
    training = "training"
    inference = "inference"
    audio_processing = "audio_processing"


class JobStatus(str, Enum):
    queued = "queued"
    running = "running"
    completed = "completed"
    failed = "failed"
    cancelled = "cancelled"


class ModelType(str, Enum):
    rvc = "rvc"
    demucs = "demucs"
    ffmpeg_preset = "ffmpeg_preset"


class ArtifactType(str, Enum):
    trained_model = "trained_model"
    inference_output = "inference_output"
    audio_output = "audio_output"
