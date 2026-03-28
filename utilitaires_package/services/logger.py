import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from .formatters import ColoredFormatter
from .config import DEFAULT_LOG_FORMAT, DEFAULT_DATE_FORMAT


class ProLogger:
    def __init__(self, name: str = "prologger", log_dir: str = "logs", level=logging.DEBUG, console: bool = True,
                 file_logging: bool = True, rotation_days: int = 30, colored: bool = True):
        self.name = name
        self.log_dir = Path(log_dir)
        self.level = level
        self.console = console
        self.file_logging = file_logging
        self.rotation_days = rotation_days
        self.colored = colored

        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.level)

        self.setup()

    def setup(self):
        if self.logger.handlers:
            return

        formatter = logging.Formatter(
            DEFAULT_LOG_FORMAT,
            DEFAULT_DATE_FORMAT
        )

        if self.file_logging:
            self.log_dir.mkdir(parents=True, exist_ok=True)

            file_handler = TimedRotatingFileHandler(
                self.log_dir / f"{self.name}.log",
                when="midnight",
                interval=1,
                backupCount=self.rotation_days,
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        if self.console:
            console_handler = logging.StreamHandler()

            if self.colored:
                console_handler.setFormatter(
                    ColoredFormatter(
                        DEFAULT_LOG_FORMAT,
                        DEFAULT_DATE_FORMAT
                    )
                )
            else:
                console_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)
    
    def get(self):
        return self.logger
