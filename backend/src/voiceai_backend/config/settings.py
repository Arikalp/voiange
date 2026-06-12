from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "VoiceAI Studio Backend"
    api_prefix: str = "/api/v1"
    environment: str = "development"
    host: str = "127.0.0.1"
    port: int = 8000
    log_level: str = "INFO"
    data_root: Path = Field(default=Path.cwd() / ".voiceai")
    max_concurrent_jobs: int = 2
    training_step_delay_seconds: float = 0.35
    inference_step_delay_seconds: float = 0.25
    audio_step_delay_seconds: float = 0.2

    model_config = SettingsConfigDict(
        env_prefix="VOICEAI_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def state_root(self) -> Path:
        return self.data_root / "state"

    @property
    def artifacts_root(self) -> Path:
        return self.data_root / "artifacts"

    @property
    def logs_root(self) -> Path:
        return self.data_root / "logs"


settings = Settings()
