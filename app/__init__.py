from flask import Flask
from app.configs import init_app, database, migration
from app import routes
from flask_cors import CORS


def create_app():

    app = Flask(__name__)
    CORS(app)

    init_app(app)
    database.init_app(app)
    migration.init_app(app)
    routes.init_app(app)

    return app
