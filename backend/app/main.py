import os

from dotenv import load_dotenv
from flask import Flask

from backend.app.config import DevelopmentConfig
from backend.app.error_handlers import register_error_handlers
from backend.app.extensions import db, cors, migrate
from backend.app.routes.user_route import user_bp
from backend.app.routes.post_route import post_bp

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(env_path)


def create_app(config_class=None):
    app = Flask(__name__)

    if config_class is None:
        config_class = DevelopmentConfig
    config = config_class()
    app.config.from_object(config)

    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_bp)
    app.register_blueprint(post_bp)

    register_error_handlers(app)

    return app
