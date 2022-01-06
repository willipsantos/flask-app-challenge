from . import CustomizedException
from http import HTTPStatus


class MissingKeysException(CustomizedException):

    def __init__(self, message: str) -> None:
        super().__init__(message, HTTPStatus.BAD_REQUEST)


class InvalidKeysException(CustomizedException):

    def __init__(self, message: str) -> None:
        super().__init__(message, HTTPStatus.BAD_REQUEST)


class EmptyValuesException(CustomizedException):

    def __init__(self, message: str) -> None:
        super().__init__(message, HTTPStatus.BAD_REQUEST)


class InvalidValuesException(CustomizedException):

    def __init__(self, message: str) -> None:
        super().__init__(message, HTTPStatus.BAD_REQUEST)


class ValueIsNotInstanceOfTypeString(CustomizedException):

    def __init__(self, message: str) -> None:
        super().__init__(message, HTTPStatus.BAD_REQUEST)
