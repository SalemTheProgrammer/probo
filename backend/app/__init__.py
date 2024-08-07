# app/__init__.py
from flask import Flask
from app.config import config_by_name
from app.extensions import bcrypt, jwt, mail, mongo
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name['dev'])

    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    mongo.init_app(app)

    from app.api.user import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/"
    }

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "My API",
            "description": "API documentation",
            "version": "1.0"
        },
        "host": "localhost:5000",  # Change to your domain
        "basePath": "/auth",
        "schemes": [
            "http",
            "https"
        ],
    }

    Swagger(app, config=swagger_config, template=swagger_template)

    return app
