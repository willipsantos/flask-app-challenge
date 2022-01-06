from . import CustomizedException
from http import HTTPStatus


class ExistentUserException(CustomizedException):

    def __init__(self, message: str) -> None:
        super().__init__(message, HTTPStatus.CONFLICT)


class UserNotExistsException(CustomizedException):

    def __init__(self, message: str) -> None:
        super().__init__(message, HTTPStatus.BAD_REQUEST)
