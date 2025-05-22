import os

from dotenv import load_dotenv
from flask import Flask

from backend.app.config import DevelopmentConfig, ProductionConfig, TestingConfig
from backend.app.error_handlers import register_error_handlers
from backend.app.extensions import db, cors, migrate
from backend.app.routes.user_route import user_bp
from backend.app.routes.post_route import post_bp

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(env_path)


def create_app():
    app = Flask(__name__)

    config_name = os.environ.get("APP_ENV", "development").lower()
    if config_name == "production":
        config = ProductionConfig()
    elif config_name == "testing":
        config = TestingConfig()
    else:
        config = DevelopmentConfig()
    app.config.from_object(config)

    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_bp)
    app.register_blueprint(post_bp)

    register_error_handlers(app)

    return app
