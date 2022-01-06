from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime
from copy import deepcopy
from . import check_keys
from app.exceptions.user_exceptions import (
    ExistentUserException,
    UserNotExistsException
)
from app.exceptions.public_exceptions import (
    InvalidValuesException,
    EmptyValuesException,
    MissingKeysException,
    ValueIsNotInstanceOfTypeString
)


@dataclass
class User(db.Model):
    """
    A class that represents an user of the
    system.

    ...

    Attributes
    ----------
    user_id : `int`
        The user identification

    name : `str`
        The name of the user

    email : `str`
        The email of the user

    password : `str`
        The password used by the user to
        login into the system

    role : `str`
        The role of the user inside the
        system (must be admin or member)

    status : `str`
        The user account status inside the
        system (can be activate, disabled
        or banned)

    avatar : `str`
        The link for the user avatar image

    created_at : `datetime`
        The account creation time

    updated_at : `datetime`
        The last time the account has been
        updated


    Methods
    -------
    check_keys(data: `dict`)
        Checks if the keys in the provided
        dictionary are valid, and if they
        represents all the required keys

    check_values(data: `dict`)
        Checks if the values in the provided
        dictionary are not empty, if the role
        value is admin or member, and if the
        provided email not exists in the
        database

    create_status_and_created_at_variables(data: `dict`)
        Add to the provided dictionary the
        status and created_at values

    check_delete_keys(data: `dict`)
        Same as check_keys method

    check_update_keys(data: `dict`)
        Same as check_keys method
    """

    name: str
    email: str
    role: str
    avatar: str

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(10))
    avatar = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    @staticmethod
    def check_create_keys(data: dict) -> None:

        REQUIRED_KEYS: tuple = ("name", "email", "password", "role", "avatar")
        VALID_KEYS: tuple = deepcopy(REQUIRED_KEYS)

        check_keys(REQUIRED_KEYS, VALID_KEYS, data)

    @staticmethod
    def check_create_values(data: dict) -> None:

        empty_values: list = []
        ROLE_VALID_VALUES: list = ("admin", "member")

        for key in data:
            if data[key] == "":
                empty_values.append(key)

        if empty_values != []:
            raise EmptyValuesException(f"The keys {empty_values} have empty values.")

        user: User = User.query.filter_by(email=data["email"]).first()

        if user is not None:
            raise ExistentUserException("This email already exists.")

        if data["role"] not in ROLE_VALID_VALUES:
            raise InvalidValuesException(f"The role '{data['role']}' is invalid. Please select a role between admin or member.")

    @staticmethod
    def create_status_and_created_at_variables(data: dict) -> dict:

        data["status"] = "active"

        data["created_at"] = datetime.now()

        return data

    @staticmethod
    def check_delete_keys(data: dict) -> None:

        REQUIRED_KEY: tuple = ("email",)
        VALID_KEY: tuple = deepcopy(REQUIRED_KEY)

        check_keys(REQUIRED_KEY, VALID_KEY, data)

    @staticmethod
    def check_delete_values(data: dict) -> None:

        user_email: str = data['email']

        if not isinstance(user_email, str):
            raise InvalidValuesException(f'The value {user_email} is not instance of type string.')

        user: User = User.query.filter_by(email=user_email).first()

        if user is None:
            raise UserNotExistsException("The user doesn't exists.")

    @staticmethod
    def check_update_keys(data: dict) -> None:

        REQUIRED_KEY: tuple = ("email",)
        VALID_KEYS: tuple = ("email", "name", "avatar")
        total_keys: int = 0

        check_keys(REQUIRED_KEY, VALID_KEYS, data)

        for key in data:
            if key in VALID_KEYS:
                total_keys += 1

        if total_keys < 2:
            raise MissingKeysException('Needs 2 keys at least ("email" plus "name" or "avatar").')

    @staticmethod
    def check_update_keys_types(data: dict) -> None:

        for value in data.values():
            if not isinstance(value, str):
                raise ValueIsNotInstanceOfTypeString(f'The value "{value}" is not instance of type string.')

    @staticmethod
    def check_update_values(data: dict) -> None:

        empty_values: list = []

        for key, value in data.items():
            if value == "":
                empty_values.append(key)

        if empty_values != []:
            raise EmptyValuesException(f"The keys {empty_values} have empty values.")
