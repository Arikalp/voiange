from pydantic import BaseModel, Field


class InferenceRequest(BaseModel):
    model_id: str
    input_audio_path: str
    output_dir: str
    pitch_shift: int = Field(default=0, ge=-24, le=24)
    protect: float = Field(default=0.33, ge=0, le=1)
