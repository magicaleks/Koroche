from abc import ABC, abstractmethod

from httpx import HTTPError


class BaseException_(Exception, ABC):
    """Base class for exceptions"""

    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None

    @abstractmethod
    def __str__(self) -> str:
        ...


class MissingRequiredArgument(BaseException_):
    """Missing required argument"""

    def __str__(self) -> str:
        if self.message:
            return f"MissingRequiredArgument: {self.message}"
        else:
            return "MissingRequiredArgument"


class RetryPolicyException(HTTPError):
    """Raise while server response with status code from retry policy forcelist"""

    def __init__(self, url: str, status_code: int) -> None:
        """Initialize exception with response."""
        msg = f"HTTP error: {url} responded with {status_code} status code"
        super().__init__(msg)
