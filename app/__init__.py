from flask import Flask
from flask_bootstrap import Bootstrap
from flask_navigation import Navigation
from config import Config


bootstrap = Bootstrap()
nav = Navigation()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)
    nav.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.home import bp as home_bp
    app.register_blueprint(home_bp)

    return app


app = create_app()
