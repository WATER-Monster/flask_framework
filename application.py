from flask import Flask
from flask_cors import CORS
from config.constans import DEFAULT_SERVICE_NAME
from config.constans import CORS_RESOURCES
from config.constans import CORS_HEADERS
from config.constans import CORS_MAX_AGE


def app_instance():
    app = Flask(DEFAULT_SERVICE_NAME)
    app.config.from_object("")

    register_blueprint(app)
    #  支持跨域
    CORS(
        app, resources=CORS_RESOURCES, expose_headers=CORS_HEADERS,
        max_age=CORS_MAX_AGE, send_wildcard=True
    )
    return app


def register_blueprint(app):
    """Register Flask blueprint."""
    app.register_blueprint(test, url_prefix="/test")


app = app_instance()