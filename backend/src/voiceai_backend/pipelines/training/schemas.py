from pydantic import BaseModel, Field


class TrainingRequest(BaseModel):
    dataset_id: str
    model_name: str
    epochs: int = Field(default=200, ge=1, le=10000)
    batch_size: int = Field(default=8, ge=1, le=128)
    learning_rate: float = Field(default=0.0001, gt=0)
    output_dir: str
