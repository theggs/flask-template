from flask import Flask
from config import Config
from router.api import main as api_route


def create_app():
    app = Flask(__name__)
    app.secret_key = Config.secret_key
    app = register_blueprints(app)
    app = configure_app(app)

    return app


def register_blueprints(app):
    app.register_blueprint(api_route, url_prefix='/api')
    return app


def configure_app(app):
    app.config['JSON_AS_ASCII'] = False  # make non-ascii characters readable
    return app


if __name__ == '__main__':
    config = dict(
        host='127.0.0.1',
        port=2004,
        debug=True,
    )
    app_ = create_app()
    app_.run(**config)
