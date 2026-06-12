from pydantic import BaseModel, Field


class AudioProcessingRequest(BaseModel):
    input_audio_path: str
    output_dir: str
    operations: list[str] = Field(default_factory=lambda: ["normalize", "trim_silence"])
    export_format: str = "wav"
