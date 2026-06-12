import logging
from logging.config import dictConfig

from voiceai_backend.config.settings import settings


def configure_logging() -> None:
    settings.logs_root.mkdir(parents=True, exist_ok=True)
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": settings.log_level,
                },
                "file": {
                    "class": "logging.FileHandler",
                    "filename": str(settings.logs_root / "backend.log"),
                    "formatter": "default",
                    "level": settings.log_level,
                    "encoding": "utf-8",
                },
            },
            "root": {
                "handlers": ["console", "file"],
                "level": settings.log_level,
            },
        }
    )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
