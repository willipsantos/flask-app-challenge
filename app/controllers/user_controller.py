from flask import request, jsonify, current_app
from flask.wrappers import Response
from app.models.user_model import User
from http import HTTPStatus
from . import default_exceptions_return
from app.exceptions.user_exceptions import (
    ExistentUserException,
    UserNotExistsException
)
from app.exceptions.public_exceptions import (
    MissingKeysException,
    InvalidKeysException,
    EmptyValuesException,
    InvalidValuesException,
    ValueIsNotInstanceOfTypeString
)


def get_all() -> Response:
    """
        Method that return a list with all users in the
        database.
    """

    data = User.query.all()

    return jsonify(data), HTTPStatus.OK


def create_user() -> tuple:

    """
        Method that creates a new user and send to the
        database.
    """
    try:

        data: dict = request.get_json()

        session = current_app.db.session

        User.check_create_keys(data)

        User.check_create_values(data)

        data = User.create_status_and_created_at_variables(data)

        user: User = User(**data)

        session.add(user)
        session.commit()

        return jsonify(user), HTTPStatus.CREATED

    except MissingKeysException as e:
        return default_exceptions_return(e)

    except InvalidKeysException as e:
        return default_exceptions_return(e)

    except EmptyValuesException as e:
        return default_exceptions_return(e)

    except ExistentUserException as e:
        return default_exceptions_return(e)

    except InvalidValuesException as e:
        return default_exceptions_return(e)


def delete_user() -> tuple:
    """
        Method that delete an user from the database
        using the email parameter to filter.
    """

    try:

        data: dict = request.get_json()

        session = current_app.db.session

        User.check_delete_keys(data)

        User.check_delete_values(data)

        user_email: str = data['email']

        user: User = User.query.filter_by(email=user_email).first()

        session.delete(user)
        session.commit()

        return jsonify(user), HTTPStatus.OK

    except MissingKeysException as e:
        return default_exceptions_return(e)

    except InvalidKeysException as e:
        return default_exceptions_return(e)

    except UserNotExistsException as e:
        return default_exceptions_return(e)

    except InvalidValuesException as e:
        return default_exceptions_return(e)


def update_user() -> tuple:

    try:

        data: dict = request.get_json()

        session = current_app.db.session

        User.check_update_keys(data)

        User.check_update_keys_types(data)

        User.check_update_values(data)

        user_email: str = data['email']

        user: User = User.query.filter_by(email=user_email).update(data)
        session.commit()

        user = User.query.filter_by(email=user_email).first()

        return jsonify(user), HTTPStatus.OK

    except InvalidKeysException as e:
        return default_exceptions_return(e)

    except MissingKeysException as e:
        return default_exceptions_return(e)

    except ValueIsNotInstanceOfTypeString as e:
        return default_exceptions_return(e)

    except EmptyValuesException as e:
        return default_exceptions_return(e)
