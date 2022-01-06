from flask import jsonify
from http import HTTPStatus


def default_exceptions_return(e):

    return jsonify({
        "error": e.get_message()
    }), e.get_code()


def check_health() -> tuple:
    """
        Method that indicates if the API is up and
        running.
    """

    return jsonify({
        "healthy": "OK"
    }), HTTPStatus.OK
