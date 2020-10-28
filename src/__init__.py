from flask import Flask

from .db import db
from .api_routes import api
from .routes import home


def create_app(config_file='config.py'):
    app = Flask(__name__, static_url_path='/static')

    app.config.from_pyfile(config_file)

    db.init_app(app)

    api.init_app(app)

    app.register_blueprint(home)

    return app
