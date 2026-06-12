import json
from pathlib import Path
from typing import Generic, TypeVar

from pydantic import BaseModel, TypeAdapter

T = TypeVar("T", bound=BaseModel)


class JsonStore(Generic[T]):
    def __init__(self, file_path: Path, model_type: type[T]):
        self.file_path = file_path
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self.adapter = TypeAdapter(list[model_type])

    def read_all(self) -> list[T]:
        if not self.file_path.exists():
            return []
        content = self.file_path.read_text(encoding="utf-8")
        if not content.strip():
            return []
        return self.adapter.validate_json(content)

    def write_all(self, items: list[T]) -> None:
        self.file_path.write_text(
            json.dumps([item.model_dump(mode="json") for item in items], indent=2),
            encoding="utf-8",
        )
