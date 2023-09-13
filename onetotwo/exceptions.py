from abc import ABC, abstractmethod


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
