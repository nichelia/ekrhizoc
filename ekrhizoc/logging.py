import logging
import os
from datetime import datetime
from pathlib import Path

from ekrhizoc.settings import LOG_DIR, LOG_LEVEL

logger = logging.getLogger(__name__)
logger_format = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
)


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors."""

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = logger_format

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)


def setup_logger(verbosity: int = 0) -> None:
    """Configure logger.

    Args:
        verbosity: Integer value for verbosity of logs (-1 to 2).

    Raises:
        NotADirectoryError: If given path directory is not valid.
    """
    base_loglevel = getattr(logging, (~LOG_LEVEL).upper(), "WARNING")
    # Limit verbosity to value 2
    verbosity = min(verbosity, 2)
    log_level = base_loglevel - (verbosity * 10)
    logger.setLevel(log_level)

    log_dir = ~LOG_DIR
    if log_dir:
        output_dir = Path(log_dir)
        if not output_dir.is_dir():
            raise NotADirectoryError(f"{output_dir} is not a directory")
        filepath = output_dir / "ekrhizoc.log"
        handler = logging.FileHandler(filepath)
        handler.setFormatter(logging.Formatter(logger_format))
    else:
        handler = logging.StreamHandler()
        handler.setLevel(log_level)
        handler.setFormatter(CustomFormatter())

    logger.addHandler(handler)
