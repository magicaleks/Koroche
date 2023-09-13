# %% Import dependencies

from importlib import import_module
from logging import Formatter, Logger, StreamHandler
from typing import Optional

from koroche.config import AppLoggerConfig


# %% Define logging ----
class AppLogger:
    """Application logger: wrapper for Python logging library."""

    def __init__(self, service_name: str, config: AppLoggerConfig) -> None:
        """Initialize and configure the logger.

        :param service_name: Service name
        :param config: AppLogger config
        """
        self._config = config
        self._logger = Logger(service_name, level=self._config.level)

        self._configure()

    def _configure(self) -> None:
        """Configure logger by self._config."""
        if "stream" in self._config.handlers:
            stream_name = self._config.handlers["stream"].get("handler")
            stream = getattr(import_module("sys"), stream_name)
            handler = StreamHandler(stream=stream)
        else:
            raise NotImplementedError("Not supported log handler")

        handler.setFormatter(
            Formatter(
                self._config.log_format,
                defaults={
                    "service_name": self._logger.name,
                },
            )
        )

        self._logger.addHandler(handler)

    def debug(self, message: str) -> None:
        """Log an debug message."""
        self._logger.debug(message)

    def info(self, message: str) -> None:
        """Log an info message."""
        self._logger.info(message)

    def warning(self, message: str) -> None:
        """Log an warning message."""
        self._logger.warning(message)

    def error(self, ex: Exception, message: Optional[str] = None) -> None:
        """Log an error message."""
        message = f"{message}. Details: {str(ex)}" if message else str(ex)
        self._logger.exception(message, exc_info=True)

    def critical(self, ex: Exception, message: Optional[str] = None) -> None:
        """Log an critical message."""
        message = f"{message}. Details: {str(ex)}" if message else str(ex)
        self._logger.critical(message, exc_info=True)
