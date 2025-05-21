import os


class Config:
    """Base configuration class."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        self.SECRET_KEY = os.environ.get("SECRET_KEY")
        if not self.SECRET_KEY:
            if os.environ.get("APP_ENV") == "production":
                raise ValueError("SECRET_KEY environment variable is required in production")
            self.SECRET_KEY = "dev_secret_key"


class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///local.db"


class ProductionConfig(Config):
    """Production configuration class."""
    DEBUG = False
    def __init__(self):
        super().__init__()
        self.SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
        if not self.SQLALCHEMY_DATABASE_URI:
            raise ValueError("DATABASE_URL environment variable is required in production")


class TestingConfig(Config):
    """Testing configuration class."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"