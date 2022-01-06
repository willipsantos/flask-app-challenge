from flask import Blueprint
from .user_blueprint import bp as bp_user
from app.controllers import check_health

bp: Blueprint = Blueprint("bp_api", __name__, url_prefix="/oauth/v1")

bp.register_blueprint(bp_user)

bp.get("/health")(check_health)
