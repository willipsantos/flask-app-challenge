from app.exceptions.public_exceptions import (
    MissingKeysException,
    InvalidKeysException
)


def check_keys(REQUIRED_KEYS: tuple, VALID_KEYS: tuple, data: dict) -> None:

    missing_keys: list = []
    invalid_keys: list = []

    for key in REQUIRED_KEYS:
        if key not in data:
            missing_keys.append(key)

    if missing_keys != []:
        raise MissingKeysException(f"The keys {missing_keys} are missing.")

    for key in data:
        if key not in VALID_KEYS:
            invalid_keys.append(key)

    if invalid_keys != []:
        raise InvalidKeysException(f'The keys {invalid_keys} are invalid.')
