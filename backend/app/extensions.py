import sqlite3

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import event
from sqlalchemy.engine import Engine


db = SQLAlchemy()
cors = CORS()
migrate = Migrate()

@event.listens_for(Engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    """
    Enable foreign key constraints for SQLite connections.
    This is necessary because SQLite does not enforce foreign key constraints by default.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()