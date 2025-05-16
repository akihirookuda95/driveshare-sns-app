import os

from dotenv import load_dotenv
from flask import Flask

from backend.app.config import DevelopmentConfig, ProductionConfig, TestingConfig
from backend.app.extensions import db, cors


# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)

    config_name = os.environ.get("APP_ENV", "development").lower()
    if config_name == "production":
        app.config.from_object(ProductionConfig)
    elif config_name == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    cors.init_app(app)

    @app.route('/')
    def index():
        return "Hello, DriveShare!"

    return app
