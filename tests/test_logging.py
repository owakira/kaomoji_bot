import logging

from src.config import BASE_DIR
from src.core.logging import configure_logging


def test_configure_logging_return() -> None:
    config = {
        "version": 1,
        "formatters": {
            "default":
                {"format": "[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s"},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "default",
                "stream": "ext://sys.stdout"
            }
        },
        "loggers": {
            "root": {"level": "INFO", "handlers": ["console"], "propagate": False}
        }
    }
    loaded_config = configure_logging(BASE_DIR / "tests" / "log_config_example.yml")

    assert config == loaded_config


def test_root_logger_has_handler() -> None:
    configure_logging(BASE_DIR / "tests" / "log_config_example.yml")
    root_logger = logging.getLogger("root")

    assert len(root_logger.handlers) > 0
