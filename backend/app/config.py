import os


class Config:
    """Base configuration class."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")


class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///local.db"


class ProductionConfig(Config):
    """Production configuration class."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL environment variable is required in production")


class TestingConfig(Config):
    """Testing configuration class."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"