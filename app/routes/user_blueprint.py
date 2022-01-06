from flask import Blueprint
from app.controllers.user_controller import (
    create_user,
    get_all,
    delete_user,
    update_user
)

bp: Blueprint = Blueprint("bp_user", __name__, url_prefix="/user")

bp.post("")(create_user)
bp.get("")(get_all)
bp.delete("")(delete_user)
bp.patch("")(update_user)
