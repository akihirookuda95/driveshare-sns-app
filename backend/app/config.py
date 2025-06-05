import os
import secrets


class Config:
    """Base configuration class."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        env = os.environ.get("APP_ENV", "development")
        self.SECRET_KEY = os.environ.get("SECRET_KEY")
        if not self.SECRET_KEY:
            if env == "production":
                raise ValueError("SECRET_KEY environment variable is required in production")
            else:
                self.SECRET_KEY = secrets.token_hex(16)


class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True

    def __init__(self):
        super().__init__()
        self.SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///local.db")


class ProductionConfig(Config):
    """Production configuration class."""
    DEBUG = False

    def __init__(self):
        super().__init__()
        self.SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
        if not self.SQLALCHEMY_DATABASE_URI:
            raise ValueError("SQLALCHEMY_DATABASE_URI environment variable is required in production")


class TestingConfig(Config):
    """Testing configuration class."""
    TESTING = True

    def __init__(self):
        super().__init__()
        # Use an in-memory SQLite database for testing
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False